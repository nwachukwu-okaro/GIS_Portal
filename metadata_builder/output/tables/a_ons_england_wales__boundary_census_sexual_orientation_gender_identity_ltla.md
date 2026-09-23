# Boundary Census Sexual Orientation Gender Identity Ltla

## Overview

- **Identifier:** `a_ons_england_wales/boundary_census_sexual_orientation_gender_identity_ltla`
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
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ons_england_wales`
- **Table:** `boundary_census_sexual_orientation_gender_identity_ltla`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 331
- **Columns:** 25
- **Metadata status:** source_mapped

## Description

Boundary Census Sexual Orientation Gender Identity Ltla is an authoritative dataset published by Office for National Statistics. It represents boundary census sexual orientation gender identity ltla features using multipolygon geometry.

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
| `gender_identity_total_t1` | `bigint` |  |
| `the_same_as_sex_registered_at_birth_t1` | `bigint` |  |
| `gender_id_diff_from_birth_sex_unspecified_t1` | `bigint` |  |
| `trans_woman_t1` | `bigint` |  |
| `trans_man_t1` | `bigint` |  |
| `non_binary` | `bigint` |  |
| `all_other_gender_identities_t1` | `bigint` |  |
| `not_answered_t1` | `bigint` |  |
| `sexual_orientation_total` | `bigint` |  |
| `straight_or_heterosexual` | `bigint` |  |
| `gay_or_lesbian` | `bigint` |  |
| `bisexual` | `bigint` |  |
| `all_other_sexual_orientations` | `bigint` |  |
| `not_answered` | `bigint` |  |
| `gender_identity_total_t2` | `bigint` |  |
| `the_same_as_sex_registered_at_birth_t2` | `bigint` |  |
| `gender_id_diff_from_birth_sex_unspecified_t2` | `bigint` |  |
| `trans_woman_t2` | `bigint` |  |
| `trans_man_t2` | `bigint` |  |
| `all_other_gender_identities_t2` | `bigint` |  |
| `not_answered_t2` | `bigint` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
