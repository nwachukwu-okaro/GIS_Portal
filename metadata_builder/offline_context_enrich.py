"""Conservatively enrich remaining placeholders without network or API access."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import defaultdict

import yaml

import build


PLACEHOLDER = 'Source attribute; its precise meaning has not yet been documented.'
NUMERIC = ('int', 'numeric', 'decimal', 'real', 'double')
ABBREVIATIONS = {
    'pop': 'population', 'hh': 'households', 'm': 'male', 'f': 'female',
    'tot': 'total', 'no': 'number', 'pct': 'percentage', 'yr': 'year',
    'desc': 'description', 'ref': 'reference', 'id': 'identifier',
}


def words(name):
    value = re.sub(r'([a-z])([A-Z])', r'\1_\2', name)
    return [ABBREVIATIONS.get(part.lower(), part.lower()) for part in re.split(r'[^A-Za-z0-9]+', value) if part]


def infer(name, data_type, table):
    lower = name.lower()
    age = re.fullmatch(r't\d+_\d+age(\d+|\d+_\d+)([mft])', lower)
    if age:
        age_value = age.group(1).replace('_', ' to ')
        sex = {'m': 'males', 'f': 'females', 't': 'persons'}[age.group(2)]
        return f"Census count of {sex} aged {age_value} in the represented area.", 'population_count'

    parts = words(name)
    if not parts:
        return None
    opaque = len(parts) == 1 and (
        bool(re.search(r'\d', parts[0])) or
        (len(parts[0]) <= 5 and not re.search(r'[aeiou]', parts[0]))
    )
    if opaque:
        return None
    label = ' '.join(parts)
    is_numeric = any(token in (data_type or '').lower() for token in NUMERIC)
    if is_numeric:
        if any(token in lower for token in ('pct', 'percent', 'percentage')):
            return f"Percentage for the {label} measure in the represented area.", 'percentage'
        if any(token in lower for token in ('area', 'length', 'height', 'depth', 'easting', 'northing', 'lat', 'lon')):
            return f"Numeric {label} value recorded for the feature.", 'measure'
        return f"Count or numeric value for {label} in the represented area.", 'statistical_value'
    if lower.endswith(('date', '_date', 'datetime', '_year', 'year')):
        return f"Date or year recorded for {label}.", 'date'
    if lower.endswith(('id', '_id', 'code', '_code', 'ref', '_ref')):
        return f"Publisher-assigned {label} for the record.", 'source_identifier'
    return f"Publisher-supplied {label} for the represented feature or record.", 'source_attribute'


def collect(schema):
    result = {}
    for path in sorted(build.METADATA_DIR.glob(f'{schema}__*.json')):
        record = build.read_json(path)
        for column in record.get('columns', []):
            if column.get('description') != PLACEHOLDER or column['name'].lower() in result:
                continue
            inferred = infer(column['name'], column.get('data_type', ''), record['table'])
            if inferred:
                description, role = inferred
                result[column['name'].lower()] = {
                    'description': description,
                    'semantic_role': role,
                }
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--schema', action='append', dest='schemas')
    args = parser.parse_args()
    dictionary = build.read_yaml(build.CONFIG_DIR / 'column_dictionary.yml')
    schemas = args.schemas or sorted({
        build.read_json(path)['schema'] for path in build.METADATA_DIR.glob('*.json')
        if build.read_json(path)['schema'] not in {
            'a_historic_england', 'a_british_geological_survey',
            'a_department_for_education', 'a_dft', 'a_environment_agency',
            'a_forestry_commission', 'a_greater_manchester_ecology_unit',
            'a_hm_land_registry',
        }
    })
    for schema in schemas:
        additions = collect(schema)
        target = dictionary.setdefault('schemas', {}).setdefault(schema, {}).setdefault('columns', {})
        target.update(additions)
        build.atomic_write(
            build.CONFIG_DIR / 'column_dictionary.yml',
            yaml.safe_dump(dictionary, sort_keys=False, allow_unicode=True, width=120),
        )
        subprocess.run(
            [sys.executable, str(build.SCRIPT_DIR / 'refresh_curated.py'), '--schema', schema],
            check=True,
        )
        print(f"OFFLINE {schema}: {len(additions)} reusable definitions added")


if __name__ == '__main__':
    main()
