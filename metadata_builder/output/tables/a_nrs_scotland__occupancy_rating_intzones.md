# Occupancy Rating Intzones

## Overview

- **Identifier:** `a_nrs_scotland/occupancy_rating_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `occupancy_rating_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Occupancy Rating Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to occupancy rating intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `all_occupied_households` | `double precision` | Count or numeric value for all occupied households in the represented area. | statistical_value | Yes | No | No |
| `one_bedroom` | `double precision` | Count or numeric value for one bedroom in the represented area. | statistical_value | Yes | No | No |
| `two_bedrooms` | `double precision` | Count or numeric value for two bedrooms in the represented area. | statistical_value | Yes | No | No |
| `three_bedrooms` | `double precision` | Count or numeric value for three bedrooms in the represented area. | statistical_value | Yes | No | No |
| `four_bedrooms` | `double precision` | Count or numeric value for four bedrooms in the represented area. | statistical_value | Yes | No | No |
| `five_or_more_bedrooms` | `double precision` | Count or numeric value for five or more bedrooms in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
