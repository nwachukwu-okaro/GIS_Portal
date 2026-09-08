# Boundary Census Scotland Demographics Migration Intzones

## Overview

- **Identifier:** `a_nrs_scotland/boundary_census_scotland_demographics_migration_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **WGS84 extent:** `[-8.650007, 54.633238, -0.724609, 60.860766]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nrs_scotland`
- **Table:** `boundary_census_scotland_demographics_migration_intzones`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1280
- **Columns:** 52
- **Metadata status:** source_mapped

## Description

Boundary Census Scotland Demographics Migration Intzones is an authoritative dataset published by National Records of Scotland. It represents boundary census scotland demographics migration intzones features using multipolygon geometry.

## Lineage

Published by National Records of Scotland as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geography_code` | `text` | Code assigned by the source dataset. |
| `geography_name` | `text` | Name associated with the represented feature. |
| `uv_age_arrival_all_people` | `bigint` | Count or numeric value for uv age arrival all people in the represented area. |
| `uv_age_arrival_born_in_the_uk` | `bigint` | Count or numeric value for uv age arrival born in the uk in the represented area. |
| `t_0_15` | `bigint` | Count or numeric value for t 0 15 in the represented area. |
| `t_16_24` | `bigint` | Count or numeric value for t 16 24 in the represented area. |
| `t_25_34` | `bigint` | Count or numeric value for t 25 34 in the represented area. |
| `t_35_49` | `bigint` | Count or numeric value for t 35 49 in the represented area. |
| `t_50_64` | `bigint` | Count or numeric value for t 50 64 in the represented area. |
| `t_65_and_over` | `bigint` | Count or numeric value for t 65 and over in the represented area. |
| `uv_year_arrival_all_people` | `bigint` | Count or numeric value for uv year arrival all people in the represented area. |
| `uv_year_arrival_born_in_the_uk` | `bigint` | Count or numeric value for uv year arrival born in the uk in the represented area. |
| `arrived_before_1941` | `bigint` | Count or numeric value for arrived before 1941 in the represented area. |
| `arrived_1941_1950` | `bigint` | Count or numeric value for arrived 1941 1950 in the represented area. |
| `arrived_1951_1960` | `bigint` | Count or numeric value for arrived 1951 1960 in the represented area. |
| `arrived_1961_1970` | `bigint` | Count or numeric value for arrived 1961 1970 in the represented area. |
| `arrived_1971_1980` | `bigint` | Count or numeric value for arrived 1971 1980 in the represented area. |
| `arrived_1981_1990` | `bigint` | Count or numeric value for arrived 1981 1990 in the represented area. |
| `arrived_1991_2000` | `bigint` | Count or numeric value for arrived 1991 2000 in the represented area. |
| `arrived_2001_2010` | `bigint` | Count or numeric value for arrived 2001 2010 in the represented area. |
| `arrived_2011_2013` | `bigint` | Count or numeric value for arrived 2011 2013 in the represented area. |
| `arrived_2014_2016` | `bigint` | Count or numeric value for arrived 2014 2016 in the represented area. |
| `arrived_2017_2019` | `bigint` | Count or numeric value for arrived 2017 2019 in the represented area. |
| `arrived_2020_2022` | `bigint` | Count or numeric value for arrived 2020 2022 in the represented area. |
| `uv_length_residence_all_people` | `bigint` | Numeric uv length residence all people value recorded for the feature. |
| `uv_length_residence_born_in_the_uk` | `bigint` | Numeric uv length residence born in the uk value recorded for the feature. |
| `less_than_2_years` | `bigint` | Count or numeric value for less than 2 years in the represented area. |
| `t_2_years_or_more_and_less_than_5_years` | `bigint` | Count or numeric value for t 2 years or more and less than 5 years in the represented area. |
| `t_5_years_or_more_and_less_than_10_years` | `bigint` | Count or numeric value for t 5 years or more and less than 10 years in the represented area. |
| `t_10_years_or_more` | `bigint` | Count or numeric value for t 10 years or more in the represented area. |
| `uv_dual_passport_all_people` | `bigint` | Count or numeric value for uv dual passport all people in the represented area. |
| `uk_and_irish_passport` | `bigint` | Count or numeric value for uk and irish passport in the represented area. |
| `uk_and_other_passport_europe_european_union` | `bigint` | Count or numeric value for uk and other passport europe european union in the represented area. |
| `uk_and_other_passport_europe_other_europe` | `bigint` | Count or numeric value for uk and other passport europe other europe in the represented area. |
| `uk_and_non_european_passport` | `bigint` | Count or numeric value for uk and non european passport in the represented area. |
| `irish_and_other_passport_europe_european_union` | `bigint` | Count or numeric value for irish and other passport europe european union in the represented area. |
| `irish_and_other_passport_europe_other_europe` | `bigint` | Count or numeric value for irish and other passport europe other europe in the represented area. |
| `irish_and_non_european_passport` | `bigint` | Count or numeric value for irish and non european passport in the represented area. |
| `other_combination_of_passports` | `bigint` | Count or numeric value for other combination of passports in the represented area. |
| `does_not_have_dual_passports` | `bigint` | Count or numeric value for does not have dual passports in the represented area. |
| `uv_passport_held_all_people` | `bigint` | Count or numeric value for uv passport held all people in the represented area. |
| `europe_total` | `bigint` | Count or numeric value for europe total in the represented area. |
| `europe_united_kingdom` | `bigint` | Count or numeric value for europe united kingdom in the represented area. |
| `europe_ireland` | `bigint` | Count or numeric value for europe ireland in the represented area. |
| `europe_eu_member_countries` | `bigint` | Count or numeric value for europe eu member countries in the represented area. |
| `europe_rest_of_europe` | `bigint` | Count or numeric value for europe rest of europe in the represented area. |
| `africa` | `bigint` | Count or numeric value for africa in the represented area. |
| `middle_east_and_asia` | `bigint` | Count or numeric value for middle east and asia in the represented area. |
| `antarctica_and_oceania` | `bigint` | Count or numeric value for antarctica and oceania in the represented area. |
| `no_passport` | `bigint` | Count or numeric value for number passport in the represented area. |
| `the_americas_and_the_caribbean` | `bigint` | Count or numeric value for the americas and the caribbean in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
