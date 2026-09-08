# Named Place

## Overview

- **Identifier:** `a_os_open_names/named_place`
- **Source organisation:** Ordnance Survey
- **Product:** OS Open Names
- **Source:** https://www.ordnancesurvey.co.uk/products/os-open-names
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.647027, 49.862958, 1.763942, 60.860284]`
- **Topic category:** location
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update
- **Schema:** `a_os_open_names`
- **Table:** `named_place`
- **Geometry:** POINT
- **CRS:** EPSG:27700
- **Rows:** 3025714
- **Columns:** 34
- **Metadata status:** source_mapped

## Description

Named Place is part of OS Open Names, published by Ordnance Survey. It represents named place features using point geometry.

## Lineage

Published by Ordnance Survey as part of OS Open Names. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `varchar` | Publisher-assigned identifier for the record. |
| `names_uri` | `varchar` | Publisher-supplied names uri for the represented feature or record. |
| `name1` | `varchar` |  |
| `name1_lang` | `varchar` | Publisher-supplied name1 lang for the represented feature or record. |
| `name2` | `varchar` |  |
| `name2_lang` | `varchar` | Publisher-supplied name2 lang for the represented feature or record. |
| `type` | `varchar` | Publisher-supplied type for the represented feature or record. |
| `local_type` | `varchar` | Publisher-supplied local type for the represented feature or record. |
| `most_detail_view_res` | `integer` | Count or numeric value for most detail view res in the represented area. |
| `least_detail_view_res` | `integer` | Count or numeric value for least detail view res in the represented area. |
| `mbr_xmin` | `real` | Count or numeric value for mbr xmin in the represented area. |
| `mbr_ymin` | `real` | Count or numeric value for mbr ymin in the represented area. |
| `mbr_xmax` | `real` | Count or numeric value for mbr xmax in the represented area. |
| `mbr_ymax` | `real` | Count or numeric value for mbr ymax in the represented area. |
| `postcode_district` | `varchar` | Publisher-supplied postcode district for the represented feature or record. |
| `postcode_district_uri` | `varchar` | Publisher-supplied postcode district uri for the represented feature or record. |
| `populated_place` | `varchar` | Publisher-supplied populated place for the represented feature or record. |
| `populated_place_uri` | `varchar` | Publisher-supplied populated place uri for the represented feature or record. |
| `populated_place_type` | `varchar` | Publisher-supplied populated place type for the represented feature or record. |
| `district_borough` | `varchar` | Publisher-supplied district borough for the represented feature or record. |
| `district_borough_uri` | `varchar` | Publisher-supplied district borough uri for the represented feature or record. |
| `district_borough_type` | `varchar` | Publisher-supplied district borough type for the represented feature or record. |
| `county_unitary` | `varchar` | Publisher-supplied county unitary for the represented feature or record. |
| `county_unitary_uri` | `varchar` | Publisher-supplied county unitary uri for the represented feature or record. |
| `county_unitary_type` | `varchar` | Publisher-supplied county unitary type for the represented feature or record. |
| `region` | `varchar` | Publisher-supplied region for the represented feature or record. |
| `region_uri` | `varchar` | Publisher-supplied region uri for the represented feature or record. |
| `country` | `varchar` | Publisher-supplied country for the represented feature or record. |
| `country_uri` | `varchar` | Publisher-supplied country uri for the represented feature or record. |
| `related_spatial_object` | `varchar` | Publisher-supplied related spatial object for the represented feature or record. |
| `same_as_dbpedia` | `varchar` | Publisher-supplied same as dbpedia for the represented feature or record. |
| `same_as_geonames` | `varchar` | Publisher-supplied same as geonames for the represented feature or record. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
