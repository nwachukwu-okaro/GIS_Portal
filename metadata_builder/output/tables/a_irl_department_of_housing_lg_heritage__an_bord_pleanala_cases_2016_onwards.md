# An Bord Pleanala Cases 2016 Onwards

## Overview

- **Identifier:** `a_irl_department_of_housing_lg_heritage/an_bord_pleanala_cases_2016_onwards`
- **Source organisation:** Department of Housing, Local Government and Heritage
- **Source:** https://www.gov.ie/en/organisation/department-of-housing-local-government-and-heritage/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.462590, 51.466604, -6.004298, 55.330960]`
- **Schema:** `a_irl_department_of_housing_lg_heritage`
- **Table:** `an_bord_pleanala_cases_2016_onwards`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 20903
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

An Bord Pleanala Cases 2016 Onwards is an authoritative dataset published by Department of Housing, Local Government and Heritage. It represents an bord pleanala cases 2016 onwards features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `pc_pk` | `integer` | Count or numeric value for pc pk in the represented area. | statistical_value | Yes | No | No |
| `abpcaseid` | `varchar(6)` | Publisher-assigned abpcaseid for the record. | source_identifier | Yes | No | No |
| `devdesc` | `varchar(254)` | Publisher-supplied devdesc for the represented feature or record. | source_attribute | Yes | No | No |
| `devaddress` | `varchar(250)` | Publisher-supplied devaddress for the represented feature or record. | source_attribute | Yes | No | No |
| `lodgedon` | `timestamp` | Publisher-supplied lodgedon for the represented feature or record. | source_attribute | Yes | No | No |
| `decision` | `varchar(140)` | Publisher-supplied decision for the represented feature or record. | source_attribute | Yes | No | No |
| `decided_on` | `timestamp` | Publisher-supplied decided on for the represented feature or record. | source_attribute | Yes | No | No |
| `linkabpweb` | `varchar(41)` | Publisher-supplied linkabpweb for the represented feature or record. | source_attribute | Yes | No | No |
| `planingaty` | `varchar(39)` | Publisher-supplied planingaty for the represented feature or record. | source_attribute | Yes | No | No |
| `category` | `varchar(28)` | Publisher-supplied category for the represented feature or record. | source_attribute | Yes | No | No |
| `updated_on` | `timestamp` | Publisher-supplied updated on for the represented feature or record. | source_attribute | Yes | No | No |
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
