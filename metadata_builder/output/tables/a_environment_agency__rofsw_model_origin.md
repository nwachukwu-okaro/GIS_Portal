# Rofsw Model Origin

## Overview

- **Identifier:** `a_environment_agency/rofsw_model_origin`
- **Source organisation:** Environment Agency
- **Source:** https://environment.data.gov.uk/
- **Schema:** `a_environment_agency`
- **Table:** `rofsw_model_origin`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1000
- **Metadata status:** source_mapped

## Description

Rofsw Model Origin is an authoritative dataset published by Environment Agency. It represents rofsw model origin features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `model` | `varchar(254)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `scale` | `varchar(8)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `model_year` | `smallint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `flood_source` | `varchar(16)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `uuid` | `char(36)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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

- Schema default only; verify dataset-specific restrictions and third-party rights.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
