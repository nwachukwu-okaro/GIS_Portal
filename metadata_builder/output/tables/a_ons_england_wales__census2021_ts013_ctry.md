# Census2021 Ts013 Ctry

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts013_ctry`
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
- **Table:** `census2021_ts013_ctry`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 3
- **Columns:** 72
- **Metadata status:** source_mapped

## Description

Census2021 Ts013 Ctry is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts013 ctry.

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
| `europe` | `bigint` |  |
| `europe_united_kingdom` | `bigint` |  |
| `europe_ireland` | `bigint` |  |
| `europe_other_europe` | `bigint` |  |
| `europe_other_europe_eu_member_countries` | `bigint` |  |
| `europe_other_europe_eu_member_countries_france` | `bigint` |  |
| `europe_other_europe_eu_member_countries_germany` | `bigint` |  |
| `europe_other_europe_eu_member_countries_italy` | `bigint` |  |
| `europe_other_europe_eu_member_countries_portugal` | `bigint` |  |
| `europe_other_europe_eu_member_countries_spain` | `bigint` |  |
| `europe_other_europe_eu_member_countries_lithuania` | `bigint` |  |
| `europe_other_europe_eu_member_countries_poland` | `bigint` |  |
| `europe_other_europe_eu_member_countries_romania` | `bigint` |  |
| `europe_other_europe_eu_member_countries_other_eu_countries` | `bigint` |  |
| `europe_other_europe_rest_of_europe` | `bigint` |  |
| `europe_other_europe_rest_of_europe_turkey` | `bigint` |  |
| `europe_other_europe_rest_of_europe_other_europe` | `bigint` |  |
| `africa` | `bigint` |  |
| `africa_north_africa` | `bigint` |  |
| `africa_central_and_western_africa` | `bigint` |  |
| `africa_central_and_western_africa_ghana` | `bigint` |  |
| `africa_central_and_western_africa_nigeria` | `bigint` |  |
| `africa_central_and_western_africa_other_central_and_western_afr` | `bigint` |  |
| `africa_south_and_eastern_africa` | `bigint` |  |
| `africa_south_and_eastern_africa_kenya` | `bigint` |  |
| `africa_south_and_eastern_africa_somalia` | `bigint` |  |
| `africa_south_and_eastern_africa_south_africa` | `bigint` |  |
| `africa_south_and_eastern_africa_zimbabwe` | `bigint` |  |
| `africa_south_and_eastern_africa_other_south_and_eastern_africa` | `bigint` |  |
| `middle_east_and_asia` | `bigint` |  |
| `middle_east_and_asia_middle_east` | `bigint` |  |
| `middle_east_and_asia_middle_east_iran` | `bigint` |  |
| `middle_east_and_asia_middle_east_iraq` | `bigint` |  |
| `middle_east_and_asia_middle_east_other_middle_east` | `bigint` |  |
| `middle_east_and_asia_eastern_asia` | `bigint` |  |
| `middle_east_and_asia_eastern_asia_china` | `bigint` |  |
| `middle_east_and_asia_eastern_asia_hong_kong_special_administrat` | `bigint` |  |
| `middle_east_and_asia_eastern_asia_japan` | `bigint` |  |
| `middle_east_and_asia_eastern_asia_other_eastern_asia` | `bigint` |  |
| `middle_east_and_asia_southern_asia` | `bigint` |  |
| `middle_east_and_asia_southern_asia_afghanistan` | `bigint` |  |
| `middle_east_and_asia_southern_asia_bangladesh` | `bigint` |  |
| `middle_east_and_asia_southern_asia_india` | `bigint` |  |
| `middle_east_and_asia_southern_asia_pakistan` | `bigint` |  |
| `middle_east_and_asia_southern_asia_sri_lanka` | `bigint` |  |
| `middle_east_and_asia_southern_asia_other_southern_asia` | `bigint` |  |
| `middle_east_and_asia_south_east_asia` | `bigint` |  |
| `middle_east_and_asia_south_east_asia_malaysia` | `bigint` |  |
| `middle_east_and_asia_south_east_asia_philippines` | `bigint` |  |
| `middle_east_and_asia_south_east_asia_singapore` | `bigint` |  |
| `middle_east_and_asia_south_east_asia_other_south_east_asia` | `bigint` |  |
| `middle_east_and_asia_central_asia` | `bigint` |  |
| `the_americas_and_the_caribbean` | `bigint` |  |
| `the_americas_and_the_caribbean_north_america` | `bigint` |  |
| `the_americas_and_the_caribbean_north_america_canada` | `bigint` |  |
| `the_americas_and_the_caribbean_north_america_united_states` | `bigint` |  |
| `the_americas_and_the_caribbean_central_america` | `bigint` |  |
| `the_americas_and_the_caribbean_south_america` | `bigint` |  |
| `the_americas_and_the_caribbean_the_caribbean` | `bigint` |  |
| `the_americas_and_the_caribbean_the_caribbean_jamaica` | `bigint` |  |
| `the_americas_and_the_caribbean_the_caribbean_other_caribbean` | `bigint` |  |
| `antarctica_and_oceania` | `bigint` |  |
| `antarctica_and_oceania_australasia` | `bigint` |  |
| `antarctica_and_oceania_australasia_australia` | `bigint` |  |
| `antarctica_and_oceania_australasia_new_zealand` | `bigint` |  |
| `antarctica_and_oceania_other_antarctica_and_oceania` | `bigint` |  |
| `british_overseas_territories` | `bigint` |  |
| `no_passport_held` | `bigint` |  |
