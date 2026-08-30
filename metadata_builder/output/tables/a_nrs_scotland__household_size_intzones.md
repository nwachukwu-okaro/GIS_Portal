# Household Size Intzones

## Overview

- **Identifier:** `a_nrs_scotland/household_size_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `household_size_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 14
- **Metadata status:** source_mapped

## Description

Household Size Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to household size intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `all_occupied_households` | `double precision` | Count or numeric value for all occupied households in the represented area. | statistical_value | Yes | No | No |
| `no_central_heating` | `double precision` | Count or numeric value for number central heating in the represented area. | statistical_value | Yes | No | No |
| `gas_central_heating_total` | `double precision` | Count or numeric value for gas central heating total in the represented area. | statistical_value | Yes | No | No |
| `gas_central_heating_mains_gas` | `double precision` | Count or numeric value for gas central heating mains gas in the represented area. | statistical_value | Yes | No | No |
| `gas_central_heating_other_gas_including_liquid_petroleum_gas` | `double precision` | Count or numeric value for gas central heating other gas including liquid petroleum gas in the represented area. | statistical_value | Yes | No | No |
| `electric_including_storage_heaters_central_heating` | `double precision` | Count or numeric value for electric including storage heaters central heating in the represented area. | statistical_value | Yes | No | No |
| `oil_central_heating` | `double precision` | Count or numeric value for oil central heating in the represented area. | statistical_value | Yes | No | No |
| `solid_fuel_excluding_wood` | `double precision` | Count or numeric value for solid fuel excluding wood in the represented area. | statistical_value | Yes | No | No |
| `wood_or_biomass_including_logs_pellets_chippings_central_hea` | `double precision` | Count or numeric value for wood or biomass including logs pellets chippings central hea in the represented area. | statistical_value | Yes | No | No |
| `other_renewable_energy_source_including_electric_and_air_hea` | `double precision` | Count or numeric value for other renewable energy source including electric and air hea in the represented area. | statistical_value | Yes | No | No |
| `district_or_communal_heat_system` | `double precision` | Count or numeric value for district or communal heat system in the represented area. | statistical_value | Yes | No | No |
| `other_central_heating` | `double precision` | Count or numeric value for other central heating in the represented area. | statistical_value | Yes | No | No |
| `two_or_more_types_of_central_heating` | `double precision` | Count or numeric value for two or more types of central heating in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
