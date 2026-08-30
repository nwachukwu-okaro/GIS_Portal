# Record Of Protected Structures

## Overview

- **Identifier:** `a_irl_meath_cc/record_of_protected_structures`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Schema:** `a_irl_meath_cc`
- **Table:** `record_of_protected_structures`
- **Geometry:** POINT
- **CRS:** EPSG:2157
- **Rows:** 1410
- **Metadata status:** source_mapped

## Description

Record Of Protected Structures is an authoritative dataset published by Meath County Council. It represents record of protected structures features using point geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `rps_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `la_rps_id` | `double precision` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `niah_reg_n` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `municipal_` | `varchar(36)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `townland` | `varchar(58)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `town` | `varchar(34)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `street_tow` | `varchar(90)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `cdp_settle` | `varchar(116)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `structure_` | `varchar(100)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `structur00` | `varchar(18)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `building_t` | `varchar(100)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `description` | `varchar(254)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
