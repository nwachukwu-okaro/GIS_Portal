# Central Heating Household Intzones

## Overview

- **Identifier:** `a_nrs_scotland/central_heating_household_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `central_heating_household_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Central Heating Household Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to central heating household intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `all_occupied_households` | `double precision` | Count or numeric value for all occupied households in the represented area. | statistical_value | Yes | No | No |
| `number_of_cars_or_vans_in_household_no_cars_or_vans` | `double precision` | Count or numeric value for number of cars or vans in household number cars or vans in the represented area. | statistical_value | Yes | No | No |
| `number_of_cars_or_vans_in_household_one_car_or_van` | `double precision` | Count or numeric value for number of cars or vans in household one car or van in the represented area. | statistical_value | Yes | No | No |
| `number_of_cars_or_vans_in_household_two_cars_or_vans` | `double precision` | Count or numeric value for number of cars or vans in household two cars or vans in the represented area. | statistical_value | Yes | No | No |
| `number_of_cars_or_vans_in_household_three_cars_or_vans` | `double precision` | Count or numeric value for number of cars or vans in household three cars or vans in the represented area. | statistical_value | Yes | No | No |
| `number_of_cars_or_vans_in_household_four_or_more_cars_or_van` | `double precision` | Count or numeric value for number of cars or vans in household four or more cars or van in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
