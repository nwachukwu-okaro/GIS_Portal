# An Bord Pleanala Cases 2016 Onwards

## Overview

- **Identifier:** `a_irl_department_of_housing_lg_heritage/an_bord_pleanala_cases_2016_onwards`
- **Source organisation:** Department of Housing, Local Government and Heritage
- **Source:** https://www.gov.ie/en/organisation/department-of-housing-local-government-and-heritage/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.462590, 51.466604, -6.004298, 55.330960]`
- **Topic category:** boundaries
- **Temporal extent:** 2024-05-22T00:00:00 to 2024-05-22T00:00:00
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_department_of_housing_lg_heritage`
- **Table:** `an_bord_pleanala_cases_2016_onwards`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 20903
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

An Bord Pleanala Cases 2016 Onwards is an authoritative dataset published by Department of Housing, Local Government and Heritage. It represents an bord pleanala cases 2016 onwards features using multipolygon geometry.

## Lineage

Published by the Department of Housing, Local Government and Heritage as open data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `pc_pk` | `integer` | Count or numeric value for pc pk in the represented area. |
| `abpcaseid` | `varchar(6)` | Publisher-assigned abpcaseid for the record. |
| `devdesc` | `varchar(254)` | Publisher-supplied devdesc for the represented feature or record. |
| `devaddress` | `varchar(250)` | Publisher-supplied devaddress for the represented feature or record. |
| `lodgedon` | `timestamp` | Publisher-supplied lodgedon for the represented feature or record. |
| `decision` | `varchar(140)` | Publisher-supplied decision for the represented feature or record. |
| `decided_on` | `timestamp` | Publisher-supplied decided on for the represented feature or record. |
| `linkabpweb` | `varchar(41)` | Publisher-supplied linkabpweb for the represented feature or record. |
| `planingaty` | `varchar(39)` | Publisher-supplied planingaty for the represented feature or record. |
| `category` | `varchar(28)` | Publisher-supplied category for the represented feature or record. |
| `updated_on` | `timestamp` | Publisher-supplied updated on for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
