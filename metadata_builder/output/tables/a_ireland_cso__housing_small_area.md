# Housing Small Area

## Overview

- **Identifier:** `a_ireland_cso/housing_small_area`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **Schema:** `a_ireland_cso`
- **Table:** `housing_small_area`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 18920
- **Columns:** 129
- **Metadata status:** source_mapped

## Description

Housing Small Area is an authoritative dataset published by Central Statistics Office Ireland. It contains records relating to housing small area.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `guid` | `text` | Publisher-assigned guid for the record. | source_identifier | Yes | No | No |
| `geogid` | `text` | Publisher-assigned geogid for the record. | source_identifier | Yes | No | No |
| `geogdesc` | `text` | Publisher-supplied geogdesc for the represented feature or record. | source_attribute | Yes | No | No |
| `ur_category` | `double precision` | Count or numeric value for ur category in the represented area. | statistical_value | Yes | No | No |
| `ur_category_desc` | `text` | Publisher-supplied ur category description for the represented feature or record. | source_attribute | Yes | No | No |
| `housebungalow_no_of_households` | `bigint` | Count or numeric value for housebungalow number of households in the represented area. | statistical_value | Yes | No | No |
| `flatapartment_no_of_households` | `bigint` | Numeric flatapartment number of households value recorded for the feature. | measure | Yes | No | No |
| `bedsit_no_of_households` | `bigint` | Count or numeric value for bedsit number of households in the represented area. | statistical_value | Yes | No | No |
| `caravanmobile_home_no_of_households` | `bigint` | Count or numeric value for caravanmobile home number of households in the represented area. | statistical_value | Yes | No | No |
| `total_no_of_households` | `bigint` | Count or numeric value for total number of households in the represented area. | statistical_value | Yes | No | No |
| `housebungalow_no_of_persons` | `bigint` | Count or numeric value for housebungalow number of persons in the represented area. | statistical_value | Yes | No | No |
| `flatapartment_no_of_persons` | `bigint` | Numeric flatapartment number of persons value recorded for the feature. | measure | Yes | No | No |
| `bedsit_no_of_persons` | `bigint` | Count or numeric value for bedsit number of persons in the represented area. | statistical_value | Yes | No | No |
| `caravanmobile_home_no_of_persons` | `bigint` | Count or numeric value for caravanmobile home number of persons in the represented area. | statistical_value | Yes | No | No |
| `total_no_of_persons` | `bigint` | Count or numeric value for total number of persons in the represented area. | statistical_value | Yes | No | No |
| `pre_1919_no_of_households` | `bigint` | Count or numeric value for pre 1919 number of households in the represented area. | statistical_value | Yes | No | No |
| `t_1919_1945_no_of_households` | `bigint` | Count or numeric value for t 1919 1945 number of households in the represented area. | statistical_value | Yes | No | No |
| `t_1946_1960_no_of_households` | `bigint` | Count or numeric value for t 1946 1960 number of households in the represented area. | statistical_value | Yes | No | No |
| `t_1961_1970_no_of_households` | `bigint` | Count or numeric value for t 1961 1970 number of households in the represented area. | statistical_value | Yes | No | No |
| `t_1971_1980_no_of_households` | `bigint` | Count or numeric value for t 1971 1980 number of households in the represented area. | statistical_value | Yes | No | No |
| `t_1981_1990_no_of_households` | `bigint` | Count or numeric value for t 1981 1990 number of households in the represented area. | statistical_value | Yes | No | No |
| `t_1991_2000_no_of_households` | `bigint` | Count or numeric value for t 1991 2000 number of households in the represented area. | statistical_value | Yes | No | No |
| `t_2001_2010_no_of_households` | `bigint` | Count or numeric value for t 2001 2010 number of households in the represented area. | statistical_value | Yes | No | No |
| `t_2011_2015_no_of_households` | `bigint` | Count or numeric value for t 2011 2015 number of households in the represented area. | statistical_value | Yes | No | No |
| `t_2016_or_later_no_of_households` | `bigint` | Numeric t 2016 or later number of households value recorded for the feature. | measure | Yes | No | No |
| `not_stated_no_of_households` | `bigint` | Count or numeric value for not stated number of households in the represented area. | statistical_value | Yes | No | No |
| `total_no_of_households_1` | `bigint` | Count or numeric value for total number of households 1 in the represented area. | statistical_value | Yes | No | No |
| `pre_1919_no_of_persons` | `bigint` | Count or numeric value for pre 1919 number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_1919_1945_no_of_persons` | `bigint` | Count or numeric value for t 1919 1945 number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_1946_1960_no_of_persons` | `bigint` | Count or numeric value for t 1946 1960 number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_1961_1970_no_of_persons` | `bigint` | Count or numeric value for t 1961 1970 number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_1971_1980_no_of_persons` | `bigint` | Count or numeric value for t 1971 1980 number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_1981_1990_no_of_persons` | `bigint` | Count or numeric value for t 1981 1990 number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_1991_2000_no_of_persons` | `bigint` | Count or numeric value for t 1991 2000 number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_2001_2010_no_of_persons` | `bigint` | Count or numeric value for t 2001 2010 number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_2011_or_2015_no_of_persons` | `bigint` | Count or numeric value for t 2011 or 2015 number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_2016_or_later_no_of_persons` | `bigint` | Numeric t 2016 or later number of persons value recorded for the feature. | measure | Yes | No | No |
| `not_stated_no_of_persons` | `bigint` | Count or numeric value for not stated number of persons in the represented area. | statistical_value | Yes | No | No |
| `total_no_of_persons_1` | `bigint` | Count or numeric value for total number of persons 1 in the represented area. | statistical_value | Yes | No | No |
| `owned_with_mortgage_or_loan_no_of_households` | `bigint` | Count or numeric value for owned with mortgage or loan number of households in the represented area. | statistical_value | Yes | No | No |
| `owned_outright_no_of_households` | `bigint` | Count or numeric value for owned outright number of households in the represented area. | statistical_value | Yes | No | No |
| `rented_from_private_landlord_no_of_households` | `bigint` | Count or numeric value for rented from private landlord number of households in the represented area. | statistical_value | Yes | No | No |
| `rented_from_local_authority_no_of_households` | `bigint` | Count or numeric value for rented from local authority number of households in the represented area. | statistical_value | Yes | No | No |
| `rented_from_voluntarycooperative_housing_body_no_of_households` | `bigint` | Count or numeric value for rented from voluntarycooperative housing body number of households in the represented area. | statistical_value | Yes | No | No |
| `occupied_free_of_rent_no_of_households` | `bigint` | Count or numeric value for occupied free of rent number of households in the represented area. | statistical_value | Yes | No | No |
| `not_stated_no_of_households_1` | `bigint` | Count or numeric value for not stated number of households 1 in the represented area. | statistical_value | Yes | No | No |
| `total_no_of_households_2` | `bigint` | Count or numeric value for total number of households 2 in the represented area. | statistical_value | Yes | No | No |
| `owned_with_mortgage_or_loan_no_of_persons` | `bigint` | Count or numeric value for owned with mortgage or loan number of persons in the represented area. | statistical_value | Yes | No | No |
| `owned_outright_no_of_persons` | `bigint` | Count or numeric value for owned outright number of persons in the represented area. | statistical_value | Yes | No | No |
| `rented_from_private_landlord_no_of_persons` | `bigint` | Count or numeric value for rented from private landlord number of persons in the represented area. | statistical_value | Yes | No | No |
| `rented_from_local_authority_no_of_persons` | `bigint` | Count or numeric value for rented from local authority number of persons in the represented area. | statistical_value | Yes | No | No |
| `rented_from_voluntarycooperative_housing_body_no_of_persons` | `bigint` | Count or numeric value for rented from voluntarycooperative housing body number of persons in the represented area. | statistical_value | Yes | No | No |
| `occupied_free_of_rent_no_of_persons` | `bigint` | Count or numeric value for occupied free of rent number of persons in the represented area. | statistical_value | Yes | No | No |
| `not_stated_no_of_persons_1` | `bigint` | Count or numeric value for not stated number of persons 1 in the represented area. | statistical_value | Yes | No | No |
| `total_no_of_persons_2` | `bigint` | Count or numeric value for total number of persons 2 in the represented area. | statistical_value | Yes | No | No |
| `t_1_room_no_of_households` | `bigint` | Count or numeric value for t 1 room number of households in the represented area. | statistical_value | Yes | No | No |
| `t_2_rooms_no_of_households` | `bigint` | Count or numeric value for t 2 rooms number of households in the represented area. | statistical_value | Yes | No | No |
| `t_3_rooms_no_of_households` | `bigint` | Count or numeric value for t 3 rooms number of households in the represented area. | statistical_value | Yes | No | No |
| `t_4_rooms_no_of_households` | `bigint` | Count or numeric value for t 4 rooms number of households in the represented area. | statistical_value | Yes | No | No |
| `t_5_rooms_no_of_households` | `bigint` | Count or numeric value for t 5 rooms number of households in the represented area. | statistical_value | Yes | No | No |
| `t_6_rooms_no_of_households` | `bigint` | Count or numeric value for t 6 rooms number of households in the represented area. | statistical_value | Yes | No | No |
| `t_7_rooms_no_of_households` | `bigint` | Count or numeric value for t 7 rooms number of households in the represented area. | statistical_value | Yes | No | No |
| `t_8_or_more_rooms_no_of_households` | `bigint` | Count or numeric value for t 8 or more rooms number of households in the represented area. | statistical_value | Yes | No | No |
| `not_stated_no_of_households_2` | `bigint` | Count or numeric value for not stated number of households 2 in the represented area. | statistical_value | Yes | No | No |
| `total_no_of_households_3` | `bigint` | Count or numeric value for total number of households 3 in the represented area. | statistical_value | Yes | No | No |
| `t_1_room_no_of_persons` | `bigint` | Count or numeric value for t 1 room number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_2_rooms_no_of_persons` | `bigint` | Count or numeric value for t 2 rooms number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_3_rooms_no_of_persons` | `bigint` | Count or numeric value for t 3 rooms number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_4_rooms_no_of_persons` | `bigint` | Count or numeric value for t 4 rooms number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_5_rooms_no_of_persons` | `bigint` | Count or numeric value for t 5 rooms number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_6_rooms_no_of_persons` | `bigint` | Count or numeric value for t 6 rooms number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_7_rooms_no_of_persons` | `bigint` | Count or numeric value for t 7 rooms number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_8_or_more_rooms_no_of_persons` | `bigint` | Count or numeric value for t 8 or more rooms number of persons in the represented area. | statistical_value | Yes | No | No |
| `not_stated_no_of_persons_2` | `bigint` | Count or numeric value for not stated number of persons 2 in the represented area. | statistical_value | Yes | No | No |
| `total_no_of_persons_3` | `bigint` | Count or numeric value for total number of persons 3 in the represented area. | statistical_value | Yes | No | No |
| `no_central_heating` | `bigint` | Count or numeric value for number central heating in the represented area. | statistical_value | Yes | No | No |
| `oil` | `bigint` | Count or numeric value for oil in the represented area. | statistical_value | Yes | No | No |
| `natural_gas` | `bigint` | Count or numeric value for natural gas in the represented area. | statistical_value | Yes | No | No |
| `electricity` | `bigint` | Count or numeric value for electricity in the represented area. | statistical_value | Yes | No | No |
| `coal_incl_anthracite` | `bigint` | Count or numeric value for coal incl anthracite in the represented area. | statistical_value | Yes | No | No |
| `peat_incl_turf` | `bigint` | Count or numeric value for peat incl turf in the represented area. | statistical_value | Yes | No | No |
| `liquid_petroleum_gas_lpg` | `bigint` | Count or numeric value for liquid petroleum gas lpg in the represented area. | statistical_value | Yes | No | No |
| `wood_incl_wood_pellets` | `bigint` | Count or numeric value for wood incl wood pellets in the represented area. | statistical_value | Yes | No | No |
| `other` | `bigint` | Count or numeric value for other in the represented area. | statistical_value | Yes | No | No |
| `not_stated` | `bigint` | Count or numeric value for not stated in the represented area. | statistical_value | Yes | No | No |
| `total` | `bigint` | Count or numeric value for total in the represented area. | statistical_value | Yes | No | No |
| `public_main` | `bigint` | Count or numeric value for public main in the represented area. | statistical_value | Yes | No | No |
| `group_scheme_with_public_source` | `bigint` | Count or numeric value for group scheme with public source in the represented area. | statistical_value | Yes | No | No |
| `group_scheme_with_private_source` | `bigint` | Count or numeric value for group scheme with private source in the represented area. | statistical_value | Yes | No | No |
| `other_private_source` | `bigint` | Count or numeric value for other private source in the represented area. | statistical_value | Yes | No | No |
| `none` | `bigint` | Count or numeric value for none in the represented area. | statistical_value | Yes | No | No |
| `not_stated_1` | `bigint` | Count or numeric value for not stated 1 in the represented area. | statistical_value | Yes | No | No |
| `total_1` | `bigint` | Count or numeric value for total 1 in the represented area. | statistical_value | Yes | No | No |
| `public_scheme` | `bigint` | Count or numeric value for public scheme in the represented area. | statistical_value | Yes | No | No |
| `individual_septic_tank` | `bigint` | Count or numeric value for individual septic tank in the represented area. | statistical_value | Yes | No | No |
| `other_individual_treatment` | `bigint` | Count or numeric value for other individual treatment in the represented area. | statistical_value | Yes | No | No |
| `other_1` | `bigint` | Count or numeric value for other 1 in the represented area. | statistical_value | Yes | No | No |
| `no_sewerage_facility` | `bigint` | Count or numeric value for number sewerage facility in the represented area. | statistical_value | Yes | No | No |
| `not_stated_2` | `bigint` | Count or numeric value for not stated 2 in the represented area. | statistical_value | Yes | No | No |
| `total_2` | `bigint` | Count or numeric value for total 2 in the represented area. | statistical_value | Yes | No | No |
| `occupied` | `bigint` | Count or numeric value for occupied in the represented area. | statistical_value | Yes | No | No |
| `temporarily_absent` | `bigint` | Count or numeric value for temporarily absent in the represented area. | statistical_value | Yes | No | No |
| `unoccupied_holiday_homes` | `bigint` | Count or numeric value for unoccupied holiday homes in the represented area. | statistical_value | Yes | No | No |
| `other_vacant_dwellings` | `bigint` | Count or numeric value for other vacant dwellings in the represented area. | statistical_value | Yes | No | No |
| `total_3` | `bigint` | Count or numeric value for total 3 in the represented area. | statistical_value | Yes | No | No |
| `t_0_bedrooms_no_of_households` | `bigint` | Count or numeric value for t 0 bedrooms number of households in the represented area. | statistical_value | Yes | No | No |
| `t_1_bedroom_no_of_households` | `bigint` | Count or numeric value for t 1 bedroom number of households in the represented area. | statistical_value | Yes | No | No |
| `t_2_bedrooms_no_of_households` | `bigint` | Count or numeric value for t 2 bedrooms number of households in the represented area. | statistical_value | Yes | No | No |
| `t_3_bedrooms_no_of_households` | `bigint` | Count or numeric value for t 3 bedrooms number of households in the represented area. | statistical_value | Yes | No | No |
| `t_4_bedrooms_no_of_households` | `bigint` | Count or numeric value for t 4 bedrooms number of households in the represented area. | statistical_value | Yes | No | No |
| `t_5_bedrooms_no_of_households` | `bigint` | Count or numeric value for t 5 bedrooms number of households in the represented area. | statistical_value | Yes | No | No |
| `total_no_of_households_4` | `bigint` | Count or numeric value for total number of households 4 in the represented area. | statistical_value | Yes | No | No |
| `t_0_bedrooms_no_of_persons` | `bigint` | Count or numeric value for t 0 bedrooms number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_1_bedroom_no_of_persons` | `bigint` | Count or numeric value for t 1 bedroom number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_2_rooms_no_of_persons_1` | `bigint` | Count or numeric value for t 2 rooms number of persons 1 in the represented area. | statistical_value | Yes | No | No |
| `t_3_bedrooms_no_of_persons` | `bigint` | Count or numeric value for t 3 bedrooms number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_4_bedrooms_no_of_persons` | `bigint` | Count or numeric value for t 4 bedrooms number of persons in the represented area. | statistical_value | Yes | No | No |
| `t_5_bedrooms_no_of_persons` | `bigint` | Count or numeric value for t 5 bedrooms number of persons in the represented area. | statistical_value | Yes | No | No |
| `total_no_of_persons_4` | `bigint` | Count or numeric value for total number of persons 4 in the represented area. | statistical_value | Yes | No | No |
| `non_stated_no_of_persons` | `bigint` | Count or numeric value for non stated number of persons in the represented area. | statistical_value | Yes | No | No |
| `non_stated_no_of_households` | `bigint` | Count or numeric value for non stated number of households in the represented area. | statistical_value | Yes | No | No |
| `has_renewable_energy` | `bigint` | Count or numeric value for has renewable energy in the represented area. | statistical_value | Yes | No | No |
| `no_renewable_energy` | `bigint` | Count or numeric value for number renewable energy in the represented area. | statistical_value | Yes | No | No |
| `not_stated_3` | `bigint` | Count or numeric value for not stated 3 in the represented area. | statistical_value | Yes | No | No |
| `total_renewables` | `bigint` | Count or numeric value for total renewables in the represented area. | statistical_value | Yes | No | No |
| `has_at_least_1_smoke_alarm` | `bigint` | Count or numeric value for has at least 1 smoke alarm in the represented area. | statistical_value | Yes | No | No |
| `no_smoke_alarms` | `bigint` | Count or numeric value for number smoke alarms in the represented area. | statistical_value | Yes | No | No |
| `not_stated_4` | `bigint` | Count or numeric value for not stated 4 in the represented area. | statistical_value | Yes | No | No |
| `total_4` | `bigint` | Count or numeric value for total 4 in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
