import datetime,hashlib,itertools,json,unittest
from pathlib import Path
from experiments.benchmark import (confusion,contacts,firmware_update,interval_order,
                                  privacy_scale,quantile,recovery,schedule_loss,telemetry)
R=Path(__file__).resolve().parents[1]

class Mechanics(unittest.TestCase):
 def test_missing_is_not_negative(self):
  result=confusion([1,1,0],[1,0,1],[True,False,True])
  self.assertEqual((result['tp'],result['fn'],result['fp'],result['observed']),(1,0,1,2))
 def test_undefined_precision_is_explicit(self):
  self.assertIsNone(confusion([0,1],[0,0])['precision'])
 def test_invalid_lengths_rejected(self):
  with self.assertRaises(ValueError):confusion([1],[])
 def test_percentile_interpolation(self):self.assertEqual(quantile([0,10],.25),2.5)
 def test_no_threshold_uses_test_period(self):
  rows,res=telemetry();m=res['methods']['robust']
  vals=[(x['value']-m['center'])/m['scale'] for x in rows if x['split']=='validation' and x['observed'] and not x['anomaly']]
  self.assertEqual(m['threshold'],quantile(vals,.9975))
  self.assertEqual(m['observed_hours'],12)
 def test_fixture_does_not_invent_robust_improvement(self):
  _,res=telemetry()
  a,b=res['methods']['robust'],res['methods']['mean_std']
  self.assertEqual((a['tp'],a['fp'],a['fn']),(80,127,0))
  self.assertEqual((a['tp'],a['fp']),(b['tp'],b['fp']))
 def test_recovery_hand_checked_objective(self):
  loss,_=schedule_loss(['identity','console','ground_link','storage','payload','archive'])
  self.assertAlmostEqual(loss,.22*3+.08*4+.16*6+.25*11+.19*15+.1*21)
 def test_prerequisites_enforced(self):
  with self.assertRaises(ValueError):schedule_loss(['payload','identity','console','ground_link','storage','archive'])
 def test_recovery_feasible_optimum(self):
  r=recovery();self.assertEqual(r['feasible_orders'],25)
  self.assertAlmostEqual(r['comparisons'][-1]['loss_service_min'],9.64)
  self.assertLessEqual(r['comparisons'][-1]['loss_service_min'],r['comparisons'][0]['loss_service_min'])
 def test_reset_recovery_boundaries(self):
  self.assertTrue(all(firmware_update(i)['safe'] for i in range(4)))
  self.assertFalse(firmware_update(1,False)['safe'])
  self.assertFalse(firmware_update(2,False)['safe'])
  self.assertTrue(firmware_update(3,False)['safe'])
 def test_reset_invalid_cut(self):
  with self.assertRaises(ValueError):firmware_update(4)
 def test_timing_ambiguity_and_touching_bounds(self):
  self.assertEqual(interval_order([96,104],[97,109]),'indeterminate')
  self.assertEqual(interval_order([0,1],[1,2]),'indeterminate')
  self.assertEqual(interval_order([0,1],[2,3]),'before')
  self.assertEqual(interval_order([2,3],[0,1]),'after')
 def test_invalid_interval(self):
  with self.assertRaises(ValueError):interval_order([2,1],[3,4])
 def test_dp_scaling_and_invalid_budget(self):
  self.assertEqual(privacy_scale(.5,2),4)
  with self.assertRaises(ValueError):privacy_scale(0)
 def test_contact_receipt_and_age(self):
  r=contacts();self.assertEqual(r['verified_receipts'],32);self.assertEqual(r['max_age_s'],52*60)
  self.assertTrue(all(x['age_s']==0 for x in r['rows'] if x['contact']))
  self.assertTrue(all(x['age_s']>0 for x in r['rows'] if not x['contact']))

class Portfolio(unittest.TestCase):
 def test_original_catalog_digest_preserved(self):
  frozen=json.loads((R/'data/research/preservation.json').read_text())
  for name,digest in frozen['files'].items():
   self.assertEqual(hashlib.sha256((R/name).read_bytes()).hexdigest(),digest,name)
 def test_all_original_missions_and_new_ids(self):
  old=json.loads((R/'data/ideas.json').read_text())['ideas']
  new=json.loads((R/'data/research/catalog.json').read_text())['missions']
  self.assertEqual([x['id'] for x in new],[f'{i:03d}' for i in range(1,181)])
  for a,b in zip(old,new):
   for field in ['title','thesis','path','anchor','source_urls']:self.assertEqual(a[field],b[field])
 def test_keV_snapshot_semantics_and_dates(self):
  s=json.loads((R/'data/research/kev_snapshot.json').read_text());records=s['records']
  self.assertEqual(len(records),1731)
  self.assertEqual(len({x['cveID'] for x in records}),len(records))
  self.assertEqual(len(s['raw_sha256']),64)
  released=datetime.date.fromisoformat(s['date_released'][:10])
  for r in records:
   self.assertEqual(set(r),set(s['fields']))
   self.assertLessEqual(datetime.date.fromisoformat(r['dateAdded']),released)
 def test_fixture_manifest_hashes(self):
  x=json.loads((R/'data/synthetic/manifest.json').read_text())
  for name,item in x['files'].items():
   b=(R/'data/synthetic'/name).read_bytes()
   self.assertEqual(hashlib.sha256(b).hexdigest(),item['sha256'])
   self.assertEqual(len(b),item['bytes'])
 def test_source_refs_and_output_files(self):
  refs={x['id'] for x in json.loads((R/'data/research/resources.json').read_text())}
  for m in json.loads((R/'data/research/catalog.json').read_text())['missions']:
   self.assertIn(m['resource_id'],refs)
   self.assertTrue((R/m['research_path']).exists())
   self.assertEqual(m['evidence_class'],'Proposed')

if __name__=='__main__':unittest.main()
