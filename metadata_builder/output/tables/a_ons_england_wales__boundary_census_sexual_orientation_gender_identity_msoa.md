# Boundary Census Sexual Orientation Gender Identity Msoa

## Overview

- **Identifier:** `a_ons_england_wales/boundary_census_sexual_orientation_gender_identity_msoa`
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
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ons_england_wales`
- **Table:** `boundary_census_sexual_orientation_gender_identity_msoa`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 7264
- **Columns:** 17
- **Metadata status:** source_mapped

## Description

Boundary Census Sexual Orientation Gender Identity Msoa is an authoritative dataset published by Office for National Statistics. It represents boundary census sexual orientation gender identity msoa features using geometry geometry.

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
| `sexual_orientation_total` | `bigint` | Count or numeric value for sexual orientation total in the represented area. |
| `straight_or_heterosexual` | `bigint` | Count or numeric value for straight or heterosexual in the represented area. |
| `gay_or_lesbian` | `bigint` | Count or numeric value for gay or lesbian in the represented area. |
| `bisexual` | `bigint` | Count or numeric value for bisexual in the represented area. |
| `all_other_sexual_orientations` | `bigint` | Count or numeric value for all other sexual orientations in the represented area. |
| `not_answered` | `bigint` | Count or numeric value for not answered in the represented area. |
| `gender_identity_total` | `bigint` | Count or numeric value for gender identity total in the represented area. |
| `the_same_as_sex_registered_at_birth` | `bigint` | Count or numeric value for the same as sex registered at birth in the represented area. |
| `gender_id_diff_from_birth_sex_unspecified` | `bigint` | Count or numeric value for gender identifier diff from birth sex unspecified in the represented area. |
| `trans_woman` | `bigint` | Count or numeric value for trans woman in the represented area. |
| `trans_man` | `bigint` | Count or numeric value for trans man in the represented area. |
| `all_other_gender_identities` | `bigint` | Count or numeric value for all other gender identities in the represented area. |
| `not_answered_2` | `bigint` | Count or numeric value for not answered 2 in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
