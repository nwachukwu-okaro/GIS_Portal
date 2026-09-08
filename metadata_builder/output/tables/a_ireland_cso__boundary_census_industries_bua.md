# Boundary Census Industries Bua

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_industries_bua`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.426272, 54.617106, 3.355468, 58.377636]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_industries_bua`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 867
- **Columns:** 31
- **Metadata status:** source_mapped

## Description

Boundary Census Industries Bua is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census industries bua features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `guid` | `text` | Publisher-assigned guid for the record. |
| `geogid` | `text` | Publisher-assigned geogid for the record. |
| `geogdesc` | `text` | Publisher-supplied geogdesc for the represented feature or record. |
| `agriculture_forestry_and_fishing_males` | `bigint` | Count or numeric value for agriculture forestry and fishing males in the represented area. |
| `building_and_construction_males` | `bigint` | Count or numeric value for building and construction males in the represented area. |
| `manufacturing_industries_males` | `bigint` | Count or numeric value for manufacturing industries males in the represented area. |
| `commerce_and_trade_males` | `bigint` | Count or numeric value for commerce and trade males in the represented area. |
| `transport_and_communications_males` | `bigint` | Count or numeric value for transport and communications males in the represented area. |
| `public_administration_males` | `bigint` | Count or numeric value for public administration males in the represented area. |
| `professional_services_males` | `bigint` | Count or numeric value for professional services males in the represented area. |
| `other_males` | `bigint` | Count or numeric value for other males in the represented area. |
| `total_males` | `bigint` | Count or numeric value for total males in the represented area. |
| `agriculture_forestry_and_fishing_females` | `bigint` | Count or numeric value for agriculture forestry and fishing females in the represented area. |
| `building_and_construction_females` | `bigint` | Count or numeric value for building and construction females in the represented area. |
| `manufacturing_industries_females` | `bigint` | Count or numeric value for manufacturing industries females in the represented area. |
| `commerce_and_trade_females` | `bigint` | Count or numeric value for commerce and trade females in the represented area. |
| `transport_and_communications_females` | `bigint` | Count or numeric value for transport and communications females in the represented area. |
| `public_administration_females` | `bigint` | Count or numeric value for public administration females in the represented area. |
| `professional_services_females` | `bigint` | Count or numeric value for professional services females in the represented area. |
| `other_females` | `bigint` | Count or numeric value for other females in the represented area. |
| `total_females` | `bigint` | Count or numeric value for total females in the represented area. |
| `agriculture_forestry_and_fishing_total` | `bigint` | Count or numeric value for agriculture forestry and fishing total in the represented area. |
| `building_and_construction_total` | `bigint` | Count or numeric value for building and construction total in the represented area. |
| `manufacturing_industries_total` | `bigint` | Count or numeric value for manufacturing industries total in the represented area. |
| `commerce_and_trade_total` | `bigint` | Count or numeric value for commerce and trade total in the represented area. |
| `transport_and_communications_total` | `bigint` | Count or numeric value for transport and communications total in the represented area. |
| `public_administration_total` | `bigint` | Count or numeric value for public administration total in the represented area. |
| `professional_services_total` | `bigint` | Count or numeric value for professional services total in the represented area. |
| `other_total` | `bigint` | Count or numeric value for other total in the represented area. |
| `total` | `bigint` | Count or numeric value for total in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
