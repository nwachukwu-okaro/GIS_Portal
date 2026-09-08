# Ramsar Sites Listed And Proposed

## Overview

- **Identifier:** `a_natural_england/ramsar_sites_listed_and_proposed`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.418622, 49.863188, 1.716710, 55.754242]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `ramsar_sites_listed_and_proposed`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1495
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Ramsar Sites Listed And Proposed is an authoritative dataset published by Natural England. It represents ramsar sites listed and proposed features using multipolygon geometry.

## Lineage

Published by Natural England as open environmental and conservation data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `name` | `text` | Official or publisher-assigned name of the represented feature. |
| `code` | `text` | Count or numeric value for code in the represented area. |
| `status` | `text` | Publisher-supplied status for the represented feature or record. |
| `file` | `text` | Publisher-supplied file for the represented feature or record. |
| `gis_date` | `text` | Date associated with the represented feature or source record. |
| `version` | `integer` | Publisher-supplied version for the represented feature or record. |
| `rse_pk` | `integer` | Count or numeric value for rse pk in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
