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
- **Schema:** `a_historic_england`
- **Table:** `parks_and_gardens`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 1720
- **Columns:** 13
- **Metadata status:** source_verified

## Description

Boundary polygons of parks and gardens of special historic interest registered in England, with their National Heritage List identifiers, grades, registration dates and official records.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `listentry` | `integer` | Historic England List Entry number — unique identifier for a designated heritage asset. | heritage_asset_identifier | Yes | No | Yes |
| `name` | `varchar(1000)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `grade` | `varchar(100)` | Registration grade: I, II* or II, indicating the site's level of historic interest. | designation_grade | Yes | No | No |
| `regdate` | `timestamp` | Date the site was officially registered or designated. | designation_date | Yes | No | No |
| `amenddate` | `timestamp` | Date the designation was last amended or updated. | amendment_date | Yes | No | No |
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
- objectid may change when the dataset is republished.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.

- Historic England, Download Listing Data - GIS Shapefiles: https://historicengland.org.uk/listing/the-list/data-downloads/
- Historic England, Understanding List Entries: https://historicengland.org.uk/listing/the-list/understanding-list-entries/
