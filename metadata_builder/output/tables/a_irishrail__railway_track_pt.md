# Railway Track Pt

## Overview

- **Identifier:** `a_irishrail/railway_track_pt`
- **Source organisation:** Iarnrod Eireann / Irish Rail
- **Source:** https://www.irishrail.ie/travel-information/iarnrod-eireann-open-data
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-9.699184, 51.846274, -6.034982, 54.274002]`
- **Schema:** `a_irishrail`
- **Table:** `railway_track_pt`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:29903
- **Rows:** 478313
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Railway Track Pt is an authoritative dataset published by Iarnrod Eireann / Irish Rail. It represents railway track pt features using multipoint geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `railway_track_pt_pk` | `integer` | Count or numeric value for railway track pt pk in the represented area. | statistical_value | Yes | No | No |
| `z` | `real` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `text_string` | `varchar(8)` | Publisher-supplied text string for the represented feature or record. | source_attribute | Yes | No | No |
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

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
