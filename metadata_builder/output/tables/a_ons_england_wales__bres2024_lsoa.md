# Bres2024 Lsoa

## Overview

- **Identifier:** `a_ons_england_wales/bres2024_lsoa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Schema:** `a_ons_england_wales`
- **Table:** `bres2024_lsoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 35672
- **Metadata status:** source_mapped

## Description

Bres2024 Lsoa is an authoritative dataset published by Office for National Statistics. It contains records relating to bres2024 lsoa.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lsoa_name` | `varchar` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `lsoa_code` | `varchar` | Code assigned by the source dataset. | code | Yes | No | No |
| `1_agriculture_forestry_and_fishing_a` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `2_mining_quarrying_and_utilities_bd_and_e` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `3_manufacturing_c` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `4_construction_f` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `5_motor_trades_part_g` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `6_wholesale_part_g` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `7_retail_part_g` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `8_transport_and_storage_inc_postal_h` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `9_accommodation_and_food_services_i` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `10_information_and_communication_j` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `11_financial_and_insurance_k` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `12_property_l` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `13_professional_scientific_and_technical_m` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `14_business_administration_and_support_services_n` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `15_public_administration_and_defence_o` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `16_education_p` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `17_health_q` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `18_arts_entertainment_recreation_and_other_services_rst_and_u` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
