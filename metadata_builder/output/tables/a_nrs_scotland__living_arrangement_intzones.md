# Living Arrangement Intzones

## Overview

- **Identifier:** `a_nrs_scotland/living_arrangement_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `living_arrangement_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Living Arrangement Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to living arrangement intzones.

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
| `all_people_aged_16_and_over_in_households` | `double precision` | Recorded census measure for the category "all people aged 16 and over in households" in the represented area. Units and population base require the source table. |
| `living_in_a_couple_total` | `double precision` |  |
| `living_in_a_couple_married_or_civil_partnership_couple` | `double precision` |  |
| `living_in_a_couple_cohabiting` | `double precision` |  |
| `not_living_in_a_couple_total` | `double precision` |  |
| `not_living_in_a_couple_single_never_married_or_never_in_a_re` | `double precision` |  |
| `not_living_in_a_couple_married_or_in_a_registered_civil_part` | `double precision` |  |
| `not_living_in_a_couple_separated_but_still_legally_married_o` | `double precision` |  |
| `not_living_in_a_couple_divorced_or_formerly_in_a_civil_partn` | `double precision` |  |
| `not_living_in_a_couple_widowed_or_surviving_partner_from_a_c` | `double precision` |  |
