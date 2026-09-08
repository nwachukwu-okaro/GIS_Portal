# Scheduled Monuments

## Overview

- **Identifier:** `a_historic_england/scheduled_monuments`
- **Source organisation:** Historic England
- **Product:** National Heritage List for England spatial data
- **Source:** https://historicengland.org.uk/listing/the-list/map-data/
- **Official dataset page:** https://opendata-historicengland.hub.arcgis.com/datasets/historicengland::national-heritage-list-for-england-nhle/explore?layer=6
- **Official documentation:** https://historicengland.org.uk/listing/the-list/data-downloads/
- **Local dataset version:** 20251124 (24 November 2025)
- **Official dataset last updated:** 28 August 2026
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.401501, 49.869551, 1.730846, 55.787087]`
- **Topic category:** society
- **Temporal extent:** 1882-01-01T00:00:00 to 2025-10-29T16:17:38
- **Dataset reference date:** 2026-08-28 (revision)
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 2
- **Missing for full compliance:** frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_historic_england`
- **Table:** `scheduled_monuments`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 19999
- **Columns:** 12
- **Metadata status:** source_verified

## Description

Boundary polygons of nationally important archaeological sites scheduled under the Ancient Monuments and Archaeological Areas Act 1979 and recorded on the National Heritage List for England.

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
| `scheddate` | `timestamp` | Date on which the monument was first scheduled. |
| `amenddate` | `timestamp` | Date the designation was last amended or updated. |
| `capturescale` | `varchar(15)` | Map scale at which the boundary was originally captured. |
| `hyperlink` | `varchar(255)` | URL linking to the official Historic England record for this asset. |
| `area_ha` | `double precision` | Area of the feature in hectares. |
| `ngr` | `varchar(1000000)` | National Grid Reference — alphanumeric grid coordinate in British National Grid. |
| `easting` | `real` | Easting coordinate in British National Grid (EPSG:27700). |
| `northing` | `real` | Northing coordinate in British National Grid (EPSG:27700). |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
