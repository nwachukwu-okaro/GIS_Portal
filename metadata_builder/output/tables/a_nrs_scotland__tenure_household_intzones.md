# Tenure Household Intzones

## Overview

- **Identifier:** `a_nrs_scotland/tenure_household_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `tenure_household_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Tenure Household Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to tenure household intzones.

## Lineage

Published by National Records of Scotland as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `all_occupied_households` | `double precision` | Count or numeric value for all occupied households in the represented area. |
| `occupancy_rating_of_bedrooms_2_or_more` | `double precision` | Count or numeric value for occupancy rating of bedrooms 2 or more in the represented area. |
| `occupancy_rating_of_bedrooms_1` | `double precision` | Count or numeric value for occupancy rating of bedrooms 1 in the represented area. |
| `occupancy_rating_of_bedrooms_0` | `double precision` | Count or numeric value for occupancy rating of bedrooms 0 in the represented area. |
| `occupancy_rating_of_bedrooms_1_or_less` | `double precision` | Count or numeric value for occupancy rating of bedrooms 1 or less in the represented area. |
