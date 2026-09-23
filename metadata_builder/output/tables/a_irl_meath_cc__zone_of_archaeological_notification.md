# Zone Of Archaeological Notification

## Overview

- **Identifier:** `a_irl_meath_cc/zone_of_archaeological_notification`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-7.328512, 53.392547, -6.212518, 53.915676]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_meath_cc`
- **Table:** `zone_of_archaeological_notification`
- **Geometry:** POLYGON
- **CRS:** EPSG:2157
- **Rows:** 1948
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Zone Of Archaeological Notification is an authoritative dataset published by Meath County Council. It represents zone of archaeological notification features using polygon geometry.

## Lineage

Published by Meath County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `zone_id` | `varchar(10)` | Identifier assigned by the source dataset. |
| `county_id` | `double precision` | Identifier assigned by the source dataset. |
| `class_code` | `varchar(4)` | Code assigned by the source dataset. |
| `map_label` | `varchar(100)` |  |
| `zan_pk` | `integer` | Primary-key identifier for records in zone_of_archaeological_notification. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
