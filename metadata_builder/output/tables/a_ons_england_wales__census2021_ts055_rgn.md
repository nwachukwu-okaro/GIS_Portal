# Census2021 Ts055 Rgn

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts055_rgn`
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
- **Table:** `census2021_ts055_rgn`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 10
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Census2021 Ts055 Rgn is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts055 rgn.

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
| `armed_forces_base_address` | `bigint` | Count or numeric value for armed forces base address in the represented area. |
| `another_address_when_working_away_from_home` | `bigint` | Count or numeric value for another address when working away from home in the represented area. |
| `holiday_home` | `bigint` | Count or numeric value for holiday home in the represented area. |
| `student_s_term_time_address` | `bigint` | Count or numeric value for student s term time address in the represented area. |
| `student_s_home_address` | `bigint` | Count or numeric value for student s home address in the represented area. |
| `another_parent_or_guardian_s_address` | `bigint` | Count or numeric value for another parent or guardian s address in the represented area. |
| `partner_s_address` | `bigint` | Count or numeric value for partner s address in the represented area. |
| `other` | `bigint` | Count or numeric value for other in the represented area. |
| `second_address_type_not_specified` | `bigint` | Count or numeric value for second address type not specified in the represented area. |
