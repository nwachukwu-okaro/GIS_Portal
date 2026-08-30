# Scheduled Monuments

## Overview

- **Identifier:** `a_historic_england/scheduled_monuments`
- **Source organisation:** Historic England
- **Product:** National Heritage List for England spatial data
- **Source:** https://historicengland.org.uk/listing/the-list/map-data/
- **Schema:** `a_historic_england`
- **Table:** `scheduled_monuments`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 19999
- **Metadata status:** source_mapped

## Description

Version: 20251124
Source: https://opendata-historicengland.hub.arcgis.com/datasets/historicengland::national-heritage-list-for-england-nhle/explore?layer=6

Attribution: © Historic England [year]. Contains Ordnance Survey data © Crown copyright and database right [year].

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `listentry` | `integer` | Historic England List Entry number — unique identifier for a designated heritage asset. | heritage_asset_identifier | Yes | No | Yes |
| `name` | `varchar(1000)` | Name of the represented feature. | feature_name | Yes | Yes | No |
| `scheddate` | `timestamp` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `amenddate` | `timestamp` | Date the designation was last amended or updated. | amendment_date | Yes | No | No |
| `capturescale` | `varchar(15)` | Map scale at which the boundary was originally captured. | capture_scale | Yes | No | No |
| `hyperlink` | `varchar(255)` | URL linking to the official Historic England record for this asset. | source_record_url | Yes | No | No |
| `area_ha` | `double precision` | Area of the feature in hectares. | area | Yes | No | No |
| `ngr` | `varchar(1000000)` | National Grid Reference — alphanumeric grid coordinate in British National Grid. | geographic_reference | Yes | No | No |
| `easting` | `real` | Easting coordinate in British National Grid (EPSG:27700). | x_coordinate | Yes | No | No |
| `northing` | `real` | Northing coordinate in British National Grid (EPSG:27700). | y_coordinate | Yes | No | No |
| `objectid` | `bigint` | Source-system object identifier. | identifier | Yes | No | No |
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

- Verify against the individual Historic England download metadata.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
