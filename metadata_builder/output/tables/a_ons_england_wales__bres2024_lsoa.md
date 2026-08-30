# Bres2024 Lsoa

## Overview

- **Identifier:** `a_ons_england_wales/bres2024_lsoa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `bres2024_lsoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 35672
- **Columns:** 21
- **Metadata status:** source_mapped

## Description

Bres2024 Lsoa is an authoritative dataset published by Office for National Statistics. It contains records relating to bres2024 lsoa.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. | statistical_value | Yes | No | No |
| `lsoa_name` | `varchar` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `lsoa_code` | `varchar` | Code assigned by the source dataset. | code | Yes | No | No |
| `1_agriculture_forestry_and_fishing_a` | `integer` | Count or numeric value for 1 agriculture forestry and fishing a in the represented area. | statistical_value | Yes | No | No |
| `2_mining_quarrying_and_utilities_bd_and_e` | `integer` | Count or numeric value for 2 mining quarrying and utilities bd and e in the represented area. | statistical_value | Yes | No | No |
| `3_manufacturing_c` | `integer` | Count or numeric value for 3 manufacturing c in the represented area. | statistical_value | Yes | No | No |
| `4_construction_f` | `integer` | Count or numeric value for 4 construction female in the represented area. | statistical_value | Yes | No | No |
| `5_motor_trades_part_g` | `integer` | Count or numeric value for 5 motor trades part g in the represented area. | statistical_value | Yes | No | No |
| `6_wholesale_part_g` | `integer` | Count or numeric value for 6 wholesale part g in the represented area. | statistical_value | Yes | No | No |
| `7_retail_part_g` | `integer` | Count or numeric value for 7 retail part g in the represented area. | statistical_value | Yes | No | No |
| `8_transport_and_storage_inc_postal_h` | `integer` | Count or numeric value for 8 transport and storage inc postal h in the represented area. | statistical_value | Yes | No | No |
| `9_accommodation_and_food_services_i` | `integer` | Count or numeric value for 9 accommodation and food services i in the represented area. | statistical_value | Yes | No | No |
| `10_information_and_communication_j` | `integer` | Count or numeric value for 10 information and communication j in the represented area. | statistical_value | Yes | No | No |
| `11_financial_and_insurance_k` | `integer` | Count or numeric value for 11 financial and insurance k in the represented area. | statistical_value | Yes | No | No |
| `12_property_l` | `integer` | Count or numeric value for 12 property l in the represented area. | statistical_value | Yes | No | No |
| `13_professional_scientific_and_technical_m` | `integer` | Count or numeric value for 13 professional scientific and technical male in the represented area. | statistical_value | Yes | No | No |
| `14_business_administration_and_support_services_n` | `integer` | Count or numeric value for 14 business administration and support services n in the represented area. | statistical_value | Yes | No | No |
| `15_public_administration_and_defence_o` | `integer` | Count or numeric value for 15 public administration and defence o in the represented area. | statistical_value | Yes | No | No |
| `16_education_p` | `integer` | Count or numeric value for 16 education p in the represented area. | statistical_value | Yes | No | No |
| `17_health_q` | `integer` | Count or numeric value for 17 health q in the represented area. | statistical_value | Yes | No | No |
| `18_arts_entertainment_recreation_and_other_services_rst_and_u` | `integer` | Count or numeric value for 18 arts entertainment recreation and other services rst and u in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
