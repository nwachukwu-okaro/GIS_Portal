# Census2021 Ts059 Lsoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts059_lsoa`
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
- **Table:** `census2021_ts059_lsoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 35672
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Census2021 Ts059 Lsoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts059 lsoa.

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
| `total_all_usual_residents_aged_16_years_and_over_in_employment` | `bigint` | Count or numeric value for total all usual residents aged 16 years and over in employment in the represented area. |
| `part_time` | `bigint` | Count or numeric value for part time in the represented area. |
| `part_time_15_hours_or_less_worked` | `bigint` | Count or numeric value for part time 15 hours or less worked in the represented area. |
| `part_time_16_to_30_hours_worked` | `bigint` | Count or numeric value for part time 16 to 30 hours worked in the represented area. |
| `full_time` | `bigint` | Count or numeric value for full time in the represented area. |
| `full_time_31_to_48_hours_worked` | `bigint` | Count or numeric value for full time 31 to 48 hours worked in the represented area. |
| `full_time_49_or_more_hours_worked` | `bigint` | Count or numeric value for full time 49 or more hours worked in the represented area. |
