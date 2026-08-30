# Household Composition Datazone

## Overview

- **Identifier:** `a_nrs_scotland/household_composition_datazone`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `household_composition_datazone`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 7392
- **Columns:** 28
- **Metadata status:** source_mapped

## Description

Household Composition Datazone is an authoritative dataset published by National Records of Scotland. It contains records relating to household composition datazone.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. | statistical_value | Yes | No | No |
| `geography_code` | `varchar` | Code assigned by the source dataset. | code | Yes | No | No |
| `all_people_in_households` | `integer` | Count or numeric value for all people in households in the represented area. | statistical_value | Yes | No | No |
| `one_family_household__all_aged_66_and_over` | `varchar` | Publisher-supplied one family household all aged 66 and over for the represented feature or record. | source_attribute | Yes | No | No |
| `one_family_household__cohabiting_couple__all_children_non-depen` | `varchar` | Publisher-supplied one family household cohabiting couple all children non depen for the represented feature or record. | source_attribute | Yes | No | No |
| `one_family_household__cohabiting_couple__no_children` | `varchar` | Publisher-supplied one family household cohabiting couple number children for the represented feature or record. | source_attribute | Yes | No | No |
| `one_family_household__cohabiting_couple__one_dependent_child` | `varchar` | Publisher-supplied one family household cohabiting couple one dependent child for the represented feature or record. | source_attribute | Yes | No | No |
| `one_family_household__cohabiting_couple__total` | `integer` | Count or numeric value for one family household cohabiting couple total in the represented area. | statistical_value | Yes | No | No |
| `one_family_household__cohabiting_couple__two_or_more_dependent_` | `varchar` | Publisher-supplied one family household cohabiting couple two or more dependent for the represented feature or record. | source_attribute | Yes | No | No |
| `one_family_household__lone_parent_family__all_children_non-depe` | `varchar` | Publisher-supplied one family household lone parent family all children non depe for the represented feature or record. | source_attribute | Yes | No | No |
| `one_family_household__lone_parent_family__one_dependent_child` | `varchar` | Publisher-supplied one family household lone parent family one dependent child for the represented feature or record. | source_attribute | Yes | No | No |
| `one_family_household__lone_parent_family__total` | `integer` | Numeric one family household lone parent family total value recorded for the feature. | measure | Yes | No | No |
| `one_family_household__lone_parent_family__two_or_more_dependent` | `varchar` | Publisher-supplied one family household lone parent family two or more dependent for the represented feature or record. | source_attribute | Yes | No | No |
| `one_family_household__married_or_civil_partnership_couple__all_` | `varchar` | Publisher-supplied one family household married or civil partnership couple all for the represented feature or record. | source_attribute | Yes | No | No |
| `one_family_household__married_or_civil_partnership_couple__no_c` | `varchar` | Publisher-supplied one family household married or civil partnership couple number c for the represented feature or record. | source_attribute | Yes | No | No |
| `one_family_household__married_or_civil_partnership_couple__one_` | `varchar` | Publisher-supplied one family household married or civil partnership couple one for the represented feature or record. | source_attribute | Yes | No | No |
| `one_family_household__married_or_civil_partnership_couple__tota` | `integer` | Count or numeric value for one family household married or civil partnership couple tota in the represented area. | statistical_value | Yes | No | No |
| `one_family_household__married_or_civil_partnership_couple__two_` | `varchar` | Publisher-supplied one family household married or civil partnership couple two for the represented feature or record. | source_attribute | Yes | No | No |
| `one_family_household__total` | `integer` | Count or numeric value for one family household total in the represented area. | statistical_value | Yes | No | No |
| `one_person_household__aged_66_and_over` | `varchar` | Publisher-supplied one person household aged 66 and over for the represented feature or record. | source_attribute | Yes | No | No |
| `one_person_household__aged_under_66` | `integer` | Count or numeric value for one person household aged under 66 in the represented area. | statistical_value | Yes | No | No |
| `one_person_household__total` | `integer` | Count or numeric value for one person household total in the represented area. | statistical_value | Yes | No | No |
| `other_household_types__all_aged_66_and_over` | `varchar` | Publisher-supplied other household types all aged 66 and over for the represented feature or record. | source_attribute | Yes | No | No |
| `other_household_types__all_full-time_students` | `varchar` | Publisher-supplied other household types all full time students for the represented feature or record. | source_attribute | Yes | No | No |
| `other_household_types__one_dependent_child` | `varchar` | Publisher-supplied other household types one dependent child for the represented feature or record. | source_attribute | Yes | No | No |
| `other_household_types__other` | `varchar` | Publisher-supplied other household types other for the represented feature or record. | source_attribute | Yes | No | No |
| `other_household_types__total` | `varchar` | Publisher-supplied other household types total for the represented feature or record. | source_attribute | Yes | No | No |
| `other_household_types__two_or_more_dependent_children` | `varchar` | Publisher-supplied other household types two or more dependent children for the represented feature or record. | source_attribute | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
