# Variable Dictionary

## Overview

- **Identifier:** `a_ons_nrs_nirsa_census_data/variable_dictionary`
- **Source organisation:** UK national statistical authorities
- **Source:** https://www.ons.gov.uk/census
- **Geographic coverage:** United Kingdom
- **Schema:** `a_ons_nrs_nirsa_census_data`
- **Table:** `variable_dictionary`
- **Geometry:** GEOMETRY
- **CRS:** Not applicable or unknown
- **Rows:** 25
- **Columns:** 6
- **Metadata status:** source_mapped

## Description

Variable Dictionary is an authoritative dataset published by UK national statistical authorities. It represents variable dictionary features using geometry geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `table name` | `varchar(58)` | Publisher-supplied table name for the represented feature or record. | source_attribute | Yes | No | No |
| `uk table id` | `varchar(5)` | Publisher-assigned uk table identifier for the record. | source_identifier | Yes | No | No |
| `unit` | `varchar(9)` | Publisher-supplied unit for the represented feature or record. | source_attribute | Yes | No | No |
| `population scope` | `varchar(285)` | Publisher-supplied population scope for the represented feature or record. | source_attribute | Yes | No | No |
| `notes` | `varchar(957)` | Publisher-supplied notes for the represented feature or record. | source_attribute | Yes | No | No |
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
