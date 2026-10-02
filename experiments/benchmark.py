"""Deterministic offline HELIOS mechanics; synthetic outputs are not field results.

Run: python -m experiments.benchmark
No network requests, host collection, offensive actions, or external packages.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import itertools
import json
import math
import random
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = 20261002


def quantile(values, q):
    v = sorted(values)
    if not v or not 0 <= q <= 1:
        raise ValueError('nonempty input and q in [0,1] required')
    idx = (len(v)-1)*q
    lo = int(idx)
    return v[lo]+(v[min(lo+1,len(v)-1)]-v[lo])*(idx-lo)


def confusion(labels, predicted, observed=None):
    if len(labels) != len(predicted) or (observed is not None and len(observed) != len(labels)):
        raise ValueError('length mismatch')
    observed = [True]*len(labels) if observed is None else observed
    if any(x not in (0,1) for x in labels+predicted):
        raise ValueError('binary labels required')
    tp=fp=tn=fn=0
    for y,p,o in zip(labels,predicted,observed):
        if not o:
            continue
        tp += int(y==1 and p==1)
        fp += int(y==0 and p==1)
        tn += int(y==0 and p==0)
        fn += int(y==1 and p==0)
    return dict(tp=tp,fp=fp,tn=tn,fn=fn,
                precision=tp/(tp+fp) if tp+fp else None,
                recall=tp/(tp+fn) if tp+fn else None,
                fpr=fp/(fp+tn) if fp+tn else None,
                observed=sum(observed))


def telemetry(seed=SEED):
    rng=random.Random(seed)
    # One 30-second synthetic sample; correlated noise, declared benign mode changes.
    rows=[]
    noise=0.
    for t in range(6000):
        split='train' if t<3000 else 'validation' if t<4500 else 'test'
        anomaly=any(a<=t<b for a,b in [(3300,3330),(3850,3870),(4750,4775),(5300,5335),(5800,5820)])
        noise=.65*noise+rng.gauss(0,.75)
        benign_shift=1.2 if t>=4500 else 0.
        value=10+noise+benign_shift+(5.5 if anomaly else 0.)
        missing=4900<=t<4940 or 5610<=t<5630
        rows.append(dict(t=t,time_s=t*30,split=split,value=value,anomaly=int(anomaly),observed=not missing,mode='shifted' if benign_shift else 'nominal'))
    train=[r['value'] for r in rows if r['split']=='train' and r['observed']]
    med=statistics.median(train)
    mad=statistics.median(abs(x-med) for x in train)
    scale=max(1.4826*mad,1e-9)
    mu=statistics.mean(train)
    sd=statistics.stdev(train)
    summaries={}
    for name,center,width in [('robust',med,scale),('mean_std',mu,sd)]:
        val=[(r['value']-center)/width for r in rows if r['split']=='validation' and r['observed'] and not r['anomaly']]
        tau=quantile(val,.9975)
        # Filtering validation anomalies uses the available synthetic labels; this is supervised calibration.
        test=[r for r in rows if r['split']=='test']
        predictions=[int((r['value']-center)/width>tau) if r['observed'] else 0 for r in test]
        result=confusion([r['anomaly'] for r in test],predictions,[r['observed'] for r in test])
        event_delays=[]
        for start,end in [(4750,4775),(5300,5335),(5800,5820)]:
            first=next((r['t'] for r,p in zip(test,predictions) if start<=r['t']<end and p and r['observed']),None)
            event_delays.append(None if first is None else (first-start)*30)
        result.update(threshold=tau,center=center,scale=width,observed_hours=result['observed']*30/3600,
                      false_alerts_per_observed_hour=result['fp']/(result['observed']*30/3600),
                      event_recall=sum(x is not None for x in event_delays)/len(event_delays),event_delays_s=event_delays,
                      unconditional_timestamp_recall=result['tp']/sum(r['anomaly'] for r in test))
        # Cluster/block resampling: approximate uncertainty under this finite synthetic fixture only.
        blocks=[list(range(i,min(i+50,len(test)))) for i in range(0,len(test),50)]
        boots=[]
        bootrng=random.Random(seed+5)
        for _ in range(200):
            ids=[i for b in bootrng.choices(blocks,k=len(blocks)) for i in b]
            m=confusion([test[i]['anomaly'] for i in ids],[predictions[i] for i in ids],[test[i]['observed'] for i in ids])
            if m['precision'] is not None:
                boots.append(m['precision'])
        result['precision_block_bootstrap_95_interval']=[quantile(boots,.025),quantile(boots,.975)] if boots else None
        summaries[name]=result
        for r in rows:
            r[name+'_score']=(r['value']-center)/width if r['observed'] else None
    return rows,dict(evidence_class='Derived from Synthetic',sample_period_s=30,seed=seed,methods=summaries,
                     limitations='One fixture, correlated samples, supervised validation-label filtering, deliberate test mean shift. Intervals are resampling diagnostics, not external validity or general performance guarantees.')


JOBS={'identity':(3.,.22,()),'storage':(5.,.25,('identity',)),
      'ground_link':(2.,.16,('identity',)),'payload':(4.,.19,('storage','ground_link')),
      'archive':(6.,.10,('storage',)),'console':(1.,.08,('identity',))}


def schedule_loss(order,jobs=JOBS):
    if len(order)!=len(jobs) or set(order)!=set(jobs):
        raise ValueError('each job exactly once')
    done=set();elapsed=loss=0.;trace=[]
    for name in order:
        duration,weight,dependencies=jobs[name]
        if duration<0 or weight<0 or not set(dependencies)<=done:
            raise ValueError('invalid prerequisites/duration/weight')
        elapsed+=duration;loss+=weight*elapsed;done.add(name)
        trace.append(dict(job=name,completion_min=elapsed,weight=weight))
    return loss,trace


def greedy_order(shortest=False):
    done=[]
    while len(done)<len(JOBS):
        ready=[x for x,(_,_,deps) in JOBS.items() if x not in done and set(deps)<=set(done)]
        if not ready:
            raise ValueError('cyclic prerequisites')
        key=(lambda n:(JOBS[n][0],n)) if shortest else (lambda n:(-JOBS[n][1],n))
        done.append(min(ready,key=key))
    return done


def recovery():
    feasible=[]
    for order in itertools.permutations(JOBS):
        try:
            loss,_=schedule_loss(order)
            feasible.append((loss,order))
        except ValueError:
            continue
    best=min(feasible)
    comparisons=[]
    for label,order in [('mission_weight_greedy',greedy_order()),('shortest_ready_first',greedy_order(True)),('enumerated_optimum',best[1])]:
        loss,trace=schedule_loss(order)
        comparisons.append(dict(method=label,loss_service_min=loss,order=list(order),trace=trace))
    return dict(evidence_class='Derived from Synthetic',jobs={k:list(v) for k,v in JOBS.items()},feasible_orders=len(feasible),comparisons=comparisons,
                limitations='Six assumed jobs; serial single-crew restores; each function becomes available at completion. No stochastic duration, partial service, production intervention or real incident claim.')


def firmware_update(cut,atomic=True):
    steps=['stage','verify','commit'] if atomic else ['erase','write','verify']
    if not 0<=cut<=len(steps):
        raise ValueError('cut outside modeled write boundaries')
    old=True;new=False;staged=False;verified=False;active='old'
    for s in steps[:cut]:
        if s=='stage': staged=True
        elif s=='erase':old=False;active=None
        elif s=='write':staged=True
        elif s=='verify':verified=staged;new=verified
        elif s=='commit':active='new' if verified else 'old'
    # Recovery selects a verified available image; atomic metadata/storage writes are ASSUMED here.
    selected='new' if new else 'old' if old else None
    return dict(cut=cut,selected=selected,safe=selected is not None,active_before_recovery=active)


def firmware():
    return dict(evidence_class='Derived from Synthetic',atomic=[firmware_update(i) for i in range(4)],single_slot=[firmware_update(i,False) for i in range(4)],
                limitations='Abstract three-operation storage model, complete-operation interruption boundaries only. Assumes atomic individual writes, reliable verification and two independent available slots. Does not test torn writes, corrupt metadata, boot trust, flash or cryptography.')


def interval_order(a,b):
    if len(a)!=2 or len(b)!=2 or a[0]>a[1] or b[0]>b[1]:
        raise ValueError('valid closed intervals required')
    return 'before' if a[1]<b[0] else 'after' if a[0]>b[1] else 'indeterminate'


def clocks():
    events=[dict(name='sensor',observed_s=100.,bound_s=4.,true_s=102.),dict(name='gateway',observed_s=103.,bound_s=6.,true_s=101.),dict(name='archive',observed_s=120.,bound_s=2.,true_s=119.)]
    for e in events:e['interval_s']=[e['observed_s']-e['bound_s'],e['observed_s']+e['bound_s']]
    pairs=[dict(a=a['name'],b=b['name'],relation=interval_order(a['interval_s'],b['interval_s'])) for a,b in itertools.combinations(events,2)]
    return dict(evidence_class='Derived from Synthetic',events=events,pairs=pairs,limitations='Bounds assumed and contain fixture truth; intervals establish temporal precedence only. No causal attribution or clock-security proof.')


def privacy_scale(epsilon,sensitivity=1.):
    if epsilon<=0 or sensitivity<0:raise ValueError('epsilon positive, sensitivity nonnegative')
    return sensitivity/epsilon


def privacy():
    rows=[dict(epsilon=e,sensitivity_count=1,laplace_scale_count=privacy_scale(e),expected_absolute_error_count=privacy_scale(e),composed_epsilon_12_releases=12*e) for e in [.1,.25,.5,1.,2.,4.]]
    return dict(evidence_class='Derived analytic relationship on Synthetic assumptions',rows=rows,
                limitations='Unit contribution-bound pure epsilon-DP count mechanism. Basic sequential composition only. Formula study, not a production privacy mechanism; no protected data, clipping implementation, cryptographic RNG or release accounting.')


def contacts():
    rows=[];age=0.;received=0;attempts=0
    for t in range(240):
        contact=(t%60)<8
        attempts+=1
        age=0 if contact else age+60
        received+=int(contact)
        rows.append(dict(time_min=t,contact=contact,age_s=age))
    return dict(evidence_class='Derived from Synthetic',rows=rows,contact_only_attempts=received,always_attempts=attempts,verified_receipts=received,
                max_age_s=max(r['age_s'] for r in rows),age_p95_s=quantile([r['age_s'] for r in rows],.95),
                limitations='Perfect verification and receipt on every modeled contact, constant 60 s time step. Attempt count is an energy proxy, not measured joules. No queue, spacecraft link, RF transmission or signing implementation.')


def outputs():
    rows,tel=telemetry()
    return rows,{'telemetry':tel,'recovery':recovery(),'firmware':firmware(),'clocks':clocks(),'privacy':privacy(),'contacts':contacts()}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args()
    rows,results=outputs()
    directory=ROOT/'data/synthetic'
    strings={f'{name}.json':json.dumps(data,indent=2,sort_keys=True)+'\n' for name,data in results.items()}
    import io
    stream=io.StringIO(newline='');writer=csv.DictWriter(stream,fieldnames=list(rows[0]),lineterminator='\n');writer.writeheader();writer.writerows(rows)
    strings['telemetry.csv']=stream.getvalue()
    manifest={'seed':SEED,'generator':'experiments/benchmark.py','evidence_class':'Synthetic; derived results only','files':{name:{'sha256':hashlib.sha256(s.encode()).hexdigest(),'bytes':len(s.encode())} for name,s in strings.items()}}
    strings['manifest.json']=json.dumps(manifest,indent=2,sort_keys=True)+'\n'
    for name,s in strings.items():
        p=directory/name
        if args.check:
            if not p.exists() or p.read_text()!=s:raise SystemExit(f'Stale experiment output: {name}')
        else:
            p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s)
    print('Verified six deterministic offline experiments and 6000 synthetic telemetry rows.')

if __name__=='__main__':main()
