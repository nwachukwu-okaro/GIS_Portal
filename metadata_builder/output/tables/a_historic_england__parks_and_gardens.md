# Registered Parks and Gardens

## Overview

- **Identifier:** `a_historic_england/parks_and_gardens`
- **Source organisation:** Historic England
- **Product:** National Heritage List for England spatial data
- **Source:** https://historicengland.org.uk/listing/the-list/map-data/
- **Official dataset page:** https://opendata-historicengland.hub.arcgis.com/datasets/historicengland::national-heritage-list-for-england-nhle/explore?layer=7
- **Official documentation:** https://historicengland.org.uk/listing/the-list/data-downloads/
- **Local dataset version:** 20251124 (24 November 2025)
- **Official dataset last updated:** 28 August 2026
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.338120, 49.944294, 1.755920, 55.685447]`
- **Topic category:** society
- **Temporal extent:** 1984-05-10T00:00:00 to 2025-10-22T15:30:24
- **Dataset reference date:** 2026-08-28 (revision)
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 2
- **Missing for full compliance:** frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_historic_england`
- **Table:** `parks_and_gardens`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1720
- **Columns:** 13
- **Metadata status:** source_verified

## Description

Boundary polygons of parks and gardens of special historic interest registered in England, with their National Heritage List identifiers, grades, registration dates and official records.

## Lineage

Published by Historic England as part of the National Heritage List for England (NHLE). Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `listentry` | `integer` | Historic England List Entry number — unique identifier for a designated heritage asset. |
| `name` | `varchar(1000)` | Official or publisher-assigned name of the represented feature. |
| `grade` | `varchar(100)` | Registration grade: I, II* or II, indicating the site's level of historic interest. |
| `regdate` | `timestamp` | Date the site was officially registered or designated. |
| `amenddate` | `timestamp` | Date the designation was last amended or updated. |
| `capturescale` | `varchar(15)` | Map scale at which the boundary was originally captured. |
| `hyperlink` | `varchar(255)` | URL linking to the official Historic England record for this asset. |
| `area_ha` | `double precision` | Area of the feature in hectares. |
| `ngr` | `varchar(1000000)` | National Grid Reference — alphanumeric grid coordinate in British National Grid. |
| `easting` | `real` | Easting coordinate in British National Grid (EPSG:27700). |
| `northing` | `real` | Northing coordinate in British National Grid (EPSG:27700). |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
