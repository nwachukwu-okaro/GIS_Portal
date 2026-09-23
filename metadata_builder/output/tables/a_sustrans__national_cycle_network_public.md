# National Cycle Network Public

## Overview

- **Identifier:** `a_sustrans/national_cycle_network_public`
- **Source organisation:** Sustrans
- **Source:** https://data.sustrans.org.uk/
- **Geographic coverage:** United Kingdom
- **WGS84 extent:** `[-7.650111, 50.062727, 1.762548, 57.817561]`
- **Topic category:** transportation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_sustrans`
- **Table:** `national_cycle_network_public`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 37210
- **Columns:** 15
- **Metadata status:** source_mapped

## Description

National Cycle Network Public is an authoritative dataset published by Sustrans. It represents national cycle network public features using multilinestring geometry.

## Lineage

Published by Sustrans as open active travel data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `desc_` | `text` |  |
| `greenway` | `text` |  |
| `routetype` | `text` |  |
| `routeno` | `integer` |  |
| `linkno` | `integer` |  |
| `routecat` | `text` |  |
| `openstatus` | `text` |  |
| `surface` | `text` |  |
| `quality` | `text` |  |
| `lighting` | `text` |  |
| `roadclass` | `text` |  |
| `globalid` | `text` | UUID-formatted identifier associated with the record; persistence across releases is not confirmed. |
| `segmentid` | `integer` |  |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
