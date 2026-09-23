# Census2021 Ts038 Msoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts038_msoa`
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
- **Table:** `census2021_ts038_msoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 7264
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Census2021 Ts038 Msoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts038 msoa.

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
| `total_all_usual_residents` | `bigint` | Census total for all usual residents in the represented geographical area; measurement unit requires the table documentation. |
| `disabled_under_the_equality_act` | `bigint` |  |
| `disabled_under_the_equality_act_day_to_day_activities_limited_a` | `bigint` |  |
| `disabled_under_the_equality_act_day_to_day_activities_limited_1` | `bigint` |  |
| `not_disabled_under_the_equality_act` | `bigint` |  |
| `not_disabled_under_the_equality_act_has_long_term_physical_or_m` | `bigint` |  |
| `not_disabled_under_the_equality_act_no_long_term_physical_or_me` | `bigint` |  |
