# Boundary Census Industries Province

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_industries_province`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.682125, 51.420091, -5.996278, 55.446936]`
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_industries_province`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 4
- **Columns:** 32
- **Metadata status:** source_mapped

## Description

Boundary Census Industries Province is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census industries province features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `guid` | `text` | Publisher-assigned guid for the record. | source_identifier | Yes | No | No |
| `geogid` | `text` | Publisher-assigned geogid for the record. | source_identifier | Yes | No | No |
| `geogdesc` | `text` | Publisher-supplied geogdesc for the represented feature or record. | source_attribute | Yes | No | No |
| `agriculture_forestry_and_fishing_males` | `bigint` | Count or numeric value for agriculture forestry and fishing males in the represented area. | statistical_value | Yes | No | No |
| `building_and_construction_males` | `bigint` | Count or numeric value for building and construction males in the represented area. | statistical_value | Yes | No | No |
| `manufacturing_industries_males` | `bigint` | Count or numeric value for manufacturing industries males in the represented area. | statistical_value | Yes | No | No |
| `commerce_and_trade_males` | `bigint` | Count or numeric value for commerce and trade males in the represented area. | statistical_value | Yes | No | No |
| `transport_and_communications_males` | `bigint` | Count or numeric value for transport and communications males in the represented area. | statistical_value | Yes | No | No |
| `public_administration_males` | `bigint` | Count or numeric value for public administration males in the represented area. | statistical_value | Yes | No | No |
| `professional_services_males` | `bigint` | Count or numeric value for professional services males in the represented area. | statistical_value | Yes | No | No |
| `other_males` | `bigint` | Count or numeric value for other males in the represented area. | statistical_value | Yes | No | No |
| `total_males` | `bigint` | Count or numeric value for total males in the represented area. | statistical_value | Yes | No | No |
| `agriculture_forestry_and_fishing_females` | `bigint` | Count or numeric value for agriculture forestry and fishing females in the represented area. | statistical_value | Yes | No | No |
| `building_and_construction_females` | `bigint` | Count or numeric value for building and construction females in the represented area. | statistical_value | Yes | No | No |
| `manufacturing_industries_females` | `bigint` | Count or numeric value for manufacturing industries females in the represented area. | statistical_value | Yes | No | No |
| `commerce_and_trade_females` | `bigint` | Count or numeric value for commerce and trade females in the represented area. | statistical_value | Yes | No | No |
| `transport_and_communications_females` | `bigint` | Count or numeric value for transport and communications females in the represented area. | statistical_value | Yes | No | No |
| `public_administration_females` | `bigint` | Count or numeric value for public administration females in the represented area. | statistical_value | Yes | No | No |
| `professional_services_females` | `bigint` | Count or numeric value for professional services females in the represented area. | statistical_value | Yes | No | No |
| `other_females` | `bigint` | Count or numeric value for other females in the represented area. | statistical_value | Yes | No | No |
| `total_females` | `bigint` | Count or numeric value for total females in the represented area. | statistical_value | Yes | No | No |
| `agriculture_forestry_and_fishing_total` | `bigint` | Count or numeric value for agriculture forestry and fishing total in the represented area. | statistical_value | Yes | No | No |
| `building_and_construction_total` | `bigint` | Count or numeric value for building and construction total in the represented area. | statistical_value | Yes | No | No |
| `manufacturing_industries_total` | `bigint` | Count or numeric value for manufacturing industries total in the represented area. | statistical_value | Yes | No | No |
| `commerce_and_trade_total` | `bigint` | Count or numeric value for commerce and trade total in the represented area. | statistical_value | Yes | No | No |
| `transport_and_communications_total` | `bigint` | Count or numeric value for transport and communications total in the represented area. | statistical_value | Yes | No | No |
| `public_administration_total` | `bigint` | Count or numeric value for public administration total in the represented area. | statistical_value | Yes | No | No |
| `professional_services_total` | `bigint` | Count or numeric value for professional services total in the represented area. | statistical_value | Yes | No | No |
| `other_total` | `bigint` | Count or numeric value for other total in the represented area. | statistical_value | Yes | No | No |
| `total` | `bigint` | Count or numeric value for total in the represented area. | statistical_value | Yes | No | No |
| `area` | `double precision` | Numeric area value recorded for the feature. | measure | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |

## Supported operations

- filter
- select
- reproject
- validate_geometry
- buffer
- clip
- intersect
- spatial_join
- export

## Operation requirements

- Intersect, clip and spatial-join inputs must use matching coordinate reference systems.
- Buffer operations require a suitable projected coordinate reference system.
- Reprojection is performed on working outputs; source tables remain unchanged.

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
