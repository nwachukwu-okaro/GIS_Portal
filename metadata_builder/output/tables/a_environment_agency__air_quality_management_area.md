# Air Quality Management Area

## Overview

- **Identifier:** `a_environment_agency/air_quality_management_area`
- **Source organisation:** Environment Agency
- **Source:** https://environment.data.gov.uk/
- **Schema:** `a_environment_agency`
- **Table:** `air_quality_management_area`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 498
- **Metadata status:** source_mapped

## Description

version: 20251122
Source: https://www.planning.data.gov.uk/dataset/air-quality-management-area

Attribution: © Crown copyright and database rights 2025 licenced under Defra's Public Sector Mapping Agreement with Ordnance Survey (licence No. 100022861)

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `dataset` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `end_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `entity` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `entry_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `name` | `varchar` | Name of the represented feature. | feature_name | Yes | Yes | No |
| `organisation_entity` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `prefix` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `quality` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `reference` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `start_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `typology` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `documentation_url` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `notes` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `aqma_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
