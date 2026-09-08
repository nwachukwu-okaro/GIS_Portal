# Risk of Flooding from Surface Water - Model Origin

## Overview

- **Identifier:** `a_environment_agency/rofsw_model_origin`
- **Source organisation:** Environment Agency
- **Source:** https://environment.data.gov.uk/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-2.585311, 55.292710, -2.001546, 55.806273]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_environment_agency`
- **Table:** `rofsw_model_origin`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1000
- **Columns:** 6
- **Metadata status:** context_curated

## Description

Areas identifying the model source and vintage used in the national Risk of Flooding from Surface Water mapping.

## Lineage

Published by Environment Agency as open environmental data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `model` | `varchar(254)` | Name or description of the flood model that produced the feature. |
| `scale` | `varchar(8)` | Geographic scale of the model, such as National. |
| `model_year` | `smallint` | Year associated with the flood-model version or run. |
| `flood_source` | `varchar(16)` | Source of flooding represented, such as river, sea or surface water. |
| `uuid` | `char(36)` | Globally unique identifier for the model-origin record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
