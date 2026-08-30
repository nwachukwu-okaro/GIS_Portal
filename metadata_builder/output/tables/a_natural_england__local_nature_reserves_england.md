# Local Nature Reserves England

## Overview

- **Identifier:** `a_natural_england/local_nature_reserves_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Local dataset version:** 20251009 (9 October 2025)
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.484388, 50.140759, 1.757926, 55.348825]`
- **Schema:** `a_natural_england`
- **Table:** `local_nature_reserves_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1710
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Version: 20251009
Source: https://www.data.gov.uk/dataset/acdf4a9e-a115-41fb-bbe9-603c819aa7f7/local-nature-reserves-england1

Attribution: © Natural England copyright. Contains Ordnance Survey data © Crown copyright and database right [year]. NB This national dataset is “indicative” not “definitive”. Definitive information can only be provided by individual local authorities and you should refer directly to their information for all purposes that require the most up to date and complete dataset.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `ref_code` | `varchar(10)` | Code assigned by the source dataset. | code | Yes | No | No |
| `name` | `varchar(120)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `measure` | `double precision` | Count or numeric value for measure in the represented area. | statistical_value | Yes | No | No |
| `label` | `varchar(140)` | Publisher-supplied label for the represented feature or record. | source_attribute | Yes | No | No |
| `globalid` | `varchar(38)` | Publisher-assigned globalid for the record. | source_identifier | Yes | No | No |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
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
