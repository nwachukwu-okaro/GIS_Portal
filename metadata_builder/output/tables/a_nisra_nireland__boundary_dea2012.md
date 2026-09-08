# Boundary Dea2012

## Overview

- **Identifier:** `a_nisra_nireland/boundary_dea2012`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177502, 54.022724, -5.432789, 55.312984]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_dea2012`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 80
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Boundary Dea2012 is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary dea2012 features using multipolygon geometry.

## Lineage

Published by the Northern Ireland Statistics and Research Agency as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `finalr_dea` | `varchar` | Publisher-supplied finalr dea for the represented feature or record. |
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
