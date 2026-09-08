# Boundary Census Migration Ethnicity Religion Languages Csoed3

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_migration_ethnicity_religion_languages_csoed3`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.726726, 54.563349, 3.417194, 58.519873]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_migration_ethnicity_religion_languages_csoed3`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 3420
- **Columns:** 49
- **Metadata status:** source_mapped

## Description

Boundary Census Migration Ethnicity Religion Languages Csoed3 is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census migration ethnicity religion languages csoed3 features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `ed_english` | `text` | Publisher-supplied ed english for the represented feature or record. |
| `guid` | `text` | Publisher-assigned guid for the record. |
| `geogid` | `text` | Publisher-assigned geogid for the record. |
| `geogdesc` | `text` | Publisher-supplied geogdesc for the represented feature or record. |
| `ireland_birthplace` | `bigint` | Count or numeric value for ireland birthplace in the represented area. |
| `uk_birthplace` | `bigint` | Count or numeric value for uk birthplace in the represented area. |
| `poland_birthplace` | `bigint` | Count or numeric value for poland birthplace in the represented area. |
| `india_birthplace` | `bigint` | Count or numeric value for india birthplace in the represented area. |
| `other_eu27_2020_birthplace` | `bigint` | Count or numeric value for other eu27 2020 birthplace in the represented area. |
| `rest_of_world_birthplace` | `bigint` | Count or numeric value for rest of world birthplace in the represented area. |
| `total_birthplace` | `bigint` | Count or numeric value for total birthplace in the represented area. |
| `ireland_citizenship` | `bigint` | Count or numeric value for ireland citizenship in the represented area. |
| `uk_citizenship` | `bigint` | Count or numeric value for uk citizenship in the represented area. |
| `poland_citizenship` | `bigint` | Count or numeric value for poland citizenship in the represented area. |
| `india_citizenship` | `bigint` | Count or numeric value for india citizenship in the represented area. |
| `other_eu27_2020_citizenship` | `bigint` | Count or numeric value for other eu27 2020 citizenship in the represented area. |
| `rest_of_world_citizenship` | `bigint` | Count or numeric value for rest of world citizenship in the represented area. |
| `not_stated_citizenship` | `bigint` | Count or numeric value for not stated citizenship in the represented area. |
| `total_citizenship` | `bigint` | Count or numeric value for total citizenship in the represented area. |
| `white_irish` | `bigint` | Count or numeric value for white irish in the represented area. |
| `white_irish_traveller` | `bigint` | Count or numeric value for white irish traveller in the represented area. |
| `other_white` | `bigint` | Count or numeric value for other white in the represented area. |
| `black_or_black_irish` | `bigint` | Count or numeric value for black or black irish in the represented area. |
| `asian_or_asian_irish` | `bigint` | Count or numeric value for asian or asian irish in the represented area. |
| `other` | `bigint` | Count or numeric value for other in the represented area. |
| `not_stated` | `bigint` | Count or numeric value for not stated in the represented area. |
| `total` | `bigint` | Count or numeric value for total in the represented area. |
| `same_address` | `bigint` | Count or numeric value for same address in the represented area. |
| `elsewhere_in_county` | `bigint` | Count or numeric value for elsewhere in county in the represented area. |
| `elsewhere_in_ireland` | `bigint` | Count or numeric value for elsewhere in ireland in the represented area. |
| `outside_ireland` | `bigint` | Count or numeric value for outside ireland in the represented area. |
| `total_1` | `bigint` | Count or numeric value for total 1 in the represented area. |
| `catholic` | `bigint` | Count or numeric value for catholic in the represented area. |
| `other_religion` | `bigint` | Count or numeric value for other religion in the represented area. |
| `no_religion` | `bigint` | Count or numeric value for number religion in the represented area. |
| `not_stated_1` | `bigint` | Count or numeric value for not stated 1 in the represented area. |
| `total_2` | `bigint` | Count or numeric value for total 2 in the represented area. |
| `polish` | `bigint` | Count or numeric value for polish in the represented area. |
| `french` | `bigint` | Count or numeric value for french in the represented area. |
| `spanish` | `bigint` | Count or numeric value for spanish in the represented area. |
| `other_incl_not_stated` | `bigint` | Count or numeric value for other incl not stated in the represented area. |
| `total_3` | `bigint` | Count or numeric value for total 3 in the represented area. |
| `very_well` | `bigint` | Count or numeric value for very well in the represented area. |
| `well` | `bigint` | Count or numeric value for well in the represented area. |
| `not_well` | `bigint` | Count or numeric value for not well in the represented area. |
| `not_at_all` | `bigint` | Count or numeric value for not at all in the represented area. |
| `not_stated_2` | `bigint` | Count or numeric value for not stated 2 in the represented area. |
| `total_4` | `bigint` | Count or numeric value for total 4 in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
