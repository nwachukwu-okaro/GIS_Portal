# Metrolink Lines

## Overview

- **Identifier:** `a_tfgm/metrolink_lines`
- **Source organisation:** Transport for Greater Manchester
- **Source:** https://developer.tfgm.com/
- **Geographic coverage:** Greater Manchester
- **WGS84 extent:** `[-2.348224, 53.365168, -2.088039, 53.617382]`
- **Topic category:** transportation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_tfgm`
- **Table:** `metrolink_lines`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 20
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Metrolink Lines is an authoritative dataset published by Transport for Greater Manchester. It represents metrolink lines features using multilinestring geometry.

## Lineage

Published by Transport for Greater Manchester as open transport data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `tramline_pk` | `integer` | Primary-key identifier for records in metrolink_lines. |
| `description` | `varchar` |  |
| `type` | `varchar` |  |
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. |
| `validfrom` | `timestamp` | Date or time from which the record is considered valid. |
| `validto` | `timestamp` | Date or time until which the record is considered valid. |
| `currentstatus` | `varchar` |  |
| `comments` | `varchar` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
