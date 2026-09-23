# Census2021 Ts061 Ctry

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts061_ctry`
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
- **Table:** `census2021_ts061_ctry`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 3
- **Columns:** 15
- **Metadata status:** source_mapped

## Description

Census2021 Ts061 Ctry is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts061 ctry.

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
| `total_all_usual_residents_aged_16_years_and_over_in_employment` | `bigint` | Recorded census measure for the category "total all usual residents aged 16 years and over in employment" in the represented area. Units and population base require the source table. |
| `work_mainly_at_or_from_home` | `bigint` |  |
| `underground_metro_light_rail_tram` | `bigint` |  |
| `train` | `bigint` |  |
| `bus_minibus_or_coach` | `bigint` |  |
| `taxi` | `bigint` |  |
| `motorcycle_scooter_or_moped` | `bigint` |  |
| `driving_a_car_or_van` | `bigint` |  |
| `passenger_in_a_car_or_van` | `bigint` |  |
| `bicycle` | `bigint` |  |
| `on_foot` | `bigint` |  |
| `other_method_of_travel_to_work` | `bigint` |  |
