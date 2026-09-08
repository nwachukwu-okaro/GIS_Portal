# Local Nature Reserves England

## Overview

- **Identifier:** `a_natural_england/local_nature_reserves_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.484388, 50.140759, 1.757926, 55.348825]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `local_nature_reserves_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1710
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Version: 20251009
Source: https://www.data.gov.uk/dataset/acdf4a9e-a115-41fb-bbe9-603c819aa7f7/local-nature-reserves-england1

Attribution: © Natural England copyright. Contains Ordnance Survey data © Crown copyright and database right [year]. NB This national dataset is “indicative” not “definitive”. Definitive information can only be provided by individual local authorities and you should refer directly to their information for all purposes that require the most up to date and complete dataset.

## Lineage

Published by Natural England as open environmental and conservation data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `ref_code` | `varchar(10)` | Code assigned by the source dataset. |
| `name` | `varchar(120)` | Official or publisher-assigned name of the represented feature. |
| `measure` | `double precision` | Count or numeric value for measure in the represented area. |
| `label` | `varchar(140)` | Publisher-supplied label for the represented feature or record. |
| `globalid` | `varchar(38)` | Publisher-assigned globalid for the record. |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
