# Geoheritage Audited Sites

## Overview

- **Identifier:** `a_irl_geological_survey/geoheritage_audited_sites`
- **Source organisation:** Geological Survey Ireland
- **Source:** https://www.gsi.ie/en-ie/data-and-maps/Pages/default.aspx
- **Schema:** `a_irl_geological_survey`
- **Table:** `geoheritage_audited_sites`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 1148
- **Metadata status:** source_mapped

## Description

Geoheritage Audited Sites is an authoritative dataset published by Geological Survey Ireland. It represents geoheritage audited sites features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `gas_id` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `sitecode` | `varchar(7)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `sitename` | `varchar(75)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `igh1` | `varchar(5)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `igh2` | `varchar(5)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `igh3` | `varchar(5)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `igh4` | `varchar(5)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `county` | `varchar(25)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `description` | `varchar(200)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `geological` | `varchar(254)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `designat` | `varchar(50)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `report` | `varchar(200)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `x_ig` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `y_ig` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `x_itm` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `y_itm` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
