# Licensed Historic Landfills

## Overview

- **Identifier:** `a_irl_environmental_protection_agency/licensed_historic_landfills`
- **Source organisation:** Environmental Protection Agency Ireland
- **Source:** https://gis.epa.ie/GetData/Download
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-9.484703, 51.737883, -6.143093, 54.283527]`
- **Topic category:** environment
- **Temporal extent:** 2009-05-11T00:00:00 to 2020-10-09T00:00:00
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_environmental_protection_agency`
- **Table:** `licensed_historic_landfills`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29903
- **Rows:** 25
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Licensed Historic Landfills is an authoritative dataset published by Environmental Protection Agency Ireland. It represents licensed historic landfills features using multipolygon geometry.

## Lineage

Published by the Environmental Protection Agency Ireland as open environmental data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `registration_code` | `varchar(10)` | Code assigned by the source dataset. |
| `certificate_of_authorisation_holder` | `varchar(254)` | Publisher-supplied certificate of authorisation holder for the represented feature or record. |
| `name_and_location_of_facility` | `varchar(254)` | Publisher-supplied name and location of facility for the represented feature or record. |
| `certificate_of_authorisation_status` | `varchar(254)` | Publisher-supplied certificate of authorisation status for the represented feature or record. |
| `application_date` | `timestamp` | Date associated with the represented feature or source record. |
| `certificate_of_authorisation_issue_date` | `timestamp` | Date associated with the represented feature or source record. |
| `estimated_landfilled_tonnage_tonnes` | `double precision` | Count or numeric value for estimated landfilled tonnage tonnes in the represented area. |
| `estimated_dates_of_operation` | `varchar(254)` | Publisher-supplied estimated dates of operation for the represented feature or record. |
| `estimated_landfilled_volume_metres_cubed` | `double precision` | Count or numeric value for estimated landfilled volume metres cubed in the represented area. |
| `facility_type` | `varchar(254)` | Publisher-supplied facility type for the represented feature or record. |
| `lhl_pk` | `bigint` | Count or numeric value for lhl pk in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
