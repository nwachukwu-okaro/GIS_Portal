# Listed Building Points

## Overview

- **Identifier:** `a_historic_england/listed_building_points`
- **Source organisation:** Historic England
- **Product:** National Heritage List for England spatial data
- **Source:** https://historicengland.org.uk/listing/the-list/map-data/
- **Official dataset page:** https://opendata-historicengland.hub.arcgis.com/datasets/historicengland::national-heritage-list-for-england-nhle/explore?layer=0
- **Official documentation:** https://historicengland.org.uk/listing/the-list/data-downloads/
- **Local dataset version:** 20251124 (24 November 2025)
- **Official dataset last updated:** 28 August 2026
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.445481, 49.872879, 1.757709, 55.784187]`
- **Topic category:** society
- **Temporal extent:** 1947-01-01T00:00:00 to 2025-11-20T12:19:13
- **Dataset reference date:** 2026-08-28 (revision)
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 2
- **Missing for full compliance:** frequency_of_update
- **Schema:** `a_historic_england`
- **Table:** `listed_building_points`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:27700
- **Rows:** 379637
- **Columns:** 12
- **Metadata status:** source_verified

## Description

Point locations of nationally listed buildings in England from the National Heritage List for England, including each building's List Entry number, official name, grade and listing dates.

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
| `grade` | `varchar(100)` | Statutory listing grade: I, II* or II, indicating the building's level of special interest. |
| `listdate` | `timestamp` | Date on which the building was first added to the statutory List. |
| `amenddate` | `timestamp` | Date the designation was last amended or updated. |
| `capturescale` | `varchar(15)` | Map scale at which the boundary was originally captured. |
| `hyperlink` | `varchar(255)` | URL linking to the official Historic England record for this asset. |
| `ngr` | `varchar(1000000)` | National Grid Reference — alphanumeric grid coordinate in British National Grid. |
| `easting` | `real` | Easting coordinate in British National Grid (EPSG:27700). |
| `northing` | `real` | Northing coordinate in British National Grid (EPSG:27700). |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
