# Passport Held Intzone

## Overview

- **Identifier:** `a_nrs_scotland/passport_held_intzone`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `passport_held_intzone`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Passport Held Intzone is an authoritative dataset published by National Records of Scotland. It contains records relating to passport held intzone.

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
| `all_people` | `double precision` | Recorded census measure for the category "all people" in the represented area. Units and population base require the source table. |
| `europe_total` | `double precision` |  |
| `europe_united_kingdom` | `double precision` |  |
| `europe_ireland` | `double precision` |  |
| `europe_eu_member_countries` | `double precision` |  |
| `europe_rest_of_europe` | `double precision` |  |
| `africa` | `double precision` |  |
| `middle_east_and_asia` | `double precision` |  |
| `antarctica_and_oceania` | `double precision` |  |
| `no_passport` | `double precision` |  |
| `the_americas_and_the_caribbean` | `double precision` |  |
