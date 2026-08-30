# Places

## Overview

- **Identifier:** `a_overture_maps/places`
- **Source organisation:** Overture Maps Foundation
- **Product:** Overture Maps
- **Source:** https://docs.overturemaps.org/
- **Geographic coverage:** Global
- **WGS84 extent:** `[-10.656273, 49.300012, 2.880000, 63.233627]`
- **Schema:** `a_overture_maps`
- **Table:** `places`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:4326
- **Rows:** 3507636
- **Columns:** 14
- **Metadata status:** source_mapped

## Description

Places is part of Overture Maps, published by Overture Maps Foundation. It represents places features using multipoint geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `varchar` | Publisher-assigned identifier for the record. | source_identifier | Yes | No | No |
| `categories.primary` | `varchar` | Publisher-supplied categories primary for the represented feature or record. | source_attribute | Yes | No | No |
| `confidence` | `double precision` | Count or numeric value for confidence in the represented area. | statistical_value | Yes | No | No |
| `brand.wikidata` | `varchar` | Publisher-supplied brand wikidata for the represented feature or record. | source_attribute | Yes | No | No |
| `brand.names.primary` | `varchar` | Publisher-supplied brand names primary for the represented feature or record. | source_attribute | Yes | No | No |
| `names.primary` | `varchar` | Publisher-supplied names primary for the represented feature or record. | source_attribute | Yes | No | No |
| `basic_category` | `varchar` | Publisher-supplied basic category for the represented feature or record. | source_attribute | Yes | No | No |
| `taxonomy.primary` | `varchar` | Publisher-supplied taxonomy primary for the represented feature or record. | source_attribute | Yes | No | No |
| `version` | `integer` | Count or numeric value for version in the represented area. | statistical_value | Yes | No | No |
| `filename` | `varchar` | Publisher-supplied filename for the represented feature or record. | source_attribute | Yes | No | No |
| `theme` | `varchar` | Publisher-supplied theme for the represented feature or record. | source_attribute | Yes | No | No |
| `type` | `varchar` | Publisher-supplied type for the represented feature or record. | source_attribute | Yes | No | No |
| `addresses` | `json` | Publisher-supplied addresses for the represented feature or record. | source_attribute | Yes | No | No |
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
