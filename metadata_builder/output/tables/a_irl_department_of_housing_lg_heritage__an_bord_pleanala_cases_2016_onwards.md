# An Bord Pleanala Cases 2016 Onwards

## Overview

- **Identifier:** `a_irl_department_of_housing_lg_heritage/an_bord_pleanala_cases_2016_onwards`
- **Source organisation:** Department of Housing, Local Government and Heritage
- **Source:** https://www.gov.ie/en/organisation/department-of-housing-local-government-and-heritage/
- **Schema:** `a_irl_department_of_housing_lg_heritage`
- **Table:** `an_bord_pleanala_cases_2016_onwards`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 20903
- **Metadata status:** source_mapped

## Description

An Bord Pleanala Cases 2016 Onwards is an authoritative dataset published by Department of Housing, Local Government and Heritage. It represents an bord pleanala cases 2016 onwards features using multipolygon geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `pc_pk` | `integer` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `abpcaseid` | `varchar(6)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `devdesc` | `varchar(254)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `devaddress` | `varchar(250)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `lodgedon` | `timestamp` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `decision` | `varchar(140)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `decided_on` | `timestamp` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `linkabpweb` | `varchar(41)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `planingaty` | `varchar(39)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `category` | `varchar(28)` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `updated_on` | `timestamp` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
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
