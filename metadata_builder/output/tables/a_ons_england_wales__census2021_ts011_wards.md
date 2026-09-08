# Census2021 Ts011 Wards

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts011_wards`
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
- **Table:** `census2021_ts011_wards`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 14
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Census2021 Ts011 Wards is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts011 wards.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. |
| `2022 ward` | `varchar` |  |
| `total_all_households` | `integer` | Count or numeric value for total all households in the represented area. |
| `household_is_not_deprived_in_any_dimension` | `integer` | Count or numeric value for household is not deprived in any dimension in the represented area. |
| `household_is_deprived_in_one_dimension` | `integer` | Count or numeric value for household is deprived in one dimension in the represented area. |
| `household_is_deprived_in_two_dimensions` | `integer` | Count or numeric value for household is deprived in two dimensions in the represented area. |
| `household_is_deprived_in_three_dimensions` | `integer` | Count or numeric value for household is deprived in three dimensions in the represented area. |
| `household_is_deprived_in_four_dimensions` | `integer` | Count or numeric value for household is deprived in four dimensions in the represented area. |
