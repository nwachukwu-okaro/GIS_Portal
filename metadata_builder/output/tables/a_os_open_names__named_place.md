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
| `id` | `varchar` |  |
| `names_uri` | `varchar` |  |
| `name1` | `varchar` |  |
| `name1_lang` | `varchar` |  |
| `name2` | `varchar` |  |
| `name2_lang` | `varchar` |  |
| `type` | `varchar` |  |
| `local_type` | `varchar` |  |
| `most_detail_view_res` | `integer` |  |
| `least_detail_view_res` | `integer` |  |
| `mbr_xmin` | `real` |  |
| `mbr_ymin` | `real` |  |
| `mbr_xmax` | `real` |  |
| `mbr_ymax` | `real` |  |
| `postcode_district` | `varchar` |  |
| `postcode_district_uri` | `varchar` |  |
| `populated_place` | `varchar` |  |
| `populated_place_uri` | `varchar` |  |
| `populated_place_type` | `varchar` |  |
| `district_borough` | `varchar` |  |
| `district_borough_uri` | `varchar` |  |
| `district_borough_type` | `varchar` |  |
| `county_unitary` | `varchar` |  |
| `county_unitary_uri` | `varchar` |  |
| `county_unitary_type` | `varchar` |  |
| `region` | `varchar` |  |
| `region_uri` | `varchar` |  |
| `country` | `varchar` |  |
| `country_uri` | `varchar` |  |
| `related_spatial_object` | `varchar` |  |
| `same_as_dbpedia` | `varchar` |  |
| `same_as_geonames` | `varchar` |  |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
