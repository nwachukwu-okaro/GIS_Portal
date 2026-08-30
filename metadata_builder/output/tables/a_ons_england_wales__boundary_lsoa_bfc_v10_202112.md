# Boundary Lsoa Bfc V10 202112

## Overview

- **Identifier:** `a_ons_england_wales/boundary_lsoa_bfc_v10_202112`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **WGS84 extent:** `[-6.418601, 49.864674, 1.763680, 55.811091]`
- **Schema:** `a_ons_england_wales`
- **Table:** `boundary_lsoa_bfc_v10_202112`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 35672
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Boundary Lsoa Bfc V10 202112 is an authoritative dataset published by Office for National Statistics. It represents boundary lsoa bfc v10 202112 features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. | statistical_value | Yes | No | No |
| `lsoa21cd` | `varchar(9)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lsoa21nm` | `varchar(40)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `globalid` | `varchar(38)` | Publisher-assigned globalid for the record. | source_identifier | Yes | No | No |
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
