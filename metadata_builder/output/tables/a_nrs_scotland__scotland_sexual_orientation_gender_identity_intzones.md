# Scotland Sexual Orientation Gender Identity Intzones

## Overview

- **Identifier:** `a_nrs_scotland/scotland_sexual_orientation_gender_identity_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `scotland_sexual_orientation_gender_identity_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1279
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Scotland Sexual Orientation Gender Identity Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to scotland sexual orientation gender identity intzones.

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
| `all_people_16plus_sexual_orient` | `bigint` | Recorded census measure for the category "all people 16plus sexual orient" in the represented area. Units and population base require the source table. |
| `heterosexual_straight` | `bigint` |  |
| `gay_or_lesbian` | `bigint` |  |
| `bisexual` | `bigint` |  |
| `other_sexual_orientation` | `bigint` |  |
| `not_answered_sexual_orient` | `bigint` |  |
| `all_people_16plus_trans_status` | `bigint` | Recorded census measure for the category "all people 16plus trans status" in the represented area. Units and population base require the source table. |
| `not_trans_no_history` | `bigint` |  |
| `trans_or_has_trans_history` | `bigint` |  |
| `not_answered_trans_status` | `bigint` |  |
