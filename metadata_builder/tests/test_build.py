import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parents[1]
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import build


class MetadataBuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources = build.read_yaml(build.CONFIG_DIR / 'sources.yml')
        cls.overrides = build.read_yaml(build.CONFIG_DIR / 'table_overrides.yml')
        cls.dictionary = build.read_yaml(build.CONFIG_DIR / 'column_dictionary.yml')

    def test_every_configured_schema_is_authoritative(self):
        schemas = self.sources['schemas']
        self.assertGreaterEqual(len(schemas), 45)
        self.assertTrue(all(name.startswith('a_') for name in schemas))

    def test_mock_tables_build_valid_records(self):
        tables, errors, _database = build.extract_schema.extract_mock()
        self.assertEqual(errors, [])
        for table in tables:
            record, digest = build.build_record(
                table, self.sources, self.overrides, self.dictionary,
            )
            self.assertEqual(build.validate_record(record), [])
            self.assertEqual(len(digest), 64)
            self.assertTrue(record['publisher']['source_url'])

    def test_report_names_failed_tables_and_counts_totals(self):
        results = [
            {'schema': 'a_example', 'table': 'good', 'status': 'built'},
            {
                'schema': 'a_example', 'table': 'bad', 'status': 'failed',
                'stage': 'build', 'error_type': 'ValueError',
                'message': 'invalid metadata', 'retryable': True,
            },
        ]
        report = build.build_report('start', 'finish', 'test', results, [], 1)
        stats = report['schemas']['a_example']
        self.assertEqual(stats['successful'], 1)
        self.assertEqual(stats['failed'], 1)
        self.assertEqual(stats['failed_tables'][0]['table'], 'bad')
        self.assertEqual(report['totals']['tables_found'], 2)

    def test_specialist_columns_are_schema_scoped_and_planner_ready(self):
        tables, _errors, _database = build.extract_schema.extract_mock()
        records = {}
        for table in tables:
            record, _digest = build.build_record(
                table, self.sources, self.overrides, self.dictionary,
            )
            records[record['identifier']] = record

        bgs = records['a_british_geological_survey/625k_bedrock_geology']
        bgs_columns = {column['name']: column for column in bgs['columns']}
        self.assertEqual(bgs_columns['lex']['semantic_role'], 'geological_unit_code')
        self.assertTrue(bgs_columns['lex']['joinable'])
        self.assertEqual(bgs_columns['lex_d']['related_column'], 'lex')

        heritage = records['a_historic_england/battlefields']
        heritage_columns = {column['name']: column for column in heritage['columns']}
        self.assertEqual(heritage_columns['regdate']['semantic_role'], 'designation_date')
        self.assertEqual(heritage_columns['listentry']['identifier_system'], 'NHLE')

        built_up = records['a_os_built_up_areas/os_open_built_up_areas']
        built_columns = {column['name']: column for column in built_up['columns']}
        self.assertTrue(built_columns['name1_text']['searchable'])
        self.assertIn('Medway', built_columns['name1_text']['value_profile']['examples'])
        self.assertEqual(built_columns['gsscode']['identifier_system'], 'ONS_GSS')
        self.assertTrue(built_columns['gsscode']['joinable'])
        self.assertFalse(built_columns['fid']['joinable'])
        self.assertIn('name1_text', built_up['discovery_hints']['searchable_columns'])
        self.assertIn('gsscode', built_up['discovery_hints']['joinable_columns'])
        self.assertIn('user for confirmation', built_up['discovery_hints']['relationship_policy'])

    def test_spatial_records_define_crs_requirements(self):
        tables, _errors, _database = build.extract_schema.extract_mock()
        record, _digest = build.build_record(
            tables[0], self.sources, self.overrides, self.dictionary,
        )
        self.assertEqual(record['geometry']['units'], 'metres')
        self.assertTrue(record['operation_requirements']['intersect']['requires_matching_crs'])
        self.assertTrue(record['operation_requirements']['buffer']['requires_projected_crs'])


if __name__ == '__main__':
    unittest.main()
