# An Bord Pleanala Strategic Housing Developments 2017 2022

## Overview

- **Identifier:** `a_irl_department_of_housing_lg_heritage/an_bord_pleanala_strategic_housing_developments_2017_2022`
- **Source organisation:** Department of Housing, Local Government and Heritage
- **Source:** https://www.gov.ie/en/organisation/department-of-housing-local-government-and-heritage/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-9.521917, 51.811537, -6.059705, 53.997486]`
- **Schema:** `a_irl_department_of_housing_lg_heritage`
- **Table:** `an_bord_pleanala_strategic_housing_developments_2017_2022`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 528
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

An Bord Pleanala Strategic Housing Developments 2017 2022 is an authoritative dataset published by Department of Housing, Local Government and Heritage. It represents an bord pleanala strategic housing developments 2017 2022 features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `shd_pk` | `integer` | Count or numeric value for shd pk in the represented area. | statistical_value | Yes | No | No |
| `abpcaseid` | `varchar(6)` | Publisher-assigned abpcaseid for the record. | source_identifier | Yes | No | No |
| `devdesc` | `varchar(254)` | Publisher-supplied devdesc for the represented feature or record. | source_attribute | Yes | No | No |
| `devaddress` | `varchar(254)` | Publisher-supplied devaddress for the represented feature or record. | source_attribute | Yes | No | No |
| `lodgedon` | `timestamp` | Publisher-supplied lodgedon for the represented feature or record. | source_attribute | Yes | No | No |
| `decision` | `varchar(39)` | Publisher-supplied decision for the represented feature or record. | source_attribute | Yes | No | No |
| `decided_on` | `timestamp` | Publisher-supplied decided on for the represented feature or record. | source_attribute | Yes | No | No |
| `linkabpweb` | `varchar(41)` | Publisher-supplied linkabpweb for the represented feature or record. | source_attribute | Yes | No | No |
| `planingaty` | `varchar(37)` | Publisher-supplied planingaty for the represented feature or record. | source_attribute | Yes | No | No |
| `category` | `varchar(21)` | Publisher-supplied category for the represented feature or record. | source_attribute | Yes | No | No |
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
