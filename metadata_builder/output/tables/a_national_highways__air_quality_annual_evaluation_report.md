# Air Quality Annual Evaluation Report

## Overview

- **Identifier:** `a_national_highways/air_quality_annual_evaluation_report`
- **Source organisation:** National Highways
- **Source:** https://developer.data.nationalhighways.co.uk/
- **Geographic coverage:** England
- **WGS84 extent:** `[-4.140956, 50.391032, 0.754152, 55.008339]`
- **Topic category:** transportation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_national_highways`
- **Table:** `air_quality_annual_evaluation_report`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 256
- **Columns:** 16
- **Metadata status:** source_mapped

## Description

Air Quality Annual Evaluation Report is an authoritative dataset published by National Highways. It represents air quality annual evaluation report features using multilinestring geometry.

## Lineage

Published by National Highways as open roads data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `objectid` | `smallint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `pcm_link_i` | `integer` |  |
| `road_name` | `varchar` | Name associated with the represented feature. |
| `road_descr` | `varchar` |  |
| `qf_within_` | `varchar` |  |
| `no2_conc` | `varchar` |  |
| `annual_eva` | `varchar` |  |
| `annual_e_1` | `varchar` |  |
| `local_no2_` | `varchar` |  |
| `datasets_r` | `varchar` |  |
| `aer_based_` | `varchar` |  |
| `commentary` | `varchar` |  |
| `view_techn` | `varchar` |  |
| `year` | `smallint` |  |
| `globalid` | `varchar` | UUID-formatted identifier associated with the record; persistence across releases is not confirmed. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
