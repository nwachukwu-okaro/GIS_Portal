# Codepoint

## Overview

- **Identifier:** `a_os_codepoint/codepoint`
- **Source organisation:** Ordnance Survey
- **Product:** Code-Point Open
- **Source:** https://www.ordnancesurvey.co.uk/products/code-point-open
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-7.557160, 49.766807, 1.762748, 60.800694]`
- **Topic category:** location
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_os_codepoint`
- **Table:** `codepoint`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 1749109
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Codepoint is part of Code-Point Open, published by Ordnance Survey. It represents codepoint features using geometry geometry.

## Lineage

Published by Ordnance Survey as part of Code-Point Open. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `postcode` | `text` | Publisher-assigned postcode for the record. |
| `positional_quality_indicator` | `integer` | Count or numeric value for positional quality indicator in the represented area. |
| `country_code` | `text` | Code assigned by the source dataset. |
| `nhs_regional_ha_code` | `text` | Code assigned by the source dataset. |
| `nhs_ha_code` | `text` | Code assigned by the source dataset. |
| `admin_county_code` | `text` | Code assigned by the source dataset. |
| `admin_district_code` | `text` | Code assigned by the source dataset. |
| `admin_ward_code` | `text` | Code assigned by the source dataset. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
