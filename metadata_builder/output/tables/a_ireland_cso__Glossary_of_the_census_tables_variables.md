# Glossary Of The Census Tables Variables

## Overview

- **Identifier:** `a_ireland_cso/Glossary_of_the_census_tables_variables`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **Schema:** `a_ireland_cso`
- **Table:** `Glossary_of_the_census_tables_variables`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 790
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Glossary Of The Census Tables Variables is an authoritative dataset published by Central Statistics Office Ireland. It contains records relating to glossary of the census tables variables.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. | statistical_value | Yes | No | No |
| `themes` | `varchar` | Publisher-supplied themes for the represented feature or record. | source_attribute | Yes | No | No |
| `tables within themes` | `varchar` | Publisher-supplied tables within themes for the represented feature or record. | source_attribute | Yes | No | No |
| `column names` | `varchar` | Publisher-supplied column names for the represented feature or record. | source_attribute | Yes | No | No |
| `description of field` | `varchar` | Publisher-supplied description of field for the represented feature or record. | source_attribute | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
