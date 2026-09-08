# Distance Travelled Work Intzones

## Overview

- **Identifier:** `a_nrs_scotland/distance_travelled_work_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `distance_travelled_work_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1282
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Distance Travelled Work Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to distance travelled work intzones.

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
| `all_people_aged_16_and_over_in_employment_the_week_before_the_c` | `text` | Publisher-supplied all people aged 16 and over in employment the week before the c for the represented feature or record. |
| `mainly_work_from_home` | `text` | Publisher-supplied mainly work from home for the represented feature or record. |
| `less_than_2km` | `text` | Publisher-supplied less than 2km for the represented feature or record. |
| `t_2km_to_less_than_5km` | `text` | Publisher-supplied t 2km to less than 5km for the represented feature or record. |
| `t_5km_to_less_than_10km` | `text` | Publisher-supplied t 5km to less than 10km for the represented feature or record. |
| `t_10km_to_less_than_20km` | `text` | Publisher-supplied t 10km to less than 20km for the represented feature or record. |
| `t_20km_to_less_than_30km` | `double precision` | Count or numeric value for t 20km to less than 30km in the represented area. |
| `t_30km_to_less_than_40km` | `double precision` | Count or numeric value for t 30km to less than 40km in the represented area. |
| `t_40km_to_less_than_60km` | `double precision` | Count or numeric value for t 40km to less than 60km in the represented area. |
| `t_60km_and_over` | `double precision` | Count or numeric value for t 60km and over in the represented area. |
| `other_no_fixed_place_of_work_or_working_outside_the_uk` | `double precision` | Count or numeric value for other number fixed place of work or working outside the uk in the represented area. |
