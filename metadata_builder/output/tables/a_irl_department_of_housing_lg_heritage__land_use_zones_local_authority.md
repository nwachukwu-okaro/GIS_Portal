# Land Use Zones Local Authority

## Overview

- **Identifier:** `a_irl_department_of_housing_lg_heritage/land_use_zones_local_authority`
- **Source organisation:** Department of Housing, Local Government and Heritage
- **Source:** https://www.gov.ie/en/organisation/department-of-housing-local-government-and-heritage/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.413342, 51.463662, -5.994535, 54.473025]`
- **Schema:** `a_irl_department_of_housing_lg_heritage`
- **Table:** `land_use_zones_local_authority`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 85330
- **Columns:** 20
- **Metadata status:** source_mapped

## Description

Land Use Zones Local Authority is an authoritative dataset published by Department of Housing, Local Government and Heritage. It represents land use zones local authority features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `zone_gzt` | `varchar` | Publisher-supplied zone gzt for the represented feature or record. | source_attribute | Yes | No | No |
| `zone_orig` | `varchar` | Publisher-supplied zone orig for the represented feature or record. | source_attribute | Yes | No | No |
| `zone_desc` | `varchar` | Publisher-supplied zone description for the represented feature or record. | source_attribute | Yes | No | No |
| `zone_link` | `varchar` | Publisher-supplied zone link for the represented feature or record. | source_attribute | Yes | No | No |
| `plan_from` | `date` | Publisher-supplied plan from for the represented feature or record. | source_attribute | Yes | No | No |
| `plan_to` | `date` | Publisher-supplied plan to for the represented feature or record. | source_attribute | Yes | No | No |
| `plan_name` | `varchar` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `colour` | `varchar` | Publisher-supplied colour for the represented feature or record. | source_attribute | Yes | No | No |
| `la_code` | `varchar` | Code assigned by the source dataset. | code | Yes | No | No |
| `gzt_desc` | `varchar` | Publisher-supplied gzt description for the represented feature or record. | source_attribute | Yes | No | No |
| `gzt_link` | `varchar` | Publisher-supplied gzt link for the represented feature or record. | source_attribute | Yes | No | No |
| `upload_date` | `date` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `current_pl` | `integer` | Count or numeric value for current pl in the represented area. | statistical_value | Yes | No | No |
| `plan_level` | `varchar` | Publisher-supplied plan level for the represented feature or record. | source_attribute | Yes | No | No |
| `szo` | `varchar` | Publisher-supplied szo for the represented feature or record. | source_attribute | Yes | No | No |
| `plan_id` | `varchar` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `la_name` | `varchar` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `zone_desc_` | `varchar` | Publisher-supplied zone description for the represented feature or record. | source_attribute | Yes | No | No |
| `luz_pk` | `integer` | Count or numeric value for luz pk in the represented area. | statistical_value | Yes | No | No |
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
