# Census2021 Ts061 Lsoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts061_lsoa`
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
- **Table:** `census2021_ts061_lsoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 35672
- **Columns:** 15
- **Metadata status:** source_mapped

## Description

Census2021 Ts061 Lsoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts061 lsoa.

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
| `work_mainly_at_or_from_home` | `bigint` | Count or numeric value for work mainly at or from home in the represented area. |
| `underground_metro_light_rail_tram` | `bigint` | Count or numeric value for underground metro light rail tram in the represented area. |
| `train` | `bigint` | Count or numeric value for train in the represented area. |
| `bus_minibus_or_coach` | `bigint` | Count or numeric value for bus minibus or coach in the represented area. |
| `taxi` | `bigint` | Count or numeric value for taxi in the represented area. |
| `motorcycle_scooter_or_moped` | `bigint` | Count or numeric value for motorcycle scooter or moped in the represented area. |
| `driving_a_car_or_van` | `bigint` | Count or numeric value for driving a car or van in the represented area. |
| `passenger_in_a_car_or_van` | `bigint` | Count or numeric value for passenger in a car or van in the represented area. |
| `bicycle` | `bigint` | Count or numeric value for bicycle in the represented area. |
| `on_foot` | `bigint` | Count or numeric value for on foot in the represented area. |
| `other_method_of_travel_to_work` | `bigint` | Count or numeric value for other method of travel to work in the represented area. |
