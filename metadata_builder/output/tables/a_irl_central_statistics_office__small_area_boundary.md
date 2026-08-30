# Small Area Boundary

## Overview

- **Identifier:** `a_irl_central_statistics_office/small_area_boundary`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.662971, 51.419897, -5.996278, 55.446580]`
- **Schema:** `a_irl_central_statistics_office`
- **Table:** `small_area_boundary`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:2157
- **Rows:** 18919
- **Columns:** 27
- **Metadata status:** source_mapped

## Description

Small Area Boundary is an authoritative dataset published by Central Statistics Office Ireland. It represents small area boundary features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `sa_guid_2016` | `text` | Publisher-supplied sa guid 2016 for the represented feature or record. | source_attribute | Yes | No | No |
| `sa_guid_2022` | `text` | Publisher-supplied sa guid 2022 for the represented feature or record. | source_attribute | Yes | No | No |
| `sa_pub2011` | `text` | Publisher-supplied sa pub2011 for the represented feature or record. | source_attribute | Yes | No | No |
| `sa_pub2016` | `text` | Publisher-supplied sa pub2016 for the represented feature or record. | source_attribute | Yes | No | No |
| `sa_pub2022` | `text` | Publisher-supplied sa pub2022 for the represented feature or record. | source_attribute | Yes | No | No |
| `sa_geogid_2022` | `text` | Publisher-supplied sa geogid 2022 for the represented feature or record. | source_attribute | Yes | No | No |
| `sa_change_code` | `smallint` | Code assigned by the source dataset. | code | Yes | No | No |
| `sa_urban_area_flag` | `smallint` | Numeric sa urban area flag value recorded for the feature. | measure | Yes | No | No |
| `sa_urban_area_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `sa_nuts1` | `text` | Publisher-supplied sa nuts1 for the represented feature or record. | source_attribute | Yes | No | No |
| `sa_nuts1_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `sa_nuts2` | `text` | Publisher-supplied sa nuts2 for the represented feature or record. | source_attribute | Yes | No | No |
| `sa_nuts2_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `sa_nuts3` | `text` | Publisher-supplied sa nuts3 for the represented feature or record. | source_attribute | Yes | No | No |
| `sa_nuts3_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `ed_guid` | `text` | Publisher-assigned ed guid for the record. | source_identifier | Yes | No | No |
| `ed_official` | `text` | Publisher-supplied ed official for the represented feature or record. | source_attribute | Yes | No | No |
| `ed_english` | `text` | Publisher-supplied ed english for the represented feature or record. | source_attribute | Yes | No | No |
| `ed_gaeilge` | `text` | Publisher-supplied ed gaeilge for the represented feature or record. | source_attribute | Yes | No | No |
| `ed_id_str` | `text` | Publisher-supplied ed identifier str for the represented feature or record. | source_attribute | Yes | No | No |
| `ed_part_count` | `smallint` | Count or numeric value for ed part count in the represented area. | statistical_value | Yes | No | No |
| `county_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `county_english` | `text` | Publisher-supplied county english for the represented feature or record. | source_attribute | Yes | No | No |
| `county_gaeilge` | `text` | Publisher-supplied county gaeilge for the represented feature or record. | source_attribute | Yes | No | No |
| `cso_lea` | `text` | Publisher-supplied cso lea for the represented feature or record. | source_attribute | Yes | No | No |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
| `shape` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |

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
