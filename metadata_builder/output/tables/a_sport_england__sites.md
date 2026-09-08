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
- **Missing for full compliance:** access_constraints, licence_name, dataset_reference_date, use_constraints, frequency_of_update
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
| `cycle_hire` | `bigint` | Count or numeric value for cycle hire in the represented area. |
| `building_name` | `varchar(90)` | Name associated with the represented feature. |
| `building_number` | `integer` | Count or numeric value for building number in the represented area. |
| `car_park_capacity` | `bigint` | Count or numeric value for car park capacity in the represented area. |
| `car_park_exists` | `bigint` | Count or numeric value for car park exists in the represented area. |
| `changing_place_toilets` | `bigint` | Count or numeric value for changing place toilets in the represented area. |
| `closure_reason` | `bigint` | Count or numeric value for closure reason in the represented area. |
| `core_city_name` | `varchar(28)` | Name associated with the represented feature. |
| `county_code` | `varchar(9)` | Code assigned by the source dataset. |
| `county_name` | `varchar(15)` | Name associated with the represented feature. |
| `has_cricket_bowling_machines` | `bigint` | Count or numeric value for has cricket bowling machines in the represented area. |
| `cycle_park` | `bigint` | Count or numeric value for cycle park in the represented area. |
| `dependent_locality` | `varchar(35)` | Publisher-supplied dependent locality for the represented feature or record. |
| `dependent_thorough_fare` | `varchar(43)` | Publisher-supplied dependent thorough fare for the represented feature or record. |
| `disability_activity_area` | `bigint` | Numeric disability activity area value recorded for the feature. |
| `disability_changing_facilities` | `bigint` | Count or numeric value for disability changing facilities in the represented area. |
| `disability_doorways` | `bigint` | Count or numeric value for disability doorways in the represented area. |
| `disability_emergency_exits` | `bigint` | Count or numeric value for disability emergency exits in the represented area. |
| `disability_finding_and_reaching_the_entrance` | `bigint` | Count or numeric value for disability finding and reaching the entrance in the represented area. |
| `disability_notes` | `varchar(1265)` | Publisher-supplied disability notes for the represented feature or record. |
| `disability_parking` | `bigint` | Count or numeric value for disability parking in the represented area. |
| `disability_reception_area` | `bigint` | Numeric disability reception area value recorded for the feature. |
| `disability_social_areas` | `bigint` | Numeric disability social areas value recorded for the feature. |
| `disability_spectator_areas` | `bigint` | Numeric disability spectator areas value recorded for the feature. |
| `disability_toilets` | `bigint` | Count or numeric value for disability toilets in the represented area. |
| `double_dependent_locality` | `varchar(31)` | Publisher-supplied double dependent locality for the represented feature or record. |
| `education_phase` | `bigint` | Count or numeric value for education phase in the represented area. |
| `email` | `varchar(64)` | Publisher-supplied email for the represented feature or record. |
| `facebook` | `varchar(197)` | Publisher-supplied facebook for the represented feature or record. |
| `has_first_aid_room` | `bigint` | Count or numeric value for has first aid room in the represented area. |
| `forename` | `varchar(50)` | Publisher-supplied forename for the represented feature or record. |
| `job_title` | `varchar(50)` | Publisher-supplied job title for the represented feature or record. |
| `ldp_code` | `varchar(6)` | Code assigned by the source dataset. |
| `ldp_name` | `varchar(51)` | Name associated with the represented feature. |
| `local_authority_code` | `varchar(9)` | Code assigned by the source dataset. |
| `local_authority_name` | `varchar(35)` | Name associated with the represented feature. |
| `lower_super_output_area_code` | `varchar(9)` | Code assigned by the source dataset. |
| `middle_super_output_area_code` | `varchar(9)` | Code assigned by the source dataset. |
| `has_nursery` | `bigint` | Count or numeric value for has nursery in the represented area. |
| `operator_name` | `varchar(66)` | Name associated with the represented feature. |
| `output_area_code` | `varchar(9)` | Code assigned by the source dataset. |
| `parliamentary_constituency_code` | `varchar(9)` | Code assigned by the source dataset. |
| `parliamentary_constituency_name` | `varchar(40)` | Name associated with the represented feature. |
| `postcode` | `varchar(9)` | Publisher-assigned postcode for the record. |
| `town` | `varchar(33)` | Publisher-supplied town for the represented feature or record. |
| `public_notes` | `varchar(1854)` | Publisher-supplied public notes for the represented feature or record. |
| `last_audit_date` | `timestamp` | Date associated with the represented feature or source record. |
| `closed_date` | `date` | Date associated with the represented feature or source record. |
| `created_date` | `timestamp` | Date associated with the represented feature or source record. |
| `last_updated_date` | `timestamp` | Date associated with the represented feature or source record. |
| `region_code` | `varchar(9)` | Code assigned by the source dataset. |
| `region_name` | `varchar(24)` | Name associated with the represented feature. |
| `cycle_repair_workshop` | `bigint` | Count or numeric value for cycle repair workshop in the represented area. |
| `site_id` | `bigint` | Identifier assigned by the source dataset. |
| `site_name` | `varchar(78)` | Name associated with the represented feature. |
| `management_start_date` | `date` | Date associated with the represented feature or source record. |
| `sub_building_name` | `varchar(57)` | Name associated with the represented feature. |
| `surname` | `varchar(43)` | Publisher-supplied surname for the represented feature or record. |
| `has_table_tennis_tables` | `bigint` | Count or numeric value for has table tennis tables in the represented area. |
| `telephone_number` | `varchar(15)` | Publisher-supplied telephone number for the represented feature or record. |
| `thoroughfare_name` | `varchar(75)` | Name associated with the represented feature. |
| `title` | `bigint` | Count or numeric value for title in the represented area. |
| `toid` | `varchar(20)` | Publisher-assigned toid for the record. |
| `twitter_x` | `varchar(210)` | Publisher-supplied twitter x for the represented feature or record. |
| `uprn` | `numeric` | Count or numeric value for uprn in the represented area. |
| `ward_code` | `varchar(9)` | Code assigned by the source dataset. |
| `ward_name` | `varchar(53)` | Name associated with the represented feature. |
| `website` | `varchar(218)` | Publisher-supplied website for the represented feature or record. |
| `easting` | `real` | Easting coordinate in metres in the dataset's projected coordinate reference system. |
| `northing` | `real` | Northing coordinate in metres in the dataset's projected coordinate reference system. |
| `site_alias` | `varchar(358)` | Publisher-supplied site alias for the represented feature or record. |
| `ownership_type_text` | `varchar(42)` | Publisher-supplied ownership type text for the represented feature or record. |
| `management_type_text` | `varchar(36)` | Publisher-supplied management type text for the represented feature or record. |
| `ownership_type_group` | `varchar(22)` | Publisher-supplied ownership type group for the represented feature or record. |
| `management_type_group` | `varchar(15)` | Publisher-supplied management type group for the represented feature or record. |
| `lat` | `real` | Numeric lat value recorded for the feature. |
| `long` | `real` | Numeric long value recorded for the feature. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
