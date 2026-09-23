# Public Rights Of Way

## Overview

- **Identifier:** `a_oxfordshire_county_council/public_rights_of_way`
- **Source organisation:** Oxfordshire County Council
- **Source:** https://insight.oxfordshire.gov.uk/cms/open-data
- **Geographic coverage:** Oxfordshire
- **WGS84 extent:** `[-1.719517, 51.473502, -0.870555, 52.157764]`
- **Topic category:** planningCadastre
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_oxfordshire_county_council`
- **Table:** `public_rights_of_way`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:4326
- **Rows:** 10469
- **Columns:** 17
- **Metadata status:** source_mapped

## Description

Public Rights Of Way is an authoritative dataset published by Oxfordshire County Council. It represents public rights of way features using multilinestring geometry.

## Lineage

Published by Oxfordshire County Council as open local government data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `legal_typed` | `varchar` |  |
| `status_description` | `varchar` |  |
| `route_number` | `varchar` |  |
| `parish_code` | `varchar` | Code assigned by the source dataset. |
| `route_code` | `varchar` | Code assigned by the source dataset. |
| `parish_name` | `varchar` | Name associated with the represented feature. |
| `status` | `varchar` |  |
| `legal_type` | `varchar` |  |
| `length_m` | `double precision` |  |
| `easting` | `double precision` | Easting coordinate in metres in the dataset's projected coordinate reference system. |
| `northing` | `double precision` | Northing coordinate in metres in the dataset's projected coordinate reference system. |
| `easting_end` | `double precision` |  |
| `northing_end` | `double precision` |  |
| `easting_start` | `double precision` |  |
| `northing_start` | `double precision` |  |
| `oprow_pk` | `integer` | Primary-key identifier for records in public_rights_of_way. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
