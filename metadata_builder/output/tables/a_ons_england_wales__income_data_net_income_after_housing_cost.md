# Income Data Net Income After Housing Cost

## Overview

- **Identifier:** `a_ons_england_wales/income_data_net_income_after_housing_cost`
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
- **Table:** `income_data_net_income_after_housing_cost`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 7264
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Income Data Net Income After Housing Cost is an authoritative dataset published by Office for National Statistics. It contains records relating to income data net income after housing cost.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `msoa_code` | `text` | Code assigned by the source dataset. |
| `msoa_name` | `text` | Name associated with the represented feature. |
| `local_authority_code` | `text` | Code assigned by the source dataset. |
| `local_authority_name` | `text` | Name associated with the represented feature. |
| `region_code` | `text` | Code assigned by the source dataset. |
| `region_name` | `text` | Name associated with the represented feature. |
| `disposable_net_annual_income_after_housing_costs` | `text` | Publisher-supplied disposable net annual income after housing costs for the represented feature or record. |
| `upper_confidence_limit` | `text` | Publisher-supplied upper confidence limit for the represented feature or record. |
| `lower_confidence_limit` | `text` | Publisher-supplied lower confidence limit for the represented feature or record. |
| `confidence_interval` | `text` | Publisher-supplied confidence interval for the represented feature or record. |
