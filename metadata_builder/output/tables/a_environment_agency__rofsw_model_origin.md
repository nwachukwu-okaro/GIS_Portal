# Risk of Flooding from Surface Water - Model Origin

## Overview

- **Identifier:** `a_environment_agency/rofsw_model_origin`
- **Source organisation:** Environment Agency
- **Source:** https://environment.data.gov.uk/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-2.585311, 55.292710, -2.001546, 55.806273]`
- **Schema:** `a_environment_agency`
- **Table:** `rofsw_model_origin`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1000
- **Columns:** 6
- **Metadata status:** context_curated

## Description

Areas identifying the model source and vintage used in the national Risk of Flooding from Surface Water mapping.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `model` | `varchar(254)` | Name or description of the flood model that produced the feature. | flood_model_name | Yes | No | No |
| `scale` | `varchar(8)` | Geographic scale of the model, such as National. | model_scale | Yes | No | No |
| `model_year` | `smallint` | Year associated with the flood-model version or run. | model_year | Yes | No | No |
| `flood_source` | `varchar(16)` | Source of flooding represented, such as river, sea or surface water. | flood_source | Yes | No | No |
| `uuid` | `char(36)` | Globally unique identifier for the model-origin record. | record_identifier | Yes | No | No |
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
