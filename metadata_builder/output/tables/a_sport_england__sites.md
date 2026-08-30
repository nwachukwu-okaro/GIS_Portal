# Sites

## Overview

- **Identifier:** `a_sport_england/sites`
- **Source organisation:** Sport England
- **Product:** Active Places
- **Source:** https://www.sportengland.org/research-and-data/data/active-places
- **Schema:** `a_sport_england`
- **Table:** `sites`
- **Geometry:** POINT
- **CRS:** EPSG:27700
- **Rows:** 42888
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
| `cycle_hire` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `building_name` | `varchar(90)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `building_number` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `car_park_capacity` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `car_park_exists` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `changing_place_toilets` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `closure_reason` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `core_city_name` | `varchar(28)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `county_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `county_name` | `varchar(15)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `has_cricket_bowling_machines` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `cycle_park` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `dependent_locality` | `varchar(35)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `dependent_thorough_fare` | `varchar(43)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `disability_activity_area` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `disability_changing_facilities` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `disability_doorways` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `disability_emergency_exits` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `disability_finding_and_reaching_the_entrance` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `disability_notes` | `varchar(1265)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `disability_parking` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `disability_reception_area` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `disability_social_areas` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `disability_spectator_areas` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `disability_toilets` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `double_dependent_locality` | `varchar(31)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `education_phase` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `email` | `varchar(64)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `facebook` | `varchar(197)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `has_first_aid_room` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `forename` | `varchar(50)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `job_title` | `varchar(50)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ldp_code` | `varchar(6)` | Code assigned by the source dataset. | code | Yes | No | No |
| `ldp_name` | `varchar(51)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `local_authority_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `local_authority_name` | `varchar(35)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `lower_super_output_area_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `middle_super_output_area_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `has_nursery` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `operator_name` | `varchar(66)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `output_area_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `parliamentary_constituency_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `parliamentary_constituency_name` | `varchar(40)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `postcode` | `varchar(9)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `town` | `varchar(33)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `public_notes` | `varchar(1854)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `last_audit_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `closed_date` | `date` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `created_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `last_updated_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `region_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `region_name` | `varchar(24)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `cycle_repair_workshop` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `site_id` | `bigint` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `site_name` | `varchar(78)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `management_start_date` | `date` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `sub_building_name` | `varchar(57)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `surname` | `varchar(43)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `has_table_tennis_tables` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `telephone_number` | `varchar(15)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `thoroughfare_name` | `varchar(75)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `title` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `toid` | `varchar(20)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `twitter_x` | `varchar(210)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `uprn` | `numeric` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ward_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `ward_name` | `varchar(53)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `website` | `varchar(218)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `easting` | `real` | Easting coordinate in the dataset coordinate reference system. | x_coordinate | Yes | No | No |
| `northing` | `real` | Northing coordinate in the dataset coordinate reference system. | y_coordinate | Yes | No | No |
| `site_alias` | `varchar(358)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ownership_type_text` | `varchar(42)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `management_type_text` | `varchar(36)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ownership_type_group` | `varchar(22)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `management_type_group` | `varchar(15)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lat` | `real` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `long` | `real` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
