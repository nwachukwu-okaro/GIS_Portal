# General Health Intzones

## Overview

- **Identifier:** `a_nrs_scotland/general_health_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `general_health_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

General Health Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to general health intzones.

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
| `all_people` | `double precision` | Count or numeric value for all people in the represented area. |
| `very_good` | `double precision` | Count or numeric value for very good in the represented area. |
| `good` | `double precision` | Count or numeric value for good in the represented area. |
| `fair` | `double precision` | Count or numeric value for fair in the represented area. |
| `bad` | `double precision` | Count or numeric value for bad in the represented area. |
| `very_bad` | `double precision` | Count or numeric value for very bad in the represented area. |
