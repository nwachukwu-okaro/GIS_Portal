# An Bord Pleanala Strategic Housing Developments 2017 2022

## Overview

- **Identifier:** `a_irl_department_of_housing_lg_heritage/an_bord_pleanala_strategic_housing_developments_2017_2022`
- **Source organisation:** Department of Housing, Local Government and Heritage
- **Source:** https://www.gov.ie/en/organisation/department-of-housing-local-government-and-heritage/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-9.521917, 51.811537, -6.059705, 53.997486]`
- **Topic category:** boundaries
- **Temporal extent:** 2024-06-21T00:00:00 to 2024-06-21T00:00:00
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_department_of_housing_lg_heritage`
- **Table:** `an_bord_pleanala_strategic_housing_developments_2017_2022`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 528
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

An Bord Pleanala Strategic Housing Developments 2017 2022 is an authoritative dataset published by Department of Housing, Local Government and Heritage. It represents an bord pleanala strategic housing developments 2017 2022 features using multipolygon geometry.

## Lineage

Published by the Department of Housing, Local Government and Heritage as open data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `shd_pk` | `integer` | Primary-key identifier for records in an_bord_pleanala_strategic_housing_developments_2017_2022. |
| `abpcaseid` | `varchar(6)` |  |
| `devdesc` | `varchar(254)` |  |
| `devaddress` | `varchar(254)` |  |
| `lodgedon` | `timestamp` |  |
| `decision` | `varchar(39)` |  |
| `decided_on` | `timestamp` |  |
| `linkabpweb` | `varchar(41)` |  |
| `planingaty` | `varchar(37)` |  |
| `category` | `varchar(21)` |  |
| `updated_on` | `timestamp` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
