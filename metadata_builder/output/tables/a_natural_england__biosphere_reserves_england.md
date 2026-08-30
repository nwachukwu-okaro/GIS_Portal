# Biosphere Reserves England

## Overview

- **Identifier:** `a_natural_england/biosphere_reserves_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Local dataset version:** 20251009 (9 October 2025)
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-4.889167, 50.553811, 0.096717, 51.292573]`
- **Schema:** `a_natural_england`
- **Table:** `biosphere_reserves_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 3
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

version: 20251009
Source: https://naturalengland-defra.opendata.arcgis.com/datasets/Defra::biosphere-reserves-england/about

Attribution: © Natural England copyright. Contains Ordnance Survey data © Crown copyright and database right [year]. Attribution statement: © Natural England copyright. Contains Ordnance Survey data © Crown copyright and database right [year].

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `status` | `varchar` | Publisher-supplied status for the represented feature or record. | source_attribute | Yes | No | No |
| `area` | `real` | Numeric area value recorded for the feature. | measure | Yes | No | No |
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
