# Blue Green Infra Air Quality Gm Lsoa Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_Air_Quality_GM_LSOA_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-2.730524, 53.327304, -1.909622, 53.685719]`
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_Air_Quality_GM_LSOA_OGL`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1673
- **Columns:** 16
- **Metadata status:** source_mapped

## Description

Blue Green Infra Air Quality Gm Lsoa Ogl is an authoritative dataset published by Natural England. It represents blue green infra air quality gm lsoa ogl features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
| `code` | `varchar(9)` | Count or numeric value for code in the represented area. | statistical_value | Yes | No | No |
| `name` | `varchar(254)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `provision` | `double precision` | Count or numeric value for provision in the represented area. | statistical_value | Yes | No | No |
| `need` | `double precision` | Count or numeric value for need in the represented area. | statistical_value | Yes | No | No |
| `lackprov` | `double precision` | Count or numeric value for lackprov in the represented area. | statistical_value | Yes | No | No |
| `zpriority` | `double precision` | Count or numeric value for zpriority in the represented area. | statistical_value | Yes | No | No |
| `sumpm25kg` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `areakm` | `double precision` | Numeric areakm value recorded for the feature. | measure | Yes | No | No |
| `pm25kgkm2` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `pm25ugm3` | `double precision` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `zscoreaqprov` | `double precision` | Count or numeric value for zscoreaqprov in the represented area. | statistical_value | Yes | No | No |
| `zaqneed` | `double precision` | Count or numeric value for zaqneed in the represented area. | statistical_value | Yes | No | No |
| `zsocneed` | `double precision` | Count or numeric value for zsocneed in the represented area. | statistical_value | Yes | No | No |
| `zneedcomb` | `double precision` | Count or numeric value for zneedcomb in the represented area. | statistical_value | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |

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
