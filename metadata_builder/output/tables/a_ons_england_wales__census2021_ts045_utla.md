# Census2021 Ts045 Utla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts045_utla`
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
- **Table:** `census2021_ts045_utla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 174
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Census2021 Ts045 Utla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts045 utla.

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
| `total_all_households` | `bigint` | Count or numeric value for total all households in the represented area. |
| `no_cars_or_vans_in_household` | `bigint` | Count or numeric value for number cars or vans in household in the represented area. |
| `col_1_car_or_van_in_household` | `bigint` | Count or numeric value for col 1 car or van in household in the represented area. |
| `col_2_cars_or_vans_in_household` | `bigint` | Count or numeric value for col 2 cars or vans in household in the represented area. |
| `col_3_or_more_cars_or_vans_in_household` | `bigint` | Count or numeric value for col 3 or more cars or vans in household in the represented area. |
