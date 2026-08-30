# Qgis Projects

## Overview

- **Identifier:** `a_national_lidar_programme/qgis_projects`
- **Source organisation:** Environment Agency
- **Product:** National LIDAR Programme
- **Source:** https://www.data.gov.uk/dataset/f0db0249-f17b-4036-9e65-309148c97ce4/national-lidar-programme
- **Geographic coverage:** England
- **Schema:** `a_national_lidar_programme`
- **Table:** `qgis_projects`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1
- **Columns:** 3
- **Metadata status:** source_mapped

## Description

Qgis Projects is part of National LIDAR Programme, published by Environment Agency. It contains records relating to qgis projects.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `name` | `text` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `metadata` | `jsonb` | Publisher-supplied metadata for the represented feature or record. | source_attribute | Yes | No | No |
| `content` | `bytea` | Publisher-supplied content for the represented feature or record. | source_attribute | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
