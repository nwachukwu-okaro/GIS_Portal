# Tenure Household Intzones

## Overview

- **Identifier:** `a_nrs_scotland/tenure_household_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `tenure_household_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Tenure Household Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to tenure household intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `all_occupied_households` | `double precision` | Count or numeric value for all occupied households in the represented area. | statistical_value | Yes | No | No |
| `occupancy_rating_of_bedrooms_2_or_more` | `double precision` | Count or numeric value for occupancy rating of bedrooms 2 or more in the represented area. | statistical_value | Yes | No | No |
| `occupancy_rating_of_bedrooms_1` | `double precision` | Count or numeric value for occupancy rating of bedrooms 1 in the represented area. | statistical_value | Yes | No | No |
| `occupancy_rating_of_bedrooms_0` | `double precision` | Count or numeric value for occupancy rating of bedrooms 0 in the represented area. | statistical_value | Yes | No | No |
| `occupancy_rating_of_bedrooms_1_or_less` | `double precision` | Count or numeric value for occupancy rating of bedrooms 1 or less in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
