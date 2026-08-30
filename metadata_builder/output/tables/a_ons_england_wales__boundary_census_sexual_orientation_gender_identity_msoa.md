# Boundary Census Sexual Orientation Gender Identity Msoa

## Overview

- **Identifier:** `a_ons_england_wales/boundary_census_sexual_orientation_gender_identity_msoa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **WGS84 extent:** `[-6.418601, 49.864798, 1.763680, 55.811120]`
- **Schema:** `a_ons_england_wales`
- **Table:** `boundary_census_sexual_orientation_gender_identity_msoa`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 7264
- **Columns:** 17
- **Metadata status:** source_mapped

## Description

Boundary Census Sexual Orientation Gender Identity Msoa is an authoritative dataset published by Office for National Statistics. It represents boundary census sexual orientation gender identity msoa features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `sexual_orientation_total` | `bigint` | Count or numeric value for sexual orientation total in the represented area. | statistical_value | Yes | No | No |
| `straight_or_heterosexual` | `bigint` | Count or numeric value for straight or heterosexual in the represented area. | statistical_value | Yes | No | No |
| `gay_or_lesbian` | `bigint` | Count or numeric value for gay or lesbian in the represented area. | statistical_value | Yes | No | No |
| `bisexual` | `bigint` | Count or numeric value for bisexual in the represented area. | statistical_value | Yes | No | No |
| `all_other_sexual_orientations` | `bigint` | Count or numeric value for all other sexual orientations in the represented area. | statistical_value | Yes | No | No |
| `not_answered` | `bigint` | Count or numeric value for not answered in the represented area. | statistical_value | Yes | No | No |
| `gender_identity_total` | `bigint` | Count or numeric value for gender identity total in the represented area. | statistical_value | Yes | No | No |
| `the_same_as_sex_registered_at_birth` | `bigint` | Count or numeric value for the same as sex registered at birth in the represented area. | statistical_value | Yes | No | No |
| `gender_id_diff_from_birth_sex_unspecified` | `bigint` | Count or numeric value for gender identifier diff from birth sex unspecified in the represented area. | statistical_value | Yes | No | No |
| `trans_woman` | `bigint` | Count or numeric value for trans woman in the represented area. | statistical_value | Yes | No | No |
| `trans_man` | `bigint` | Count or numeric value for trans man in the represented area. | statistical_value | Yes | No | No |
| `all_other_gender_identities` | `bigint` | Count or numeric value for all other gender identities in the represented area. | statistical_value | Yes | No | No |
| `not_answered_2` | `bigint` | Count or numeric value for not answered 2 in the represented area. | statistical_value | Yes | No | No |
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
