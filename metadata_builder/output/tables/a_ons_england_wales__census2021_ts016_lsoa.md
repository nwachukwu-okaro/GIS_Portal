# Census2021 Ts016 Lsoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts016_lsoa`
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
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts016_lsoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 35672
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Census2021 Ts016 Lsoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts016 lsoa.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `geography_code` | `text` | Code assigned by the source dataset. |
| `total_all_usual_residents` | `bigint` | Count or numeric value for total all usual residents in the represented area. |
| `born_in_the_uk` | `bigint` | Count or numeric value for born in the uk in the represented area. |
| `col_10_years_or_more` | `bigint` | Count or numeric value for col 10 years or more in the represented area. |
| `col_5_years_or_more_but_less_than_10_years` | `bigint` | Count or numeric value for col 5 years or more but less than 10 years in the represented area. |
| `col_2_years_or_more_but_less_than_5_years` | `bigint` | Count or numeric value for col 2 years or more but less than 5 years in the represented area. |
| `less_than_2_years` | `bigint` | Count or numeric value for less than 2 years in the represented area. |
