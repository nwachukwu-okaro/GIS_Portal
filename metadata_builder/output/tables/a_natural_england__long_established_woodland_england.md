# Long Established Woodland England

## Overview

- **Identifier:** `a_natural_england/long_established_woodland_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-2.991100, 50.778680, 1.244674, 54.194787]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `long_established_woodland_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 9518
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Version: 20251028
Source: https://naturalengland-defra.opendata.arcgis.com/datasets/Defra::long-established-woodland-england/about
Attribution: © Natural England 2025, Contains OS data © Crown copyright and database rights 2025. OS AC0000851168

## Lineage

Published by Natural England as open environmental and conservation data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. |
| `theme` | `varchar` | Publisher-supplied theme for the represented feature or record. |
| `themname` | `varchar` | Publisher-supplied themname for the represented feature or record. |
| `status` | `varchar` | Publisher-supplied status for the represented feature or record. |
| `themid` | `varchar` | Publisher-assigned themid for the record. |
| `x_coord` | `integer` | Count or numeric value for x coord in the represented area. |
| `y_coord` | `integer` | Count or numeric value for y coord in the represented area. |
| `area` | `real` | Numeric area value recorded for the feature. |
| `perimeter` | `real` | Count or numeric value for perimeter in the represented area. |
| `county` | `varchar` | Publisher-supplied county for the represented feature or record. |
| `globalid` | `varchar` | Publisher-assigned globalid for the record. |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
