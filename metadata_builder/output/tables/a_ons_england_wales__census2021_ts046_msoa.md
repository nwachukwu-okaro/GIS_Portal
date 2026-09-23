# Census2021 Ts046 Msoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts046_msoa`
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
- **Table:** `census2021_ts046_msoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 7264
- **Columns:** 16
- **Metadata status:** source_mapped

## Description

Census2021 Ts046 Msoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts046 msoa.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `date` | `bigint` |  |
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `geography_code` | `text` | Code assigned by the source dataset. |
| `total_all_households` | `bigint` | Census total for all households in the represented geographical area; measurement unit requires the table documentation. |
| `no_central_heating` | `bigint` |  |
| `mains_gas_only` | `bigint` |  |
| `tank_or_bottled_gas_only` | `bigint` |  |
| `electric_only` | `bigint` |  |
| `oil_only` | `bigint` |  |
| `wood_only` | `bigint` |  |
| `solid_fuel_only` | `bigint` |  |
| `renewable_energy_only` | `bigint` |  |
| `district_or_communal_heat_networks_only` | `bigint` |  |
| `other_central_heating_only` | `bigint` |  |
| `two_or_more_types_of_central_heating_not_including_renewable_en` | `bigint` |  |
| `two_or_more_types_of_central_heating_including_renewable_energy` | `bigint` |  |
