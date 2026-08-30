# Scotland Sexual Orientation Gender Identity Intzones

## Overview

- **Identifier:** `a_nrs_scotland/scotland_sexual_orientation_gender_identity_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `scotland_sexual_orientation_gender_identity_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1279
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Scotland Sexual Orientation Gender Identity Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to scotland sexual orientation gender identity intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `geography_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `all_people_16plus_sexual_orient` | `bigint` | Count or numeric value for all people 16plus sexual orient in the represented area. | statistical_value | Yes | No | No |
| `heterosexual_straight` | `bigint` | Count or numeric value for heterosexual straight in the represented area. | statistical_value | Yes | No | No |
| `gay_or_lesbian` | `bigint` | Count or numeric value for gay or lesbian in the represented area. | statistical_value | Yes | No | No |
| `bisexual` | `bigint` | Count or numeric value for bisexual in the represented area. | statistical_value | Yes | No | No |
| `other_sexual_orientation` | `bigint` | Count or numeric value for other sexual orientation in the represented area. | statistical_value | Yes | No | No |
| `not_answered_sexual_orient` | `bigint` | Count or numeric value for not answered sexual orient in the represented area. | statistical_value | Yes | No | No |
| `all_people_16plus_trans_status` | `bigint` | Count or numeric value for all people 16plus trans status in the represented area. | statistical_value | Yes | No | No |
| `not_trans_no_history` | `bigint` | Count or numeric value for not trans number history in the represented area. | statistical_value | Yes | No | No |
| `trans_or_has_trans_history` | `bigint` | Count or numeric value for trans or has trans history in the represented area. | statistical_value | Yes | No | No |
| `not_answered_trans_status` | `bigint` | Count or numeric value for not answered trans status in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
