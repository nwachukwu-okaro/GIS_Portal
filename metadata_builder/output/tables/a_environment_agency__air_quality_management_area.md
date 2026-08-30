# Air Quality Management Areas

## Overview

- **Identifier:** `a_environment_agency/air_quality_management_area`
- **Source organisation:** Environment Agency
- **Source:** https://environment.data.gov.uk/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.319875, 50.204441, 1.447693, 55.010160]`
- **Schema:** `a_environment_agency`
- **Table:** `air_quality_management_area`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 498
- **Columns:** 15
- **Metadata status:** context_curated

## Description

Boundaries of Air Quality Management Areas declared by UK local authorities where air-quality objectives are unlikely to be met.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `dataset` | `varchar` | Machine-readable name of the source dataset. | dataset_name | Yes | No | No |
| `end_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `entity` | `varchar` | Unique identifier assigned to the published geographic entity. | entity_identifier | Yes | No | No |
| `entry_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `organisation_entity` | `varchar` | Identifier of the organisation responsible for the entity record. | responsible_organisation_identifier | Yes | No | No |
| `prefix` | `varchar` | Dataset prefix used to construct or classify the entity identifier. | dataset_prefix | Yes | No | No |
| `quality` | `varchar` | Source quality classification recorded for the geographic entity. | data_quality_class | Yes | No | No |
| `reference` | `varchar` | Publisher reference number for the Air Quality Management Area. | aqma_reference | Yes | No | No |
| `start_date` | `varchar` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `typology` | `varchar` | Entity type classification, such as geography. | entity_type | Yes | No | No |
| `documentation_url` | `varchar` | URL of the official detailed record for the Air Quality Management Area. | source_record_url | Yes | No | No |
| `notes` | `varchar` | Related local-authority geographic code recorded against the area. | local_authority_code | Yes | No | No |
| `aqma_pk` | `integer` | Internal primary-key value for the imported Air Quality Management Area. | record_identifier | Yes | No | No |
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
