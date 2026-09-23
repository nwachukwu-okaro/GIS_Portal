# Census2021 Ts016 Rgn

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts016_rgn`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence v3.0 — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts016_rgn`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 10
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Census2021 Ts016 Rgn is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts016 rgn.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `date` | `bigint` |  |
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `geography_code` | `text` | Code assigned by the source dataset. |
| `total_all_usual_residents` | `bigint` | Census total for all usual residents in the represented geographical area; measurement unit requires the table documentation. |
| `born_in_the_uk` | `bigint` | Recorded census measure for the category "born in the UK" in the represented area. Units and population base require the source table. |
| `col_10_years_or_more` | `bigint` |  |
| `col_5_years_or_more_but_less_than_10_years` | `bigint` |  |
| `col_2_years_or_more_but_less_than_5_years` | `bigint` |  |
| `less_than_2_years` | `bigint` |  |
