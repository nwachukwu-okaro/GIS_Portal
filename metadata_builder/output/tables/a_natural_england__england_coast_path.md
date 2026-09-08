# England Coast Path

## Overview

- **Identifier:** `a_natural_england/england_coast_path`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.715202, 49.959480, 1.755965, 55.810694]`
- **Topic category:** environment
- **Temporal extent:** 2012-06-29T00:00:00 to 2026-03-25T00:00:00
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `england_coast_path`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 16667
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

England Coast Path is an authoritative dataset published by Natural England. It represents england coast path features using multilinestring geometry.

## Lineage

Published by Natural England as open environmental and conservation data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `integer` | Publisher-assigned identifier for the record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `stretch` | `varchar(75)` | Publisher-supplied stretch for the represented feature or record. |
| `section_id` | `varchar(15)` | Identifier assigned by the source dataset. |
| `chapter` | `varchar(16)` | Publisher-supplied chapter for the represented feature or record. |
| `status` | `varchar(65)` | Publisher-supplied status for the represented feature or record. |
| `alt_route` | `varchar(3)` | Publisher-supplied alt route for the represented feature or record. |
| `rollback_` | `varchar(40)` | Publisher-supplied rollback for the represented feature or record. |
| `pub_date` | `timestamp` | Date associated with the represented feature or source record. |
| `shape_leng` | `double precision` | Count or numeric value for shape leng in the represented area. |
| `globalid` | `varchar(38)` | Publisher-assigned globalid for the record. |
