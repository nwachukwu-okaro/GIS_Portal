# Metrolink Park And Ride

## Overview

- **Identifier:** `a_tfgm/metrolink_park_and_ride`
- **Source organisation:** Transport for Greater Manchester
- **Source:** https://developer.tfgm.com/
- **Geographic coverage:** Greater Manchester
- **WGS84 extent:** `[-2.719122, 53.358241, -1.948611, 53.643312]`
- **Topic category:** transportation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_tfgm`
- **Table:** `metrolink_park_and_ride`
- **Geometry:** POINT
- **CRS:** EPSG:27700
- **Rows:** 80
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Metrolink Park And Ride is an authoritative dataset published by Transport for Greater Manchester. It represents metrolink park and ride features using point geometry.

## Lineage

Published by Transport for Greater Manchester as open transport data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `park_and_ride_pk` | `integer` | Count or numeric value for park and ride pk in the represented area. |
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. |
| `stationcod` | `varchar` | Publisher-supplied stationcod for the represented feature or record. |
| `mode` | `varchar` | Publisher-supplied mode for the represented feature or record. |
| `spaces` | `integer` | Count or numeric value for spaces in the represented area. |
| `url` | `varchar` | Publisher-supplied url for the represented feature or record. |
| `uprn` | `bigint` | Count or numeric value for uprn in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
