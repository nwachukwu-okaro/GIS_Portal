# Uv304 Long Term Health Conditions Oa

## Overview

- **Identifier:** `a_nrs_scotland/uv304_long_term_health_conditions_oa`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `uv304_long_term_health_conditions_oa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 46368
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Uv304 Long Term Health Conditions Oa is an authoritative dataset published by National Records of Scotland. It contains records relating to uv304 long term health conditions oa.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `all_people` | `double precision` | Count or numeric value for all people in the represented area. | statistical_value | Yes | No | No |
| `deaf_or_partially_hearing_impaired` | `double precision` | Count or numeric value for deaf or partially hearing impaired in the represented area. | statistical_value | Yes | No | No |
| `blind_or_partially_vision_impaired` | `double precision` | Count or numeric value for blind or partially vision impaired in the represented area. | statistical_value | Yes | No | No |
| `full_partial_loss_of_voice_or_difficulty_speaking` | `double precision` | Count or numeric value for full partial loss of voice or difficulty speaking in the represented area. | statistical_value | Yes | No | No |
| `has_one_or_more_of_learning_disability_learning_difficulty_or_d` | `double precision` | Human-readable description associated with the corresponding coded attribute. | description | Yes | Yes | No |
| `physical_disability` | `double precision` | Count or numeric value for physical disability in the represented area. | statistical_value | Yes | No | No |
| `mental_health_condition` | `double precision` | Count or numeric value for mental health condition in the represented area. | statistical_value | Yes | No | No |
| `long_term_illness_disease_or_condition` | `double precision` | Numeric long term illness disease or condition value recorded for the feature. | measure | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
