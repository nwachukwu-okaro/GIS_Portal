# Registered Battlefields

## Overview

- **Identifier:** `a_historic_england/battlefields`
- **Source organisation:** Historic England
- **Product:** National Heritage List for England spatial data
- **Source:** https://historicengland.org.uk/listing/the-list/map-data/
- **Official dataset page:** https://opendata-historicengland.hub.arcgis.com/datasets/historicengland::national-heritage-list-for-england-nhle/explore?layer=8
- **Official documentation:** https://historicengland.org.uk/listing/the-list/data-downloads/
- **Local dataset version:** 20251124 (24 November 2025)
- **Official dataset last updated:** 28 August 2026
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-4.679074, 50.359658, 0.709448, 55.802926]`
- **Topic category:** society
- **Temporal extent:** 1995-06-06T00:00:00 to 2018-01-31T11:01:31
- **Dataset reference date:** 2026-08-28 (revision)
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 2
- **Missing for full compliance:** frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_historic_england`
- **Table:** `battlefields`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 47
- **Columns:** 12
- **Metadata status:** source_verified

## Description

Authoritative boundary polygons for the 47 historic battlefields registered in England. Each feature represents one registered battlefield and includes its National Heritage List for England identifier, official name, registration dates, mapped area, location reference and link to the official designation record. The register supports recognition, conservation and consideration of nationally important battlefield sites in planning decisions.

## Lineage

Published by Historic England as part of the National Heritage List for England (NHLE). Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `listentry` | `integer` | Unique seven-digit National Heritage List for England entry number, such as 1000000. |
| `name` | `text` | Official registered battlefield name, usually including the battle year, such as Edgehill 1642. |
| `regdate` | `timestamp` | Date the battlefield was first entered on the Register. |
| `amenddate` | `timestamp` | Date the registration record was most recently amended; empty where no amendment is recorded. |
| `capturescale` | `varchar(15)` | Map scale used to capture the battlefield boundary, such as 1:10000 or 1:25000. |
| `hyperlink` | `varchar(255)` | URL of the battlefield's official Historic England List entry. |
| `area_ha` | `real` | Area enclosed by the registered battlefield boundary, measured in hectares. |
| `ngr` | `varchar(1000000)` | Ordnance Survey National Grid Reference used to locate the battlefield. |
| `easting` | `real` | British National Grid easting in metres for the battlefield's reference location. |
| `northing` | `real` | British National Grid northing in metres for the battlefield's reference location. |
| `objectid` | `bigint` | ArcGIS source-system row identifier; not a persistent heritage asset identifier. |
| `geom` | `geometry` | Multipolygon boundary of the registered battlefield in British National Grid coordinates. |
