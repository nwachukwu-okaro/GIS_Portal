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
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
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
| `all_people_16plus` | `bigint` | Count or numeric value for all people 16plus in the represented area. |
| `no_quals` | `bigint` | Count or numeric value for number quals in the represented area. |
| `lower_school_quals` | `bigint` | Count or numeric value for lower school quals in the represented area. |
| `upper_school_quals` | `bigint` | Count or numeric value for upper school quals in the represented area. |
| `apprenticeship` | `bigint` | Count or numeric value for apprenticeship in the represented area. |
| `fe_and_sub_degree_he_incl_hnc_hnd` | `bigint` | Count or numeric value for fe and sub degree he incl hnc hnd in the represented area. |
| `degree_level_or_above` | `bigint` | Count or numeric value for degree level or above in the represented area. |
