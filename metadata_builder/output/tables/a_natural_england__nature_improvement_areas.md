# Nature Improvement Areas

## Overview

- **Identifier:** `a_natural_england/nature_improvement_areas`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Local dataset version:** 20170425 (25 April 2017)
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-4.475307, 50.576379, 1.025990, 54.345053]`
- **Schema:** `a_natural_england`
- **Table:** `nature_improvement_areas`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 12
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

version: 20170425
Source: https://environment.data.gov.uk/dataset/899230b5-0247-4af8-9265-ff65009287eb

Attribution: © Natural England copyright. Contains Ordnance Survey data © Crown copyright and database right [year].

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
| `nia_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `hectares` | `double precision` | Count or numeric value for hectares in the represented area. | statistical_value | Yes | No | No |
| `gdb_geomattr_data` | `bytea` | Publisher-supplied gdb geomattr data for the represented feature or record. | source_attribute | Yes | No | No |
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
