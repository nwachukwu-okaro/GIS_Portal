# Scotland Armed Forces Intzones

## Overview

- **Identifier:** `a_nrs_scotland/scotland_armed_forces_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `scotland_armed_forces_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1279
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Scotland Armed Forces Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to scotland armed forces intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `geography_name` | `text` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `all_households` | `bigint` | Count or numeric value for all households in the represented area. | statistical_value | Yes | No | No |
| `hh_has_af_veteran` | `bigint` | Count or numeric value for households has af veteran in the represented area. | statistical_value | Yes | No | No |
| `hh_no_af_veteran` | `bigint` | Count or numeric value for households number af veteran in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
