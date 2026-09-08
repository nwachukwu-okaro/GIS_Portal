# Multiple Ethnic Group Intzone

## Overview

- **Identifier:** `a_nrs_scotland/multiple_ethnic_group_intzone`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `multiple_ethnic_group_intzone`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Multiple Ethnic Group Intzone is an authoritative dataset published by National Records of Scotland. It contains records relating to multiple ethnic group intzone.

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
| `all_occupied_households` | `double precision` | Count or numeric value for all occupied households in the represented area. |
| `one_person_household` | `double precision` | Count or numeric value for one person household in the represented area. |
| `all_household_members_have_the_same_ethnic_group` | `double precision` | Count or numeric value for all household members have the same ethnic group in the represented area. |
| `different_identities_between_the_generations_only` | `double precision` | Count or numeric value for different identities between the generations only in the represented area. |
| `different_identities_within_partnerships_whether_or_not_also` | `double precision` | Count or numeric value for different identities within partnerships whether or not also in the represented area. |
| `any_other_combination_of_multiple_ethnic_identities` | `double precision` | Count or numeric value for any other combination of multiple ethnic identities in the represented area. |
