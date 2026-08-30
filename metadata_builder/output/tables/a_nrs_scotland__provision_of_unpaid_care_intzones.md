# Provision Of Unpaid Care Intzones

## Overview

- **Identifier:** `a_nrs_scotland/provision_of_unpaid_care_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `provision_of_unpaid_care_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Provision Of Unpaid Care Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to provision of unpaid care intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `all_people_aged_3_and_over` | `double precision` | Count or numeric value for all people aged 3 and over in the represented area. | statistical_value | Yes | No | No |
| `no` | `double precision` | Count or numeric value for number in the represented area. | statistical_value | Yes | No | No |
| `all_unpaid_carers` | `double precision` | Count or numeric value for all unpaid carers in the represented area. | statistical_value | Yes | No | No |
| `yes_1_to_19_hours_a_week` | `double precision` | Count or numeric value for yes 1 to 19 hours a week in the represented area. | statistical_value | Yes | No | No |
| `yes_20_to_34_hours_a_week` | `double precision` | Count or numeric value for yes 20 to 34 hours a week in the represented area. | statistical_value | Yes | No | No |
| `yes_35_to_49_hours_a_week` | `double precision` | Count or numeric value for yes 35 to 49 hours a week in the represented area. | statistical_value | Yes | No | No |
| `yes_50_or_more_hours_a_week` | `double precision` | Count or numeric value for yes 50 or more hours a week in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
