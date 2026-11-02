import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import build_reviews
import build_labs


class PrimaryResearch(unittest.TestCase):
    def test_every_review_binds_real_features_to_retrieval_receipts(self):
        catalog,sources=build_reviews.load();lookup={s['id']:s for s in sources['sources']}
        self.assertGreaterEqual(len(catalog['entries']),60)
        self.assertGreaterEqual(len(lookup),47)
        for entry in catalog['entries']:
            self.assertGreaterEqual(len(entry['specs']),3)
            self.assertTrue(set(entry['source_ids'])<=lookup.keys())
            self.assertTrue(all(f['source_id'] in entry['source_ids'] for f in entry['specs']))
            self.assertIn('review',entry['basis'].lower())
        self.assertTrue(all('youtube' not in s['url'] for s in lookup.values()))

    def test_model_and_source_disagreements_are_not_silently_flattened(self):
        entries={e['id']:e for e in build_reviews.load()[0]['entries']}
        self.assertNotEqual(entries['thinknode-m1']['specs'],entries['thinknode-m5']['specs'])
        self.assertIn('PoE',entries['thinknode-m7']['assessment'])
        self.assertIn('unstable',entries['proxmark5']['specs'][-1]['value'])
        self.assertIn('discrepancy',json.dumps(entries['hydra-rf-424']).lower())

    def test_rendered_metadata_is_escaped_and_video_directory_removed(self):
        catalog,sources=build_reviews.load();catalog['entries'][0]['name']='<img src=x onerror=alert(1)>'
        sources['sources'][0]['title']='<script>alert(1)</script>'
        with patch.object(build_reviews,'load',return_value=(catalog,sources)):
            output=build_reviews.content()
        self.assertNotIn('<img src=x onerror=alert(1)>',output)
        self.assertNotIn('<script>alert(1)</script>',output)
        self.assertIn('&lt;script&gt;',output)
        self.assertNotIn('creator-library',output);self.assertNotIn('video-sources',output)

    def test_mixed_order_is_complete_stable_and_category_diverse(self):
        entries=build_reviews.load()[0]['entries'];mixed=build_reviews.mixed_entries(entries)
        self.assertEqual({e['id'] for e in entries},{e['id'] for e in mixed})
        self.assertEqual(mixed,build_reviews.mixed_entries(entries))
        count=len({e['category'] for e in entries})
        self.assertEqual(len({e['category'] for e in mixed[:count]}),count)

    def test_invalid_primary_citation_prevents_publication(self):
        catalog,sources=build_reviews.load()
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);(root/'data/reviews').mkdir(parents=True)
            catalog['entries'][0]['specs'][0]['source_id']='missing-source'
            (root/'data/reviews/catalog.json').write_text(json.dumps(catalog))
            (root/'data/reviews/sources.json').write_text(json.dumps(sources))
            with patch.object(build_reviews,'ROOT',root):
                with self.assertRaisesRegex(ValueError,'Unbound feature'):build_reviews.load()

    def test_every_product_has_full_documentation_and_every_lab_has_a_method(self):
        files=build_reviews.generated_files()
        for entry in build_reviews.load()[0]['entries']:
            document=files[Path(entry['doc'])]
            for heading in ['## Documented features','## Our review','## Choose it when','## Skip it when','## Setup and firmware route','## Sources read']:
                self.assertIn(heading,document)
        labs=build_labs.load();self.assertEqual(len(labs),24)
        self.assertEqual({e['mode'] for e in labs},{'Offline fixture','Physical device','Optional tool'})
        self.assertTrue(all(e['expected'] and e['failures'] for e in labs))


if __name__=='__main__':unittest.main()
