# Census2021 Ts046 Utla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts046_utla`
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
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts046_utla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 174
- **Columns:** 16
- **Metadata status:** source_mapped

## Description

Census2021 Ts046 Utla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts046 utla.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `geography_code` | `text` | Code assigned by the source dataset. |
| `total_all_households` | `bigint` | Count or numeric value for total all households in the represented area. |
| `no_central_heating` | `bigint` | Count or numeric value for number central heating in the represented area. |
| `mains_gas_only` | `bigint` | Count or numeric value for mains gas only in the represented area. |
| `tank_or_bottled_gas_only` | `bigint` | Count or numeric value for tank or bottled gas only in the represented area. |
| `electric_only` | `bigint` | Count or numeric value for electric only in the represented area. |
| `oil_only` | `bigint` | Count or numeric value for oil only in the represented area. |
| `wood_only` | `bigint` | Count or numeric value for wood only in the represented area. |
| `solid_fuel_only` | `bigint` | Count or numeric value for solid fuel only in the represented area. |
| `renewable_energy_only` | `bigint` | Count or numeric value for renewable energy only in the represented area. |
| `district_or_communal_heat_networks_only` | `bigint` | Count or numeric value for district or communal heat networks only in the represented area. |
| `other_central_heating_only` | `bigint` | Count or numeric value for other central heating only in the represented area. |
| `two_or_more_types_of_central_heating_not_including_renewable_en` | `bigint` | Count or numeric value for two or more types of central heating not including renewable en in the represented area. |
| `two_or_more_types_of_central_heating_including_renewable_energy` | `bigint` | Count or numeric value for two or more types of central heating including renewable energy in the represented area. |
