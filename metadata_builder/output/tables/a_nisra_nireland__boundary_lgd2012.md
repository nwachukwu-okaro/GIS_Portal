# Boundary Lgd2012

## Overview

- **Identifier:** `a_nisra_nireland/boundary_lgd2012`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177503, 54.022724, -5.432784, 55.312985]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_lgd2012`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 11
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Boundary Lgd2012 is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary lgd2012 features using multipolygon geometry.

## Lineage

Published by the Northern Ireland Statistics and Research Agency as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `integer` | Primary-key identifier for records in boundary_lgd2012. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `lgdname` | `varchar` |  |
| `area` | `double precision` |  |
| `lgdcode` | `varchar` |  |
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
