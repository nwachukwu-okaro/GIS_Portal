# Income Data Total Annual Income

## Overview

- **Identifier:** `a_ons_england_wales/income_data_total_annual_income`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Schema:** `a_ons_england_wales`
- **Table:** `income_data_total_annual_income`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 7264
- **Metadata status:** source_mapped

## Description

Income Data Total Annual Income is an authoritative dataset published by Office for National Statistics. It contains records relating to income data total annual income.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `msoa_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `msoa_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `local_authority_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `local_authority_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `region_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `region_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `total_annual_income` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `upper_confidence_limit` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lower_confidence_limit` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `confidence_interval` | `text` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
