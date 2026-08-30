# National Cycle Network Public

## Overview

- **Identifier:** `a_sustrans/national_cycle_network_public`
- **Source organisation:** Sustrans
- **Source:** https://data.sustrans.org.uk/
- **Geographic coverage:** United Kingdom
- **WGS84 extent:** `[-7.650111, 50.062727, 1.762548, 57.817561]`
- **Schema:** `a_sustrans`
- **Table:** `national_cycle_network_public`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 37210
- **Columns:** 15
- **Metadata status:** source_mapped

## Description

National Cycle Network Public is an authoritative dataset published by Sustrans. It represents national cycle network public features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `desc_` | `text` | Publisher-supplied description for the represented feature or record. | source_attribute | Yes | No | No |
| `greenway` | `text` | Publisher-supplied greenway for the represented feature or record. | source_attribute | Yes | No | No |
| `routetype` | `text` | Publisher-supplied routetype for the represented feature or record. | source_attribute | Yes | No | No |
| `routeno` | `integer` | Count or numeric value for routeno in the represented area. | statistical_value | Yes | No | No |
| `linkno` | `integer` | Count or numeric value for linkno in the represented area. | statistical_value | Yes | No | No |
| `routecat` | `text` | Publisher-supplied routecat for the represented feature or record. | source_attribute | Yes | No | No |
| `openstatus` | `text` | Publisher-supplied openstatus for the represented feature or record. | source_attribute | Yes | No | No |
| `surface` | `text` | Publisher-supplied surface for the represented feature or record. | source_attribute | Yes | No | No |
| `quality` | `text` | Publisher-supplied quality for the represented feature or record. | source_attribute | Yes | No | No |
| `lighting` | `text` | Publisher-supplied lighting for the represented feature or record. | source_attribute | Yes | No | No |
| `roadclass` | `text` | Publisher-supplied roadclass for the represented feature or record. | source_attribute | Yes | No | No |
| `globalid` | `text` | Publisher-assigned globalid for the record. | source_identifier | Yes | No | No |
| `segmentid` | `integer` | Count or numeric value for segmentid in the represented area. | statistical_value | Yes | No | No |
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

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
