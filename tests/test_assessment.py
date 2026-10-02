import json,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def load(p):return json.loads((R/p).read_text())

class AssessmentIntegrity(unittest.TestCase):
 def test_exact_learning_progression(self):
  x=load('data/assessment/modules.json');m=x['modules']
  self.assertEqual(x['count'],150)
  self.assertEqual([i['id'] for i in m],[f'RT{i:03d}' for i in range(1,151)])
  self.assertEqual(len({i['title'].casefold() for i in m}),150)
  for phase in range(1,7):self.assertEqual(sum(i['phase']==phase for i in m),25)
 def test_research_links_have_existing_missions(self):
  ids={x['id'] for x in load('data/ideas.json')['ideas']}
  for m in load('data/assessment/modules.json')['modules']:
   self.assertIn(m['related_mission'],ids)
   self.assertTrue((R/'assessment/modules'/f'{m["id"]}.md').exists())
   self.assertIn('untouched', (R/'assessment/modules'/f'{m["id"]}.md').read_text())
 def test_source_claim_profile_referential_integrity(self):
  sources={s['id'] for s in load('data/intelligence/sources.json')}
  claims={c['id']:c for c in load('data/intelligence/claims.json')}
  self.assertEqual(len(sources),6);self.assertEqual(len(claims),11)
  for c in claims.values():
   self.assertIn(c['source_id'],sources);self.assertTrue(c['limitation'])
  for p in load('data/intelligence/profiles.json'):
   for cid in p['claim_ids']:self.assertIn(cid,claims)
 def test_public_bylines_are_not_threat_actor_labels(self):
  profiles=load('data/intelligence/profiles.json')
  bylines=[p for p in profiles if p['slug'] in {'ek0mssavi0r','leviathan','trilltechnician','n0mad1k'}]
  self.assertEqual(len(bylines),4)
  self.assertTrue(all(p['entity_type'].startswith('Public homepage') for p in bylines))
  self.assertTrue(all('Source-bounded' in p['status'] for p in bylines))
 def test_persona_and_operator_claims_remain_distinct(self):
  c={c['id']:c for c in load('data/intelligence/claims.json')}
  self.assertNotEqual(c['CL01']['subject'],c['CL02']['subject'])
  self.assertIn('does not establish',c['CL01']['limitation'])
  self.assertIn('does not identify',c['CL02']['limitation'])
 def test_research_mission_and_module_counts_not_conflated(self):
  self.assertEqual(load('data/research/catalog.json')['count'],180)
  self.assertEqual(load('data/ideas.json')['count'],150)
  self.assertEqual(load('data/assessment/modules.json')['count'],150)

if __name__=='__main__':unittest.main()
