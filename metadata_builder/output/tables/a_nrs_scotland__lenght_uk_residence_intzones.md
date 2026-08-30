# Lenght UK Residence Intzones

## Overview

- **Identifier:** `a_nrs_scotland/lenght_uk_residence_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `lenght_uk_residence_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Lenght UK Residence Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to lenght uk residence intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `all_people` | `double precision` | Count or numeric value for all people in the represented area. | statistical_value | Yes | No | No |
| `born_in_the_uk` | `double precision` | Count or numeric value for born in the uk in the represented area. | statistical_value | Yes | No | No |
| `less_than_2_years` | `double precision` | Count or numeric value for less than 2 years in the represented area. | statistical_value | Yes | No | No |
| `col_2_years_or_more_and_less_than_5_years` | `double precision` | Count or numeric value for col 2 years or more and less than 5 years in the represented area. | statistical_value | Yes | No | No |
| `col_5_years_or_more_and_less_than_10_years` | `double precision` | Count or numeric value for col 5 years or more and less than 10 years in the represented area. | statistical_value | Yes | No | No |
| `col_10_years_or_more` | `double precision` | Count or numeric value for col 10 years or more in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
