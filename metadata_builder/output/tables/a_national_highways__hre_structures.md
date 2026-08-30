# Hre Structures

## Overview

- **Identifier:** `a_national_highways/hre_structures`
- **Source organisation:** National Highways
- **Source:** https://developer.data.nationalhighways.co.uk/
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.422375, 50.114472, 1.748077, 57.678794]`
- **Schema:** `a_national_highways`
- **Table:** `hre_structures`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 3287
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Hre Structures is an authoritative dataset published by National Highways. It represents hre structures features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `fid` | `smallint` | Feature identifier assigned by the source or import process. | identifier | Yes | No | No |
| `long_descr` | `varchar` | Publisher-supplied long descr for the represented feature or record. | source_attribute | Yes | No | No |
| `globalid` | `varchar` | Publisher-assigned globalid for the record. | source_identifier | Yes | No | No |
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
