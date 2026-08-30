# Boundary Lad Dec 2025 UK Bfe

## Overview

- **Identifier:** `a_ons_england_wales/boundary_lad_dec_2025_uk_bfe`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **WGS84 extent:** `[-8.650007, 49.864637, 1.768950, 60.860846]`
- **Schema:** `a_ons_england_wales`
- **Table:** `boundary_lad_dec_2025_uk_bfe`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 361
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Boundary Lad Dec 2025 UK Bfe is an authoritative dataset published by Office for National Statistics. It represents boundary lad dec 2025 uk bfe features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `fid` | `integer` | Feature identifier assigned by the source or import process. | identifier | Yes | No | No |
| `lad25cd` | `varchar(9)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lad25nm` | `varchar(100)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lad25nmw` | `varchar(24)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `bng_e` | `integer` | Count or numeric value for bng e in the represented area. | statistical_value | Yes | No | No |
| `bng_n` | `integer` | Count or numeric value for bng n in the represented area. | statistical_value | Yes | No | No |
| `long` | `real` | Numeric long value recorded for the feature. | measure | Yes | No | No |
| `lat` | `real` | Numeric lat value recorded for the feature. | measure | Yes | No | No |
| `globalid` | `varchar(38)` | Publisher-assigned globalid for the record. | source_identifier | Yes | No | No |
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

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
