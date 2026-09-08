# Protected Views Cdp 2022 2028

## Overview

- **Identifier:** `a_irl_galway_cc/protected_views_cdp_2022_2028`
- **Source organisation:** Galway County Council
- **Source:** https://data.gov.ie/organization/galway-county-council
- **Geographic coverage:** County Galway
- **WGS84 extent:** `[-10.144643, 53.017321, -7.992847, 53.607277]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_irl_galway_cc`
- **Table:** `protected_views_cdp_2022_2028`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:2157
- **Rows:** 52
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Protected Views Cdp 2022 2028 is an authoritative dataset published by Galway County Council. It represents protected views cdp 2022 2028 features using multipoint geometry.

## Lineage

Published by Galway County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `description_of_view` | `varchar` | Publisher-supplied description of view for the represented feature or record. |
| `location_of_view` | `varchar` | Publisher-supplied location of view for the represented feature or record. |
| `object_id` | `integer` | Identifier assigned by the source dataset. |
| `photos_report` | `varchar` | Publisher-supplied photos report for the represented feature or record. |
| `significance` | `varchar` | Publisher-supplied significance for the represented feature or record. |
| `view_angle` | `integer` | Count or numeric value for view angle in the represented area. |
| `view_rotation` | `integer` | Count or numeric value for view rotation in the represented area. |
| `vp_name` | `varchar` | Name associated with the represented feature. |
| `vp_ref` | `integer` | Count or numeric value for vp reference in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
