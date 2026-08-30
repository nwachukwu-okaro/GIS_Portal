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
- **Schema:** `a_historic_england`
- **Table:** `certificate_of_immunity_points`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:27700
- **Rows:** 209
- **Columns:** 11
- **Metadata status:** source_verified

## Description

Point locations of buildings with a Certificate of Immunity from Listing published on the National Heritage List for England. A certificate confirms that the Secretary of State does not intend to list the building and normally prevents a Building Preservation Notice for five years.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `listentry` | `integer` | Historic England List Entry number — unique identifier for a designated heritage asset. | heritage_asset_identifier | Yes | No | Yes |
| `name` | `varchar(1000)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `coistart` | `timestamp` | Date on which the Certificate of Immunity took effect. | certificate_start_date | Yes | No | No |
| `coiexpire` | `timestamp` | Date on which the Certificate of Immunity expires, normally five years after issue. | certificate_expiry_date | Yes | No | No |
| `capturescale` | `varchar(15)` | Map scale at which the boundary was originally captured. | capture_scale | Yes | No | No |
| `hyperlink` | `varchar(255)` | URL linking to the official Historic England record for this asset. | source_record_url | Yes | No | No |
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

- Check the official dataset before relying on whether a certificate remains current.
- objectid may change when the dataset is republished.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.

- Historic England, Download Listing Data - GIS Shapefiles: https://historicengland.org.uk/listing/the-list/data-downloads/
- Historic England, Building Preservation Notices and Certificates of Immunity: https://historicengland.org.uk/listing/protect-historic-places/building-preservation-notices-and-certificates-of-immunity/
