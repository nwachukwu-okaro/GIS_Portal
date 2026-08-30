# 625k Faults

## Overview

- **Identifier:** `a_british_geological_survey/625k_faults`
- **Source organisation:** British Geological Survey
- **Product:** BGS geological data
- **Source:** https://www.bgs.ac.uk/geological-data/
- **Schema:** `a_british_geological_survey`
- **Table:** `625k_faults`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 2741
- **Metadata status:** source_mapped

## Description

Contains British Geological Survey materials © UKRI 2026

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `category` | `varchar(32)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `feature` | `varchar(60)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `feature_d` | `varchar(100)` | Human-readable description associated with the corresponding coded attribute. | description | Yes | Yes | No |
| `fltname_c` | `varchar(6)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `fltname_d` | `varchar(100)` | Human-readable description associated with the corresponding coded attribute. | description | Yes | Yes | No |
| `sheet` | `varchar(60)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `version` | `varchar(10)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `released` | `varchar(10)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `nom_scale` | `varchar(10)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `nom_os_yr` | `varchar(10)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `nom_bgs_yr` | `varchar(10)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `mslink` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `625f_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
