# Household Lifestage Intzones

## Overview

- **Identifier:** `a_nrs_scotland/household_lifestage_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `household_lifestage_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 22
- **Metadata status:** source_mapped

## Description

Household Lifestage Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to household lifestage intzones.

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
| `all_households` | `double precision` | Recorded census measure for the category "all households" in the represented area. Units and population base require the source table. |
| `hrp_aged_under_35_total` | `double precision` |  |
| `hrp_aged_under_35_one_person_household` | `double precision` |  |
| `hrp_aged_under_35_two_or_more_person_household_no_dependent_` | `double precision` |  |
| `hrp_aged_under_35_two_or_more_person_household_with_dependen` | `double precision` |  |
| `hrp_aged_35_to_54_total` | `double precision` |  |
| `hrp_aged_35_to_54_one_person_household` | `double precision` |  |
| `hrp_aged_35_to_54_two_or_more_person_household_no_dependent_` | `double precision` |  |
| `hrp_aged_35_to_54_two_or_more_person_household_with_dependen` | `double precision` |  |
| `hrp_aged_55_to_64_total` | `double precision` |  |
| `hrp_aged_55_to_64_one_person_household` | `double precision` |  |
| `hrp_aged_55_to_64_two_or_more_person_household_no_dependent_` | `double precision` |  |
| `hrp_aged_55_to_64_two_or_more_person_household_with_dependen` | `double precision` |  |
| `hrp_aged_65_to_74_total` | `double precision` |  |
| `hrp_aged_65_to_74_one_person_household` | `double precision` |  |
| `hrp_aged_65_to_74_two_or_more_person_household_no_dependent_` | `double precision` |  |
| `hrp_aged_65_to_74_two_or_more_person_household_with_dependen` | `double precision` |  |
| `hrp_aged_75_and_over_total` | `double precision` |  |
| `hrp_aged_75_and_over_one_person_household` | `double precision` |  |
| `hrp_aged_75_and_over_two_or_more_person_household_no_depende` | `double precision` |  |
| `hrp_aged_75_and_over_two_or_more_person_household_with_depen` | `double precision` |  |
