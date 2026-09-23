# Bres2024 Lsoa

## Overview

- **Identifier:** `a_ons_england_wales/bres2024_lsoa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence v3.0 — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update
- **Schema:** `a_ons_england_wales`
- **Table:** `bres2024_lsoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 35672
- **Columns:** 21
- **Metadata status:** source_mapped

## Description

Bres2024 Lsoa is an authoritative dataset published by Office for National Statistics. It contains records relating to bres2024 lsoa.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `integer` | Primary-key identifier for records in bres2024_lsoa. |
| `lsoa_name` | `varchar` | Name associated with the represented feature. |
| `lsoa_code` | `varchar` | Code assigned by the source dataset. |
| `1_agriculture_forestry_and_fishing_a` | `integer` |  |
| `2_mining_quarrying_and_utilities_bd_and_e` | `integer` |  |
| `3_manufacturing_c` | `integer` |  |
| `4_construction_f` | `integer` |  |
| `5_motor_trades_part_g` | `integer` |  |
| `6_wholesale_part_g` | `integer` |  |
| `7_retail_part_g` | `integer` |  |
| `8_transport_and_storage_inc_postal_h` | `integer` |  |
| `9_accommodation_and_food_services_i` | `integer` |  |
| `10_information_and_communication_j` | `integer` |  |
| `11_financial_and_insurance_k` | `integer` |  |
| `12_property_l` | `integer` |  |
| `13_professional_scientific_and_technical_m` | `integer` |  |
| `14_business_administration_and_support_services_n` | `integer` |  |
| `15_public_administration_and_defence_o` | `integer` |  |
| `16_education_p` | `integer` |  |
| `17_health_q` | `integer` |  |
| `18_arts_entertainment_recreation_and_other_services_rst_and_u` | `integer` |  |
