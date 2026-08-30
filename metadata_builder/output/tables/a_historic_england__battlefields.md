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
- **Schema:** `a_historic_england`
- **Table:** `battlefields`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 47
- **Columns:** 12
- **Metadata status:** source_verified

## Description

Authoritative boundary polygons for the 47 historic battlefields registered in England. Each feature represents one registered battlefield and includes its National Heritage List for England identifier, official name, registration dates, mapped area, location reference and link to the official designation record. The register supports recognition, conservation and consideration of nationally important battlefield sites in planning decisions.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `listentry` | `integer` | Unique seven-digit National Heritage List for England entry number, such as 1000000. | heritage_asset_identifier | Yes | No | Yes |
| `name` | `text` | Official registered battlefield name, usually including the battle year, such as Edgehill 1642. | feature_name | Yes | Yes | No |
| `regdate` | `timestamp` | Date the battlefield was first entered on the Register. | designation_date | Yes | No | No |
| `amenddate` | `timestamp` | Date the registration record was most recently amended; empty where no amendment is recorded. | amendment_date | Yes | No | No |
| `capturescale` | `varchar(15)` | Map scale used to capture the battlefield boundary, such as 1:10000 or 1:25000. | capture_scale | Yes | No | No |
| `hyperlink` | `varchar(255)` | URL of the battlefield's official Historic England List entry. | source_record_url | Yes | No | No |
| `area_ha` | `real` | Area enclosed by the registered battlefield boundary, measured in hectares. | area | Yes | No | No |
| `ngr` | `varchar(1000000)` | Ordnance Survey National Grid Reference used to locate the battlefield. | geographic_reference | Yes | No | No |
| `easting` | `real` | British National Grid easting in metres for the battlefield's reference location. | x_coordinate | Yes | No | No |
| `northing` | `real` | British National Grid northing in metres for the battlefield's reference location. | y_coordinate | Yes | No | No |
| `objectid` | `bigint` | ArcGIS source-system row identifier; not a persistent heritage asset identifier. | identifier | Yes | No | No |
| `geom` | `geometry` | Multipolygon boundary of the registered battlefield in British National Grid coordinates. | geometry | No | No | No |

## Supported operations

- filter
- select
- reproject
- validate_geometry
- buffer
- clip
- intersect
- spatial_join
- export

## Operation requirements

- Intersect, clip and spatial-join inputs must use matching coordinate reference systems.
- Buffer operations require a suitable projected coordinate reference system.
- Reprojection is performed on working outputs; source tables remain unchanged.

## Metadata warnings

- This local table is version 20251124, while Historic England reports a newer official dataset update dated 28 August 2026.
- Check the official Historic England dataset before analyses that require the latest registration boundaries or attributes.
- objectid is a source-system identifier and may change when the dataset is republished.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.

- Historic England, Download Listing Data - GIS Shapefiles: https://historicengland.org.uk/listing/the-list/data-downloads/
- Historic England, What Are Registered Battlefields?: https://historicengland.org.uk/listing/what-is-designation/registered-battlefields/
