# National Nature Reserves

## Overview

- **Identifier:** `a_natural_england/national_nature_reserves`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.268715, 49.958805, 1.728821, 55.722838]`
- **Schema:** `a_natural_england`
- **Table:** `national_nature_reserves`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 224
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

National Nature Reserves is an authoritative dataset published by Natural England. It represents national nature reserves features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Publisher-assigned identifier for the record. | source_identifier | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |
| `OBJECTID` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
| `HYPERLINK` | `varchar(16)` | URL of the corresponding record on the publisher's website. | source_record_url | Yes | No | No |
| `REF_CODE` | `varchar(10)` | Code assigned by the source dataset. | code | Yes | No | No |
| `NAME` | `varchar(120)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `MEASURE` | `double precision` | Count or numeric value for measure in the represented area. | statistical_value | Yes | No | No |
| `LABEL` | `varchar(140)` | Publisher-supplied label for the represented feature or record. | source_attribute | Yes | No | No |
| `GlobalID` | `varchar(38)` | Publisher-assigned globalid for the record. | source_identifier | Yes | No | No |

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
