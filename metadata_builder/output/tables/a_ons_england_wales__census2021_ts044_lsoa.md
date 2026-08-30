# Census2021 Ts044 Lsoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts044_lsoa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts044_lsoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 35672
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Census2021 Ts044 Lsoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts044 lsoa.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_households` | `bigint` | Count or numeric value for total all households in the represented area. | statistical_value | Yes | No | No |
| `detached` | `bigint` | Count or numeric value for detached in the represented area. | statistical_value | Yes | No | No |
| `semi_detached` | `bigint` | Count or numeric value for semi detached in the represented area. | statistical_value | Yes | No | No |
| `terraced` | `bigint` | Count or numeric value for terraced in the represented area. | statistical_value | Yes | No | No |
| `in_a_purpose_built_block_of_flats_or_tenement` | `bigint` | Numeric in a purpose built block of flats or tenement value recorded for the feature. | measure | Yes | No | No |
| `part_of_a_converted_or_shared_house_including_bedsits` | `bigint` | Count or numeric value for part of a converted or shared house including bedsits in the represented area. | statistical_value | Yes | No | No |
| `part_of_another_converted_building_for_example_former_school_ch` | `bigint` | Count or numeric value for part of another converted building for example former school ch in the represented area. | statistical_value | Yes | No | No |
| `in_a_commercial_building_for_example_in_an_office_building_hote` | `bigint` | Count or numeric value for in a commercial building for example in an office building hote in the represented area. | statistical_value | Yes | No | No |
| `a_caravan_or_other_mobile_or_temporary_structure` | `bigint` | Count or numeric value for a caravan or other mobile or temporary structure in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
