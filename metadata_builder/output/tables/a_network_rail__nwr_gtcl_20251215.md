# Nwr Gtcl 20251215

## Overview

- **Identifier:** `a_network_rail/nwr_gtcl_20251215`
- **Source organisation:** Network Rail
- **Source:** https://www.networkrail.co.uk/who-we-are/transparency-and-ethics/transparency/open-data-feeds/
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-5.845925, 50.121776, 1.834690, 58.589994]`
- **Topic category:** transportation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_network_rail`
- **Table:** `nwr_gtcl_20251215`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 48103
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Nwr Gtcl 20251215 is an authoritative dataset published by Network Rail. It represents nwr gtcl 20251215 features using multilinestring geometry.

## Lineage

Published by Network Rail as open transport data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `assetid` | `text` | Publisher-assigned assetid for the record. |
| `elr` | `text` | Publisher-supplied elr for the represented feature or record. |
| `trid` | `text` | Publisher-assigned trid for the record. |
| `source` | `text` | Publisher-supplied source for the represented feature or record. |
| `superceded` | `text` | Publisher-supplied superceded for the represented feature or record. |
| `geometry_updated` | `text` | Publisher-supplied geometry updated for the represented feature or record. |
| `id` | `bigint` | Count or numeric value for identifier in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
