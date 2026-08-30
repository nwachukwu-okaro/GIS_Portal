# Scotland Housing Intzones

## Overview

- **Identifier:** `a_nrs_scotland/scotland_housing_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `scotland_housing_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1279
- **Columns:** 72
- **Metadata status:** source_mapped

## Description

Scotland Housing Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to scotland housing intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `geography_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `accom_hh_all_occupied_hhs` | `bigint` | Count or numeric value for accom households all occupied hhs in the represented area. | statistical_value | Yes | No | No |
| `accom_hh_house_bungalow_total` | `bigint` | Count or numeric value for accom households house bungalow total in the represented area. | statistical_value | Yes | No | No |
| `accom_hh_house_detached` | `bigint` | Count or numeric value for accom households house detached in the represented area. | statistical_value | Yes | No | No |
| `accom_hh_house_semi_detached` | `bigint` | Count or numeric value for accom households house semi detached in the represented area. | statistical_value | Yes | No | No |
| `accom_hh_house_terraced` | `bigint` | Count or numeric value for accom households house terraced in the represented area. | statistical_value | Yes | No | No |
| `accom_hh_flat_total` | `bigint` | Numeric accom households flat total value recorded for the feature. | measure | Yes | No | No |
| `accom_hh_flat_purpose_built` | `bigint` | Numeric accom households flat purpose built value recorded for the feature. | measure | Yes | No | No |
| `accom_hh_flat_converted_or_shared` | `bigint` | Numeric accom households flat converted or shared value recorded for the feature. | measure | Yes | No | No |
| `accom_hh_flat_commercial_building` | `bigint` | Numeric accom households flat commercial building value recorded for the feature. | measure | Yes | No | No |
| `accom_hh_caravan_or_temporary` | `bigint` | Count or numeric value for accom households caravan or temporary in the represented area. | statistical_value | Yes | No | No |
| `all_people_in_hhs` | `bigint` | Count or numeric value for all people in hhs in the represented area. | statistical_value | Yes | No | No |
| `accom_people_house_bungalow_total` | `bigint` | Count or numeric value for accom people house bungalow total in the represented area. | statistical_value | Yes | No | No |
| `accom_people_house_detached` | `bigint` | Count or numeric value for accom people house detached in the represented area. | statistical_value | Yes | No | No |
| `accom_people_house_semi_detached` | `bigint` | Count or numeric value for accom people house semi detached in the represented area. | statistical_value | Yes | No | No |
| `accom_people_house_terraced` | `bigint` | Count or numeric value for accom people house terraced in the represented area. | statistical_value | Yes | No | No |
| `accom_people_flat_total` | `bigint` | Numeric accom people flat total value recorded for the feature. | measure | Yes | No | No |
| `accom_people_flat_purpose_built` | `bigint` | Numeric accom people flat purpose built value recorded for the feature. | measure | Yes | No | No |
| `accom_people_flat_converted_or_shared` | `bigint` | Numeric accom people flat converted or shared value recorded for the feature. | measure | Yes | No | No |
| `accom_people_flat_commercial_building` | `bigint` | Numeric accom people flat commercial building value recorded for the feature. | measure | Yes | No | No |
| `accom_people_caravan_or_temporary` | `bigint` | Count or numeric value for accom people caravan or temporary in the represented area. | statistical_value | Yes | No | No |
| `central_heating_all_occupied_hhs` | `bigint` | Count or numeric value for central heating all occupied hhs in the represented area. | statistical_value | Yes | No | No |
| `no_heating` | `bigint` | Count or numeric value for number heating in the represented area. | statistical_value | Yes | No | No |
| `gas_heating_total` | `bigint` | Count or numeric value for gas heating total in the represented area. | statistical_value | Yes | No | No |
| `gas_heating_mains` | `bigint` | Count or numeric value for gas heating mains in the represented area. | statistical_value | Yes | No | No |
| `gas_heating_other` | `bigint` | Count or numeric value for gas heating other in the represented area. | statistical_value | Yes | No | No |
| `electric_heating` | `bigint` | Count or numeric value for electric heating in the represented area. | statistical_value | Yes | No | No |
| `oil_heating` | `bigint` | Count or numeric value for oil heating in the represented area. | statistical_value | Yes | No | No |
| `solid_fuel_heating` | `bigint` | Count or numeric value for solid fuel heating in the represented area. | statistical_value | Yes | No | No |
| `wood_biomass_heating` | `bigint` | Count or numeric value for wood biomass heating in the represented area. | statistical_value | Yes | No | No |
| `renewable_heating` | `bigint` | Count or numeric value for renewable heating in the represented area. | statistical_value | Yes | No | No |
| `district_communal_heating` | `bigint` | Count or numeric value for district communal heating in the represented area. | statistical_value | Yes | No | No |
| `other_heating` | `bigint` | Count or numeric value for other heating in the represented area. | statistical_value | Yes | No | No |
| `two_plus_heating_types` | `bigint` | Count or numeric value for two plus heating types in the represented area. | statistical_value | Yes | No | No |
| `num_bedrooms_all_occupied_hhs` | `bigint` | Count or numeric value for num bedrooms all occupied hhs in the represented area. | statistical_value | Yes | No | No |
| `one_bedroom` | `bigint` | Count or numeric value for one bedroom in the represented area. | statistical_value | Yes | No | No |
| `two_bedrooms` | `bigint` | Count or numeric value for two bedrooms in the represented area. | statistical_value | Yes | No | No |
| `three_bedrooms` | `bigint` | Count or numeric value for three bedrooms in the represented area. | statistical_value | Yes | No | No |
| `four_bedrooms` | `bigint` | Count or numeric value for four bedrooms in the represented area. | statistical_value | Yes | No | No |
| `t_5plus_bedrooms` | `bigint` | Count or numeric value for t 5plus bedrooms in the represented area. | statistical_value | Yes | No | No |
| `all_occupied_hh_spaces` | `bigint` | Count or numeric value for all occupied households spaces in the represented area. | statistical_value | Yes | No | No |
| `one_person` | `bigint` | Count or numeric value for one person in the represented area. | statistical_value | Yes | No | No |
| `two_people` | `bigint` | Count or numeric value for two people in the represented area. | statistical_value | Yes | No | No |
| `three_people` | `bigint` | Count or numeric value for three people in the represented area. | statistical_value | Yes | No | No |
| `four_people` | `bigint` | Count or numeric value for four people in the represented area. | statistical_value | Yes | No | No |
| `five_people` | `bigint` | Count or numeric value for five people in the represented area. | statistical_value | Yes | No | No |
| `six_people` | `bigint` | Count or numeric value for six people in the represented area. | statistical_value | Yes | No | No |
| `seven_people` | `bigint` | Count or numeric value for seven people in the represented area. | statistical_value | Yes | No | No |
| `t_8plus_people` | `bigint` | Count or numeric value for t 8plus people in the represented area. | statistical_value | Yes | No | No |
| `occupancy_all_occupied_hhs` | `bigint` | Count or numeric value for occupancy all occupied hhs in the represented area. | statistical_value | Yes | No | No |
| `occupancy_2plus` | `bigint` | Count or numeric value for occupancy 2plus in the represented area. | statistical_value | Yes | No | No |
| `occupancy_plus1` | `bigint` | Count or numeric value for occupancy plus1 in the represented area. | statistical_value | Yes | No | No |
| `occupancy_0` | `bigint` | Count or numeric value for occupancy 0 in the represented area. | statistical_value | Yes | No | No |
| `occupancy_minus1_or_less` | `bigint` | Count or numeric value for occupancy minus1 or less in the represented area. | statistical_value | Yes | No | No |
| `tenure_all_occupied_hhs` | `bigint` | Count or numeric value for tenure all occupied hhs in the represented area. | statistical_value | Yes | No | No |
| `owned_total` | `bigint` | Count or numeric value for owned total in the represented area. | statistical_value | Yes | No | No |
| `owned_outright` | `bigint` | Count or numeric value for owned outright in the represented area. | statistical_value | Yes | No | No |
| `owned_mortgage_or_loan` | `bigint` | Count or numeric value for owned mortgage or loan in the represented area. | statistical_value | Yes | No | No |
| `owned_shared_ownership` | `bigint` | Count or numeric value for owned shared ownership in the represented area. | statistical_value | Yes | No | No |
| `owned_shared_equity` | `bigint` | Count or numeric value for owned shared equity in the represented area. | statistical_value | Yes | No | No |
| `social_rented` | `bigint` | Count or numeric value for social rented in the represented area. | statistical_value | Yes | No | No |
| `private_rented_total` | `bigint` | Count or numeric value for private rented total in the represented area. | statistical_value | Yes | No | No |
| `private_rented_landlord` | `bigint` | Count or numeric value for private rented landlord in the represented area. | statistical_value | Yes | No | No |
| `private_rented_other` | `bigint` | Count or numeric value for private rented other in the represented area. | statistical_value | Yes | No | No |
| `rent_free` | `bigint` | Count or numeric value for rent free in the represented area. | statistical_value | Yes | No | No |
| `cars_vans_all_occupied_hhs` | `bigint` | Count or numeric value for cars vans all occupied hhs in the represented area. | statistical_value | Yes | No | No |
| `no_cars_or_vans` | `bigint` | Count or numeric value for number cars or vans in the represented area. | statistical_value | Yes | No | No |
| `one_car_or_van` | `bigint` | Count or numeric value for one car or van in the represented area. | statistical_value | Yes | No | No |
| `two_cars_or_vans` | `bigint` | Count or numeric value for two cars or vans in the represented area. | statistical_value | Yes | No | No |
| `three_cars_or_vans` | `bigint` | Count or numeric value for three cars or vans in the represented area. | statistical_value | Yes | No | No |
| `four_plus_cars_or_vans` | `bigint` | Count or numeric value for four plus cars or vans in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
