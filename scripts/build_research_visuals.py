"""Exact SVG plots from pinned metadata and offline reference experiment outputs."""
import argparse,csv,html,json,collections
from pathlib import Path
R=Path(__file__).resolve().parents[1]
C=['#5be0ce','#9dbdff','#ffcb78','#e6a2df']

def load(name):return json.loads((R/'data/synthetic'/f'{name}.json').read_text())

def label(x,y,s,size=15,color='#c9d9ee',anchor='start'):
 return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{html.escape(str(s))}</text>'

def frame(title,evidence,body,note):
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="590" viewBox="0 0 1000 590" role="img" aria-label="{html.escape(title)}"><rect width="1000" height="590" rx="16" fill="#0b192e"/><g font-family="Arial,sans-serif">{label(35,43,title,25,"#f5f8ff")}{label(35,76,evidence,15,"#5be0ce")}{body}{label(35,560,note,13)}</g></svg>\n'

def lineplot(title,evidence,series,xlabel,ylabel,note):
 xs=[x for _,pts in series for x,y in pts];ys=[y for _,pts in series for x,y in pts]
 xmin,xmax=min(xs),max(xs);ymin=min(0,min(ys));ymax=max(ys)*1.06 or 1
 px=lambda x:95+(x-xmin)/(xmax-xmin or 1)*855
 py=lambda y:450-(y-ymin)/(ymax-ymin)*320
 body=''
 for i in range(6):
  y=ymin+(ymax-ymin)*i/5
  body+=f'<path d="M95 {py(y):.2f} H950" stroke="#2c425e"/>'+label(83,py(y)+5,f'{y:.2g}',13,anchor='end')
  x=xmin+(xmax-xmin)*i/5
  body+=label(px(x),474,f'{x:.3g}',13,anchor='middle')
 body+=label(95,114,ylabel,14)+label(520,505,xlabel,16,anchor='middle')
 for i,(name,pts) in enumerate(series):
  path=' '.join(('M' if j==0 else 'L')+f'{px(x):.2f},{py(y):.2f}' for j,(x,y) in enumerate(pts))
  body+=f'<path d="{path}" fill="none" stroke="{C[i%4]}" stroke-width="2"/>'+label(95+i*360,532,name,14,C[i%4])
 return frame(title,evidence,body,note)

def bars(title,evidence,values,ylabel,note):
 maxv=max(v for _,v in values)*1.13 or 1;body=label(95,114,ylabel,14);w=855/len(values)
 for i in range(6):
  y=i*maxv/5;yp=450-y/maxv*320
  body+=f'<path d="M95 {yp:.2f} H950" stroke="#2c425e"/>'+label(83,yp+5,f'{y:.3g}',13,anchor='end')
 for i,(name,v) in enumerate(values):
  x=95+i*w+w*.12;h=v/maxv*320
  body+=f'<rect x="{x:.2f}" y="{450-h:.2f}" width="{w*.76:.2f}" height="{h:.2f}" fill="{C[i%4]}"/>'+label(x+w*.38,440-h,f'{v:.3g}',14,anchor='middle')+label(x+w*.38,479,name,13,anchor='middle')
 return frame(title,evidence,body,note)

def render():
 out={};rows=list(csv.DictReader((R/'data/synthetic/telemetry.csv').open()))
 pts=[(float(r['time_s'])/3600,float(r['value'])) for r in rows if r['split']=='test' and r['observed']=='True']
 # Plot every observed test sample, without interpolation across missing blocks.
 tel=load('telemetry');m=tel['methods']['robust'];threshold=m['center']+m['scale']*m['threshold']
 out['telemetry.svg']=lineplot('KEPLER Nightwatch: drift challenges a frozen detector','Derived from Synthetic | 30-second samples | seed 20261002', [('observed synthetic value',pts),('frozen decision threshold',[(pts[0][0],threshold),(pts[-1][0],threshold)])],'Relative time (hours)','Synthetic scalar (arbitrary units)','Plot connects observed samples; missing blocks remain excluded. No deployed detection claim.')
 rec=load('recovery');out['recovery.svg']=bars('PHOENIX Relay: recovery order changes mission loss','Derived from Synthetic | six services | one repair crew',[(x['method'].replace('_',' '),x['loss_service_min']) for x in rec['comparisons']],'Weighted lost service-minutes','Shortest-ready-first matches the enumerated optimum in this fixture; no universal optimum claim.')
 fw=load('firmware');out['firmware.svg']=bars('ORION Lifeboat: interruption boundary outcomes','Derived from Synthetic | three abstract storage operations', [('two-slot model',sum(x['safe'] for x in fw['atomic'])),('single-slot model',sum(x['safe'] for x in fw['single_slot']))],'Recoverable enumerated cases (out of four)','Assumes atomic operations and reliable verification; excludes torn writes and corrupt metadata.')
 pri=load('privacy');out['privacy.svg']=lineplot('LUNAR Veil: privacy parameter and expected count error','Derived analytic relationship | unit contribution-bound assumption',[('Laplace expected absolute error',[(x['epsilon'],x['expected_absolute_error_count']) for x in pri['rows']])],'Privacy parameter epsilon (dimensionless)','Expected absolute error (count)','Single release relation only; sequential releases consume additional privacy budget.')
 con=load('contacts');out['contacts.svg']=lineplot('LUNAR GATEWAY Courier: information age between contacts','Derived from Synthetic | four ideal contact windows',[('age of newest verified record',[(x['time_min'],x['age_s']/60) for x in con['rows']])],'Relative mission time (minutes)','Age of information (minutes)','Every modeled contact succeeds; attempt count is an energy proxy, not measured spacecraft power.')
 clk=load('clocks');body=''
 px=lambda x:95+(x-94)/30*855
 for i,e in enumerate(clk['events']):
  y=190+i*100;lo,hi=e['interval_s']
  body+=label(35,y-30,e['name'],17,C[i])+f'<path d="M{px(lo):.2f} {y} H{px(hi):.2f}" stroke="{C[i]}" stroke-width="12"/><circle cx="{px(e["observed_s"]):.2f}" cy="{y}" r="8" fill="white"/>'+label(px(hi)+15,y+5,f'[{lo:g}, {hi:g}] s',14)
 for x in [95,100,105,110,115,120]:body+=label(px(x),464,x,13,anchor='middle')
 body+=label(500,496,'Observed timestamp with declared closed uncertainty interval (seconds)',15,anchor='middle')+label(95,531,'Sensor/gateway ordering is indeterminate; both precede archive.',15)
 out['clocks.svg']=frame('EUROPA Clock: preserve uncertainty in event ordering','Derived from Synthetic | declared clock error bounds',body,'Intervals establish temporal precedence, not causality; timestamp sort reverses two fixture events.')
 kev=json.loads((R/'data/research/kev_snapshot.json').read_text());counts=collections.Counter(x['dateAdded'][:7] for x in kev['records']);recent=sorted(counts)[-12:]
 out['kev.svg']=bars('NEOWISE Chronicle: KEV catalog additions','Derived from Observed public catalog metadata | snapshot '+kev['date_released'][:10],[(s[2:],counts[s]) for s in recent],'Catalog entries added per month','Issuer catalog selection and addition dates only; these counts are not exploitation rates.')
 return {R/'research/assets'/k:v for k,v in out.items()}

def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args()
 for path,s in render().items():
  if a.check:
   if not path.exists() or path.read_text()!=s:raise SystemExit('Stale plot: '+path.name)
  else:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(s)
 print('Verified seven SVG figures bound to declared inputs and evidence classes.')
if __name__=='__main__':main()
