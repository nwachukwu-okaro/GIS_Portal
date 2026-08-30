# Blue Green Infra Heat Mitigation Lsoa Ogl

## Overview

- **Identifier:** `a_natural_england/blue_green_infra_Heat_Mitigation_LSOA_OGL`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.418942, 49.864636, 1.768912, 55.811660]`
- **Schema:** `a_natural_england`
- **Table:** `blue_green_infra_Heat_Mitigation_LSOA_OGL`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 32844
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Blue Green Infra Heat Mitigation Lsoa Ogl is an authoritative dataset published by Natural England. It represents blue green infra heat mitigation lsoa ogl features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
| `code` | `varchar(9)` | Count or numeric value for code in the represented area. | statistical_value | Yes | No | No |
| `name` | `varchar(254)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `label` | `varchar(36)` | Publisher-supplied label for the represented feature or record. | source_attribute | Yes | No | No |
| `area` | `integer` | Numeric area value recorded for the feature. | measure | Yes | No | No |
| `mean` | `double precision` | Count or numeric value for mean in the represented area. | statistical_value | Yes | No | No |
| `provision` | `double precision` | Count or numeric value for provision in the represented area. | statistical_value | Yes | No | No |
| `need` | `double precision` | Count or numeric value for need in the represented area. | statistical_value | Yes | No | No |
| `lackprov` | `double precision` | Count or numeric value for lackprov in the represented area. | statistical_value | Yes | No | No |
| `zpriority` | `double precision` | Count or numeric value for zpriority in the represented area. | statistical_value | Yes | No | No |
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
