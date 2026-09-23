# Boundary Census Education Lsoa

## Overview

- **Identifier:** `a_ons_england_wales/boundary_census_education_lsoa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **WGS84 extent:** `[-6.418601, 49.864798, 1.763680, 55.811120]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence v3.0 — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ons_england_wales`
- **Table:** `boundary_census_education_lsoa`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 35672
- **Columns:** 15
- **Metadata status:** source_mapped

## Description

Boundary Census Education Lsoa is an authoritative dataset published by Office for National Statistics. It represents boundary census education lsoa features using geometry geometry.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `date` | `bigint` |  |
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `geography_code` | `text` | Code assigned by the source dataset. |
| `highest_qual_total` | `bigint` |  |
| `no_qualifications` | `bigint` |  |
| `level_1_and_entry_level_qualifications` | `bigint` |  |
| `level_2_qualifications` | `bigint` |  |
| `apprenticeship` | `bigint` |  |
| `level_3_qualifications` | `bigint` |  |
| `level_4_qualifications_and_above` | `bigint` |  |
| `other_qualifications` | `bigint` |  |
| `student_indicator_total` | `bigint` |  |
| `student` | `bigint` |  |
| `not_a_student` | `bigint` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
