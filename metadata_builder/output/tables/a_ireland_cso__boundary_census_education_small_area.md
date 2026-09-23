# Boundary Census Education Small Area

## Overview

- **Identifier:** `a_ireland_cso/boundary_census_education_small_area`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-1.726726, 54.563349, 3.417194, 58.519873]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `boundary_census_education_small_area`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 18919
- **Columns:** 81
- **Metadata status:** source_mapped

## Description

Boundary Census Education Small Area is an authoritative dataset published by Central Statistics Office Ireland. It represents boundary census education small area features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `guid` | `text` | UUID-formatted identifier associated with the record; persistence across releases is not confirmed. |
| `geogid` | `text` | Code identifying the geographical area represented by the row. |
| `geogdesc` | `text` |  |
| `ur_category` | `double precision` |  |
| `ur_category_desc` | `text` |  |
| `age_under_15_males` | `bigint` |  |
| `age_15_males` | `bigint` | Census measure for males aged 15 years in the represented area; count or percentage must be checked against the source table. |
| `age_16_males` | `bigint` | Census measure for males aged 16 years in the represented area; count or percentage must be checked against the source table. |
| `age_17_males` | `bigint` | Census measure for males aged 17 years in the represented area; count or percentage must be checked against the source table. |
| `age_18_males` | `bigint` | Census measure for males aged 18 years in the represented area; count or percentage must be checked against the source table. |
| `age_19_males` | `bigint` | Census measure for males aged 19 years in the represented area; count or percentage must be checked against the source table. |
| `age_20_males` | `bigint` | Census measure for males aged 20 years in the represented area; count or percentage must be checked against the source table. |
| `age_21_and_over_males` | `bigint` |  |
| `not_stated_males` | `bigint` |  |
| `total_males` | `bigint` | Census total for males in the represented geographical area; measurement unit requires the table documentation. |
| `age_under_15_females` | `bigint` |  |
| `age_15_females` | `bigint` | Census measure for females aged 15 years in the represented area; count or percentage must be checked against the source table. |
| `age_16_females` | `bigint` | Census measure for females aged 16 years in the represented area; count or percentage must be checked against the source table. |
| `age_17_females` | `bigint` | Census measure for females aged 17 years in the represented area; count or percentage must be checked against the source table. |
| `age_18_females` | `bigint` | Census measure for females aged 18 years in the represented area; count or percentage must be checked against the source table. |
| `age_19_females` | `bigint` | Census measure for females aged 19 years in the represented area; count or percentage must be checked against the source table. |
| `age_20_females` | `bigint` | Census measure for females aged 20 years in the represented area; count or percentage must be checked against the source table. |
| `age_21_and_over_females` | `bigint` |  |
| `not_stated_females` | `bigint` |  |
| `total_females` | `bigint` | Census total for females in the represented geographical area; measurement unit requires the table documentation. |
| `age_under_15_total` | `bigint` |  |
| `age_15_total` | `bigint` | Census measure for persons aged 15 years in the represented area; count or percentage must be checked against the source table. |
| `age_16_total` | `bigint` | Census measure for persons aged 16 years in the represented area; count or percentage must be checked against the source table. |
| `age_17_total` | `bigint` | Census measure for persons aged 17 years in the represented area; count or percentage must be checked against the source table. |
| `age_18_total` | `bigint` | Census measure for persons aged 18 years in the represented area; count or percentage must be checked against the source table. |
| `age_19_total` | `bigint` | Census measure for persons aged 19 years in the represented area; count or percentage must be checked against the source table. |
| `age_20_total` | `bigint` | Census measure for persons aged 20 years in the represented area; count or percentage must be checked against the source table. |
| `age_21_and_over_total` | `bigint` |  |
| `not_stated_total` | `bigint` |  |
| `total` | `bigint` |  |
| `still_at_school_or_college_males` | `bigint` |  |
| `other_males` | `bigint` |  |
| `still_at_school_or_college_females` | `bigint` |  |
| `other_females` | `bigint` |  |
| `still_at_school_or_college_total` | `bigint` |  |
| `other_total` | `bigint` |  |
| `no_formal_education_males` | `bigint` |  |
| `primary_education_males` | `bigint` |  |
| `lower_secondary_males` | `bigint` |  |
| `upper_secondary_males` | `bigint` |  |
| `technical_or_vocational_qualification_males` | `bigint` |  |
| `advanced_certificatecompleted_apprenticeship_males` | `bigint` |  |
| `higher_certificate_males` | `bigint` |  |
| `ordinary_bachelor_degree_or_national_diploma_males` | `bigint` |  |
| `honours_bachelor_degree_professional_qualification_or_both_male` | `bigint` |  |
| `postgraduate_diploma_or_degree_males` | `bigint` |  |
| `doctoratephd_or_higher_males` | `bigint` |  |
| `not_stated_males_1` | `bigint` |  |
| `total_males_1` | `bigint` |  |
| `no_formal_education_females` | `bigint` |  |
| `primary_education_females` | `bigint` |  |
| `lower_secondary_females` | `bigint` |  |
| `upper_secondary_females` | `bigint` |  |
| `technical_or_vocational_qualification_females` | `bigint` |  |
| `advanced_certificatecompleted_apprenticeship_females` | `bigint` |  |
| `higher_certificate_females` | `bigint` |  |
| `ordinary_bachelor_degree_or_national_diploma_females` | `bigint` |  |
| `honours_bachelor_degree_professional_qualification_or_both_fema` | `bigint` |  |
| `postgraduate_diploma_or_degree_females` | `bigint` |  |
| `doctoratephd_or_higher_females` | `bigint` |  |
| `not_stated_females_1` | `bigint` |  |
| `total_females_1` | `bigint` |  |
| `no_formal_education_total` | `bigint` |  |
| `primary_education_total` | `bigint` |  |
| `lower_secondary_total` | `bigint` |  |
| `upper_secondary_total` | `bigint` |  |
| `technical_or_vocational_qualification_total` | `bigint` |  |
| `advanced_certificatecompleted_apprenticeship_total` | `bigint` |  |
| `higher_certificate_total` | `bigint` |  |
| `ordinary_bachelor_degree_or_national_diploma_total` | `bigint` |  |
| `honours_bachelor_degree_professional_qualification_or_both_tota` | `bigint` |  |
| `postgraduate_diploma_or_degree_total` | `bigint` |  |
| `doctoratephd_or_higher_total` | `bigint` |  |
| `not_stated_total_1` | `bigint` |  |
| `total_1` | `bigint` |  |
