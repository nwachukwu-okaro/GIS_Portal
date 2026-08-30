# Ancient Woodland England

## Overview

- **Identifier:** `a_natural_england/ancient_woodland_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Local dataset version:** 20251009 (9 October 2025)
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.560508, 50.036191, 1.739062, 55.773698]`
- **Schema:** `a_natural_england`
- **Table:** `ancient_woodland_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 53636
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Version: 20251009
Source: https://www.data.gov.uk/dataset/9461f463-c363-4309-ae77-fdcd7e9df7d3/ancient-woodland-england

Attribution: © Natural England copyright. Contains Ordnance Survey data © Crown copyright and database right [year].

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `name` | `varchar(150)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `theme` | `varchar(19)` | Publisher-supplied theme for the represented feature or record. | source_attribute | Yes | No | No |
| `themname` | `varchar(37)` | Publisher-supplied themname for the represented feature or record. | source_attribute | Yes | No | No |
| `status` | `varchar(8)` | Publisher-supplied status for the represented feature or record. | source_attribute | Yes | No | No |
| `x_coord` | `integer` | Count or numeric value for x coord in the represented area. | statistical_value | Yes | No | No |
| `y_coord` | `integer` | Count or numeric value for y coord in the represented area. | statistical_value | Yes | No | No |
| `themid` | `varchar(255)` | Publisher-assigned themid for the record. | source_identifier | Yes | No | No |
| `area` | `real` | Numeric area value recorded for the feature. | measure | Yes | No | No |
| `perimeter` | `real` | Count or numeric value for perimeter in the represented area. | statistical_value | Yes | No | No |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. | identifier | Yes | No | No |
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
