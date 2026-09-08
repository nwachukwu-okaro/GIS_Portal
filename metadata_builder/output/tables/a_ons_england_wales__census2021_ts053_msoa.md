# Census2021 Ts053 Msoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts053_msoa`
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
- **Table:** `census2021_ts053_msoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 7264
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Census2021 Ts053 Msoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts053 msoa.

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
| `occupancy_rating_of_rooms_2_or_more` | `bigint` | Count or numeric value for occupancy rating of rooms 2 or more in the represented area. |
| `occupancy_rating_of_rooms_1` | `bigint` | Count or numeric value for occupancy rating of rooms 1 in the represented area. |
| `occupancy_rating_of_rooms_0` | `bigint` | Count or numeric value for occupancy rating of rooms 0 in the represented area. |
| `occupancy_rating_of_rooms_1_1` | `bigint` | Count or numeric value for occupancy rating of rooms 1 1 in the represented area. |
| `occupancy_rating_of_rooms_2_or_less` | `bigint` | Count or numeric value for occupancy rating of rooms 2 or less in the represented area. |
