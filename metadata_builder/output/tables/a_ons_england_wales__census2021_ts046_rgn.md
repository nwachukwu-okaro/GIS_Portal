# Census2021 Ts046 Rgn

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts046_rgn`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts046_rgn`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 10
- **Columns:** 16
- **Metadata status:** source_mapped

## Description

Census2021 Ts046 Rgn is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts046 rgn.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_households` | `bigint` | Count or numeric value for total all households in the represented area. | statistical_value | Yes | No | No |
| `no_central_heating` | `bigint` | Count or numeric value for number central heating in the represented area. | statistical_value | Yes | No | No |
| `mains_gas_only` | `bigint` | Count or numeric value for mains gas only in the represented area. | statistical_value | Yes | No | No |
| `tank_or_bottled_gas_only` | `bigint` | Count or numeric value for tank or bottled gas only in the represented area. | statistical_value | Yes | No | No |
| `electric_only` | `bigint` | Count or numeric value for electric only in the represented area. | statistical_value | Yes | No | No |
| `oil_only` | `bigint` | Count or numeric value for oil only in the represented area. | statistical_value | Yes | No | No |
| `wood_only` | `bigint` | Count or numeric value for wood only in the represented area. | statistical_value | Yes | No | No |
| `solid_fuel_only` | `bigint` | Count or numeric value for solid fuel only in the represented area. | statistical_value | Yes | No | No |
| `renewable_energy_only` | `bigint` | Count or numeric value for renewable energy only in the represented area. | statistical_value | Yes | No | No |
| `district_or_communal_heat_networks_only` | `bigint` | Count or numeric value for district or communal heat networks only in the represented area. | statistical_value | Yes | No | No |
| `other_central_heating_only` | `bigint` | Count or numeric value for other central heating only in the represented area. | statistical_value | Yes | No | No |
| `two_or_more_types_of_central_heating_not_including_renewable_en` | `bigint` | Count or numeric value for two or more types of central heating not including renewable en in the represented area. | statistical_value | Yes | No | No |
| `two_or_more_types_of_central_heating_including_renewable_energy` | `bigint` | Count or numeric value for two or more types of central heating including renewable energy in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
