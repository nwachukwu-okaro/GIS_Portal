# Household Composition Alt People Intzones

## Overview

- **Identifier:** `a_nrs_scotland/household_composition_alt_people_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `household_composition_alt_people_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Household Composition Alt People Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to household composition alt people intzones.

## Lineage

Published by National Records of Scotland as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `all_people_in_households` | `double precision` | Recorded census measure for the category "all people in households" in the represented area. Units and population base require the source table. |
| `one_person_household_total` | `double precision` | Recorded census measure for the category "one person household total" in the represented area. Units and population base require the source table. |
| `one_person_household_person_aged_66_and_over` | `double precision` | Recorded census measure for the category "one person household person aged 66 and over" in the represented area. Units and population base require the source table. |
| `one_person_household_person_aged_under_66` | `double precision` |  |
| `other_households_total` | `double precision` |  |
| `other_households_no_adults_or_one_adult_and_one_or_more_chil` | `double precision` |  |
| `other_households_one_adult_aged_16_to_65_and_one_aged_66_and` | `double precision` |  |
| `other_households_two_adults_and_one_or_two_children` | `double precision` |  |
| `other_households_two_adults_aged_16_to_65_and_no_children` | `double precision` |  |
| `other_households_two_adults_and_three_or_more_children` | `double precision` |  |
| `other_households_three_or_more_adults_and_one_or_more_childr` | `double precision` |  |
| `other_households_three_or_more_adults_and_no_children` | `double precision` |  |
