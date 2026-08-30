# Protected Views Angles Of View Cdp 2022 2028

## Overview

- **Identifier:** `a_irl_galway_cc/protected_views_angles_of_view_cdp_2022_2028`
- **Source organisation:** Galway County Council
- **Source:** https://data.gov.ie/organization/galway-county-council
- **Geographic coverage:** County Galway
- **WGS84 extent:** `[-10.167256, 53.004080, -7.978482, 53.620748]`
- **Schema:** `a_irl_galway_cc`
- **Table:** `protected_views_angles_of_view_cdp_2022_2028`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 52
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Protected Views Angles Of View Cdp 2022 2028 is an authoritative dataset published by Galway County Council. It represents protected views angles of view cdp 2022 2028 features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `description_of_view` | `varchar` | Publisher-supplied description of view for the represented feature or record. | source_attribute | Yes | No | No |
| `location_of_view` | `varchar` | Publisher-supplied location of view for the represented feature or record. | source_attribute | Yes | No | No |
| `object_id` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `photos_report` | `varchar` | Publisher-supplied photos report for the represented feature or record. | source_attribute | Yes | No | No |
| `significance` | `varchar` | Publisher-supplied significance for the represented feature or record. | source_attribute | Yes | No | No |
| `view_angle` | `integer` | Count or numeric value for view angle in the represented area. | statistical_value | Yes | No | No |
| `view_rotation` | `integer` | Count or numeric value for view rotation in the represented area. | statistical_value | Yes | No | No |
| `vp_name` | `varchar` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `vp_ref` | `integer` | Count or numeric value for vp reference in the represented area. | statistical_value | Yes | No | No |
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
