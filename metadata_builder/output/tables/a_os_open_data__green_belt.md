# Green Belt

## Overview

- **Identifier:** `a_os_open_data/green_belt`
- **Source organisation:** Ordnance Survey
- **Product:** OS OpenData
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-data
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-3.199715, 50.679562, 0.866302, 55.274430]`
- **Schema:** `a_os_open_data`
- **Table:** `green_belt`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 190
- **Columns:** 15
- **Metadata status:** source_mapped

## Description

Green Belt is part of OS OpenData, published by Ordnance Survey. It represents green belt features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. | statistical_value | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |
| `dataset` | `varchar` | Publisher-supplied dataset for the represented feature or record. | source_attribute | Yes | No | No |
| `end-date` | `varchar` | Date or year recorded for end date. | date | Yes | No | No |
| `entity` | `varchar` | Publisher-supplied entity for the represented feature or record. | source_attribute | Yes | No | No |
| `entry-date` | `date` | Date or year recorded for entry date. | date | Yes | No | No |
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `organisation-entity` | `varchar` | Publisher-supplied organisation entity for the represented feature or record. | source_attribute | Yes | No | No |
| `prefix` | `varchar` | Publisher-supplied prefix for the represented feature or record. | source_attribute | Yes | No | No |
| `quality` | `varchar` | Publisher-supplied quality for the represented feature or record. | source_attribute | Yes | No | No |
| `reference` | `varchar` | Publisher-supplied reference for the represented feature or record. | source_attribute | Yes | No | No |
| `start-date` | `varchar` | Date or year recorded for start date. | date | Yes | No | No |
| `typology` | `varchar` | Publisher-supplied typology for the represented feature or record. | source_attribute | Yes | No | No |
| `green-belt-core` | `varchar` | Publisher-supplied green belt core for the represented feature or record. | source_attribute | Yes | No | No |
| `local-authority-district` | `varchar` | Publisher-supplied local authority district for the represented feature or record. | source_attribute | Yes | No | No |

## Supported operations

- filter
- select
- reproject
- validate_geometry
- buffer
- clip
- intersect
- spatial_join
- export

## Operation requirements

- Intersect, clip and spatial-join inputs must use matching coordinate reference systems.
- Buffer operations require a suitable projected coordinate reference system.
- Reprojection is performed on working outputs; source tables remain unchanged.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
