# Licensed Historic Landfills

## Overview

- **Identifier:** `a_irl_environmental_protection_agency/licensed_historic_landfills`
- **Source organisation:** Environmental Protection Agency Ireland
- **Source:** https://gis.epa.ie/GetData/Download
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-9.484703, 51.737883, -6.143093, 54.283527]`
- **Schema:** `a_irl_environmental_protection_agency`
- **Table:** `licensed_historic_landfills`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:29903
- **Rows:** 25
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Licensed Historic Landfills is an authoritative dataset published by Environmental Protection Agency Ireland. It represents licensed historic landfills features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `registration_code` | `varchar(10)` | Code assigned by the source dataset. | code | Yes | No | No |
| `certificate_of_authorisation_holder` | `varchar(254)` | Publisher-supplied certificate of authorisation holder for the represented feature or record. | source_attribute | Yes | No | No |
| `name_and_location_of_facility` | `varchar(254)` | Publisher-supplied name and location of facility for the represented feature or record. | source_attribute | Yes | No | No |
| `certificate_of_authorisation_status` | `varchar(254)` | Publisher-supplied certificate of authorisation status for the represented feature or record. | source_attribute | Yes | No | No |
| `application_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `certificate_of_authorisation_issue_date` | `timestamp` | Date associated with the represented feature or source record. | date | Yes | No | No |
| `estimated_landfilled_tonnage_tonnes` | `double precision` | Count or numeric value for estimated landfilled tonnage tonnes in the represented area. | statistical_value | Yes | No | No |
| `estimated_dates_of_operation` | `varchar(254)` | Publisher-supplied estimated dates of operation for the represented feature or record. | source_attribute | Yes | No | No |
| `estimated_landfilled_volume_metres_cubed` | `double precision` | Count or numeric value for estimated landfilled volume metres cubed in the represented area. | statistical_value | Yes | No | No |
| `facility_type` | `varchar(254)` | Publisher-supplied facility type for the represented feature or record. | source_attribute | Yes | No | No |
| `lhl_pk` | `bigint` | Count or numeric value for lhl pk in the represented area. | statistical_value | Yes | No | No |
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
