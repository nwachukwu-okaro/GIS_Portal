# Tenure People Intzones

## Overview

- **Identifier:** `a_nrs_scotland/tenure_people_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `tenure_people_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Tenure People Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to tenure people intzones.

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
| `all_occupied_households` | `double precision` | Recorded census measure for the category "all occupied households" in the represented area. Units and population base require the source table. |
| `owned_total` | `double precision` |  |
| `owned_owned_outright` | `double precision` |  |
| `owned_owned_with_a_mortgage_or_loan` | `double precision` |  |
| `owned_shared_ownership_part_owned_and_part_rented` | `double precision` |  |
| `owned_shared_equity_e_g_lift_or_help_to_buy` | `double precision` |  |
| `social_rented_council_la_or_housing_association_registered_s` | `double precision` |  |
| `private_rented_total` | `double precision` |  |
| `private_rented_private_landlord_or_letting_agency` | `double precision` |  |
| `private_rented_other` | `double precision` |  |
| `lives_rent_free` | `double precision` |  |
