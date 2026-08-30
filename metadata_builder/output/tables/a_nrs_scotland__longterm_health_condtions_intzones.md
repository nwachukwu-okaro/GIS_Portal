# Longterm Health Condtions Intzones

## Overview

- **Identifier:** `a_nrs_scotland/longterm_health_condtions_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `longterm_health_condtions_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Longterm Health Condtions Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to longterm health condtions intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `all_people` | `double precision` | Count or numeric value for all people in the represented area. | statistical_value | Yes | No | No |
| `deaf_or_partially_hearing_impaired` | `double precision` | Count or numeric value for deaf or partially hearing impaired in the represented area. | statistical_value | Yes | No | No |
| `blind_or_partially_vision_impaired` | `double precision` | Count or numeric value for blind or partially vision impaired in the represented area. | statistical_value | Yes | No | No |
| `full_partial_loss_of_voice_or_difficulty_speaking` | `double precision` | Count or numeric value for full partial loss of voice or difficulty speaking in the represented area. | statistical_value | Yes | No | No |
| `has_one_or_more_of_learning_disability_learning_difficulty_o` | `double precision` | Count or numeric value for has one or more of learning disability learning difficulty o in the represented area. | statistical_value | Yes | No | No |
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
