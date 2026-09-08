# Census2021 Ts027 Utla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts027_utla`
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
- **Table:** `census2021_ts027_utla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 174
- **Columns:** 23
- **Metadata status:** source_mapped

## Description

Census2021 Ts027 Utla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts027 utla.

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
| `total_all_usual_residents` | `bigint` | Count or numeric value for total all usual residents in the represented area. |
| `british_only_identity` | `bigint` | Count or numeric value for british only identity in the represented area. |
| `english_only_identity` | `bigint` | Count or numeric value for english only identity in the represented area. |
| `english_and_british_only_identity` | `bigint` | Count or numeric value for english and british only identity in the represented area. |
| `welsh_only_identity` | `bigint` | Count or numeric value for welsh only identity in the represented area. |
| `welsh_and_british_only_identity` | `bigint` | Count or numeric value for welsh and british only identity in the represented area. |
| `any_other_combination_of_only_uk_identities` | `bigint` | Count or numeric value for any other combination of only uk identities in the represented area. |
| `scottish_only_identity` | `bigint` | Count or numeric value for scottish only identity in the represented area. |
| `scottish_and_british_only_identity` | `bigint` | Count or numeric value for scottish and british only identity in the represented area. |
| `northern_irish_only_identity` | `bigint` | Count or numeric value for northern irish only identity in the represented area. |
| `northern_irish_and_british_only_identity` | `bigint` | Count or numeric value for northern irish and british only identity in the represented area. |
| `cornish_only_identity` | `bigint` | Count or numeric value for cornish only identity in the represented area. |
| `cornish_and_british_only_identity` | `bigint` | Count or numeric value for cornish and british only identity in the represented area. |
| `any_other_combination_of_only_uk_identities_1` | `bigint` | Count or numeric value for any other combination of only uk identities 1 in the represented area. |
| `irish_only_identity` | `bigint` | Count or numeric value for irish only identity in the represented area. |
| `irish_and_at_least_one_uk_identity` | `bigint` | Count or numeric value for irish and at least one uk identity in the represented area. |
| `other_identity_only` | `bigint` | Count or numeric value for other identity only in the represented area. |
| `other_identity_and_at_least_one_uk_identity` | `bigint` | Count or numeric value for other identity and at least one uk identity in the represented area. |
| `non_uk_identity_only` | `bigint` | Count or numeric value for non uk identity only in the represented area. |
| `uk_identity_and_non_uk_identity` | `bigint` | Count or numeric value for uk identity and non uk identity in the represented area. |
