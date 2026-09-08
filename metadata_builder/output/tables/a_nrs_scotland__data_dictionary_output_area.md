# Data Dictionary Output Area

## Overview

- **Identifier:** `a_nrs_scotland/data_dictionary_output_area`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `data_dictionary_output_area`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 2162
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Data Dictionary Output Area is an authoritative dataset published by National Records of Scotland. It contains records relating to data dictionary output area.

## Lineage

Published by National Records of Scotland as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `theme` | `text` | Publisher-supplied theme for the represented feature or record. |
| `table_code` | `text` | Code assigned by the source dataset. |
| `source_file` | `text` | Publisher-supplied source file for the represented feature or record. |
| `original_label` | `text` | Publisher-supplied original label for the represented feature or record. |
| `processed_column_name` | `text` | Name associated with the represented feature. |
| `output_file` | `text` | Publisher-supplied output file for the represented feature or record. |
