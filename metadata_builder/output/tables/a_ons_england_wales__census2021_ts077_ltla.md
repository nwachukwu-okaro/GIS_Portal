# Census2021 Ts077 Ltla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts077_ltla`
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
- **Table:** `census2021_ts077_ltla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 331
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Census2021 Ts077 Ltla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts077 ltla.

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
| `straight_or_heterosexual` | `bigint` | Count or numeric value for straight or heterosexual in the represented area. |
| `gay_or_lesbian` | `bigint` | Count or numeric value for gay or lesbian in the represented area. |
| `bisexual` | `bigint` | Count or numeric value for bisexual in the represented area. |
| `all_other_sexual_orientations` | `bigint` | Count or numeric value for all other sexual orientations in the represented area. |
| `not_answered` | `bigint` | Count or numeric value for not answered in the represented area. |
