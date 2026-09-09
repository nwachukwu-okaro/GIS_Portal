"""Offline regression tests: python -m unittest discover -s scripts -p 'test_migrate_fix_links.py'."""
import json
import unittest
from unittest.mock import MagicMock

from migrate_fix_links import normalize_links, repair_links


class LinksTests(unittest.TestCase):
    def test_bare_url(self):
        self.assertEqual(normalize_links('https://example.com/data'),
                         'Dataset,Publisher resource,WWW:LINK,https://example.com/data')

    def test_json_and_delimiters(self):
        value = json.dumps([{'title': 'A,B^C', 'href': 'https://example.com/a,b^c'},
                            {'href': 'postgresql://host/db/schema/table'}])
        result = normalize_links(value)
        for link in result.split('^'):
            fields = link.split(',')
            self.assertEqual(len(fields), 4)
            self.assertEqual(fields[2], 'WWW:LINK')
        self.assertIn('/a%2Cb%5Ec', result)
        self.assertEqual(normalize_links(result), result)

    def test_correct_links_unchanged(self):
        value = 'Dataset,Resource,WWW:LINK,https://example.com/a^Other,,WWW:LINK,https://example.com/b'
        self.assertEqual(normalize_links(value), value)

    def test_null_empty(self):
        for value in (None, '', '  ', '[]'):
            self.assertIsNone(normalize_links(value))

    def test_invalid_not_silently_discarded(self):
        for value in ('garbage', '[bad json', '[{}]', 'A,B,C,https://example.com^broken'):
            with self.assertRaises(ValueError):
                normalize_links(value)

    def connection(self, rows):
        conn = MagicMock()
        cur = conn.cursor.return_value.__enter__.return_value
        cur.fetchall.return_value = rows
        cur.rowcount = 1
        return conn, cur

    def test_dry_run_no_writes(self):
        conn, cur = self.connection([('id', 'https://example.com')])
        self.assertEqual(repair_links(conn, True), 1)
        self.assertEqual(cur.execute.call_count, 1)
        conn.commit.assert_not_called()

    def test_only_links_updated(self):
        conn, cur = self.connection([('id', 'https://example.com')])
        repair_links(conn)
        statement, params = cur.execute.call_args.args
        self.assertIn('SET links = %s', statement)
        self.assertEqual(params[1:], ('id', 'https://example.com'))
        conn.commit.assert_called_once()

    def test_error_rolls_back(self):
        conn, cur = self.connection([('first', 'https://example.com'), ('bad', 'nonsense')])
        with self.assertRaises(ValueError):
            repair_links(conn)
        conn.rollback.assert_called_once()
        conn.commit.assert_not_called()


if __name__ == '__main__':
    unittest.main()
