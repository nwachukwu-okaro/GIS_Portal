# Boundary Census Volunteers Csoed3

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_volunteers_csoed3`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.726726, 54.563349, 3.417194, 58.519873]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_volunteers_csoed3`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 3420
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Boundary Census Volunteers Csoed3 is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census volunteers csoed3 features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `ed_english` | `text` | Publisher-supplied ed english for the represented feature or record. |
| `guid` | `text` | Publisher-assigned guid for the record. |
| `geogid` | `text` | Publisher-assigned geogid for the record. |
| `geogdesc` | `text` | Publisher-supplied geogdesc for the represented feature or record. |
| `number_of_volunteers` | `bigint` | Count or numeric value for number of volunteers in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
