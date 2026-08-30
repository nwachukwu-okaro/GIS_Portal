# Sexual Orientation Data 2021 Dz

## Overview

- **Identifier:** `a_nisra_nireland/sexual_orientation_data_2021_dz`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **Schema:** `a_nisra_nireland`
- **Table:** `sexual_orientation_data_2021_dz`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 3780
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Sexual Orientation Data 2021 Dz is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It contains records relating to sexual orientation data 2021 dz.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Publisher-assigned geocode for the record. | source_identifier | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `year` | `bigint` | Count or numeric value for year in the represented area. | statistical_value | Yes | No | No |
| `population` | `text` | Publisher-supplied population for the represented feature or record. | source_attribute | Yes | No | No |
| `sexual_orientation_gay_lesbian_bisexual_or_other_sexual_orienta` | `bigint` | Publisher-supplied sexual orientation gay lesbian bisexual or other sexual orienta for the represented feature or record. | source_attribute | Yes | No | No |
| `sexual_orientation_prefer_not_to_say_or_not_stated` | `bigint` | Publisher-supplied sexual orientation prefer not to say or not stated for the represented feature or record. | source_attribute | Yes | No | No |
| `sexual_orientation_straight_or_heterosexual` | `text` | Publisher-supplied sexual orientation straight or heterosexual for the represented feature or record. | source_attribute | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
