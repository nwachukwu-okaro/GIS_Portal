# Air Quality Sites

## Overview

- **Identifier:** `a_irl_environmental_protection_agency/air_quality_sites`
- **Source organisation:** Environmental Protection Agency Ireland
- **Source:** https://gis.epa.ie/GetData/Download
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.240986, 51.855000, -6.122076, 55.358472]`
- **Schema:** `a_irl_environmental_protection_agency`
- **Table:** `air_quality_sites`
- **Geometry:** POINT
- **CRS:** EPSG:29902
- **Rows:** 43
- **Columns:** 24
- **Metadata status:** source_mapped

## Description

Air Quality Sites is an authoritative dataset published by Environmental Protection Agency Ireland. It represents air quality sites features using point geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `aqih_pk` | `integer` | Count or numeric value for aqih pk in the represented area. | statistical_value | Yes | No | No |
| `name` | `varchar(254)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `code` | `varchar(254)` | Publisher-assigned code for the record. | source_identifier | Yes | No | No |
| `location` | `varchar(254)` | Publisher-supplied location for the represented feature or record. | source_attribute | Yes | No | No |
| `status` | `varchar(254)` | Publisher-supplied status for the represented feature or record. | source_attribute | Yes | No | No |
| `url` | `varchar(254)` | Publisher-supplied url for the represented feature or record. | source_attribute | Yes | No | No |
| `easting` | `double precision` | Easting coordinate in metres in the dataset's projected coordinate reference system. | x_coordinate | Yes | No | No |
| `northing` | `double precision` | Northing coordinate in metres in the dataset's projected coordinate reference system. | y_coordinate | Yes | No | No |
| `address1` | `varchar(254)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `address2` | `varchar(254)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `region` | `varchar(20)` | Publisher-supplied region for the represented feature or record. | source_attribute | Yes | No | No |
| `coverage` | `varchar(254)` | Publisher-supplied coverage for the represented feature or record. | source_attribute | Yes | No | No |
| `operator` | `varchar(254)` | Publisher-supplied operator for the represented feature or record. | source_attribute | Yes | No | No |
| `eio_net_code` | `varchar(20)` | Code assigned by the source dataset. | code | Yes | No | No |
| `para_1` | `varchar(254)` | Publisher-supplied para 1 for the represented feature or record. | source_attribute | Yes | No | No |
| `para_2` | `varchar(254)` | Publisher-supplied para 2 for the represented feature or record. | source_attribute | Yes | No | No |
| `para_3` | `varchar(254)` | Publisher-supplied para 3 for the represented feature or record. | source_attribute | Yes | No | No |
| `para_4` | `varchar(254)` | Publisher-supplied para 4 for the represented feature or record. | source_attribute | Yes | No | No |
| `para_5` | `varchar(254)` | Publisher-supplied para 5 for the represented feature or record. | source_attribute | Yes | No | No |
| `para_6` | `varchar(254)` | Publisher-supplied para 6 for the represented feature or record. | source_attribute | Yes | No | No |
| `para_7` | `varchar(254)` | Publisher-supplied para 7 for the represented feature or record. | source_attribute | Yes | No | No |
| `para_8` | `varchar(254)` | Publisher-supplied para 8 for the represented feature or record. | source_attribute | Yes | No | No |
| `operational` | `integer` | Count or numeric value for operational in the represented area. | statistical_value | Yes | No | No |
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
