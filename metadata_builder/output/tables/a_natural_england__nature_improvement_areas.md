# Nature Improvement Areas

## Overview

- **Identifier:** `a_natural_england/nature_improvement_areas`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-4.475307, 50.576379, 1.025990, 54.345053]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `nature_improvement_areas`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 12
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

version: 20170425
Source: https://environment.data.gov.uk/dataset/899230b5-0247-4af8-9265-ff65009287eb

Attribution: © Natural England copyright. Contains Ordnance Survey data © Crown copyright and database right [year].

## Lineage

Published by Natural England as open environmental and conservation data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `nia_name` | `text` | Name associated with the represented feature. |
| `hectares` | `double precision` | Count or numeric value for hectares in the represented area. |
| `gdb_geomattr_data` | `bytea` | Publisher-supplied gdb geomattr data for the represented feature or record. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
