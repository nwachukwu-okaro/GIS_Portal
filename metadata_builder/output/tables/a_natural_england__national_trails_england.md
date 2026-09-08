# National Trails England

## Overview

- **Identifier:** `a_natural_england/national_trails_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.715260, 49.959466, 1.319627, 55.547168]`
- **Topic category:** environment
- **Temporal extent:** 2013-04-23T00:00:00 to 2026-03-18T00:00:00
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `national_trails_england`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:3857
- **Rows:** 14
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

National Trails England is an authoritative dataset published by Natural England. It represents national trails england features using multilinestring geometry.

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
| `objectid_1` | `bigint` | Count or numeric value for objectid 1 in the represented area. |
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `name` | `varchar(50)` | Official or publisher-assigned name of the represented feature. |
| `opened` | `timestamp` | Publisher-supplied opened for the represented feature or record. |
| `start` | `varchar(100)` | Publisher-supplied start for the represented feature or record. |
| `end_` | `varchar(100)` | Publisher-supplied end for the represented feature or record. |
| `length_km` | `integer` | Numeric length km value recorded for the feature. |
| `length_mil` | `integer` | Numeric length mil value recorded for the feature. |
| `updated` | `timestamp` | Publisher-supplied updated for the represented feature or record. |
| `last_vr` | `integer` | Count or numeric value for last vr in the represented area. |
| `globalid` | `varchar(38)` | Publisher-assigned globalid for the record. |
