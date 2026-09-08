# Census2021 Ts030 Lsoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts030_lsoa`
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
- **Table:** `census2021_ts030_lsoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 35672
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Census2021 Ts030 Lsoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts030 lsoa.

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
| `no_religion` | `bigint` | Count or numeric value for number religion in the represented area. |
| `christian` | `bigint` | Count or numeric value for christian in the represented area. |
| `buddhist` | `bigint` | Count or numeric value for buddhist in the represented area. |
| `hindu` | `bigint` | Count or numeric value for hindu in the represented area. |
| `jewish` | `bigint` | Count or numeric value for jewish in the represented area. |
| `muslim` | `bigint` | Count or numeric value for muslim in the represented area. |
| `sikh` | `bigint` | Count or numeric value for sikh in the represented area. |
| `other_religion` | `bigint` | Count or numeric value for other religion in the represented area. |
| `not_answered` | `bigint` | Count or numeric value for not answered in the represented area. |
