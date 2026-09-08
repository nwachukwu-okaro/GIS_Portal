# Air Quality Management Areas

## Overview

- **Identifier:** `a_environment_agency/air_quality_management_area`
- **Source organisation:** Environment Agency
- **Source:** https://environment.data.gov.uk/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.319875, 50.204441, 1.447693, 55.010160]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_environment_agency`
- **Table:** `air_quality_management_area`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 498
- **Columns:** 15
- **Metadata status:** context_curated

## Description

Boundaries of Air Quality Management Areas declared by UK local authorities where air-quality objectives are unlikely to be met.

## Lineage

Published by Environment Agency as open environmental data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `dataset` | `varchar` | Machine-readable name of the source dataset. |
| `end_date` | `varchar` | Date associated with the represented feature or source record. |
| `entity` | `varchar` | Unique identifier assigned to the published geographic entity. |
| `entry_date` | `varchar` | Date associated with the represented feature or source record. |
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. |
| `organisation_entity` | `varchar` | Identifier of the organisation responsible for the entity record. |
| `prefix` | `varchar` | Dataset prefix used to construct or classify the entity identifier. |
| `quality` | `varchar` | Source quality classification recorded for the geographic entity. |
| `reference` | `varchar` | Publisher reference number for the Air Quality Management Area. |
| `start_date` | `varchar` | Date associated with the represented feature or source record. |
| `typology` | `varchar` | Entity type classification, such as geography. |
| `documentation_url` | `varchar` | URL of the official detailed record for the Air Quality Management Area. |
| `notes` | `varchar` | Related local-authority geographic code recorded against the area. |
| `aqma_pk` | `integer` | Internal primary-key value for the imported Air Quality Management Area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
