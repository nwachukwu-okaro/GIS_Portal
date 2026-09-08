# Census2021 Ts070 Utla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts070_utla`
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
- **Table:** `census2021_ts070_utla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 174
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Census2021 Ts070 Utla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts070 utla.

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
| `total_all_usual_residents_aged_16_years_and_over` | `bigint` | Count or numeric value for total all usual residents aged 16 years and over in the represented area. |
| `gender_identity_the_same_as_sex_registered_at_birth` | `bigint` | Count or numeric value for gender identity the same as sex registered at birth in the represented area. |
| `gender_identity_different_from_sex_registered_at_birth_but_no_s` | `bigint` | Count or numeric value for gender identity different from sex registered at birth but number s in the represented area. |
| `trans_woman` | `bigint` | Count or numeric value for trans woman in the represented area. |
| `trans_man` | `bigint` | Count or numeric value for trans man in the represented area. |
| `non_binary` | `bigint` | Count or numeric value for non binary in the represented area. |
| `all_other_gender_identities` | `bigint` | Count or numeric value for all other gender identities in the represented area. |
| `not_answered` | `bigint` | Count or numeric value for not answered in the represented area. |
