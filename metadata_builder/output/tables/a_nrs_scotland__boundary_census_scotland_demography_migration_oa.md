# Boundary Census Scotland Demography Migration Oa

## Overview

- **Identifier:** `a_nrs_scotland/boundary_census_scotland_demography_migration_oa`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **WGS84 extent:** `[-8.649996, 54.633220, -0.724450, 60.860787]`
- **Schema:** `a_nrs_scotland`
- **Table:** `boundary_census_scotland_demography_migration_oa`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:2157
- **Rows:** 46363
- **Columns:** 30
- **Metadata status:** source_mapped

## Description

Boundary Census Scotland Demography Migration Oa is an authoritative dataset published by National Records of Scotland. It represents boundary census scotland demography migration oa features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `all_people_arrival_yr` | `bigint` | Count or numeric value for all people arrival year in the represented area. | statistical_value | Yes | No | No |
| `born_in_the_uk_arrival_yr` | `bigint` | Count or numeric value for born in the uk arrival year in the represented area. | statistical_value | Yes | No | No |
| `arrived_before_1941` | `double precision` | Count or numeric value for arrived before 1941 in the represented area. | statistical_value | Yes | No | No |
| `arrived_1941_1950` | `double precision` | Count or numeric value for arrived 1941 1950 in the represented area. | statistical_value | Yes | No | No |
| `arrived_1951_1960` | `double precision` | Count or numeric value for arrived 1951 1960 in the represented area. | statistical_value | Yes | No | No |
| `arrived_1961_1970` | `double precision` | Count or numeric value for arrived 1961 1970 in the represented area. | statistical_value | Yes | No | No |
| `arrived_1971_1980` | `double precision` | Count or numeric value for arrived 1971 1980 in the represented area. | statistical_value | Yes | No | No |
| `arrived_1981_1990` | `double precision` | Count or numeric value for arrived 1981 1990 in the represented area. | statistical_value | Yes | No | No |
| `arrived_1991_2000` | `double precision` | Count or numeric value for arrived 1991 2000 in the represented area. | statistical_value | Yes | No | No |
| `arrived_2001_2010` | `double precision` | Count or numeric value for arrived 2001 2010 in the represented area. | statistical_value | Yes | No | No |
| `arrived_2011_2013` | `double precision` | Count or numeric value for arrived 2011 2013 in the represented area. | statistical_value | Yes | No | No |
| `arrived_2014_2016` | `double precision` | Count or numeric value for arrived 2014 2016 in the represented area. | statistical_value | Yes | No | No |
| `arrived_2017_2019` | `double precision` | Count or numeric value for arrived 2017 2019 in the represented area. | statistical_value | Yes | No | No |
| `arrived_2020_2022` | `double precision` | Count or numeric value for arrived 2020 2022 in the represented area. | statistical_value | Yes | No | No |
| `all_people_arrival_age` | `bigint` | Count or numeric value for all people arrival age in the represented area. | statistical_value | Yes | No | No |
| `born_in_the_uk_arrival_age` | `bigint` | Count or numeric value for born in the uk arrival age in the represented area. | statistical_value | Yes | No | No |
| `arrived_aged_0_15` | `double precision` | Count or numeric value for arrived aged 0 15 in the represented area. | statistical_value | Yes | No | No |
| `arrived_aged_16_24` | `double precision` | Count or numeric value for arrived aged 16 24 in the represented area. | statistical_value | Yes | No | No |
| `arrived_aged_25_34` | `double precision` | Count or numeric value for arrived aged 25 34 in the represented area. | statistical_value | Yes | No | No |
| `arrived_aged_35_49` | `double precision` | Count or numeric value for arrived aged 35 49 in the represented area. | statistical_value | Yes | No | No |
| `arrived_aged_50_64` | `double precision` | Count or numeric value for arrived aged 50 64 in the represented area. | statistical_value | Yes | No | No |
| `arrived_aged_65_and_over` | `double precision` | Count or numeric value for arrived aged 65 and over in the represented area. | statistical_value | Yes | No | No |
| `all_people_residence_len` | `bigint` | Count or numeric value for all people residence len in the represented area. | statistical_value | Yes | No | No |
| `born_in_the_uk_residence_len` | `bigint` | Count or numeric value for born in the uk residence len in the represented area. | statistical_value | Yes | No | No |
| `less_than_2_years` | `double precision` | Count or numeric value for less than 2 years in the represented area. | statistical_value | Yes | No | No |
| `t_2_years_or_more_and_less_than_5_years` | `double precision` | Count or numeric value for t 2 years or more and less than 5 years in the represented area. | statistical_value | Yes | No | No |
| `t_5_years_or_more_and_less_than_10_years` | `double precision` | Count or numeric value for t 5 years or more and less than 10 years in the represented area. | statistical_value | Yes | No | No |
| `t_10_years_or_more` | `double precision` | Count or numeric value for t 10 years or more in the represented area. | statistical_value | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |

## Supported operations

- filter
- select
- reproject
- validate_geometry
- buffer
- clip
- intersect
- spatial_join
- export

## Operation requirements

- Intersect, clip and spatial-join inputs must use matching coordinate reference systems.
- Buffer operations require a suitable projected coordinate reference system.
- Reprojection is performed on working outputs; source tables remain unchanged.

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
