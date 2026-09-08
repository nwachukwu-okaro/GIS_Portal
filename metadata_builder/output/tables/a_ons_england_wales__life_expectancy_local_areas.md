# Life Expectancy Local Areas

## Overview

- **Identifier:** `a_ons_england_wales/life_expectancy_local_areas`
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
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update
- **Schema:** `a_ons_england_wales`
- **Table:** `life_expectancy_local_areas`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 0
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Life Expectancy Local Areas is an authoritative dataset published by Office for National Statistics. It contains records relating to life expectancy local areas.

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
| `period` | `varchar` |  |
| `country` | `varchar` |  |
| `area type` | `varchar` |  |
| `area code` | `varchar` |  |
| `area name` | `varchar` |  |
| `sex` | `varchar` |  |
| `sex code` | `integer` |  |
| `age group` | `varchar` |  |
| `age code` | `integer` |  |
| `life expectancy` | `double precision` |  |
| `lower confidence interval` | `double precision` |  |
| `upper confidence interval` | `double precision` |  |
