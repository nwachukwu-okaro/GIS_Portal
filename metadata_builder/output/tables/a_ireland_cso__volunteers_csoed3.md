# Volunteers Csoed3

## Overview

- **Identifier:** `a_ireland_cso/volunteers_csoed3`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **Schema:** `a_ireland_cso`
- **Table:** `volunteers_csoed3`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 3421
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Volunteers Csoed3 is an authoritative dataset published by Central Statistics Office Ireland. It contains records relating to volunteers csoed3.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `guid` | `text` | Publisher-assigned guid for the record. | source_identifier | Yes | No | No |
| `geogid` | `text` | Publisher-assigned geogid for the record. | source_identifier | Yes | No | No |
| `geogdesc` | `text` | Publisher-supplied geogdesc for the represented feature or record. | source_attribute | Yes | No | No |
| `number_of_volunteers` | `bigint` | Count or numeric value for number of volunteers in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
