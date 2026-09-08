# Sites Of Special Scientific Interest England

## Overview

- **Identifier:** `a_natural_england/sites_of_special_scientific_interest_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.418622, 49.863188, 1.753083, 55.811678]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `sites_of_special_scientific_interest_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 4128
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

version: 20251009
Source: https://www.data.gov.uk/dataset/5b632bd7-9838-4ef2-9101-ea9384421b0d/sites-of-special-scientific-interest-england3

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
| `ref_code` | `varchar` | Code assigned by the source dataset. |
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. |
| `measure` | `real` | Count or numeric value for measure in the represented area. |
| `label` | `varchar` | Publisher-supplied label for the represented feature or record. |
| `hyperlink` | `varchar` | URL of the corresponding record on the publisher's website. |
| `contact_no` | `varchar` | Publisher-supplied contact number for the represented feature or record. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
