# Census2021 Ts034 Rgn

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts034_rgn`
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
- **Table:** `census2021_ts034_rgn`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Census2021 Ts034 Rgn is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts034 rgn.

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
| `cannot_write_welsh` | `bigint` | Count or numeric value for cannot write welsh in the represented area. |
| `can_write_welsh` | `bigint` | Count or numeric value for can write welsh in the represented area. |
