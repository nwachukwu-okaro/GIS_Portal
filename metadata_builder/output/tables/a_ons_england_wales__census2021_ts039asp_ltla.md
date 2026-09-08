# Census2021 Ts039asp Ltla

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts039asp_ltla`
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
- **Table:** `census2021_ts039asp_ltla`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 331
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Census2021 Ts039asp Ltla is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts039asp ltla.

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
| `provides_no_unpaid_care` | `double precision` | Count or numeric value for provides number unpaid care in the represented area. |
| `provides_19_or_less_hours_unpaid_care_a_week` | `double precision` | Count or numeric value for provides 19 or less hours unpaid care a week in the represented area. |
| `provides_20_to_49_hours_unpaid_care_a_week` | `double precision` | Count or numeric value for provides 20 to 49 hours unpaid care a week in the represented area. |
| `provides_50_or_more_hours_unpaid_carea_week` | `double precision` | Numeric provides 50 or more hours unpaid carea week value recorded for the feature. |
