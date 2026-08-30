# Conservation Areas

## Overview

- **Identifier:** `a_historic_england/conservation_areas`
- **Source organisation:** Historic England
- **Product:** National Heritage List for England spatial data
- **Source:** https://historicengland.org.uk/listing/the-list/map-data/
- **Official dataset page:** https://opendata-historicengland.hub.arcgis.com/datasets/historicengland::conservation-areas/explore
- **Official documentation:** https://historicengland.org.uk/listing/the-list/data-downloads/
- **Local dataset version:** 20250702 (2 July 2025)
- **Official dataset last updated:** 2 July 2025
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.418945, 49.864637, 1.759226, 55.776545]`
- **Schema:** `a_historic_england`
- **Table:** `conservation_areas`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 8162
- **Columns:** 10
- **Metadata status:** source_verified

## Description

Boundaries of conservation areas designated by local planning authorities in England for their special architectural or historic interest. The dataset is compiled and published by Historic England.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `uid` | `bigint` | Unique identifier assigned to the conservation-area record by the source dataset. | record_identifier | Yes | No | No |
| `name` | `varchar(150)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `date_of_de` | `varchar(50)` | Date on which the local planning authority designated the conservation area. | designation_date | Yes | No | No |
| `date_updat` | `varchar(50)` | Date on which the conservation-area record or boundary was last updated. | update_date | Yes | No | No |
| `lpa` | `varchar(50)` | Local planning authority responsible for designating and managing the conservation area. | responsible_organisation | Yes | Yes | No |
| `capture_sc` | `varchar(50)` | Map scale used to capture the conservation-area boundary. | capture_scale | Yes | No | No |
| `x` | `integer` | British National Grid easting in metres for the area's reference location. | x_coordinate | Yes | No | No |
| `y` | `integer` | British National Grid northing in metres for the area's reference location. | y_coordinate | Yes | No | No |
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

- Local planning authorities are the designating bodies; consult the relevant authority for the latest legal boundary.
- objectid may change when the dataset is republished.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.

- Historic England, Download Listing Data - GIS Shapefiles: https://historicengland.org.uk/listing/the-list/data-downloads/
- Historic England, Designating and Managing a Conservation Area: https://historicengland.org.uk/advice/planning/conservation-areas/
