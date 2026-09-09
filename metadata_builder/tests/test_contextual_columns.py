import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from contextual_columns import enrich_record, generic
from review_column_descriptions import update_markdown


class ContextualColumnsTests(unittest.TestCase):
    def record(self, name, description='', **kwargs):
        return {'schema': 'a_os_addressbase_premium', 'table': 'blpu',
                'primary_key': [], 'columns': [{'name': name, 'data_type': 'bigint',
                'description': description, 'provenance': 'safe_fallback', **kwargs}]}

    def test_official_identifier_is_not_count(self):
        record = self.record('uprn', 'Count or numeric value for uprn in the represented area.')
        enrich_record(record)
        self.assertIn('Unique Property Reference Number', record['columns'][0]['description'])
        self.assertEqual(record['columns'][0]['confidence'], 'high')
        self.assertEqual(record['columns'][0]['provenance'], 'authoritative')

    def test_ambiguous_is_empty(self):
        record = self.record('status', 'Publisher-supplied status for the represented feature or record.')
        enrich_record(record)
        self.assertEqual(record['columns'][0]['description'], '')

    def test_primary_key_verified_not_assumed(self):
        record = self.record('thing_pk')
        enrich_record(record)
        self.assertEqual(record['columns'][0]['description'], '')
        record['primary_key'] = ['thing_pk']
        enrich_record(record)
        self.assertIn('Primary-key identifier', record['columns'][0]['description'])

    def test_specific_description_preserved(self):
        desc = 'Numeric BGS index for the oldest age boundary of the deposit.'
        self.assertFalse(generic(desc))
        record = self.record('max_age_no', desc)
        before = copy.deepcopy(record)
        self.assertEqual(enrich_record(record), [])
        self.assertEqual(record, before)

    def test_database_comment_preserved(self):
        record = self.record('status', 'Publisher-assigned status for the record.', provenance='database_comment')
        self.assertEqual(enrich_record(record), [])

    def test_census_units_not_invented(self):
        record = self.record('total_males')
        record['schema'] = 'a_ons_england_wales'
        enrich_record(record)
        self.assertIn('unit requires', record['columns'][0]['description'])
        self.assertEqual(record['columns'][0]['confidence'], 'high')

    def test_idempotent(self):
        for name in ('uprn', 'unknown_37'):
            record = self.record(name)
            enrich_record(record)
            before = copy.deepcopy(record)
            self.assertEqual(enrich_record(record), [])
            self.assertEqual(before, record)

    def test_markdown_only_columns(self):
        text = '# Title\n\n## Columns\n\n| Column | Type | Description |\n|---|---|---|\n| `status` | `text` | Old |\n\n## Other\nKeep me\n'
        updated = update_markdown(text, [{'name': 'status', 'description': ''}])
        self.assertEqual(updated, text.replace('| Old |', '|  |'))

    def test_medium_capacity(self):
        record = self.record('capacity')
        record.update(schema='a_tfgm', table='cycle_hubs_2022')
        enrich_record(record)
        col = record['columns'][0]
        self.assertEqual((col['provenance'], col['confidence']), ('inferred', 'medium'))
        self.assertNotIn('spaces', col['description'])

    def test_age_inference_and_opaque_columns(self):
        record = self.record('age_15_males')
        record['schema'] = 'a_ireland_cso'
        enrich_record(record)
        self.assertIn('males aged 15', record['columns'][0]['description'])
        for name in ('total_1', 'unnamed_2', 't1_2sglm', 'other', 'country_of_birth_' + 'x'*60):
            record = self.record(name)
            record['schema'] = 'a_ons_england_wales'
            enrich_record(record)
            self.assertEqual(record['columns'][0]['description'], '')
            self.assertEqual(record['columns'][0]['confidence'], 'low')

    def test_pass_one_labels_updated(self):
        record = self.record('uprn', 'Unique Property Reference Number identifying the addressable location.',
                             provenance='official_definition_with_context', confidence='verified',
                             description_review={'rule_version': 1})
        enrich_record(record)
        self.assertEqual(record['columns'][0]['provenance'], 'authoritative')
        self.assertEqual(enrich_record(record), [])


if __name__ == '__main__':
    unittest.main()
