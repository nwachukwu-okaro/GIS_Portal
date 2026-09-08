# Gm Sbi Polygon

## Overview

- **Identifier:** `a_greater_manchester_ecology_unit/gm_sbi_polygon`
- **Source organisation:** Greater Manchester Ecology Unit
- **Source:** https://www.gmenvironment.org.uk/gmeu/
- **WGS84 extent:** `[-2.723911, 53.345913, -1.909622, 53.683676]`
- **Topic category:** environment
- **Temporal extent:** 1976-07-01 to 2022-07-20
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_greater_manchester_ecology_unit`
- **Table:** `gm_sbi_polygon`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 539
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Gm Sbi Polygon is an authoritative dataset published by Greater Manchester Ecology Unit. It represents gm sbi polygon features using multipolygon geometry.

## Lineage

Published by Greater Manchester Ecology Unit as open ecological data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `site_id` | `text` | Identifier assigned by the source dataset. |
| `site_name` | `text` | Name associated with the represented feature. |
| `cent_gr` | `text` | Ordnance Survey National Grid Reference for the centre of the site. |
| `site_gra` | `text` | Ecological site grade, such as A, B or C. |
| `district` | `text` | Greater Manchester district containing the ecological site. |
| `features` | `text` | Habitats, species or ecological features supporting the site's designation. |
| `date_est` | `date` | Date on which the ecological site record or designation was established. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
