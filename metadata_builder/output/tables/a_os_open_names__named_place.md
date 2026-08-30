# Named Place

## Overview

- **Identifier:** `a_os_open_names/named_place`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Names
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-names
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.647027, 49.862958, 1.763942, 60.860284]`
- **Schema:** `a_os_open_names`
- **Table:** `named_place`
- **Geometry:** POINT
- **CRS:** EPSG:27700
- **Rows:** 3025714
- **Columns:** 34
- **Metadata status:** source_mapped

## Description

Named Place is part of OS Open Names, published by Ordnance Survey. It represents named place features using point geometry.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `id` | `varchar` | Publisher-assigned identifier for the record. | source_identifier | Yes | No | No |
| `names_uri` | `varchar` | Publisher-supplied names uri for the represented feature or record. | source_attribute | Yes | No | No |
| `name1` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `name1_lang` | `varchar` | Publisher-supplied name1 lang for the represented feature or record. | source_attribute | Yes | No | No |
| `name2` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `name2_lang` | `varchar` | Publisher-supplied name2 lang for the represented feature or record. | source_attribute | Yes | No | No |
| `type` | `varchar` | Publisher-supplied type for the represented feature or record. | source_attribute | Yes | No | No |
| `local_type` | `varchar` | Publisher-supplied local type for the represented feature or record. | source_attribute | Yes | No | No |
| `most_detail_view_res` | `integer` | Count or numeric value for most detail view res in the represented area. | statistical_value | Yes | No | No |
| `least_detail_view_res` | `integer` | Count or numeric value for least detail view res in the represented area. | statistical_value | Yes | No | No |
| `mbr_xmin` | `real` | Count or numeric value for mbr xmin in the represented area. | statistical_value | Yes | No | No |
| `mbr_ymin` | `real` | Count or numeric value for mbr ymin in the represented area. | statistical_value | Yes | No | No |
| `mbr_xmax` | `real` | Count or numeric value for mbr xmax in the represented area. | statistical_value | Yes | No | No |
| `mbr_ymax` | `real` | Count or numeric value for mbr ymax in the represented area. | statistical_value | Yes | No | No |
| `postcode_district` | `varchar` | Publisher-supplied postcode district for the represented feature or record. | source_attribute | Yes | No | No |
| `postcode_district_uri` | `varchar` | Publisher-supplied postcode district uri for the represented feature or record. | source_attribute | Yes | No | No |
| `populated_place` | `varchar` | Publisher-supplied populated place for the represented feature or record. | source_attribute | Yes | No | No |
| `populated_place_uri` | `varchar` | Publisher-supplied populated place uri for the represented feature or record. | source_attribute | Yes | No | No |
| `populated_place_type` | `varchar` | Publisher-supplied populated place type for the represented feature or record. | source_attribute | Yes | No | No |
| `district_borough` | `varchar` | Publisher-supplied district borough for the represented feature or record. | source_attribute | Yes | No | No |
| `district_borough_uri` | `varchar` | Publisher-supplied district borough uri for the represented feature or record. | source_attribute | Yes | No | No |
| `district_borough_type` | `varchar` | Publisher-supplied district borough type for the represented feature or record. | source_attribute | Yes | No | No |
| `county_unitary` | `varchar` | Publisher-supplied county unitary for the represented feature or record. | source_attribute | Yes | No | No |
| `county_unitary_uri` | `varchar` | Publisher-supplied county unitary uri for the represented feature or record. | source_attribute | Yes | No | No |
| `county_unitary_type` | `varchar` | Publisher-supplied county unitary type for the represented feature or record. | source_attribute | Yes | No | No |
| `region` | `varchar` | Publisher-supplied region for the represented feature or record. | source_attribute | Yes | No | No |
| `region_uri` | `varchar` | Publisher-supplied region uri for the represented feature or record. | source_attribute | Yes | No | No |
| `country` | `varchar` | Publisher-supplied country for the represented feature or record. | source_attribute | Yes | No | No |
| `country_uri` | `varchar` | Publisher-supplied country uri for the represented feature or record. | source_attribute | Yes | No | No |
| `related_spatial_object` | `varchar` | Publisher-supplied related spatial object for the represented feature or record. | source_attribute | Yes | No | No |
| `same_as_dbpedia` | `varchar` | Publisher-supplied same as dbpedia for the represented feature or record. | source_attribute | Yes | No | No |
| `same_as_geonames` | `varchar` | Publisher-supplied same as geonames for the represented feature or record. | source_attribute | Yes | No | No |
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
