# Census2021 Wp001 Rgn

## Overview

- **Identifier:** `a_ons_england_wales/census2021_wp001_rgn`
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
- **Table:** `census2021_wp001_rgn`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 10
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Census2021 Wp001 Rgn is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 wp001 rgn.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. |
| `regions code` | `varchar` | Publisher-assigned regions code for the record. |
| `regions label` | `varchar` | Publisher-supplied regions label for the represented feature or record. |
| `count` | `varchar` | Publisher-supplied count for the represented feature or record. |
