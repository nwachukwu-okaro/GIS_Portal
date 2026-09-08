# Census2021 Ts062 Rgn

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts062_rgn`
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
- **Table:** `census2021_ts062_rgn`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 10
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Census2021 Ts062 Rgn is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts062 rgn.

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
| `total_all_usual_residents_aged_16_years_and_over` | `bigint` | Count or numeric value for total all usual residents aged 16 years and over in the represented area. |
| `l1_l2_and_l3_higher_managerial_administrative_and_professional` | `bigint` | Count or numeric value for l1 l2 and l3 higher managerial administrative and professional in the represented area. |
| `l4_l5_and_l6_lower_managerial_administrative_and_professional_o` | `bigint` | Count or numeric value for l4 l5 and l6 lower managerial administrative and professional o in the represented area. |
| `l7_intermediate_occupations` | `bigint` | Count or numeric value for l7 intermediate occupations in the represented area. |
| `l8_and_l9_small_employers_and_own_account_workers` | `bigint` | Count or numeric value for l8 and l9 small employers and own account workers in the represented area. |
| `l10_and_l11_lower_supervisory_and_technical_occupations` | `bigint` | Count or numeric value for l10 and l11 lower supervisory and technical occupations in the represented area. |
| `l12_semi_routine_occupations` | `bigint` | Count or numeric value for l12 semi routine occupations in the represented area. |
| `l13_routine_occupations` | `bigint` | Count or numeric value for l13 routine occupations in the represented area. |
| `l14_1_and_l14_2_never_worked_and_long_term_unemployed` | `bigint` | Numeric l14 1 and l14 2 never worked and long term unemployed value recorded for the feature. |
| `l15_full_time_students` | `bigint` | Count or numeric value for l15 full time students in the represented area. |
