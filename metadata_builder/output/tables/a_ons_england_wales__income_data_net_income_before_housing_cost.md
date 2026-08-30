# Income Data Net Income Before Housing Cost

## Overview

- **Identifier:** `a_ons_england_wales/income_data_net_income_before_housing_cost`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `income_data_net_income_before_housing_cost`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 7264
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Income Data Net Income Before Housing Cost is an authoritative dataset published by Office for National Statistics. It contains records relating to income data net income before housing cost.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `msoa_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `msoa_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `local_authority_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `local_authority_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `region_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `region_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `disposable_net_annual_income_before_housing_costs` | `text` | Publisher-supplied disposable net annual income before housing costs for the represented feature or record. | source_attribute | Yes | No | No |
| `upper_confidence_limit` | `text` | Publisher-supplied upper confidence limit for the represented feature or record. | source_attribute | Yes | No | No |
| `lower_confidence_limit` | `text` | Publisher-supplied lower confidence limit for the represented feature or record. | source_attribute | Yes | No | No |
| `confidence_interval` | `text` | Publisher-supplied confidence interval for the represented feature or record. | source_attribute | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
