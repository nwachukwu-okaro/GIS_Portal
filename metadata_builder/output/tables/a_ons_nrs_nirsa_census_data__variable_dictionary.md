# Variable Dictionary

## Overview

- **Identifier:** `a_ons_nrs_nirsa_census_data/variable_dictionary`
- **Source organisation:** UK national statistical authorities
- **Source:** https://www.ons.gov.uk/census
- **Geographic coverage:** United Kingdom
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ons_nrs_nirsa_census_data`
- **Table:** `variable_dictionary`
- **Geometry:** GEOMETRY
- **CRS:** Not applicable or unknown
- **Rows:** 25
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Variable Dictionary is an authoritative dataset published by UK national statistical authorities. It represents variable dictionary features using geometry geometry.

## Lineage

Published jointly by the UK's national statistical authorities (ONS, NRS and NISRA) as census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `table name` | `varchar(58)` |  |
| `uk table id` | `varchar(5)` |  |
| `unit` | `varchar(9)` |  |
| `population scope` | `varchar(285)` |  |
| `notes` | `varchar(957)` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
