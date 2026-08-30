# National Inventory Of Architectural Inventory

## Overview

- **Identifier:** `a_irl_national_built_heritage_service/national_inventory_of_architectural_inventory`
- **Source organisation:** National Built Heritage Service
- **Source:** https://www.buildingsofireland.ie/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.514248, 51.413382, 169.323852, 78.263859]`
- **Schema:** `a_irl_national_built_heritage_service`
- **Table:** `national_inventory_of_architectural_inventory`
- **Geometry:** POINT
- **CRS:** EPSG:2157
- **Rows:** 43322
- **Columns:** 22
- **Metadata status:** source_mapped

## Description

National Inventory Of Architectural Inventory is an authoritative dataset published by National Built Heritage Service. It represents national inventory of architectural inventory features using point geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `reg_no` | `bigint` | Count or numeric value for reg number in the represented area. | statistical_value | Yes | No | No |
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `number` | `varchar` | Publisher-supplied number for the represented feature or record. | source_attribute | Yes | No | No |
| `street1` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `street2` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `town` | `varchar` | Publisher-supplied town for the represented feature or record. | source_attribute | Yes | No | No |
| `townland` | `varchar` | Publisher-supplied townland for the represented feature or record. | source_attribute | Yes | No | No |
| `county` | `varchar` | Publisher-supplied county for the represented feature or record. | source_attribute | Yes | No | No |
| `county_id` | `varchar` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `planauth` | `varchar` | Publisher-supplied planauth for the represented feature or record. | source_attribute | Yes | No | No |
| `composition` | `varchar` | Publisher-supplied composition for the represented feature or record. | source_attribute | Yes | No | No |
| `appraisal` | `varchar` | Publisher-supplied appraisal for the represented feature or record. | source_attribute | Yes | No | No |
| `datefrom` | `bigint` | Count or numeric value for datefrom in the represented area. | statistical_value | Yes | No | No |
| `dateto` | `bigint` | Count or numeric value for dateto in the represented area. | statistical_value | Yes | No | No |
| `rating` | `varchar` | Publisher-supplied rating for the represented feature or record. | source_attribute | Yes | No | No |
| `original_type` | `varchar` | Publisher-supplied original type for the represented feature or record. | source_attribute | Yes | No | No |
| `image_link` | `varchar` | Publisher-supplied image link for the represented feature or record. | source_attribute | Yes | No | No |
| `website_link` | `varchar` | Publisher-supplied website link for the represented feature or record. | source_attribute | Yes | No | No |
| `survey_id` | `varchar` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `niah_area` | `varchar` | Publisher-supplied niah area for the represented feature or record. | source_attribute | Yes | No | No |
| `niah_pk` | `integer` | Count or numeric value for niah pk in the represented area. | statistical_value | Yes | No | No |
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

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
