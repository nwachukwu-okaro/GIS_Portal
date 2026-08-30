# Borehole Records

## Overview

- **Identifier:** `a_british_geological_survey/borehole_records`
- **Source organisation:** British Geological Survey
- **Product:** BGS geological data
- **Source:** https://www.bgs.ac.uk/geological-data/
- **Schema:** `a_british_geological_survey`
- **Table:** `borehole_records`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:27700
- **Rows:** 1351536
- **Metadata status:** source_mapped

## Description

Contains British Geological Survey materials © UKRI 2026

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `qs` | `varchar(6)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `numb` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `bsuff` | `varchar(4)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `regno` | `varchar(51)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `rt` | `varchar(2)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `grid_refer` | `varchar(14)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `confidenti` | `varchar(1)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `strtheight` | `real` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `name` | `varchar(150)` | Name of the represented feature. | feature_name | Yes | Yes | No |
| `length` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `bgs_id` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `date_known` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `date_k_typ` | `varchar(68)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `date_enter` | `date` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ags_log_ur` | `varchar(254)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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

- Verify the licence against the individual BGS product; not all BGS products are open.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
