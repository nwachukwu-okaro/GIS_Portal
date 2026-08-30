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
- **Schema:** `a_historic_england`
- **Table:** `world_heritage_sites`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 28
- **Columns:** 13
- **Metadata status:** source_verified

## Description

Boundary polygons for World Heritage Sites in England recorded by Historic England, including their National Heritage List identifiers, inscription dates and official record links.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `listentry` | `integer` | Historic England List Entry number — unique identifier for a designated heritage asset. | heritage_asset_identifier | Yes | No | Yes |
| `name` | `varchar(1000)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `inscrdate` | `timestamp` | Date on which the site was inscribed on the UNESCO World Heritage List. | inscription_date | Yes | No | No |
| `amenddate` | `timestamp` | Date the designation was last amended or updated. | amendment_date | Yes | No | No |
| `notes` | `varchar(240)` | Additional source note about the World Heritage Site record or boundary. | note | Yes | Yes | No |
| `capturescale` | `varchar(15)` | Map scale at which the boundary was originally captured. | capture_scale | Yes | No | No |
| `hyperlink` | `varchar(255)` | URL linking to the official Historic England record for this asset. | source_record_url | Yes | No | No |
| `area_ha` | `double precision` | Area of the feature in hectares. | area | Yes | No | No |
| `ngr` | `varchar(1000000)` | National Grid Reference — alphanumeric grid coordinate in British National Grid. | geographic_reference | Yes | No | No |
| `easting` | `real` | Easting coordinate in British National Grid (EPSG:27700). | x_coordinate | Yes | No | No |
| `northing` | `real` | Northing coordinate in British National Grid (EPSG:27700). | y_coordinate | Yes | No | No |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. | identifier | Yes | No | No |
| `geom` | `geometry` | Spatial geometry of the represented feature. | geometry | No | No | No |

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

- This local snapshot predates the latest official dataset update.
- Some World Heritage Sites contain multiple component polygons or records.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.

- Historic England, Download Listing Data - GIS Shapefiles: https://historicengland.org.uk/listing/the-list/data-downloads/
- Historic England, Understanding List Entries: https://historicengland.org.uk/listing/the-list/understanding-list-entries/
