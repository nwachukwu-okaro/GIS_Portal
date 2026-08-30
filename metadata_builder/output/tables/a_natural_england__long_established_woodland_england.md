# Long Established Woodland England

## Overview

- **Identifier:** `a_natural_england/long_established_woodland_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Local dataset version:** 20251028 (28 October 2025)
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-2.991100, 50.778680, 1.244674, 54.194787]`
- **Schema:** `a_natural_england`
- **Table:** `long_established_woodland_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 9518
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Version: 20251028
Source: https://naturalengland-defra.opendata.arcgis.com/datasets/Defra::long-established-woodland-england/about
Attribution: © Natural England 2025, Contains OS data © Crown copyright and database rights 2025. OS AC0000851168

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `theme` | `varchar` | Publisher-supplied theme for the represented feature or record. | source_attribute | Yes | No | No |
| `themname` | `varchar` | Publisher-supplied themname for the represented feature or record. | source_attribute | Yes | No | No |
| `status` | `varchar` | Publisher-supplied status for the represented feature or record. | source_attribute | Yes | No | No |
| `themid` | `varchar` | Publisher-assigned themid for the record. | source_identifier | Yes | No | No |
| `x_coord` | `integer` | Count or numeric value for x coord in the represented area. | statistical_value | Yes | No | No |
| `y_coord` | `integer` | Count or numeric value for y coord in the represented area. | statistical_value | Yes | No | No |
| `area` | `real` | Numeric area value recorded for the feature. | measure | Yes | No | No |
| `perimeter` | `real` | Count or numeric value for perimeter in the represented area. | statistical_value | Yes | No | No |
| `county` | `varchar` | Publisher-supplied county for the represented feature or record. | source_attribute | Yes | No | No |
| `globalid` | `varchar` | Publisher-assigned globalid for the record. | source_identifier | Yes | No | No |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
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
