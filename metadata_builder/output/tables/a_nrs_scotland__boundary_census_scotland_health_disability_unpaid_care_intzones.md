# Boundary Census Scotland Health Disability Unpaid Care Intzones

## Overview

- **Identifier:** `a_nrs_scotland/boundary_census_scotland_health_disability_unpaid_care_intzones`
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
- **Table:** `boundary_census_scotland_health_disability_unpaid_care_intzones`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1280
- **Columns:** 28
- **Metadata status:** source_mapped

## Description

Boundary Census Scotland Health Disability Unpaid Care Intzones is an authoritative dataset published by National Records of Scotland. It represents boundary census scotland health disability unpaid care intzones features using multipolygon geometry.

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
| `general_health_all_people` | `bigint` | Count or numeric value for general health all people in the represented area. |
| `very_good` | `bigint` | Count or numeric value for very good in the represented area. |
| `good` | `bigint` | Count or numeric value for good in the represented area. |
| `fair` | `bigint` | Count or numeric value for fair in the represented area. |
| `bad` | `bigint` | Count or numeric value for bad in the represented area. |
| `very_bad` | `bigint` | Count or numeric value for very bad in the represented area. |
| `lt_disability_all_people` | `bigint` | Count or numeric value for lt disability all people in the represented area. |
| `daily_activities_limited_a_lot` | `bigint` | Count or numeric value for daily activities limited a lot in the represented area. |
| `daily_activities_limited_a_little` | `bigint` | Count or numeric value for daily activities limited a little in the represented area. |
| `daily_activities_not_limited` | `bigint` | Count or numeric value for daily activities not limited in the represented area. |
| `lt_health_all_people` | `bigint` | Count or numeric value for lt health all people in the represented area. |
| `hearing_impairment` | `bigint` | Count or numeric value for hearing impairment in the represented area. |
| `vision_impairment` | `bigint` | Count or numeric value for vision impairment in the represented area. |
| `speech_impairment` | `bigint` | Count or numeric value for speech impairment in the represented area. |
| `learning_disability_or_difficulty` | `bigint` | Count or numeric value for learning disability or difficulty in the represented area. |
| `physical_disability` | `bigint` | Count or numeric value for physical disability in the represented area. |
| `mental_health_condition` | `bigint` | Count or numeric value for mental health condition in the represented area. |
| `long_term_illness` | `bigint` | Numeric long term illness value recorded for the feature. |
| `all_people_3plus` | `bigint` | Count or numeric value for all people 3plus in the represented area. |
| `no_unpaid_care` | `bigint` | Count or numeric value for number unpaid care in the represented area. |
| `all_unpaid_carers` | `bigint` | Count or numeric value for all unpaid carers in the represented area. |
| `unpaid_care_1_19hrs_pw` | `bigint` | Count or numeric value for unpaid care 1 19hrs pw in the represented area. |
| `unpaid_care_20_34hrs_pw` | `bigint` | Count or numeric value for unpaid care 20 34hrs pw in the represented area. |
| `unpaid_care_35_49hrs_pw` | `bigint` | Count or numeric value for unpaid care 35 49hrs pw in the represented area. |
| `unpaid_care_50plus_hrs_pw` | `bigint` | Count or numeric value for unpaid care 50plus hrs pw in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
