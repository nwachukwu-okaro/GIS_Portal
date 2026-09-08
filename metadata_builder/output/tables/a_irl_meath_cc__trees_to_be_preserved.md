# Trees To Be Preserved

## Overview

- **Identifier:** `a_irl_meath_cc/trees_to_be_preserved`
- **Source organisation:** Meath County Council
- **Source:** https://data.gov.ie/organization/meath-county-council
- **Geographic coverage:** County Meath
- **WGS84 extent:** `[-6.681319, 53.632670, -6.645055, 53.659739]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_meath_cc`
- **Table:** `trees_to_be_preserved`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 9
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Trees To Be Preserved is an authoritative dataset published by Meath County Council. It represents trees to be preserved features using multipolygon geometry.

## Lineage

Published by Meath County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `ttbp_pk` | `integer` | Count or numeric value for ttbp pk in the represented area. |
| `reference` | `varchar(5)` | Publisher-supplied reference for the represented feature or record. |
| `location_se` | `varchar(254)` | Publisher-supplied location se for the represented feature or record. |
| `settlement` | `varchar(100)` | Count or numeric value for settlement in the represented area. |
| `plan_name` | `varchar(120)` | Name associated with the represented feature. |
| `map_label` | `varchar(100)` | Publisher-supplied map label for the represented feature or record. |
| `object_inf` | `varchar(20)` | Publisher-supplied object inf for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
