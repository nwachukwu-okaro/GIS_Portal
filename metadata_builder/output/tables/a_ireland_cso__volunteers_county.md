# Volunteers County

## Overview

- **Identifier:** `a_ireland_cso/volunteers_county`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Schema:** `a_ireland_cso`
- **Table:** `volunteers_county`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 32
- **Metadata status:** source_mapped

## Description

Volunteers County is an authoritative dataset published by Central Statistics Office Ireland. It contains records relating to volunteers county.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `guid` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `geogid` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `geogdesc` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `number_of_volunteers` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
