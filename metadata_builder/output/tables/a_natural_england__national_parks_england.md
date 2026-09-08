# National Parks England

## Overview

- **Identifier:** `a_natural_england/national_parks_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-4.165771, 50.392027, 1.728156, 55.591511]`
- **Topic category:** environment
- **Temporal extent:** 1951-04-17T00:00:00 to 2010-03-31T00:00:00
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `national_parks_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 10
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Version: 20251009
Source: https://www.data.gov.uk/dataset/334e1b27-e193-4ef5-b14e-696b58bb7e95/national-parks-england1

Attribution: © Natural England copyright. Contains Ordnance Survey data © Crown copyright and database right [year]. Attribution statement: © Natural England copyright. Contains Ordnance Survey data © Crown copyright and database right [year].

## Lineage

Published by Natural England as open environmental and conservation data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `code` | `smallint` | Count or numeric value for code in the represented area. |
| `name` | `varchar(200)` | Official or publisher-assigned name of the represented feature. |
| `measure` | `double precision` | Count or numeric value for measure in the represented area. |
| `desig_date` | `timestamp` | Date associated with the represented feature or source record. |
| `hotlink` | `varchar(200)` | Publisher-supplied hotlink for the represented feature or record. |
| `status` | `varchar(32)` | Publisher-supplied status for the represented feature or record. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
