# Boundary Census Education Ltla

## Overview

- **Identifier:** `a_ons_england_wales/boundary_census_education_ltla`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **WGS84 extent:** `[-6.418601, 49.864798, 1.763680, 55.811118]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence v3.0 — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ons_england_wales`
- **Table:** `boundary_census_education_ltla`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 331
- **Columns:** 15
- **Metadata status:** source_mapped

## Description

Boundary Census Education Ltla is an authoritative dataset published by Office for National Statistics. It represents boundary census education ltla features using multipolygon geometry.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `geography_code` | `text` | Code assigned by the source dataset. |
| `highest_qual_total` | `bigint` | Count or numeric value for highest qual total in the represented area. |
| `no_qualifications` | `bigint` | Count or numeric value for number qualifications in the represented area. |
| `level_1_and_entry_level_qualifications` | `bigint` | Count or numeric value for level 1 and entry level qualifications in the represented area. |
| `level_2_qualifications` | `bigint` | Count or numeric value for level 2 qualifications in the represented area. |
| `apprenticeship` | `bigint` | Count or numeric value for apprenticeship in the represented area. |
| `level_3_qualifications` | `bigint` | Count or numeric value for level 3 qualifications in the represented area. |
| `level_4_qualifications_and_above` | `bigint` | Count or numeric value for level 4 qualifications and above in the represented area. |
| `other_qualifications` | `bigint` | Count or numeric value for other qualifications in the represented area. |
| `student_indicator_total` | `bigint` | Count or numeric value for student indicator total in the represented area. |
| `student` | `bigint` | Count or numeric value for student in the represented area. |
| `not_a_student` | `bigint` | Count or numeric value for not a student in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
