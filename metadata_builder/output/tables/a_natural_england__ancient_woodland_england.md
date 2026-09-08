# Ancient Woodland England

## Overview

- **Identifier:** `a_natural_england/ancient_woodland_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.560508, 50.036191, 1.739062, 55.773698]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `ancient_woodland_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 53636
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Version: 20251009
Source: https://www.data.gov.uk/dataset/9461f463-c363-4309-ae77-fdcd7e9df7d3/ancient-woodland-england

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
| `name` | `varchar(150)` | Official or publisher-assigned name of the represented feature. |
| `theme` | `varchar(19)` | Publisher-supplied theme for the represented feature or record. |
| `themname` | `varchar(37)` | Publisher-supplied themname for the represented feature or record. |
| `status` | `varchar(8)` | Publisher-supplied status for the represented feature or record. |
| `x_coord` | `integer` | Count or numeric value for x coord in the represented area. |
| `y_coord` | `integer` | Count or numeric value for y coord in the represented area. |
| `themid` | `varchar(255)` | Publisher-assigned themid for the record. |
| `area` | `real` | Numeric area value recorded for the feature. |
| `perimeter` | `real` | Count or numeric value for perimeter in the represented area. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
