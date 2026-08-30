# Land Use Zonings Cdp 2022 2028

## Overview

- **Identifier:** `a_irl_galway_cc/land_use_zonings_cdp_2022_2028`
- **Source organisation:** Galway County Council
- **Source:** https://data.gov.ie/organization/galway-county-council
- **Geographic coverage:** County Galway
- **WGS84 extent:** `[-10.033886, 53.079719, -8.194687, 53.622603]`
- **Schema:** `a_irl_galway_cc`
- **Table:** `land_use_zonings_cdp_2022_2028`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 2480
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Land Use Zonings Cdp 2022 2028 is an authoritative dataset published by Galway County Council. It represents land use zonings cdp 2022 2028 features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `object_id` | `smallint` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `id` | `varchar` | Publisher-assigned identifier for the record. | source_identifier | Yes | No | No |
| `zoning` | `varchar` | Publisher-supplied zoning for the represented feature or record. | source_attribute | Yes | No | No |
| `status` | `varchar` | Publisher-supplied status for the represented feature or record. | source_attribute | Yes | No | No |
| `town` | `varchar` | Publisher-supplied town for the represented feature or record. | source_attribute | Yes | No | No |
| `plan_name` | `varchar` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `zoning_iri` | `varchar` | Publisher-supplied zoning iri for the represented feature or record. | source_attribute | Yes | No | No |
| `opportunit` | `varchar` | Publisher-supplied opportunit for the represented feature or record. | source_attribute | Yes | No | No |
| `flood_note` | `varchar` | Publisher-supplied flood note for the represented feature or record. | source_attribute | Yes | No | No |
| `field` | `varchar` | Publisher-supplied field for the represented feature or record. | source_attribute | Yes | No | No |
| `policy_obj` | `varchar` | Publisher-supplied policy obj for the represented feature or record. | source_attribute | Yes | No | No |
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
