# Scotland Health Disability Unpaid Care Intzones

## Overview

- **Identifier:** `a_nrs_scotland/scotland_health_disability_unpaid_care_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `scotland_health_disability_unpaid_care_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1279
- **Columns:** 27
- **Metadata status:** source_mapped

## Description

Scotland Health Disability Unpaid Care Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to scotland health disability unpaid care intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `geography_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `general_health_all_people` | `bigint` | Count or numeric value for general health all people in the represented area. | statistical_value | Yes | No | No |
| `very_good` | `bigint` | Count or numeric value for very good in the represented area. | statistical_value | Yes | No | No |
| `good` | `bigint` | Count or numeric value for good in the represented area. | statistical_value | Yes | No | No |
| `fair` | `bigint` | Count or numeric value for fair in the represented area. | statistical_value | Yes | No | No |
| `bad` | `bigint` | Count or numeric value for bad in the represented area. | statistical_value | Yes | No | No |
| `very_bad` | `bigint` | Count or numeric value for very bad in the represented area. | statistical_value | Yes | No | No |
| `lt_disability_all_people` | `bigint` | Count or numeric value for lt disability all people in the represented area. | statistical_value | Yes | No | No |
| `daily_activities_limited_a_lot` | `bigint` | Count or numeric value for daily activities limited a lot in the represented area. | statistical_value | Yes | No | No |
| `daily_activities_limited_a_little` | `bigint` | Count or numeric value for daily activities limited a little in the represented area. | statistical_value | Yes | No | No |
| `daily_activities_not_limited` | `bigint` | Count or numeric value for daily activities not limited in the represented area. | statistical_value | Yes | No | No |
| `lt_health_all_people` | `bigint` | Count or numeric value for lt health all people in the represented area. | statistical_value | Yes | No | No |
| `hearing_impairment` | `bigint` | Count or numeric value for hearing impairment in the represented area. | statistical_value | Yes | No | No |
| `vision_impairment` | `bigint` | Count or numeric value for vision impairment in the represented area. | statistical_value | Yes | No | No |
| `speech_impairment` | `bigint` | Count or numeric value for speech impairment in the represented area. | statistical_value | Yes | No | No |
| `learning_disability_or_difficulty` | `bigint` | Count or numeric value for learning disability or difficulty in the represented area. | statistical_value | Yes | No | No |
| `physical_disability` | `bigint` | Count or numeric value for physical disability in the represented area. | statistical_value | Yes | No | No |
| `mental_health_condition` | `bigint` | Count or numeric value for mental health condition in the represented area. | statistical_value | Yes | No | No |
| `long_term_illness` | `bigint` | Numeric long term illness value recorded for the feature. | measure | Yes | No | No |
| `all_people_3plus` | `bigint` | Count or numeric value for all people 3plus in the represented area. | statistical_value | Yes | No | No |
| `no_unpaid_care` | `bigint` | Count or numeric value for number unpaid care in the represented area. | statistical_value | Yes | No | No |
| `all_unpaid_carers` | `bigint` | Count or numeric value for all unpaid carers in the represented area. | statistical_value | Yes | No | No |
| `unpaid_care_1_19hrs_pw` | `bigint` | Count or numeric value for unpaid care 1 19hrs pw in the represented area. | statistical_value | Yes | No | No |
| `unpaid_care_20_34hrs_pw` | `bigint` | Count or numeric value for unpaid care 20 34hrs pw in the represented area. | statistical_value | Yes | No | No |
| `unpaid_care_35_49hrs_pw` | `bigint` | Count or numeric value for unpaid care 35 49hrs pw in the represented area. | statistical_value | Yes | No | No |
| `unpaid_care_50plus_hrs_pw` | `bigint` | Count or numeric value for unpaid care 50plus hrs pw in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
