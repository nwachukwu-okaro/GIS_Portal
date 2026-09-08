# Census2021 Ts004 Oa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts004_oa`
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
- **Table:** `census2021_ts004_oa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 188880
- **Columns:** 18
- **Metadata status:** source_mapped

## Description

Census2021 Ts004 Oa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts004 oa.

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
| `total` | `bigint` | Count or numeric value for total in the represented area. |
| `europe` | `bigint` | Count or numeric value for europe in the represented area. |
| `europe_united_kingdom` | `bigint` | Count or numeric value for europe united kingdom in the represented area. |
| `europe_eu_countries` | `bigint` | Count or numeric value for europe eu countries in the represented area. |
| `europe_eu_countries_european_union_eu14` | `bigint` | Count or numeric value for europe eu countries european union eu14 in the represented area. |
| `europe_eu_countries_european_union_eu8` | `bigint` | Count or numeric value for europe eu countries european union eu8 in the represented area. |
| `europe_eu_countries_european_union_eu2` | `bigint` | Count or numeric value for europe eu countries european union eu2 in the represented area. |
| `europe_eu_countries_all_other_eu_countries` | `bigint` | Count or numeric value for europe eu countries all other eu countries in the represented area. |
| `europe_non_eu_countries` | `bigint` | Count or numeric value for europe non eu countries in the represented area. |
| `europe_non_eu_countries_all_other_non_eu_countries` | `bigint` | Count or numeric value for europe non eu countries all other non eu countries in the represented area. |
| `africa` | `bigint` | Count or numeric value for africa in the represented area. |
| `middle_east_and_asia` | `bigint` | Count or numeric value for middle east and asia in the represented area. |
| `the_americas_and_the_caribbean` | `bigint` | Count or numeric value for the americas and the caribbean in the represented area. |
| `antarctica_and_oceania_including_australasia_and_other` | `bigint` | Count or numeric value for antarctica and oceania including australasia and other in the represented area. |
| `british_overseas` | `bigint` | Count or numeric value for british overseas in the represented area. |
