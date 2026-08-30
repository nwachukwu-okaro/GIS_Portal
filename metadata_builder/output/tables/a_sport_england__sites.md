# Sites

## Overview

- **Identifier:** `a_sport_england/sites`
- **Source organisation:** Sport England
- **Product:** Active Places
- **Source:** https://www.sportengland.org/research-and-data/data/active-places
- **Local dataset version:** 20251203 (3 December 2025)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.354919, 49.894105, 1.757824, 55.787085]`
- **Schema:** `a_sport_england`
- **Table:** `sites`
- **Geometry:** POINT
- **CRS:** EPSG:27700
- **Rows:** 42888
- **Columns:** 80
- **Metadata status:** source_mapped

## Description

Version: 20251203
Source: https://www.activeplacespower.com/pages/downloads#download_fac
Attribution: Contains data Copyright Sport England.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `active_partnership_code` | `varchar(6)` | Code assigned by the source dataset. | code | Yes | No | No |
| `active_partnership_name` | `varchar(53)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `cycle_hire` | `bigint` | Count or numeric value for cycle hire in the represented area. | statistical_value | Yes | No | No |
| `building_name` | `varchar(90)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `building_number` | `integer` | Count or numeric value for building number in the represented area. | statistical_value | Yes | No | No |
| `car_park_capacity` | `bigint` | Count or numeric value for car park capacity in the represented area. | statistical_value | Yes | No | No |
| `car_park_exists` | `bigint` | Count or numeric value for car park exists in the represented area. | statistical_value | Yes | No | No |
| `changing_place_toilets` | `bigint` | Count or numeric value for changing place toilets in the represented area. | statistical_value | Yes | No | No |
| `closure_reason` | `bigint` | Count or numeric value for closure reason in the represented area. | statistical_value | Yes | No | No |
| `core_city_name` | `varchar(28)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `county_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `county_name` | `varchar(15)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `has_cricket_bowling_machines` | `bigint` | Count or numeric value for has cricket bowling machines in the represented area. | statistical_value | Yes | No | No |
| `cycle_park` | `bigint` | Count or numeric value for cycle park in the represented area. | statistical_value | Yes | No | No |
| `dependent_locality` | `varchar(35)` | Publisher-supplied dependent locality for the represented feature or record. | source_attribute | Yes | No | No |
| `dependent_thorough_fare` | `varchar(43)` | Publisher-supplied dependent thorough fare for the represented feature or record. | source_attribute | Yes | No | No |
| `disability_activity_area` | `bigint` | Numeric disability activity area value recorded for the feature. | measure | Yes | No | No |
| `disability_changing_facilities` | `bigint` | Count or numeric value for disability changing facilities in the represented area. | statistical_value | Yes | No | No |
| `disability_doorways` | `bigint` | Count or numeric value for disability doorways in the represented area. | statistical_value | Yes | No | No |
| `disability_emergency_exits` | `bigint` | Count or numeric value for disability emergency exits in the represented area. | statistical_value | Yes | No | No |
| `disability_finding_and_reaching_the_entrance` | `bigint` | Count or numeric value for disability finding and reaching the entrance in the represented area. | statistical_value | Yes | No | No |
| `disability_notes` | `varchar(1265)` | Publisher-supplied disability notes for the represented feature or record. | source_attribute | Yes | No | No |
| `disability_parking` | `bigint` | Count or numeric value for disability parking in the represented area. | statistical_value | Yes | No | No |
| `disability_reception_area` | `bigint` | Numeric disability reception area value recorded for the feature. | measure | Yes | No | No |
| `disability_social_areas` | `bigint` | Numeric disability social areas value recorded for the feature. | measure | Yes | No | No |
| `disability_spectator_areas` | `bigint` | Numeric disability spectator areas value recorded for the feature. | measure | Yes | No | No |
| `disability_toilets` | `bigint` | Count or numeric value for disability toilets in the represented area. | statistical_value | Yes | No | No |
| `double_dependent_locality` | `varchar(31)` | Publisher-supplied double dependent locality for the represented feature or record. | source_attribute | Yes | No | No |
| `education_phase` | `bigint` | Count or numeric value for education phase in the represented area. | statistical_value | Yes | No | No |
| `email` | `varchar(64)` | Publisher-supplied email for the represented feature or record. | source_attribute | Yes | No | No |
| `facebook` | `varchar(197)` | Publisher-supplied facebook for the represented feature or record. | source_attribute | Yes | No | No |
| `has_first_aid_room` | `bigint` | Count or numeric value for has first aid room in the represented area. | statistical_value | Yes | No | No |
| `forename` | `varchar(50)` | Publisher-supplied forename for the represented feature or record. | source_attribute | Yes | No | No |
| `job_title` | `varchar(50)` | Publisher-supplied job title for the represented feature or record. | source_attribute | Yes | No | No |
| `ldp_code` | `varchar(6)` | Code assigned by the source dataset. | code | Yes | No | No |
| `ldp_name` | `varchar(51)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `local_authority_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `local_authority_name` | `varchar(35)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `lower_super_output_area_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `middle_super_output_area_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `has_nursery` | `bigint` | Count or numeric value for has nursery in the represented area. | statistical_value | Yes | No | No |
| `operator_name` | `varchar(66)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `output_area_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `parliamentary_constituency_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `parliamentary_constituency_name` | `varchar(40)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `postcode` | `varchar(9)` | Publisher-assigned postcode for the record. | source_identifier | Yes | No | No |
| `town` | `varchar(33)` | Publisher-supplied town for the represented feature or record. | source_attribute | Yes | No | No |
| `public_notes` | `varchar(1854)` | Publisher-supplied public notes for the represented feature or record. | source_attribute | Yes | No | No |
| `last_audit_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `closed_date` | `date` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `created_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `last_updated_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `region_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `region_name` | `varchar(24)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `cycle_repair_workshop` | `bigint` | Count or numeric value for cycle repair workshop in the represented area. | statistical_value | Yes | No | No |
| `site_id` | `bigint` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `site_name` | `varchar(78)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `management_start_date` | `date` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `sub_building_name` | `varchar(57)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `surname` | `varchar(43)` | Publisher-supplied surname for the represented feature or record. | source_attribute | Yes | No | No |
| `has_table_tennis_tables` | `bigint` | Count or numeric value for has table tennis tables in the represented area. | statistical_value | Yes | No | No |
| `telephone_number` | `varchar(15)` | Publisher-supplied telephone number for the represented feature or record. | source_attribute | Yes | No | No |
| `thoroughfare_name` | `varchar(75)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `title` | `bigint` | Count or numeric value for title in the represented area. | statistical_value | Yes | No | No |
| `toid` | `varchar(20)` | Publisher-assigned toid for the record. | source_identifier | Yes | No | No |
| `twitter_x` | `varchar(210)` | Publisher-supplied twitter x for the represented feature or record. | source_attribute | Yes | No | No |
| `uprn` | `numeric` | Count or numeric value for uprn in the represented area. | statistical_value | Yes | No | No |
| `ward_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `ward_name` | `varchar(53)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `website` | `varchar(218)` | Publisher-supplied website for the represented feature or record. | source_attribute | Yes | No | No |
| `easting` | `real` | Easting coordinate in metres in the dataset's projected coordinate reference system. | x_coordinate | Yes | No | No |
| `northing` | `real` | Northing coordinate in metres in the dataset's projected coordinate reference system. | y_coordinate | Yes | No | No |
| `site_alias` | `varchar(358)` | Publisher-supplied site alias for the represented feature or record. | source_attribute | Yes | No | No |
| `ownership_type_text` | `varchar(42)` | Publisher-supplied ownership type text for the represented feature or record. | source_attribute | Yes | No | No |
| `management_type_text` | `varchar(36)` | Publisher-supplied management type text for the represented feature or record. | source_attribute | Yes | No | No |
| `ownership_type_group` | `varchar(22)` | Publisher-supplied ownership type group for the represented feature or record. | source_attribute | Yes | No | No |
| `management_type_group` | `varchar(15)` | Publisher-supplied management type group for the represented feature or record. | source_attribute | Yes | No | No |
| `lat` | `real` | Numeric lat value recorded for the feature. | measure | Yes | No | No |
| `long` | `real` | Numeric long value recorded for the feature. | measure | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |

## Supported operations

- filter
- select
- reproject
- validate_geometry
- buffer
- clip
- intersect
- spatial_join
- export

## Operation requirements

- Intersect, clip and spatial-join inputs must use matching coordinate reference systems.
- Buffer operations require a suitable projected coordinate reference system.
- Reprojection is performed on working outputs; source tables remain unchanged.

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
