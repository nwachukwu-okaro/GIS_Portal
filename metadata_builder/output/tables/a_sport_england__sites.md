# Sites

## Overview

- **Identifier:** `a_sport_england/sites`
- **Source organisation:** Sport England
- **Product:** Active Places
- **Source:** https://www.sportengland.org/research-and-data/data/active-places
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.354919, 49.894105, 1.757824, 55.787085]`
- **Topic category:** society
- **Temporal extent:** 2007-06-06T00:00:00 to 2025-12-02T21:32:49
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
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

## Lineage

Published by Sport England as part of Active Places. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `active_partnership_code` | `varchar(6)` | Code assigned by the source dataset. |
| `active_partnership_name` | `varchar(53)` | Name associated with the represented feature. |
| `cycle_hire` | `bigint` |  |
| `building_name` | `varchar(90)` | Name associated with the represented feature. |
| `building_number` | `integer` |  |
| `car_park_capacity` | `bigint` |  |
| `car_park_exists` | `bigint` |  |
| `changing_place_toilets` | `bigint` |  |
| `closure_reason` | `bigint` |  |
| `core_city_name` | `varchar(28)` | Name associated with the represented feature. |
| `county_code` | `varchar(9)` | Code assigned by the source dataset. |
| `county_name` | `varchar(15)` | Name associated with the represented feature. |
| `has_cricket_bowling_machines` | `bigint` |  |
| `cycle_park` | `bigint` |  |
| `dependent_locality` | `varchar(35)` |  |
| `dependent_thorough_fare` | `varchar(43)` |  |
| `disability_activity_area` | `bigint` |  |
| `disability_changing_facilities` | `bigint` |  |
| `disability_doorways` | `bigint` |  |
| `disability_emergency_exits` | `bigint` |  |
| `disability_finding_and_reaching_the_entrance` | `bigint` |  |
| `disability_notes` | `varchar(1265)` |  |
| `disability_parking` | `bigint` |  |
| `disability_reception_area` | `bigint` |  |
| `disability_social_areas` | `bigint` |  |
| `disability_spectator_areas` | `bigint` |  |
| `disability_toilets` | `bigint` |  |
| `double_dependent_locality` | `varchar(31)` |  |
| `education_phase` | `bigint` |  |
| `email` | `varchar(64)` |  |
| `facebook` | `varchar(197)` |  |
| `has_first_aid_room` | `bigint` |  |
| `forename` | `varchar(50)` |  |
| `job_title` | `varchar(50)` |  |
| `ldp_code` | `varchar(6)` | Code assigned by the source dataset. |
| `ldp_name` | `varchar(51)` | Name associated with the represented feature. |
| `local_authority_code` | `varchar(9)` | Code assigned by the source dataset. |
| `local_authority_name` | `varchar(35)` | Name associated with the represented feature. |
| `lower_super_output_area_code` | `varchar(9)` | Code assigned by the source dataset. |
| `middle_super_output_area_code` | `varchar(9)` | Code assigned by the source dataset. |
| `has_nursery` | `bigint` |  |
| `operator_name` | `varchar(66)` | Name associated with the represented feature. |
| `output_area_code` | `varchar(9)` | Code assigned by the source dataset. |
| `parliamentary_constituency_code` | `varchar(9)` | Code assigned by the source dataset. |
| `parliamentary_constituency_name` | `varchar(40)` | Name associated with the represented feature. |
| `postcode` | `varchar(9)` |  |
| `town` | `varchar(33)` |  |
| `public_notes` | `varchar(1854)` |  |
| `last_audit_date` | `timestamp` | Date associated with the represented feature or source record. |
| `closed_date` | `date` | Date associated with the represented feature or source record. |
| `created_date` | `timestamp` | Date associated with the represented feature or source record. |
| `last_updated_date` | `timestamp` | Date associated with the represented feature or source record. |
| `region_code` | `varchar(9)` | Code assigned by the source dataset. |
| `region_name` | `varchar(24)` | Name associated with the represented feature. |
| `cycle_repair_workshop` | `bigint` |  |
| `site_id` | `bigint` | Identifier assigned by the source dataset. |
| `site_name` | `varchar(78)` | Name associated with the represented feature. |
| `management_start_date` | `date` | Date associated with the represented feature or source record. |
| `sub_building_name` | `varchar(57)` | Name associated with the represented feature. |
| `surname` | `varchar(43)` |  |
| `has_table_tennis_tables` | `bigint` |  |
| `telephone_number` | `varchar(15)` |  |
| `thoroughfare_name` | `varchar(75)` | Name associated with the represented feature. |
| `title` | `bigint` |  |
| `toid` | `varchar(20)` |  |
| `twitter_x` | `varchar(210)` |  |
| `uprn` | `numeric` |  |
| `ward_code` | `varchar(9)` | Code assigned by the source dataset. |
| `ward_name` | `varchar(53)` | Name associated with the represented feature. |
| `website` | `varchar(218)` | Web address associated with the record. |
| `easting` | `real` | Easting coordinate in metres in the dataset's projected coordinate reference system. |
| `northing` | `real` | Northing coordinate in metres in the dataset's projected coordinate reference system. |
| `site_alias` | `varchar(358)` |  |
| `ownership_type_text` | `varchar(42)` |  |
| `management_type_text` | `varchar(36)` |  |
| `ownership_type_group` | `varchar(22)` |  |
| `management_type_group` | `varchar(15)` |  |
| `lat` | `real` |  |
| `long` | `real` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
