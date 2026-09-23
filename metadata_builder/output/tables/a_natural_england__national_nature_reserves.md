# National Nature Reserves

## Overview

- **Identifier:** `a_natural_england/national_nature_reserves`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.268715, 49.958805, 1.728821, 55.722838]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `national_nature_reserves`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 224
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

National Nature Reserves is an authoritative dataset published by Natural England. It represents national nature reserves features using multipolygon geometry.

## Lineage

Published by Natural England as open environmental and conservation data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `integer` | Primary-key identifier for records in national_nature_reserves. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `OBJECTID` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `HYPERLINK` | `varchar(16)` | URL of the corresponding record on the publisher's website. |
| `REF_CODE` | `varchar(10)` | Code assigned by the source dataset. |
| `NAME` | `varchar(120)` | Official or publisher-assigned name of the represented feature. |
| `MEASURE` | `double precision` |  |
| `LABEL` | `varchar(140)` |  |
| `GlobalID` | `varchar(38)` | UUID-formatted identifier associated with the record; persistence across releases is not confirmed. |
