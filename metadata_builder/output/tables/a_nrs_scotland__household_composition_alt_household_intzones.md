# Household Composition Alt Household Intzones

## Overview

- **Identifier:** `a_nrs_scotland/household_composition_alt_household_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `household_composition_alt_household_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Household Composition Alt Household Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to household composition alt household intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `all_households` | `double precision` | Count or numeric value for all households in the represented area. | statistical_value | Yes | No | No |
| `one_person_household_total` | `double precision` | Count or numeric value for one person household total in the represented area. | statistical_value | Yes | No | No |
| `one_person_household_person_aged_66_and_over` | `double precision` | Count or numeric value for one person household person aged 66 and over in the represented area. | statistical_value | Yes | No | No |
| `one_person_household_person_aged_under_66` | `double precision` | Count or numeric value for one person household person aged under 66 in the represented area. | statistical_value | Yes | No | No |
| `other_households_total` | `double precision` | Count or numeric value for other households total in the represented area. | statistical_value | Yes | No | No |
| `other_households_no_adults_or_one_adult_and_one_or_more_chil` | `double precision` | Count or numeric value for other households number adults or one adult and one or more chil in the represented area. | statistical_value | Yes | No | No |
| `other_households_one_adult_aged_16_to_65_and_one_aged_66_and` | `double precision` | Count or numeric value for other households one adult aged 16 to 65 and one aged 66 and in the represented area. | statistical_value | Yes | No | No |
| `other_households_two_adults_and_one_or_two_children` | `double precision` | Count or numeric value for other households two adults and one or two children in the represented area. | statistical_value | Yes | No | No |
| `other_households_two_adults_aged_16_to_65_and_no_children` | `double precision` | Count or numeric value for other households two adults aged 16 to 65 and number children in the represented area. | statistical_value | Yes | No | No |
| `other_households_two_adults_and_three_or_more_children` | `double precision` | Count or numeric value for other households two adults and three or more children in the represented area. | statistical_value | Yes | No | No |
| `other_households_three_or_more_adults_and_one_or_more_childr` | `double precision` | Count or numeric value for other households three or more adults and one or more childr in the represented area. | statistical_value | Yes | No | No |
| `other_households_three_or_more_adults_and_no_children` | `double precision` | Count or numeric value for other households three or more adults and number children in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
