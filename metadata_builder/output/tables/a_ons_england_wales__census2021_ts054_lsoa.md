# Census2021 Ts054 Lsoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts054_lsoa`
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
- **Table:** `census2021_ts054_lsoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 35672
- **Columns:** 16
- **Metadata status:** source_mapped

## Description

Census2021 Ts054 Lsoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts054 lsoa.

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
| `owned` | `bigint` |  |
| `owned_owns_outright` | `bigint` |  |
| `owned_owns_with_a_mortgage_or_loan` | `bigint` |  |
| `shared_ownership` | `bigint` |  |
| `shared_ownership_shared_ownership` | `bigint` |  |
| `social_rented` | `bigint` |  |
| `social_rented_rents_from_council_or_local_authority` | `bigint` |  |
| `social_rented_other_social_rented` | `bigint` |  |
| `private_rented` | `bigint` |  |
| `private_rented_private_landlord_or_letting_agency` | `bigint` |  |
| `private_rented_other_private_rented` | `bigint` |  |
| `lives_rent_free` | `bigint` |  |
