# Areas Of Outstanding Natural Beauty England

## Overview

- **Identifier:** `a_natural_england/areas_of_outstanding_natural_beauty_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.462536, 49.854671, 1.729622, 55.748905]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `areas_of_outstanding_natural_beauty_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 33
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Version: 20251009
Source: https://www.data.gov.uk/dataset/8e3ae3b9-a827-47f1-b025-f08527a4e84e/areas-of-outstanding-natural-beauty-england1

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
| `code` | `integer` | Count or numeric value for code in the represented area. |
| `name` | `varchar(200)` | Official or publisher-assigned name of the represented feature. |
| `measure` | `real` | Count or numeric value for measure in the represented area. |
| `desig_date` | `varchar(14)` | Date associated with the represented feature or source record. |
| `hotlink` | `varchar(200)` | Publisher-supplied hotlink for the represented feature or record. |
| `stat_area` | `varchar(32)` | Publisher-supplied stat area for the represented feature or record. |
| `shape_length` | `real` | Numeric shape length value recorded for the feature. |
| `shape_area` | `real` | Numeric shape area value recorded for the feature. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
