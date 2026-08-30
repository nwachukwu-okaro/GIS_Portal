# Sites Of Special Scientific Interest England

## Overview

- **Identifier:** `a_natural_england/sites_of_special_scientific_interest_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Local dataset version:** 20251009 (9 October 2025)
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.418622, 49.863188, 1.753083, 55.811678]`
- **Schema:** `a_natural_england`
- **Table:** `sites_of_special_scientific_interest_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 4128
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

version: 20251009
Source: https://www.data.gov.uk/dataset/5b632bd7-9838-4ef2-9101-ea9384421b0d/sites-of-special-scientific-interest-england3

Attribution: © Natural England copyright. Contains Ordnance Survey data © Crown copyright and database right [year].

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `ref_code` | `varchar` | Code assigned by the source dataset. | code | Yes | No | No |
| `name` | `varchar` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `measure` | `real` | Count or numeric value for measure in the represented area. | statistical_value | Yes | No | No |
| `label` | `varchar` | Publisher-supplied label for the represented feature or record. | source_attribute | Yes | No | No |
| `hyperlink` | `varchar` | URL of the corresponding record on the publisher's website. | source_record_url | Yes | No | No |
| `contact_no` | `varchar` | Publisher-supplied contact number for the represented feature or record. | source_attribute | Yes | No | No |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. | identifier | Yes | No | No |
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

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
