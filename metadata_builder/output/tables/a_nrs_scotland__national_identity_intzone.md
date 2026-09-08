# National Identity Intzone

## Overview

- **Identifier:** `a_nrs_scotland/national_identity_intzone`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `national_identity_intzone`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

National Identity Intzone is an authoritative dataset published by National Records of Scotland. It contains records relating to national identity intzone.

## Lineage

Published by National Records of Scotland as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `all_people` | `double precision` | Count or numeric value for all people in the represented area. |
| `scottish_identity_only` | `double precision` | Count or numeric value for scottish identity only in the represented area. |
| `british_identity_only` | `double precision` | Count or numeric value for british identity only in the represented area. |
| `scottish_and_british_identities_only` | `double precision` | Count or numeric value for scottish and british identities only in the represented area. |
| `scottish_and_any_other_identities` | `double precision` | Count or numeric value for scottish and any other identities in the represented area. |
| `english_identity_only` | `double precision` | Count or numeric value for english identity only in the represented area. |
| `any_other_combination_of_uk_identities_uk_only` | `double precision` | Count or numeric value for any other combination of uk identities uk only in the represented area. |
| `other_identity_only_1` | `double precision` | Count or numeric value for other identity only 1 in the represented area. |
| `other_identity_and_at_least_one_uk_identity` | `double precision` | Count or numeric value for other identity and at least one uk identity in the represented area. |
