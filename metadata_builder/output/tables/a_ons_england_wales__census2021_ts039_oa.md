# Census2021 Ts039 Oa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts039_oa`
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
- **Table:** `census2021_ts039_oa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 188880
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Census2021 Ts039 Oa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts039 oa.

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
| `total_all_usual_residents_aged_5_and_over` | `bigint` | Recorded census measure for the category "total all usual residents aged 5 and over" in the represented area. Units and population base require the source table. |
| `provides_no_unpaid_care` | `bigint` |  |
| `provides_19_hours_or_less_unpaid_care_a_week` | `bigint` |  |
| `provides_9_hours_or_less_unpaid_care_a_week` | `bigint` |  |
| `provides_10_to_19_hours_unpaid_care_a_week` | `bigint` |  |
| `provides_20_to_49_hours_unpaid_care_a_week` | `bigint` |  |
| `provides_20_to_34_hours_unpaid_care_a_week` | `bigint` |  |
| `provides_35_to_49_hours_unpaid_care_a_week` | `bigint` |  |
| `provides_50_or_more_hours_unpaid_care_a_week` | `bigint` |  |
