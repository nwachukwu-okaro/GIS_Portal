# Longterm Disabilities Intzones

## Overview

- **Identifier:** `a_nrs_scotland/longterm_disabilities_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `longterm_disabilities_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Longterm Disabilities Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to longterm disabilities intzones.

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
| `day_to_day_activities_limited_a_lot` | `double precision` | Count or numeric value for day to day activities limited a lot in the represented area. |
| `day_to_day_activities_limited_a_little` | `double precision` | Count or numeric value for day to day activities limited a little in the represented area. |
| `day_to_day_activities_not_limited` | `double precision` | Count or numeric value for day to day activities not limited in the represented area. |
