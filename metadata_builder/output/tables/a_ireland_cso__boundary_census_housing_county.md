# Boundary Census Housing County

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_housing_county`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.746471, 54.563349, 3.417194, 58.520162]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_housing_county`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 31
- **Columns:** 129
- **Metadata status:** source_mapped

## Description

Boundary Census Housing County is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census housing county features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `guid` | `text` | UUID-formatted identifier associated with the record; persistence across releases is not confirmed. |
| `geogid` | `text` | Code identifying the geographical area represented by the row. |
| `geogdesc` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `housebungalow_no_of_households` | `bigint` |  |
| `flatapartment_no_of_households` | `bigint` |  |
| `bedsit_no_of_households` | `bigint` |  |
| `caravanmobile_home_no_of_households` | `bigint` |  |
| `total_no_of_households` | `bigint` | Recorded census measure for the category "total number of households" in the represented area. Units and population base require the source table. |
| `housebungalow_no_of_persons` | `bigint` |  |
| `flatapartment_no_of_persons` | `bigint` |  |
| `bedsit_no_of_persons` | `bigint` |  |
| `caravanmobile_home_no_of_persons` | `bigint` |  |
| `total_no_of_persons` | `bigint` | Recorded census measure for the category "total number of persons" in the represented area. Units and population base require the source table. |
| `pre_1919_no_of_households` | `bigint` |  |
| `t_1919_1945_no_of_households` | `bigint` |  |
| `t_1946_1960_no_of_households` | `bigint` |  |
| `t_1961_1970_no_of_households` | `bigint` |  |
| `t_1971_1980_no_of_households` | `bigint` |  |
| `t_1981_1990_no_of_households` | `bigint` |  |
| `t_1991_2000_no_of_households` | `bigint` |  |
| `t_2001_2010_no_of_households` | `bigint` |  |
| `t_2011_2015_no_of_households` | `bigint` |  |
| `t_2016_or_later_no_of_households` | `bigint` |  |
| `not_stated_no_of_households` | `bigint` |  |
| `total_no_of_households_1` | `bigint` |  |
| `pre_1919_no_of_persons` | `bigint` |  |
| `t_1919_1945_no_of_persons` | `bigint` |  |
| `t_1946_1960_no_of_persons` | `bigint` |  |
| `t_1961_1970_no_of_persons` | `bigint` |  |
| `t_1971_1980_no_of_persons` | `bigint` |  |
| `t_1981_1990_no_of_persons` | `bigint` |  |
| `t_1991_2000_no_of_persons` | `bigint` |  |
| `t_2001_2010_no_of_persons` | `bigint` |  |
| `t_2011_or_2015_no_of_persons` | `bigint` |  |
| `t_2016_or_later_no_of_persons` | `bigint` |  |
| `not_stated_no_of_persons` | `bigint` |  |
| `total_no_of_persons_1` | `bigint` |  |
| `owned_with_mortgage_or_loan_no_of_households` | `bigint` |  |
| `owned_outright_no_of_households` | `bigint` |  |
| `rented_from_private_landlord_no_of_households` | `bigint` |  |
| `rented_from_local_authority_no_of_households` | `bigint` |  |
| `rented_from_voluntarycooperative_housing_body_no_of_households` | `bigint` |  |
| `occupied_free_of_rent_no_of_households` | `bigint` |  |
| `not_stated_no_of_households_1` | `bigint` |  |
| `total_no_of_households_2` | `bigint` |  |
| `owned_with_mortgage_or_loan_no_of_persons` | `bigint` |  |
| `owned_outright_no_of_persons` | `bigint` |  |
| `rented_from_private_landlord_no_of_persons` | `bigint` |  |
| `rented_from_local_authority_no_of_persons` | `bigint` |  |
| `rented_from_voluntarycooperative_housing_body_no_of_persons` | `bigint` |  |
| `occupied_free_of_rent_no_of_persons` | `bigint` |  |
| `not_stated_no_of_persons_1` | `bigint` |  |
| `total_no_of_persons_2` | `bigint` |  |
| `t_1_room_no_of_households` | `bigint` |  |
| `t_2_rooms_no_of_households` | `bigint` |  |
| `t_3_rooms_no_of_households` | `bigint` |  |
| `t_4_rooms_no_of_households` | `bigint` |  |
| `t_5_rooms_no_of_households` | `bigint` |  |
| `t_6_rooms_no_of_households` | `bigint` |  |
| `t_7_rooms_no_of_households` | `bigint` |  |
| `t_8_or_more_rooms_no_of_households` | `bigint` |  |
| `not_stated_no_of_households_2` | `bigint` |  |
| `total_no_of_households_3` | `bigint` |  |
| `t_1_room_no_of_persons` | `bigint` |  |
| `t_2_rooms_no_of_persons` | `bigint` |  |
| `t_3_rooms_no_of_persons` | `bigint` |  |
| `t_4_rooms_no_of_persons` | `bigint` |  |
| `t_5_rooms_no_of_persons` | `bigint` |  |
| `t_6_rooms_no_of_persons` | `bigint` |  |
| `t_7_rooms_no_of_persons` | `bigint` |  |
| `t_8_or_more_rooms_no_of_persons` | `bigint` |  |
| `not_stated_no_of_persons_2` | `bigint` |  |
| `total_no_of_persons_3` | `bigint` |  |
| `no_central_heating` | `bigint` |  |
| `oil` | `bigint` |  |
| `natural_gas` | `bigint` |  |
| `electricity` | `bigint` |  |
| `coal_incl_anthracite` | `bigint` |  |
| `peat_incl_turf` | `bigint` |  |
| `liquid_petroleum_gas_lpg` | `bigint` |  |
| `wood_incl_wood_pellets` | `bigint` |  |
| `other` | `bigint` |  |
| `not_stated` | `bigint` |  |
| `total` | `bigint` |  |
| `public_main` | `bigint` |  |
| `group_scheme_with_public_source` | `bigint` |  |
| `group_scheme_with_private_source` | `bigint` |  |
| `other_private_source` | `bigint` |  |
| `none` | `bigint` |  |
| `not_stated_1` | `bigint` |  |
| `total_1` | `bigint` |  |
| `public_scheme` | `bigint` |  |
| `individual_septic_tank` | `bigint` |  |
| `other_individual_treatment` | `bigint` |  |
| `other_1` | `bigint` |  |
| `no_sewerage_facility` | `bigint` |  |
| `not_stated_2` | `bigint` |  |
| `total_2` | `bigint` |  |
| `occupied` | `bigint` |  |
| `temporarily_absent` | `bigint` |  |
| `unoccupied_holiday_homes` | `bigint` |  |
| `other_vacant_dwellings` | `bigint` |  |
| `total_3` | `bigint` |  |
| `t_0_bedrooms_no_of_households` | `bigint` |  |
| `t_1_bedroom_no_of_households` | `bigint` |  |
| `t_2_bedrooms_no_of_households` | `bigint` |  |
| `t_3_bedrooms_no_of_households` | `bigint` |  |
| `t_4_bedrooms_no_of_households` | `bigint` |  |
| `t_5_bedrooms_no_of_households` | `bigint` |  |
| `total_no_of_households_4` | `bigint` |  |
| `t_0_bedrooms_no_of_persons` | `bigint` |  |
| `t_1_bedroom_no_of_persons` | `bigint` |  |
| `t_2_rooms_no_of_persons_1` | `bigint` |  |
| `t_3_bedrooms_no_of_persons` | `bigint` |  |
| `t_4_bedrooms_no_of_persons` | `bigint` |  |
| `t_5_bedrooms_no_of_persons` | `bigint` |  |
| `total_no_of_persons_4` | `bigint` |  |
| `non_stated_no_of_persons` | `bigint` |  |
| `non_stated_no_of_households` | `bigint` |  |
| `has_renewable_energy` | `bigint` |  |
| `no_renewable_energy` | `bigint` |  |
| `not_stated_3` | `bigint` |  |
| `total_renewables` | `bigint` |  |
| `has_at_least_1_smoke_alarm` | `bigint` |  |
| `no_smoke_alarms` | `bigint` |  |
| `not_stated_4` | `bigint` |  |
| `total_4` | `bigint` |  |
| `area` | `double precision` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
