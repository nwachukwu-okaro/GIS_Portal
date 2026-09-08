# Certificates of Immunity from Listing

## Overview

- **Identifier:** `a_historic_england/certificate_of_immunity_points`
- **Source organisation:** Historic England
- **Product:** National Heritage List for England spatial data
- **Source:** https://historicengland.org.uk/listing/the-list/map-data/
- **Official dataset page:** https://opendata-historicengland.hub.arcgis.com/datasets/historicengland::national-heritage-list-for-england-nhle/explore?layer=2
- **Official documentation:** https://historicengland.org.uk/listing/the-list/data-downloads/
- **Local dataset version:** 20251124 (24 November 2025)
- **Official dataset last updated:** 28 August 2026
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-4.169137, 50.365850, 1.319359, 54.965135]`
- **Topic category:** society
- **Dataset reference date:** 2026-08-28 (revision)
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, frequency_of_update
- **Schema:** `a_historic_england`
- **Table:** `certificate_of_immunity_points`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:27700
- **Rows:** 209
- **Columns:** 11
- **Metadata status:** source_verified

## Description

Point locations of buildings with a Certificate of Immunity from Listing published on the National Heritage List for England. A certificate confirms that the Secretary of State does not intend to list the building and normally prevents a Building Preservation Notice for five years.

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
| `coistart` | `timestamp` | Date on which the Certificate of Immunity took effect. |
| `coiexpire` | `timestamp` | Date on which the Certificate of Immunity expires, normally five years after issue. |
| `capturescale` | `varchar(15)` | Map scale at which the boundary was originally captured. |
| `hyperlink` | `varchar(255)` | URL linking to the official Historic England record for this asset. |
| `ngr` | `varchar(1000000)` | National Grid Reference — alphanumeric grid coordinate in British National Grid. |
| `easting` | `real` | Easting coordinate in British National Grid (EPSG:27700). |
| `northing` | `real` | Northing coordinate in British National Grid (EPSG:27700). |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
