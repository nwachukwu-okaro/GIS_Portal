# Datazone Dictionary Datazone

## Overview

- **Identifier:** `a_nrs_scotland/datazone_dictionary_datazone`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `datazone_dictionary_datazone`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 2883
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Datazone Dictionary Datazone is an authoritative dataset published by National Records of Scotland. It contains records relating to datazone dictionary datazone.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `country` | `text` | Publisher-supplied country for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_level` | `text` | Publisher-supplied geography level for the represented feature or record. | source_attribute | Yes | No | No |
| `theme` | `text` | Publisher-supplied theme for the represented feature or record. | source_attribute | Yes | No | No |
| `source_table_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `table_description` | `text` | Publisher-supplied table description for the represented feature or record. | source_attribute | Yes | No | No |
| `source_filename` | `text` | Publisher-supplied source filename for the represented feature or record. | source_attribute | Yes | No | No |
| `merged_output_file` | `text` | Publisher-supplied merged output file for the represented feature or record. | source_attribute | Yes | No | No |
| `source_available` | `text` | Publisher-supplied source available for the represented feature or record. | source_attribute | Yes | No | No |
| `original_column_label` | `text` | Publisher-supplied original column label for the represented feature or record. | source_attribute | Yes | No | No |
| `cleaned_column_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
