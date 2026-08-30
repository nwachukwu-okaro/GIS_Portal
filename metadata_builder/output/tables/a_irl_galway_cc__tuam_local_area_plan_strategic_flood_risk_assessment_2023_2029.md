# Tuam Local Area Plan Strategic Flood Risk Assessment 2023 2029

## Overview

- **Identifier:** `a_irl_galway_cc/tuam_local_area_plan_strategic_flood_risk_assessment_2023_2029`
- **Source organisation:** Galway County Council
- **Source:** https://data.gov.ie/organization/galway-county-council
- **Geographic coverage:** County Galway
- **WGS84 extent:** `[-8.887475, 53.503134, -8.827930, 53.531496]`
- **Schema:** `a_irl_galway_cc`
- **Table:** `tuam_local_area_plan_strategic_flood_risk_assessment_2023_2029`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 2
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Tuam Local Area Plan Strategic Flood Risk Assessment 2023 2029 is an authoritative dataset published by Galway County Council. It represents tuam local area plan strategic flood risk assessment 2023 2029 features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `object_id` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `flood_zone` | `varchar` | Publisher-supplied flood zone for the represented feature or record. | source_attribute | Yes | No | No |
| `description` | `varchar` | Publisher-supplied description for the represented feature or record. | source_attribute | Yes | No | No |
| `town` | `varchar` | Publisher-supplied town for the represented feature or record. | source_attribute | Yes | No | No |
| `plan_name` | `varchar` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
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
