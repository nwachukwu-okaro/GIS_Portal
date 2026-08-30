# Cycle Hubs 2022

## Overview

- **Identifier:** `a_tfgm/cycle_hubs_2022`
- **Source organisation:** Transport for Greater Manchester
- **Source:** https://developer.tfgm.com/
- **Schema:** `a_tfgm`
- **Table:** `cycle_hubs_2022`
- **Geometry:** POINT
- **CRS:** EPSG:27700
- **Rows:** 20
- **Metadata status:** source_mapped

## Description

version: 20220903
Source: https://www.data.gov.uk/dataset/e3236cd9-48c7-44c6-9c6e-efd76b67d8e5/gm-cycle-hubs

Attribution: Contains Transport for Greater Manchester data. Contains OS data © Crown copyright and database right 2022.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `hub_name` | `varchar(30)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `easting` | `bigint` | Easting coordinate in the dataset coordinate reference system. | x_coordinate | Yes | No | No |
| `northing` | `bigint` | Northing coordinate in the dataset coordinate reference system. | y_coordinate | Yes | No | No |
| `capacity` | `bigint` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `open_mon_f` | `varchar(20)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `open_sat` | `varchar(20)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `open_sun` | `varchar(20)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lockers` | `varchar(4)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `showers` | `varchar(4)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `membership` | `varchar(10)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `descriptio` | `varchar(200)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `district` | `varchar(10)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `hotlink` | `varchar(200)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `open` | `varchar(1)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |
| `cycle_hubs_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |

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
