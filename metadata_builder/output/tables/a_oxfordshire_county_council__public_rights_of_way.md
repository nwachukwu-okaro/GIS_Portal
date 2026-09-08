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
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
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
| `legal_typed` | `varchar` | Publisher-supplied legal typed for the represented feature or record. |
| `status_description` | `varchar` | Publisher-supplied status description for the represented feature or record. |
| `route_number` | `varchar` | Publisher-supplied route number for the represented feature or record. |
| `parish_code` | `varchar` | Code assigned by the source dataset. |
| `route_code` | `varchar` | Code assigned by the source dataset. |
| `parish_name` | `varchar` | Name associated with the represented feature. |
| `status` | `varchar` | Publisher-supplied status for the represented feature or record. |
| `legal_type` | `varchar` | Publisher-supplied legal type for the represented feature or record. |
| `length_m` | `double precision` | Numeric length male value recorded for the feature. |
| `easting` | `double precision` | Easting coordinate in metres in the dataset's projected coordinate reference system. |
| `northing` | `double precision` | Northing coordinate in metres in the dataset's projected coordinate reference system. |
| `easting_end` | `double precision` | Numeric easting end value recorded for the feature. |
| `northing_end` | `double precision` | Numeric northing end value recorded for the feature. |
| `easting_start` | `double precision` | Numeric easting start value recorded for the feature. |
| `northing_start` | `double precision` | Numeric northing start value recorded for the feature. |
| `oprow_pk` | `integer` | Count or numeric value for oprow pk in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
