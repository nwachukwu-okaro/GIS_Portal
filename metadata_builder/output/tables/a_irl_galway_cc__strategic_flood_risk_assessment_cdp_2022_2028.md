# Strategic Flood Risk Assessment Cdp 2022 2028

## Overview

- **Identifier:** `a_irl_galway_cc/strategic_flood_risk_assessment_cdp_2022_2028`
- **Source organisation:** Galway County Council
- **Source:** https://data.gov.ie/organization/galway-county-council
- **Geographic coverage:** County Galway
- **WGS84 extent:** `[-10.033216, 53.079719, -8.194687, 53.622603]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_galway_cc`
- **Table:** `strategic_flood_risk_assessment_cdp_2022_2028`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 30
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Strategic Flood Risk Assessment Cdp 2022 2028 is an authoritative dataset published by Galway County Council. It represents strategic flood risk assessment cdp 2022 2028 features using multipolygon geometry.

## Lineage

Published by Galway County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `object_id` | `smallint` | Identifier assigned by the source dataset. |
| `flood_zone` | `varchar` | Publisher-supplied flood zone for the represented feature or record. |
| `town` | `varchar` | Publisher-supplied town for the represented feature or record. |
| `plan` | `varchar` | Publisher-supplied plan for the represented feature or record. |
| `sfra_pk` | `integer` | Count or numeric value for sfra pk in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
