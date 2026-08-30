# Qgis Projects

## Overview

- **Identifier:** `a_os_open_map_local/qgis_projects`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Map Local
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-map-local
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **Schema:** `a_os_open_map_local`
- **Table:** `qgis_projects`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1
- **Columns:** 3
- **Metadata status:** source_mapped

## Description

Qgis Projects is part of OS Open Map Local, published by Ordnance Survey. It contains records relating to qgis projects.

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

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
