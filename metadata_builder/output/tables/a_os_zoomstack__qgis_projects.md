# Qgis Projects

## Overview

- **Identifier:** `a_os_zoomstack/qgis_projects`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Zoomstack
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-zoomstack
- **Schema:** `a_os_zoomstack`
- **Table:** `qgis_projects`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1
- **Metadata status:** source_mapped

## Description

Qgis Projects is part of OS Open Zoomstack, published by Ordnance Survey. It contains records relating to qgis projects.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `name` | `text` | Name of the represented feature. | feature_name | Yes | Yes | No |
| `metadata` | `jsonb` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `content` | `bytea` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
