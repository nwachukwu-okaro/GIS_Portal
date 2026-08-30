# UK Boundary Output Areas

## Overview

- **Identifier:** `a_ons_england_wales/uk_boundary_output_areas`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **WGS84 extent:** `[-6.418601, 49.864674, 1.763680, 55.811091]`
- **Schema:** `a_ons_england_wales`
- **Table:** `uk_boundary_output_areas`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 188880
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

UK Boundary Output Areas is an authoritative dataset published by Office for National Statistics. It represents uk boundary output areas features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `oa21cd` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lsoa21cd` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lsoa21nm` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lsoa21nmw` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `bng_e` | `integer` | Count or numeric value for bng e in the represented area. | statistical_value | Yes | No | No |
| `bng_n` | `integer` | Count or numeric value for bng n in the represented area. | statistical_value | Yes | No | No |
| `lat` | `real` | Numeric lat value recorded for the feature. | measure | Yes | No | No |
| `long` | `real` | Numeric long value recorded for the feature. | measure | Yes | No | No |
| `globalid` | `text` | Publisher-assigned globalid for the record. | source_identifier | Yes | No | No |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. | identifier | Yes | No | No |
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
