# Counties And Unitary Authorities December 2024 Boundaries

## Overview

- **Identifier:** `a_ons_england_wales/Counties_and_Unitary_Authorities_December_2024_Boundaries`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **WGS84 extent:** `[-8.650007, 49.864798, 1.763680, 60.860745]`
- **Schema:** `a_ons_england_wales`
- **Table:** `Counties_and_Unitary_Authorities_December_2024_Boundaries`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 218
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Counties And Unitary Authorities December 2024 Boundaries is an authoritative dataset published by Office for National Statistics. It represents counties and unitary authorities december 2024 boundaries features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. | statistical_value | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. | identifier | Yes | No | No |
| `ctyua24cd` | `varchar(9)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ctyua24nm` | `varchar(36)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `ctyua24nmw` | `varchar(24)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
