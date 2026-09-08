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
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update
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
| `date` | `bigint` | Count or numeric value for date in the represented area. |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `geography_code` | `text` | Code assigned by the source dataset. |
| `total_all_households` | `bigint` | Count or numeric value for total all households in the represented area. |
| `owned` | `bigint` | Count or numeric value for owned in the represented area. |
| `owned_owns_outright` | `bigint` | Count or numeric value for owned owns outright in the represented area. |
| `owned_owns_with_a_mortgage_or_loan` | `bigint` | Count or numeric value for owned owns with a mortgage or loan in the represented area. |
| `shared_ownership` | `bigint` | Count or numeric value for shared ownership in the represented area. |
| `shared_ownership_shared_ownership` | `bigint` | Count or numeric value for shared ownership shared ownership in the represented area. |
| `social_rented` | `bigint` | Count or numeric value for social rented in the represented area. |
| `social_rented_rents_from_council_or_local_authority` | `bigint` | Count or numeric value for social rented rents from council or local authority in the represented area. |
| `social_rented_other_social_rented` | `bigint` | Count or numeric value for social rented other social rented in the represented area. |
| `private_rented` | `bigint` | Count or numeric value for private rented in the represented area. |
| `private_rented_private_landlord_or_letting_agency` | `bigint` | Count or numeric value for private rented private landlord or letting agency in the represented area. |
| `private_rented_other_private_rented` | `bigint` | Count or numeric value for private rented other private rented in the represented area. |
| `lives_rent_free` | `bigint` | Count or numeric value for lives rent free in the represented area. |
