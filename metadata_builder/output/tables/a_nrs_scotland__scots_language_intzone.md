# Scots Language Intzone

## Overview

- **Identifier:** `a_nrs_scotland/scots_language_intzone`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `scots_language_intzone`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Scots Language Intzone is an authoritative dataset published by National Records of Scotland. It contains records relating to scots language intzone.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `all_people_aged_3_and_over` | `double precision` | Count or numeric value for all people aged 3 and over in the represented area. | statistical_value | Yes | No | No |
| `understands_but_does_not_speak_read_or_write_scots` | `double precision` | Count or numeric value for understands but does not speak read or write scots in the represented area. | statistical_value | Yes | No | No |
| `speaks_reads_and_writes_scots` | `double precision` | Count or numeric value for speaks reads and writes scots in the represented area. | statistical_value | Yes | No | No |
| `speaks_but_does_not_read_or_write_scots` | `double precision` | Count or numeric value for speaks but does not read or write scots in the represented area. | statistical_value | Yes | No | No |
| `speaks_and_reads_but_does_not_write_scots` | `double precision` | Count or numeric value for speaks and reads but does not write scots in the represented area. | statistical_value | Yes | No | No |
| `reads_but_does_not_speak_or_write_scots` | `double precision` | Count or numeric value for reads but does not speak or write scots in the represented area. | statistical_value | Yes | No | No |
| `other_combination_of_skills_in_scots` | `double precision` | Count or numeric value for other combination of skills in scots in the represented area. | statistical_value | Yes | No | No |
| `no_skills_in_scots` | `double precision` | Count or numeric value for number skills in scots in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
