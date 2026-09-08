# Conservation Areas

## Overview

- **Identifier:** `a_historic_england/conservation_areas`
- **Source organisation:** Historic England
- **Product:** National Heritage List for England spatial data
- **Source:** https://historicengland.org.uk/listing/the-list/map-data/
- **Official dataset page:** https://opendata-historicengland.hub.arcgis.com/datasets/historicengland::conservation-areas/explore
- **Official documentation:** https://historicengland.org.uk/listing/the-list/data-downloads/
- **Local dataset version:** 20250702 (2 July 2025)
- **Official dataset last updated:** 2 July 2025
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.418945, 49.864637, 1.759226, 55.776545]`
- **Topic category:** society
- **Dataset reference date:** 2025-07-02 (revision)
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_historic_england`
- **Table:** `conservation_areas`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 8162
- **Columns:** 10
- **Metadata status:** source_verified

## Description

Boundaries of conservation areas designated by local planning authorities in England for their special architectural or historic interest. The dataset is compiled and published by Historic England.

## Lineage

Published by Historic England as part of the National Heritage List for England (NHLE). Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `uid` | `bigint` | Unique identifier assigned to the conservation-area record by the source dataset. |
| `name` | `varchar(150)` | Official or publisher-assigned name of the represented feature. |
| `date_of_de` | `varchar(50)` | Date on which the local planning authority designated the conservation area. |
| `date_updat` | `varchar(50)` | Date on which the conservation-area record or boundary was last updated. |
| `lpa` | `varchar(50)` | Local planning authority responsible for designating and managing the conservation area. |
| `capture_sc` | `varchar(50)` | Map scale used to capture the conservation-area boundary. |
| `x` | `integer` | British National Grid easting in metres for the area's reference location. |
| `y` | `integer` | British National Grid northing in metres for the area's reference location. |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
