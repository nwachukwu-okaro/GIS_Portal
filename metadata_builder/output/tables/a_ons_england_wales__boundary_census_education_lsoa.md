# Boundary Census Education Lsoa

## Overview

- **Identifier:** `a_ons_england_wales/boundary_census_education_lsoa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **WGS84 extent:** `[-6.418601, 49.864798, 1.763680, 55.811120]`
- **Schema:** `a_ons_england_wales`
- **Table:** `boundary_census_education_lsoa`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 35672
- **Columns:** 15
- **Metadata status:** source_mapped

## Description

Boundary Census Education Lsoa is an authoritative dataset published by Office for National Statistics. It represents boundary census education lsoa features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `highest_qual_total` | `bigint` | Count or numeric value for highest qual total in the represented area. | statistical_value | Yes | No | No |
| `no_qualifications` | `bigint` | Count or numeric value for number qualifications in the represented area. | statistical_value | Yes | No | No |
| `level_1_and_entry_level_qualifications` | `bigint` | Count or numeric value for level 1 and entry level qualifications in the represented area. | statistical_value | Yes | No | No |
| `level_2_qualifications` | `bigint` | Count or numeric value for level 2 qualifications in the represented area. | statistical_value | Yes | No | No |
| `apprenticeship` | `bigint` | Count or numeric value for apprenticeship in the represented area. | statistical_value | Yes | No | No |
| `level_3_qualifications` | `bigint` | Count or numeric value for level 3 qualifications in the represented area. | statistical_value | Yes | No | No |
| `level_4_qualifications_and_above` | `bigint` | Count or numeric value for level 4 qualifications and above in the represented area. | statistical_value | Yes | No | No |
| `other_qualifications` | `bigint` | Count or numeric value for other qualifications in the represented area. | statistical_value | Yes | No | No |
| `student_indicator_total` | `bigint` | Count or numeric value for student indicator total in the represented area. | statistical_value | Yes | No | No |
| `student` | `bigint` | Count or numeric value for student in the represented area. | statistical_value | Yes | No | No |
| `not_a_student` | `bigint` | Count or numeric value for not a student in the represented area. | statistical_value | Yes | No | No |
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

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
