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
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
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
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `all_occupied_households` | `double precision` | Recorded census measure for the category "all occupied households" in the represented area. Units and population base require the source table. |
| `one_person_household` | `double precision` | Recorded census measure for the category "one person household" in the represented area. Units and population base require the source table. |
| `all_household_members_have_the_same_ethnic_group` | `double precision` |  |
| `different_identities_between_the_generations_only` | `double precision` |  |
| `different_identities_within_partnerships_whether_or_not_also` | `double precision` |  |
| `any_other_combination_of_multiple_ethnic_identities` | `double precision` |  |
