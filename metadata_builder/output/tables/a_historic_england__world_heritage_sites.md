# World Heritage Sites

## Overview

- **Identifier:** `a_historic_england/world_heritage_sites`
- **Source organisation:** Historic England
- **Product:** National Heritage List for England spatial data
- **Source:** https://historicengland.org.uk/listing/the-list/map-data/
- **Official dataset page:** https://opendata-historicengland.hub.arcgis.com/datasets/historicengland::national-heritage-list-for-england-nhle/explore?layer=10
- **Official documentation:** https://historicengland.org.uk/listing/the-list/data-downloads/
- **Local dataset version:** 20251124 (24 November 2025)
- **Official dataset last updated:** 28 August 2026
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.710650, 50.088655, 1.096214, 55.074245]`
- **Topic category:** society
- **Temporal extent:** 1986-01-01T00:00:00 to 2019-07-30T16:00:43
- **Dataset reference date:** 2026-08-28 (revision)
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 2
- **Missing for full compliance:** frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_historic_england`
- **Table:** `world_heritage_sites`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 28
- **Columns:** 13
- **Metadata status:** source_verified

## Description

Boundary polygons for World Heritage Sites in England recorded by Historic England, including their National Heritage List identifiers, inscription dates and official record links.

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
| `inscrdate` | `timestamp` | Date on which the site was inscribed on the UNESCO World Heritage List. |
| `amenddate` | `timestamp` | Date the designation was last amended or updated. |
| `notes` | `varchar(240)` | Additional source note about the World Heritage Site record or boundary. |
| `capturescale` | `varchar(15)` | Map scale at which the boundary was originally captured. |
| `hyperlink` | `varchar(255)` | URL linking to the official Historic England record for this asset. |
| `area_ha` | `double precision` | Area of the feature in hectares. |
| `ngr` | `varchar(1000000)` | National Grid Reference — alphanumeric grid coordinate in British National Grid. |
| `easting` | `real` | Easting coordinate in British National Grid (EPSG:27700). |
| `northing` | `real` | Northing coordinate in British National Grid (EPSG:27700). |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
