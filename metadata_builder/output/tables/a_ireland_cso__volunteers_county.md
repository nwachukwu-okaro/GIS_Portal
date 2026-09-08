# Volunteers County

## Overview

- **Identifier:** `a_ireland_cso/volunteers_county`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_ireland_cso`
- **Table:** `volunteers_county`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 32
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Volunteers County is an authoritative dataset published by Central Statistics Office Ireland. It contains records relating to volunteers county.

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
| `number_of_volunteers` | `bigint` | Count or numeric value for number of volunteers in the represented area. |
