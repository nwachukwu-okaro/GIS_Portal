# Inspire Polygons

## Overview

- **Identifier:** `a_hm_land_registry/inspire_polygons`
- **Source organisation:** HM Land Registry
- **Source:** https://use-land-property-data.service.gov.uk/
- **WGS84 extent:** `[-6.418949, 49.864637, 1.763316, 55.811678]`
- **Schema:** `a_hm_land_registry`
- **Table:** `inspire_polygons`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 24422678
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Inspire Polygons is an authoritative dataset published by HM Land Registry. It represents inspire polygons features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `ogc_fid` | `integer` | Internal OGC feature identifier assigned during publication. | record_identifier | Yes | No | No |
| `gml_id` | `text` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `inspireid` | `integer` | INSPIRE identifier assigned to the cadastral parcel feature. | inspire_identifier | Yes | No | No |
| `label` | `integer` | Numeric label used to identify or display the cadastral parcel. | parcel_label | Yes | No | No |
| `nationalcadastralreference` | `integer` | National cadastral reference associated with the parcel polygon. | cadastral_reference | Yes | No | No |
| `validfrom` | `text` | Date and time from which the cadastral feature is valid in the source dataset. | valid_from_datetime | Yes | No | No |
| `beginlifespanversion` | `text` | Date and time when this version of the INSPIRE feature began its lifecycle. | lifecycle_start_datetime | Yes | No | No |
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
