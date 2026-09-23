# Boundary Census Scotland Education Oa

## Overview

- **Identifier:** `a_nrs_scotland/boundary_census_scotland_education_oa`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **WGS84 extent:** `[-8.649996, 54.633220, -0.724450, 60.860787]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nrs_scotland`
- **Table:** `boundary_census_scotland_education_oa`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:2157
- **Rows:** 46363
- **Columns:** 51
- **Metadata status:** source_mapped

## Description

Boundary Census Scotland Education Oa is an authoritative dataset published by National Records of Scotland. It represents boundary census scotland education oa features using geometry geometry.

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
| `all_people_aged_16_and_over_qual` | `bigint` | Recorded census measure for the category "all people aged 16 and over qual" in the represented area. Units and population base require the source table. |
| `no_qualifications_total` | `double precision` |  |
| `lower_school_qualifications_total` | `double precision` |  |
| `upper_school_qualifications_total` | `double precision` |  |
| `apprenticeship_qualifications_total` | `double precision` |  |
| `fe_sub_degree_he_qual_total` | `double precision` |  |
| `degree_level_qualifications_or_above_total` | `double precision` |  |
| `all_people_aged_16_and_over_qual_age` | `bigint` | Recorded census measure for the category "all people aged 16 and over qual age" in the represented area. Units and population base require the source table. |
| `all_people_aged_16_and_over_16_24` | `double precision` |  |
| `all_people_aged_16_and_over_25_34` | `double precision` |  |
| `all_people_aged_16_and_over_35_49` | `double precision` |  |
| `all_people_aged_16_and_over_50_64` | `double precision` |  |
| `all_people_aged_16_and_over_65_plus` | `double precision` | Recorded census measure for the category "all people aged 16 and over 65 plus" in the represented area. Units and population base require the source table. |
| `no_qualifications_age` | `double precision` |  |
| `no_qualifications_16_24` | `double precision` |  |
| `no_qualifications_25_34` | `double precision` |  |
| `no_qualifications_35_49` | `double precision` |  |
| `no_qualifications_50_64` | `double precision` |  |
| `no_qualifications_65_plus` | `double precision` |  |
| `lower_school_qualifications_age` | `double precision` |  |
| `lower_school_qualifications_16_24` | `double precision` |  |
| `lower_school_qualifications_25_34` | `double precision` |  |
| `lower_school_qualifications_35_49` | `double precision` |  |
| `lower_school_qualifications_50_64` | `double precision` |  |
| `lower_school_qualifications_65_plus` | `double precision` |  |
| `upper_school_qualifications_age` | `double precision` |  |
| `upper_school_qualifications_16_24` | `double precision` |  |
| `upper_school_qualifications_25_34` | `double precision` |  |
| `upper_school_qualifications_35_49` | `double precision` |  |
| `upper_school_qualifications_50_64` | `double precision` |  |
| `upper_school_qualifications_65_plus` | `double precision` |  |
| `apprenticeship_qualifications_age` | `double precision` |  |
| `apprenticeship_qualifications_16_24` | `double precision` |  |
| `apprenticeship_qualifications_25_34` | `double precision` |  |
| `apprenticeship_qualifications_35_49` | `double precision` |  |
| `apprenticeship_qualifications_50_64` | `double precision` |  |
| `apprenticeship_qualifications_65_plus` | `double precision` |  |
| `fe_sub_degree_he_qual_age` | `double precision` |  |
| `fe_sub_degree_he_qual_16_24` | `double precision` |  |
| `fe_sub_degree_he_qual_25_34` | `double precision` |  |
| `fe_sub_degree_he_qual_35_49` | `double precision` |  |
| `fe_sub_degree_he_qual_50_64` | `double precision` |  |
| `fe_sub_degree_he_qual_65_plus` | `double precision` |  |
| `degree_level_qualifications_or_above_age` | `double precision` |  |
| `degree_level_qualifications_or_above_16_24` | `double precision` |  |
| `degree_level_qualifications_or_above_25_34` | `double precision` |  |
| `degree_level_qualifications_or_above_35_49` | `double precision` |  |
| `degree_level_qualifications_or_above_50_64` | `double precision` |  |
| `degree_level_qualifications_or_above_65_plus` | `double precision` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
