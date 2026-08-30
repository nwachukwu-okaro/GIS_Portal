# Passport Held Intzone

## Overview

- **Identifier:** `a_nrs_scotland/passport_held_intzone`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `passport_held_intzone`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Passport Held Intzone is an authoritative dataset published by National Records of Scotland. It contains records relating to passport held intzone.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `all_people` | `double precision` | Count or numeric value for all people in the represented area. | statistical_value | Yes | No | No |
| `europe_total` | `double precision` | Count or numeric value for europe total in the represented area. | statistical_value | Yes | No | No |
| `europe_united_kingdom` | `double precision` | Count or numeric value for europe united kingdom in the represented area. | statistical_value | Yes | No | No |
| `europe_ireland` | `double precision` | Count or numeric value for europe ireland in the represented area. | statistical_value | Yes | No | No |
| `europe_eu_member_countries` | `double precision` | Count or numeric value for europe eu member countries in the represented area. | statistical_value | Yes | No | No |
| `europe_rest_of_europe` | `double precision` | Count or numeric value for europe rest of europe in the represented area. | statistical_value | Yes | No | No |
| `africa` | `double precision` | Count or numeric value for africa in the represented area. | statistical_value | Yes | No | No |
| `middle_east_and_asia` | `double precision` | Count or numeric value for middle east and asia in the represented area. | statistical_value | Yes | No | No |
| `antarctica_and_oceania` | `double precision` | Count or numeric value for antarctica and oceania in the represented area. | statistical_value | Yes | No | No |
| `no_passport` | `double precision` | Count or numeric value for number passport in the represented area. | statistical_value | Yes | No | No |
| `the_americas_and_the_caribbean` | `double precision` | Count or numeric value for the americas and the caribbean in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
