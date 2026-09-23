# Census2021 Ts015 Msoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts015_msoa`
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
- **Table:** `census2021_ts015_msoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 7264
- **Columns:** 16
- **Metadata status:** source_mapped

## Description

Census2021 Ts015 Msoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts015 msoa.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `date` | `bigint` |  |
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `geography_code` | `text` | Code assigned by the source dataset. |
| `total_all_usual_residents` | `bigint` | Census total for all usual residents in the represented geographical area; measurement unit requires the table documentation. |
| `born_in_the_uk` | `bigint` | Recorded census measure for the category "born in the UK" in the represented area. Units and population base require the source table. |
| `arrived_before_1951` | `bigint` |  |
| `arrived_1951_to_1960` | `bigint` |  |
| `arrived_1961_to_1970` | `bigint` |  |
| `arrived_1971_to_1980` | `bigint` |  |
| `arrived_1981_to_1990` | `bigint` |  |
| `arrived_1991_to_2000` | `bigint` |  |
| `arrived_2001_to_2010` | `bigint` |  |
| `arrived_2011_to_2013` | `bigint` |  |
| `arrived_2014_to_2016` | `bigint` |  |
| `arrived_2017_to_2019` | `bigint` |  |
| `arrived_2020_to_2021` | `bigint` |  |
