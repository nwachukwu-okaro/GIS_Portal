# Scotland Education Intzones

## Overview

- **Identifier:** `a_nrs_scotland/scotland_education_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `scotland_education_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1279
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Scotland Education Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to scotland education intzones.

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
| `all_people_16plus` | `bigint` | Recorded census measure for the category "all people 16plus" in the represented area. Units and population base require the source table. |
| `no_quals` | `bigint` |  |
| `lower_school_quals` | `bigint` |  |
| `upper_school_quals` | `bigint` |  |
| `apprenticeship` | `bigint` |  |
| `fe_and_sub_degree_he_incl_hnc_hnd` | `bigint` |  |
| `degree_level_or_above` | `bigint` |  |
