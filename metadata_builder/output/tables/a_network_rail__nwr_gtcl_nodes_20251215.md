# Nwr Gtcl Nodes 20251215

## Overview

- **Identifier:** `a_network_rail/nwr_gtcl_nodes_20251215`
- **Source organisation:** Network Rail
- **Source:** https://www.networkrail.co.uk/who-we-are/transparency-and-ethics/transparency/open-data-feeds/
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-5.841335, 50.121776, 1.834690, 58.589994]`
- **Topic category:** transportation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_network_rail`
- **Table:** `nwr_gtcl_nodes_20251215`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:27700
- **Rows:** 37489
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Nwr Gtcl Nodes 20251215 is an authoritative dataset published by Network Rail. It represents nwr gtcl nodes 20251215 features using multipoint geometry.

## Lineage

Published by Network Rail as open transport data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `assetid` | `text` |  |
| `valancy` | `integer` |  |
| `source` | `text` |  |
| `superceded` | `text` |  |
| `geometry_updated` | `text` |  |
| `id` | `bigint` | Primary-key identifier for records in nwr_gtcl_nodes_20251215. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
