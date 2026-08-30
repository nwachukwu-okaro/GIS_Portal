# Public Rights Of Way

## Overview

- **Identifier:** `a_oxfordshire_county_council/public_rights_of_way`
- **Source organisation:** Oxfordshire County Council
- **Source:** https://insight.oxfordshire.gov.uk/cms/open-data
- **Schema:** `a_oxfordshire_county_council`
- **Table:** `public_rights_of_way`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:4326
- **Rows:** 10469
- **Metadata status:** source_mapped

## Description

Public Rights Of Way is an authoritative dataset published by Oxfordshire County Council. It represents public rights of way features using multilinestring geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `legal_typed` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `status_description` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `route_number` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `parish_code` | `varchar` | Code assigned by the source dataset. | code | Yes | No | No |
| `route_code` | `varchar` | Code assigned by the source dataset. | code | Yes | No | No |
| `parish_name` | `varchar` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `status` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `legal_type` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `length_m` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `easting` | `double precision` | Easting coordinate in the dataset coordinate reference system. | x_coordinate | Yes | No | No |
| `northing` | `double precision` | Northing coordinate in the dataset coordinate reference system. | y_coordinate | Yes | No | No |
| `easting_end` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `northing_end` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `easting_start` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `northing_start` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `oprow_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
