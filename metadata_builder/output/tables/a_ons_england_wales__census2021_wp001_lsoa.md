# Census2021 Wp001 Lsoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_wp001_lsoa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_wp001_lsoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 35672
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Census2021 Wp001 Lsoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 wp001 lsoa.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. | statistical_value | Yes | No | No |
| `lower layer super output areas code` | `varchar` | Publisher-assigned lower layer super output areas code for the record. | source_identifier | Yes | No | No |
| `lower layer super output areas label` | `varchar` | Publisher-supplied lower layer super output areas label for the represented feature or record. | source_attribute | Yes | No | No |
| `count` | `varchar` | Publisher-supplied count for the represented feature or record. | source_attribute | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
