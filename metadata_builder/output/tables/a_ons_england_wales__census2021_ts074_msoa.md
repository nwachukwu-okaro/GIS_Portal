# Census2021 Ts074 Msoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts074_msoa`
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
- **Table:** `census2021_ts074_msoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 7264
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Census2021 Ts074 Msoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts074 msoa.

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
| `household_reference_person_previously_served_in_regular_uk_arme` | `bigint` | Count or numeric value for household reference person previously served in regular uk arme in the represented area. |
| `household_reference_person_previously_served_in_reserve_uk_arme` | `bigint` | Count or numeric value for household reference person previously served in reserve uk arme in the represented area. |
| `household_reference_person_previously_served_in_both_regular_an` | `bigint` | Count or numeric value for household reference person previously served in both regular an in the represented area. |
| `household_reference_person_has_not_previously_served_in_regular` | `bigint` | Count or numeric value for household reference person has not previously served in regular in the represented area. |
