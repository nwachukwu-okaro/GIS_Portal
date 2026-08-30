# British Sign Language Intzones

## Overview

- **Identifier:** `a_nrs_scotland/british_sign_language_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `british_sign_language_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

British Sign Language Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to british sign language intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `all_people_aged_3_and_over` | `double precision` | Count or numeric value for all people aged 3 and over in the represented area. | statistical_value | Yes | No | No |
| `bsl_user` | `double precision` | Count or numeric value for bsl user in the represented area. | statistical_value | Yes | No | No |
| `not_a_bsl_user` | `double precision` | Count or numeric value for not a bsl user in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
