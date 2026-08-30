# Ltla Boundary Bgc

## Overview

- **Identifier:** `a_ons_england_wales/ltla_boundary_bgc`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **WGS84 extent:** `[-6.418601, 49.864798, 1.763680, 55.811118]`
- **Schema:** `a_ons_england_wales`
- **Table:** `ltla_boundary_bgc`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 331
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Ltla Boundary Bgc is an authoritative dataset published by Office for National Statistics. It represents ltla boundary bgc features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. | statistical_value | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. | identifier | Yes | No | No |
| `lad22cd` | `varchar(9)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lad22nm` | `varchar(36)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `bng_e` | `integer` | Count or numeric value for bng e in the represented area. | statistical_value | Yes | No | No |
| `bng_n` | `integer` | Count or numeric value for bng n in the represented area. | statistical_value | Yes | No | No |
| `long` | `double precision` | Numeric long value recorded for the feature. | measure | Yes | No | No |
| `lat` | `double precision` | Numeric lat value recorded for the feature. | measure | Yes | No | No |
| `globalid` | `varchar(38)` | Publisher-assigned globalid for the record. | source_identifier | Yes | No | No |

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
