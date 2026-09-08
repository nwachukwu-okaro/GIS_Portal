# Census2021 Ts071 Rgn

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts071_rgn`
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
- **Table:** `census2021_ts071_rgn`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 10
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Census2021 Ts071 Rgn is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts071 rgn.

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
| `previously_served_in_uk_armed_forces` | `bigint` | Count or numeric value for previously served in uk armed forces in the represented area. |
| `previously_served_in_uk_reserve_armed_forces` | `bigint` | Count or numeric value for previously served in uk reserve armed forces in the represented area. |
| `previously_served_in_both_regular_and_reserve_uk_armed_forces` | `bigint` | Count or numeric value for previously served in both regular and reserve uk armed forces in the represented area. |
| `has_not_previously_served_in_any_uk_armed_forces` | `bigint` | Count or numeric value for has not previously served in any uk armed forces in the represented area. |
