# Living Arrangement Intzones

## Overview

- **Identifier:** `a_nrs_scotland/living_arrangement_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `living_arrangement_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Living Arrangement Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to living arrangement intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `all_people_aged_16_and_over_in_households` | `double precision` | Count or numeric value for all people aged 16 and over in households in the represented area. | statistical_value | Yes | No | No |
| `living_in_a_couple_total` | `double precision` | Count or numeric value for living in a couple total in the represented area. | statistical_value | Yes | No | No |
| `living_in_a_couple_married_or_civil_partnership_couple` | `double precision` | Count or numeric value for living in a couple married or civil partnership couple in the represented area. | statistical_value | Yes | No | No |
| `living_in_a_couple_cohabiting` | `double precision` | Count or numeric value for living in a couple cohabiting in the represented area. | statistical_value | Yes | No | No |
| `not_living_in_a_couple_total` | `double precision` | Count or numeric value for not living in a couple total in the represented area. | statistical_value | Yes | No | No |
| `not_living_in_a_couple_single_never_married_or_never_in_a_re` | `double precision` | Count or numeric value for not living in a couple single never married or never in a re in the represented area. | statistical_value | Yes | No | No |
| `not_living_in_a_couple_married_or_in_a_registered_civil_part` | `double precision` | Count or numeric value for not living in a couple married or in a registered civil part in the represented area. | statistical_value | Yes | No | No |
| `not_living_in_a_couple_separated_but_still_legally_married_o` | `double precision` | Count or numeric value for not living in a couple separated but still legally married o in the represented area. | statistical_value | Yes | No | No |
| `not_living_in_a_couple_divorced_or_formerly_in_a_civil_partn` | `double precision` | Count or numeric value for not living in a couple divorced or formerly in a civil partn in the represented area. | statistical_value | Yes | No | No |
| `not_living_in_a_couple_widowed_or_surviving_partner_from_a_c` | `double precision` | Count or numeric value for not living in a couple widowed or surviving partner from a c in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
