# Census2021 Ts032 Utla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts032_utla`
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
- **Table:** `census2021_ts032_utla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 22
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Census2021 Ts032 Utla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts032 utla.

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
| `total_all_usual_residents_aged_3_years_and_over` | `bigint` | Count or numeric value for total all usual residents aged 3 years and over in the represented area. |
| `can_understand_spoken_welsh_only` | `bigint` | Count or numeric value for can understand spoken welsh only in the represented area. |
| `can_speak_read_and_write_welsh` | `bigint` | Count or numeric value for can speak read and write welsh in the represented area. |
| `can_speak_but_cannot_read_or_write_welsh` | `bigint` | Count or numeric value for can speak but cannot read or write welsh in the represented area. |
| `can_speak_and_read_but_cannot_write_welsh` | `bigint` | Count or numeric value for can speak and read but cannot write welsh in the represented area. |
| `can_read_but_cannot_speak_or_write_welsh` | `bigint` | Count or numeric value for can read but cannot speak or write welsh in the represented area. |
| `can_write_but_cannot_speak_or_read_welsh` | `bigint` | Count or numeric value for can write but cannot speak or read welsh in the represented area. |
| `can_read_and_write_but_cannot_speak_welsh` | `bigint` | Count or numeric value for can read and write but cannot speak welsh in the represented area. |
| `can_speak_and_other_combinations_of_skills_in_welsh` | `bigint` | Count or numeric value for can speak and other combinations of skills in welsh in the represented area. |
| `no_skills_in_welsh` | `bigint` | Count or numeric value for number skills in welsh in the represented area. |
