# Census2021 Ts044 Lsoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts044_lsoa`
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
- **Table:** `census2021_ts044_lsoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 35672
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Census2021 Ts044 Lsoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts044 lsoa.

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
| `detached` | `bigint` | Count or numeric value for detached in the represented area. |
| `semi_detached` | `bigint` | Count or numeric value for semi detached in the represented area. |
| `terraced` | `bigint` | Count or numeric value for terraced in the represented area. |
| `in_a_purpose_built_block_of_flats_or_tenement` | `bigint` | Numeric in a purpose built block of flats or tenement value recorded for the feature. |
| `part_of_a_converted_or_shared_house_including_bedsits` | `bigint` | Count or numeric value for part of a converted or shared house including bedsits in the represented area. |
| `part_of_another_converted_building_for_example_former_school_ch` | `bigint` | Count or numeric value for part of another converted building for example former school ch in the represented area. |
| `in_a_commercial_building_for_example_in_an_office_building_hote` | `bigint` | Count or numeric value for in a commercial building for example in an office building hote in the represented area. |
| `a_caravan_or_other_mobile_or_temporary_structure` | `bigint` | Count or numeric value for a caravan or other mobile or temporary structure in the represented area. |
