# Land Use Zonings Cdp 2022 2028

## Overview

- **Identifier:** `a_irl_galway_cc/land_use_zonings_cdp_2022_2028`
- **Source organisation:** Galway County Council
- **Source:** https://data.gov.ie/organization/galway-county-council
- **Geographic coverage:** County Galway
- **WGS84 extent:** `[-10.033886, 53.079719, -8.194687, 53.622603]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_galway_cc`
- **Table:** `land_use_zonings_cdp_2022_2028`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 2480
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Land Use Zonings Cdp 2022 2028 is an authoritative dataset published by Galway County Council. It represents land use zonings cdp 2022 2028 features using multipolygon geometry.

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
| `id` | `varchar` |  |
| `zoning` | `varchar` |  |
| `status` | `varchar` |  |
| `town` | `varchar` |  |
| `plan_name` | `varchar` | Name associated with the represented feature. |
| `zoning_iri` | `varchar` |  |
| `opportunit` | `varchar` |  |
| `flood_note` | `varchar` |  |
| `field` | `varchar` |  |
| `policy_obj` | `varchar` |  |
| `luz_pk` | `integer` | Primary-key identifier for records in land_use_zonings_cdp_2022_2028. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
