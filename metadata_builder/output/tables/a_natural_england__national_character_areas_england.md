# National Character Areas England

## Overview

- **Identifier:** `a_natural_england/national_character_areas_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Schema:** `a_natural_england`
- **Table:** `national_character_areas_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 159
- **Metadata status:** source_mapped

## Description

version: 20251009
Source: https://www.data.gov.uk/dataset/21104eeb-4a53-4e41-8ada-d2d442e416e0/national-character-areas-england1

© Natural England copyright. Contains Ordnance Survey data © Crown copyright and database right [year].

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `jcacode` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `jcaname` | `varchar(55)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `nca_name` | `varchar(55)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `naid` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `naname` | `varchar(45)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `area_sqkm` | `real` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `hotlink` | `varchar(254)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `alt` | `varchar(80)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `blt` | `varchar(75)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
