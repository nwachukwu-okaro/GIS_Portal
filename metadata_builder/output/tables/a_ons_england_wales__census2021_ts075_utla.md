# Census2021 Ts075 Utla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts075_utla`
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
- **Table:** `census2021_ts075_utla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 174
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Census2021 Ts075 Utla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts075 utla.

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
| `total` | `bigint` | Count or numeric value for total in the represented area. |
| `one_person_household` | `bigint` | Count or numeric value for one person household in the represented area. |
| `multi_person_household_no_people_stated_their_religion` | `bigint` | Count or numeric value for multi person household number people stated their religion in the represented area. |
| `multi_person_household_same_religion_at_least_one_person_has_st` | `bigint` | Count or numeric value for multi person household same religion at least one person has st in the represented area. |
| `multi_person_household_no_religion_household_may_include_people` | `bigint` | Count or numeric value for multi person household number religion household may include people in the represented area. |
| `multi_person_household_same_religion_and_no_religion_household` | `bigint` | Count or numeric value for multi person household same religion and number religion household in the represented area. |
| `multi_person_household_at_least_two_different_religions_stated` | `bigint` | Count or numeric value for multi person household at least two different religions stated in the represented area. |
