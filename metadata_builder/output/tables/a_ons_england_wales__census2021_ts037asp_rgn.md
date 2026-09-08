# Census2021 Ts037asp Rgn

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts037asp_rgn`
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
- **Table:** `census2021_ts037asp_rgn`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 10
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Census2021 Ts037asp Rgn is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts037asp rgn.

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
| `very_good_health` | `double precision` | Count or numeric value for very good health in the represented area. |
| `good_health` | `double precision` | Count or numeric value for good health in the represented area. |
| `fair_health` | `double precision` | Count or numeric value for fair health in the represented area. |
| `bad_health` | `double precision` | Count or numeric value for bad health in the represented area. |
| `very_bad_health` | `double precision` | Count or numeric value for very bad health in the represented area. |
