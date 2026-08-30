# Ramsar Sites Listed And Proposed

## Overview

- **Identifier:** `a_natural_england/ramsar_sites_listed_and_proposed`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.418622, 49.863188, 1.716710, 55.754242]`
- **Schema:** `a_natural_england`
- **Table:** `ramsar_sites_listed_and_proposed`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1495
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Ramsar Sites Listed And Proposed is an authoritative dataset published by Natural England. It represents ramsar sites listed and proposed features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `name` | `text` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `code` | `text` | Count or numeric value for code in the represented area. | statistical_value | Yes | No | No |
| `status` | `text` | Publisher-supplied status for the represented feature or record. | source_attribute | Yes | No | No |
| `file` | `text` | Publisher-supplied file for the represented feature or record. | source_attribute | Yes | No | No |
| `gis_date` | `text` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `version` | `integer` | Publisher-supplied version for the represented feature or record. | source_attribute | Yes | No | No |
| `rse_pk` | `integer` | Count or numeric value for rse pk in the represented area. | statistical_value | Yes | No | No |
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

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
