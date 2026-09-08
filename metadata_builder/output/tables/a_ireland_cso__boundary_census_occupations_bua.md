# Boundary Census Occupations Bua

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_occupations_bua`
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
- **Table:** `boundary_census_occupations_bua`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 867
- **Columns:** 37
- **Metadata status:** source_mapped

## Description

Boundary Census Occupations Bua is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census occupations bua features using geometry geometry.

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
| `managers_directors_and_senior_officials_males` | `bigint` | Count or numeric value for managers directors and senior officials males in the represented area. |
| `professional_occupations_males` | `bigint` | Count or numeric value for professional occupations males in the represented area. |
| `associate_professional_and_technical_occupations_males` | `bigint` | Count or numeric value for associate professional and technical occupations males in the represented area. |
| `administrative_and_secretarial_occupations_males` | `bigint` | Count or numeric value for administrative and secretarial occupations males in the represented area. |
| `skilled_trades_occupations_males` | `bigint` | Count or numeric value for skilled trades occupations males in the represented area. |
| `caring_leisure_and_other_service_occupations_males` | `bigint` | Count or numeric value for caring leisure and other service occupations males in the represented area. |
| `sales_and_customer_service_occupations_males` | `bigint` | Count or numeric value for sales and customer service occupations males in the represented area. |
| `process_plant_and_machine_operatives_males` | `bigint` | Count or numeric value for process plant and machine operatives males in the represented area. |
| `elementary_occupations_males` | `bigint` | Count or numeric value for elementary occupations males in the represented area. |
| `not_stated_males` | `bigint` | Count or numeric value for not stated males in the represented area. |
| `total_males` | `bigint` | Count or numeric value for total males in the represented area. |
| `managers_directors_and_senior_officials_females` | `bigint` | Count or numeric value for managers directors and senior officials females in the represented area. |
| `professional_occupations_females` | `bigint` | Count or numeric value for professional occupations females in the represented area. |
| `associate_professional_and_technical_occupations_females` | `bigint` | Count or numeric value for associate professional and technical occupations females in the represented area. |
| `administrative_and_secretarial_occupations_females` | `bigint` | Count or numeric value for administrative and secretarial occupations females in the represented area. |
| `skilled_trades_occupations_females` | `bigint` | Count or numeric value for skilled trades occupations females in the represented area. |
| `caring_leisure_and_other_service_occupations_females` | `bigint` | Count or numeric value for caring leisure and other service occupations females in the represented area. |
| `sales_and_customer_service_occupations_females` | `bigint` | Count or numeric value for sales and customer service occupations females in the represented area. |
| `process_plant_and_machine_operatives_females` | `bigint` | Count or numeric value for process plant and machine operatives females in the represented area. |
| `elementary_occupations_females` | `bigint` | Count or numeric value for elementary occupations females in the represented area. |
| `not_stated_females` | `bigint` | Count or numeric value for not stated females in the represented area. |
| `total_females` | `bigint` | Count or numeric value for total females in the represented area. |
| `managers_directors_and_senior_officials_total` | `bigint` | Count or numeric value for managers directors and senior officials total in the represented area. |
| `professional_occupations_total` | `bigint` | Count or numeric value for professional occupations total in the represented area. |
| `associate_professional_and_technical_occupations_total` | `bigint` | Count or numeric value for associate professional and technical occupations total in the represented area. |
| `administrative_and_secretarial_occupations_total` | `bigint` | Count or numeric value for administrative and secretarial occupations total in the represented area. |
| `skilled_trades_occupations_total` | `bigint` | Count or numeric value for skilled trades occupations total in the represented area. |
| `caring_leisure_and_other_service_occupations_total` | `bigint` | Count or numeric value for caring leisure and other service occupations total in the represented area. |
| `sales_and_customer_service_occupations_total` | `bigint` | Count or numeric value for sales and customer service occupations total in the represented area. |
| `process_plant_and_machine_operatives_total` | `bigint` | Count or numeric value for process plant and machine operatives total in the represented area. |
| `elementary_occupations_total` | `bigint` | Count or numeric value for elementary occupations total in the represented area. |
| `not_stated_total` | `bigint` | Count or numeric value for not stated total in the represented area. |
| `total` | `bigint` | Count or numeric value for total in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
