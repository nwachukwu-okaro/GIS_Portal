# Qgis Projects

## Overview

- **Identifier:** `a_national_lidar_programme/qgis_projects`
- **Source organisation:** Environment Agency
- **Product:** National LIDAR Programme
- **Source:** https://www.data.gov.uk/dataset/f0db0249-f17b-4036-9e65-309148c97ce4/national-lidar-programme
- **Geographic coverage:** England
- **Topic category:** elevation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_national_lidar_programme`
- **Table:** `qgis_projects`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1
- **Columns:** 3
- **Metadata status:** source_mapped

## Description

Qgis Projects is part of National LIDAR Programme, published by Environment Agency. It contains records relating to qgis projects.

## Lineage

Published by Environment Agency as part of the National LIDAR Programme. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `name` | `text` | Official or publisher-assigned name of the represented feature. |
| `metadata` | `jsonb` | Publisher-supplied metadata for the represented feature or record. |
| `content` | `bytea` | Publisher-supplied content for the represented feature or record. |
