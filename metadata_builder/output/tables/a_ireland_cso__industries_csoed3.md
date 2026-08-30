# Industries Csoed3

## Overview

- **Identifier:** `a_ireland_cso/industries_csoed3`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **Schema:** `a_ireland_cso`
- **Table:** `industries_csoed3`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 3421
- **Columns:** 30
- **Metadata status:** source_mapped

## Description

Industries Csoed3 is an authoritative dataset published by Central Statistics Office Ireland. It contains records relating to industries csoed3.

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

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
