# National Character Areas England

## Overview

- **Identifier:** `a_natural_england/national_character_areas_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.418547, 49.864687, 1.762917, 55.811557]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `national_character_areas_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 159
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

version: 20251009
Source: https://www.data.gov.uk/dataset/21104eeb-4a53-4e41-8ada-d2d442e416e0/national-character-areas-england1

© Natural England copyright. Contains Ordnance Survey data © Crown copyright and database right [year].

## Lineage

Published by Natural England as open environmental and conservation data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `jcacode` | `integer` | Count or numeric value for jcacode in the represented area. |
| `jcaname` | `varchar(55)` | Publisher-supplied jcaname for the represented feature or record. |
| `nca_name` | `varchar(55)` | Name associated with the represented feature. |
| `naid` | `integer` | Count or numeric value for naid in the represented area. |
| `naname` | `varchar(45)` | Publisher-supplied naname for the represented feature or record. |
| `area_sqkm` | `real` | Numeric area sqkm value recorded for the feature. |
| `hotlink` | `varchar(254)` | Publisher-supplied hotlink for the represented feature or record. |
| `alt` | `varchar(80)` | Publisher-supplied alt for the represented feature or record. |
| `blt` | `varchar(75)` |  |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
