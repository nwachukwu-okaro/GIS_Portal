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
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
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
| `pcm_link_i` | `integer` | Count or numeric value for pcm link i in the represented area. |
| `road_name` | `varchar` | Name associated with the represented feature. |
| `road_descr` | `varchar` | Publisher-supplied road descr for the represented feature or record. |
| `qf_within_` | `varchar` | Publisher-supplied qf within for the represented feature or record. |
| `no2_conc` | `varchar` | Publisher-supplied no2 conc for the represented feature or record. |
| `annual_eva` | `varchar` | Publisher-supplied annual eva for the represented feature or record. |
| `annual_e_1` | `varchar` | Publisher-supplied annual e 1 for the represented feature or record. |
| `local_no2_` | `varchar` | Publisher-supplied local no2 for the represented feature or record. |
| `datasets_r` | `varchar` | Publisher-supplied datasets r for the represented feature or record. |
| `aer_based_` | `varchar` | Publisher-supplied aer based for the represented feature or record. |
| `commentary` | `varchar` | Publisher-supplied commentary for the represented feature or record. |
| `view_techn` | `varchar` | Publisher-supplied view techn for the represented feature or record. |
| `year` | `smallint` | Count or numeric value for year in the represented area. |
| `globalid` | `varchar` | Publisher-assigned globalid for the record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
