# Boundary Census Scotland Scotland Armed Forces Intzones

## Overview

- **Identifier:** `a_nrs_scotland/boundary_census_scotland_scotland_armed_forces_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **WGS84 extent:** `[-8.650007, 54.633238, -0.724609, 60.860766]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nrs_scotland`
- **Table:** `boundary_census_scotland_scotland_armed_forces_intzones`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1280
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Boundary Census Scotland Scotland Armed Forces Intzones is an authoritative dataset published by National Records of Scotland. It represents boundary census scotland scotland armed forces intzones features using multipolygon geometry.

## Lineage

Published by National Records of Scotland as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geography_code` | `text` | Code assigned by the source dataset. |
| `geography_name` | `text` | Name associated with the represented feature. |
| `all_households` | `bigint` | Count or numeric value for all households in the represented area. |
| `hh_has_af_veteran` | `bigint` | Count or numeric value for households has af veteran in the represented area. |
| `hh_no_af_veteran` | `bigint` | Count or numeric value for households number af veteran in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
