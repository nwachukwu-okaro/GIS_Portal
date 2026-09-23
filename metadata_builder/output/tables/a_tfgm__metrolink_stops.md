# Metrolink Stops

## Overview

- **Identifier:** `a_tfgm/metrolink_stops`
- **Source organisation:** Transport for Greater Manchester
- **Source:** https://developer.tfgm.com/
- **Geographic coverage:** Greater Manchester
- **WGS84 extent:** `[-2.347795, 53.365343, -2.089550, 53.617318]`
- **Topic category:** transportation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_tfgm`
- **Table:** `metrolink_stops`
- **Geometry:** POINT
- **CRS:** EPSG:27700
- **Rows:** 99
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Metrolink Stops is an authoritative dataset published by Transport for Greater Manchester. It represents metrolink stops features using point geometry.

## Lineage

Published by Transport for Greater Manchester as open transport data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `stop_pk` | `integer` | Primary-key identifier for records in metrolink_stops. |
| `description` | `varchar` |  |
| `type` | `varchar` |  |
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. |
| `validfrom` | `timestamp` | Date or time from which the record is considered valid. |
| `validto` | `timestamp` | Date or time until which the record is considered valid. |
| `currentstatus` | `varchar` |  |
| `comments` | `varchar` |  |
| `stationcode` | `varchar` |  |
| `ticketzone` | `varchar` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
