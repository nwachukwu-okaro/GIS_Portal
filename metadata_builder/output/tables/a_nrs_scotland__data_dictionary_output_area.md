# Data Dictionary Output Area

## Overview

- **Identifier:** `a_nrs_scotland/data_dictionary_output_area`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `data_dictionary_output_area`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 2162
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Data Dictionary Output Area is an authoritative dataset published by National Records of Scotland. It contains records relating to data dictionary output area.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `theme` | `text` | Publisher-supplied theme for the represented feature or record. | source_attribute | Yes | No | No |
| `table_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `source_file` | `text` | Publisher-supplied source file for the represented feature or record. | source_attribute | Yes | No | No |
| `original_label` | `text` | Publisher-supplied original label for the represented feature or record. | source_attribute | Yes | No | No |
| `processed_column_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `output_file` | `text` | Publisher-supplied output file for the represented feature or record. | source_attribute | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
