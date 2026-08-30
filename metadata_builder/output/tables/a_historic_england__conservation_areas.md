# Conservation Areas

## Overview

- **Identifier:** `a_historic_england/conservation_areas`
- **Source organisation:** Historic England
- **Product:** National Heritage List for England spatial data
- **Source:** https://historicengland.org.uk/listing/the-list/map-data/
- **Schema:** `a_historic_england`
- **Table:** `conservation_areas`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 8162
- **Metadata status:** source_mapped

## Description

Version: 20250702
Source: https://opendata-historicengland.hub.arcgis.com/datasets/historicengland::conservation-areas/explore

Attribution: © Historic England [year]. Contains Ordnance Survey data © Crown copyright and database right [year].

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `uid` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `name` | `varchar(150)` | Name of the represented feature. | feature_name | Yes | Yes | No |
| `date_of_de` | `varchar(50)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `date_updat` | `varchar(50)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lpa` | `varchar(50)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `capture_sc` | `varchar(50)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `x` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `y` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `objectid` | `bigint` | Source-system object identifier. | identifier | Yes | No | No |
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

- Verify against the individual Historic England download metadata.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
