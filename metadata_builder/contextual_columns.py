"""Conservative, reproducible description enrichment; no network or DB access.

Only replaces empty/known boilerplate descriptions. Specific pre-existing
descriptions and database comments are preserved, not claimed as reverified.
"""
import re

RULE_VERSION = 2
LOGICAL_STATUS_SOURCE = 'https://docs.os.uk/os-downloads/products/addresses-and-names-portfolio/addressbase-fundamentals/code-lists-and-enumerations/logicalstatuscode'
IDENTIFIER_SOURCE = 'https://www.gov.uk/government/publications/open-standards-for-government/identifying-property-and-street-information'
GENERIC = (
    r'^Source attribute; its precise meaning has not yet been documented\.$',
    r'^Publisher-supplied .+ for the represented feature or record\.$',
    r'^Count or numeric value for .+ in the represented area\.$',
    r'^Publisher-assigned .+ for the record\.$',
    r'^Numeric .+ value recorded for the feature\.$',
    r'^Date or year recorded for .+\.$',
    r'^Percentage for the .+ measure in the represented area\.$',
)
STAT_SCHEMAS = {'a_ons_england_wales', 'a_nrs_scotland', 'a_nisra_nireland',
                'a_ireland_cso', 'a_irl_central_statistics_office',
                'a_ons_nrs_nirsa_census_data'}


def generic(description):
    return not description or any(re.fullmatch(p, description) for p in GENERIC)


def decide(record, column):
    """Return description, basis, evidence; never infer measurement units."""
    name = column['name'].lower()
    schema = record.get('schema', '')
    table = record.get('table', '')
    samples = (column.get('value_profile') or {}).get('examples') or []
    evidence = f'Schema={schema}; table={table}; column={column["name"]}; type={column.get("data_type")}'
    if schema == 'a_os_addressbase_premium' and table in {'blpu', 'lpi'} and name == 'logical_status':
        return 'Code indicating the lifecycle status of the address record.', 'official_definition_with_context', LOGICAL_STATUS_SOURCE
    primary = record.get('primary_key') or []
    if column['name'] in primary:
        label = 'Component of the primary key' if len(primary) > 1 else 'Primary-key identifier'
        return f'{label} for records in {table}.', 'verified_local_structure', evidence + '; primary_key metadata'
    geometry = record.get('geometry') or {}
    if column['name'] == geometry.get('column'):
        geomtype, crs = geometry.get('type'), geometry.get('crs')
        detail = f' ({geomtype})' if geomtype else ''
        return f'Spatial geometry{detail} of the feature' + (f' in {crs}.' if crs else '.'), 'verified_local_structure', evidence + '; geometry metadata'
    if schema.startswith('a_os_') or schema in {'a_tfgm', 'a_department_for_education', 'a_hm_land_registry'}:
        if name in {'uprn', 'usrn', 'parent_uprn'}:
            desc = {'uprn': 'Unique Property Reference Number identifying the addressable location.',
                    'usrn': 'Unique Street Reference Number identifying the street.',
                    'parent_uprn': 'Unique Property Reference Number of the parent addressable location.'}[name]
            return desc, 'official_definition_with_context', IDENTIFIER_SOURCE
    if schema in STAT_SCHEMAS:
        if name in {'geography', 'geogdesc'} and samples and all(isinstance(s, str) and re.search('[A-Za-z]', s) for s in samples):
            return 'Name or descriptive label of the geographical area represented by the row.', 'inferred_context', evidence + '; text area-name samples'
        if name in {'geocode', 'geogid', 'geography_code'}:
            return 'Code identifying the geographical area represented by the row.', 'inferred_context', evidence
        if name in {'year'}:
            return 'Reference year recorded for the statistical observation.', 'inferred_context', evidence
        if name in {'total_all_usual_residents', 'total_all_households', 'total_males', 'total_females'}:
            # Census products include counts AND percentages; the label alone
            # establishes the population group, not the unit or denominator.
            group = name.removeprefix('total_').replace('_', ' ')
            return f'Census total for {group} in the represented geographical area; measurement unit requires the table documentation.', 'inferred_context', evidence
        if name == 'population_density_number_of_usual_residents_per_hectare':
            return 'Population density expressed as the number of usual residents per hectare.', 'inferred_context', evidence
    if schema in {'a_ireland_cso', 'a_irl_central_statistics_office'} and ('boundar' in table or 'administrative' in table):
        names = {'english': 'English-language name of the administrative area.',
                 'gaeilge': 'Irish-language name of the administrative area.',
                 'county': 'County associated with the represented administrative area.',
                 'province': 'Province associated with the represented administrative area.'}
        if name in names:
            return names[name], 'inferred_context', evidence
    if schema == 'a_tfgm':
        rules = {
            ('bus_routes', 'service_no'): 'Displayed bus service number.',
            ('bus_routes', 'direction'): 'Direction of the bus service, such as inbound or outbound.',
            ('bus_routes', 'day'): 'Day category on which the bus service operates.',
            ('cycle_hubs_2022', 'hub_name'): 'Name of the cycle hub.',
            ('cycle_hubs_2022', 'open_mon_f'): 'Cycle-hub opening hours from Monday to Friday.',
            ('cycle_hubs_2022', 'open_sat'): 'Cycle-hub opening hours on Saturday.',
            ('cycle_hubs_2022', 'open_sun'): 'Cycle-hub opening hours on Sunday.',
        }
        if (table, name) in rules and samples:
            return rules[(table, name)], 'inferred_context', evidence + '; supporting sample values'
        if 'cycle_hub' in table and name in {'lockers', 'showers'} and samples and set(samples) <= {'Y', 'N'}:
            return f'Indicates whether {name} are available at the cycle hub (Y=yes; N=no).', 'inferred_context', evidence + '; Y/N samples'
    # Explicitly named coordinates are safe; units are deliberately not invented.
    if name in {'centroid_x', 'centroid_y'}:
        return f'{name[-1].upper()} coordinate of the feature centroid; units and reference system are not confirmed for this attribute.', 'inferred_context', evidence
    if name in {'url', 'hyperlink', 'web_url', 'website'} and samples and all(isinstance(s, str) and re.match(r'^https?://\S+$', s) for s in samples):
        return 'Web address associated with the record.', 'inferred_context', evidence + '; HTTP(S) URL samples'
    return infer_second_pass(record, column, evidence)


def infer_second_pass(record, column, evidence):
    """Scoped interpretations: describe the concept without inventing units/codes."""
    name = column['name'].lower()
    schema, table = record.get('schema', ''), record.get('table', '')
    samples = (column.get('value_profile') or {}).get('examples') or []
    dtype = (column.get('data_type') or '').lower()
    numeric = any(t in dtype for t in ('int', 'numeric', 'decimal', 'double', 'real', 'float'))
    if dtype == 'text' and samples:
        numeric = all(re.fullmatch(r'-?\d[\d,]*(?:\.\d+)?%?', str(s).strip()) for s in samples)
    # PostgreSQL truncation limit and import-disambiguated names obscure meaning.
    ambiguous = len(name.encode('utf-8')) >= 63 or bool(re.match(r'(unnamed|unknown|field|column)_?\d*$', name))
    if schema in STAT_SCHEMAS and numeric and not ambiguous:
        age = re.fullmatch(r'age_(\d{1,3})(?:_(\d{1,3}))?_(males|females|total)', name)
        if age:
            age_label = age[1] + (f' to {age[2]}' if age[2] else '')
            people = 'persons' if age[3] == 'total' else age[3]
            return f'Census measure for {people} aged {age_label} years in the represented area; count or percentage must be checked against the source table.', 'inferred_context', evidence + '; explicit age and sex labels'
        # Do not turn total_1, other_2, geographic labels, or opaque CSO codes
        # into invented populations. Only self-describing category prefixes.
        safe_prefixes = ('total_all_', 'total_no_of_', 'all_people', 'all_households',
                         'all_occupied_households', 'one_person_household',
                         'born_in_', 'lives_in_', 'speaks_', 'reads_', 'writes_',
                         'ethnic_group_', 'religion_', 'country_of_birth_',
                         'household_contains_', 'address_one_year_ago_')
        if name.startswith(safe_prefixes) and not re.search(r'_\d+$', name):
            label = name.replace('_', ' ').replace(' no of ', ' number of ')
            label = re.sub(r'\b(uk|ni)\b', lambda m: m[0].upper(), label)
            return f'Recorded census measure for the category "{label}" in the represented area. Units and population base require the source table.', 'inferred_medium', evidence + '; readable population/category label; units not confirmed'
    if schema == 'a_tfgm' and 'cycle_hub' in table and name == 'capacity' and numeric:
        return 'Capacity recorded for the cycle hub; the capacity unit has not been confirmed.', 'inferred_medium', evidence
    if schema.startswith('a_os_addressbase'):
        address_fields = {
            'building_number': 'Building number used in the address.',
            'building_name': 'Building name used in the address.',
            'dependent_thoroughfare': 'Dependent thoroughfare component of the address.',
            'post_town': 'Postal town component of the address.',
            'postcode_locator': 'Postcode recorded as a location reference for the address.',
            'organisation': 'Organisation name associated with the address.',
            'cross_reference': 'Reference linking this address record to another source record; the target system is not confirmed.',
            'x_coordinate': 'X coordinate recorded for the address; coordinate units require the product documentation.',
            'y_coordinate': 'Y coordinate recorded for the address; coordinate units require the product documentation.',
        }
        if name in address_fields:
            return address_fields[name], 'inferred_medium', evidence + '; addressing dataset context'
    if name in {'guid', 'globalid'} and samples and all(re.fullmatch(r'\{?[0-9A-Fa-f]{8}(?:-[0-9A-Fa-f]{4}){3}-[0-9A-Fa-f]{12}\}?', str(s)) for s in samples):
        return 'UUID-formatted identifier associated with the record; persistence across releases is not confirmed.', 'inferred_context', evidence + '; UUID-formatted samples'
    if not ambiguous and name in {'validfrom', 'validto', 'date_created', 'date_updated', 'date_updat', 'last_update_date'} and ('date' in dtype or 'time' in dtype):
        description = {'validfrom': 'Date or time from which the record is considered valid.',
                       'validto': 'Date or time until which the record is considered valid.',
                       'date_created': 'Creation date or time recorded for this record.',
                       'date_updated': 'Most recent update date or time recorded for this record.',
                       'date_updat': 'Update date recorded for this record.',
                       'last_update_date': 'Most recent update date recorded for this record.'}[name]
        return description, 'inferred_medium', evidence + '; date/time data type'
    return '', 'unresolved', evidence + '; insufficient evidence for a specific meaning'


def enrich_record(record):
    changes = []
    for column in record.get('columns', []):
        before = column.get('description')
        previous_review = column.get('description_review', {})
        if column.get('provenance') == 'database_comment' or (not generic(before) and not previous_review):
            continue
        description, basis, evidence = decide(record, column)
        provenance = 'authoritative' if basis == 'official_definition_with_context' else 'unresolved' if basis == 'unresolved' else 'inferred'
        confidence = 'low' if basis == 'unresolved' else 'medium' if basis == 'inferred_medium' else 'high'
        review = {'basis': basis, 'evidence': evidence, 'rule_version': RULE_VERSION}
        if before == description and previous_review == review and column.get('provenance') == provenance and column.get('confidence') == confidence:
            continue
        column['description'] = description
        column['description_review'] = review
        column['provenance'] = provenance
        column['confidence'] = confidence
        changes.append({'column': column['name'], 'before': before, 'after': description,
                        'basis': basis, 'evidence': evidence, 'provenance': provenance,
                        'confidence': confidence})
    return changes
