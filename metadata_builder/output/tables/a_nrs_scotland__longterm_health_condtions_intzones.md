# Longterm Health Condtions Intzones

## Overview

- **Identifier:** `a_nrs_scotland/longterm_health_condtions_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `longterm_health_condtions_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Longterm Health Condtions Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to longterm health condtions intzones.

## Lineage

Published by National Records of Scotland as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `all_people` | `double precision` | Recorded census measure for the category "all people" in the represented area. Units and population base require the source table. |
| `deaf_or_partially_hearing_impaired` | `double precision` |  |
| `blind_or_partially_vision_impaired` | `double precision` |  |
| `full_partial_loss_of_voice_or_difficulty_speaking` | `double precision` |  |
| `has_one_or_more_of_learning_disability_learning_difficulty_o` | `double precision` |  |
| `physical_disability` | `double precision` |  |
| `mental_health_condition` | `double precision` |  |
| `long_term_illness_disease_or_condition` | `double precision` |  |
