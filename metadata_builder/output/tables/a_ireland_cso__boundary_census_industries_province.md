# Boundary Census Industries Province

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_industries_province`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.682125, 51.420091, -5.996278, 55.446936]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_industries_province`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 4
- **Columns:** 32
- **Metadata status:** source_mapped

## Description

Boundary Census Industries Province is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census industries province features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `guid` | `text` | UUID-formatted identifier associated with the record; persistence across releases is not confirmed. |
| `geogid` | `text` | Code identifying the geographical area represented by the row. |
| `geogdesc` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `agriculture_forestry_and_fishing_males` | `bigint` |  |
| `building_and_construction_males` | `bigint` |  |
| `manufacturing_industries_males` | `bigint` |  |
| `commerce_and_trade_males` | `bigint` |  |
| `transport_and_communications_males` | `bigint` |  |
| `public_administration_males` | `bigint` |  |
| `professional_services_males` | `bigint` |  |
| `other_males` | `bigint` |  |
| `total_males` | `bigint` | Census total for males in the represented geographical area; measurement unit requires the table documentation. |
| `agriculture_forestry_and_fishing_females` | `bigint` |  |
| `building_and_construction_females` | `bigint` |  |
| `manufacturing_industries_females` | `bigint` |  |
| `commerce_and_trade_females` | `bigint` |  |
| `transport_and_communications_females` | `bigint` |  |
| `public_administration_females` | `bigint` |  |
| `professional_services_females` | `bigint` |  |
| `other_females` | `bigint` |  |
| `total_females` | `bigint` | Census total for females in the represented geographical area; measurement unit requires the table documentation. |
| `agriculture_forestry_and_fishing_total` | `bigint` |  |
| `building_and_construction_total` | `bigint` |  |
| `manufacturing_industries_total` | `bigint` |  |
| `commerce_and_trade_total` | `bigint` |  |
| `transport_and_communications_total` | `bigint` |  |
| `public_administration_total` | `bigint` |  |
| `professional_services_total` | `bigint` |  |
| `other_total` | `bigint` |  |
| `total` | `bigint` |  |
| `area` | `double precision` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
