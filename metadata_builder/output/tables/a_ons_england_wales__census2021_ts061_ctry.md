# Census2021 Ts061 Ctry

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts061_ctry`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts061_ctry`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 3
- **Columns:** 15
- **Metadata status:** source_mapped

## Description

Census2021 Ts061 Ctry is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts061 ctry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_usual_residents_aged_16_years_and_over_in_employment` | `bigint` | Count or numeric value for total all usual residents aged 16 years and over in employment in the represented area. | statistical_value | Yes | No | No |
| `work_mainly_at_or_from_home` | `bigint` | Count or numeric value for work mainly at or from home in the represented area. | statistical_value | Yes | No | No |
| `underground_metro_light_rail_tram` | `bigint` | Count or numeric value for underground metro light rail tram in the represented area. | statistical_value | Yes | No | No |
| `train` | `bigint` | Count or numeric value for train in the represented area. | statistical_value | Yes | No | No |
| `bus_minibus_or_coach` | `bigint` | Count or numeric value for bus minibus or coach in the represented area. | statistical_value | Yes | No | No |
| `taxi` | `bigint` | Count or numeric value for taxi in the represented area. | statistical_value | Yes | No | No |
| `motorcycle_scooter_or_moped` | `bigint` | Count or numeric value for motorcycle scooter or moped in the represented area. | statistical_value | Yes | No | No |
| `driving_a_car_or_van` | `bigint` | Count or numeric value for driving a car or van in the represented area. | statistical_value | Yes | No | No |
| `passenger_in_a_car_or_van` | `bigint` | Count or numeric value for passenger in a car or van in the represented area. | statistical_value | Yes | No | No |
| `bicycle` | `bigint` | Count or numeric value for bicycle in the represented area. | statistical_value | Yes | No | No |
| `on_foot` | `bigint` | Count or numeric value for on foot in the represented area. | statistical_value | Yes | No | No |
| `other_method_of_travel_to_work` | `bigint` | Count or numeric value for other method of travel to work in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
