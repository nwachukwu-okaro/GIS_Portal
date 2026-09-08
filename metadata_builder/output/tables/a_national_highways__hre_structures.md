# Hre Structures

## Overview

- **Identifier:** `a_national_highways/hre_structures`
- **Source organisation:** National Highways
- **Source:** https://developer.data.nationalhighways.co.uk/
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.422375, 50.114472, 1.748077, 57.678794]`
- **Topic category:** transportation
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_national_highways`
- **Table:** `hre_structures`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 3287
- **Columns:** 4
- **Metadata status:** source_mapped

## Description

Hre Structures is an authoritative dataset published by National Highways. It represents hre structures features using multipolygon geometry.

## Lineage

Published by National Highways as open roads data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `fid` | `smallint` | Feature identifier assigned by the source or import process. |
| `long_descr` | `varchar` | Publisher-supplied long descr for the represented feature or record. |
| `globalid` | `varchar` | Publisher-assigned globalid for the record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
