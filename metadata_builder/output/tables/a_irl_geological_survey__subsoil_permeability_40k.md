# Subsoil Permeability 40k

## Overview

- **Identifier:** `a_irl_geological_survey/subsoil_permeability_40k`
- **Source organisation:** Geological Survey Ireland
- **Source:** https://www.gsi.ie/en-ie/data-and-maps/Pages/default.aspx
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.416020, 51.461104, -8.352703, 53.405467]`
- **Topic category:** geoscientificInformation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_geological_survey`
- **Table:** `subsoil_permeability_40k`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 2000
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Subsoil Permeability 40k is an authoritative dataset published by Geological Survey Ireland. It represents subsoil permeability 40k features using multipolygon geometry.

## Lineage

Published by Geological Survey Ireland as open geological data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `object_id` | `integer` | Identifier assigned by the source dataset. |
| `sspm40kid` | `varchar` |  |
| `sspermcode` | `varchar` |  |
| `sspermdesc` | `varchar` |  |
| `global_id` | `varchar` | Identifier assigned by the source dataset. |
| `sspermrank` | `varchar` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
