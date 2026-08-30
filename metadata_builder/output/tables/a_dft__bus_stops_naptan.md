# NaPTAN Bus Stops

## Overview

- **Identifier:** `a_dft/bus_stops_naptan`
- **Source organisation:** Department for Transport
- **Source:** https://www.data.gov.uk/search?filters%5Bpublisher%5D=Department+for+Transport
- **WGS84 extent:** `[-7.557160, 49.766807, 3.187673, 60.825872]`
- **Schema:** `a_dft`
- **Table:** `bus_stops_naptan`
- **Geometry:** POINT
- **CRS:** EPSG:27700
- **Rows:** 433655
- **Columns:** 45
- **Metadata status:** context_curated

## Description

Point locations and reference attributes for bus stops from the National Public Transport Access Nodes dataset, including national identifiers, passenger-facing names, locality hierarchy, stop classifications, timing status and record lifecycle information.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `atcocode` | `varchar` | Unique national ATCO identifier for the stop point. | stop_identifier | Yes | No | No |
| `naptancode` | `varchar` | Short public-facing NaPTAN code printed or displayed for the stop. | public_stop_code | Yes | No | No |
| `platecode` | `varchar` | Local code shown on the physical stop plate where supplied. | stop_plate_code | Yes | No | No |
| `cleardowncode` | `varchar` | Code used by some operators to clear or identify the stop in operational systems. | operational_stop_code | Yes | No | No |
| `commonname` | `varchar` | Primary name by which the stop is publicly known. | feature_name | Yes | Yes | No |
| `commonnamelang` | `varchar` | Language code for the primary stop name. | language_code | Yes | No | No |
| `shortcommonname` | `varchar` | Abbreviated public name for the stop where supplied. | short_feature_name | Yes | Yes | No |
| `shortcommonnamelang` | `varchar` | Language code for the abbreviated stop name. | language_code | Yes | No | No |
| `landmark` | `varchar` | Nearby landmark used to help passengers locate the stop. | landmark | Yes | Yes | No |
| `landmarklang` | `varchar` | Language code for the landmark text. | language_code | Yes | No | No |
| `street` | `varchar` | Street or road on which the stop is located. | street_name | Yes | Yes | No |
| `streetlang` | `varchar` | Language code for the street name. | language_code | Yes | No | No |
| `crossing` | `varchar` | Nearby crossing or intersecting street used to describe the stop location. | crossing_name | Yes | No | No |
| `crossinglang` | `varchar` | Language code for the crossing description. | language_code | Yes | No | No |
| `indicator` | `varchar` | Location indicator distinguishing the stop, such as a stand, bay, direction or outside landmark. | stop_indicator | Yes | No | No |
| `indicatorlang` | `varchar` | Language code for the stop indicator. | language_code | Yes | No | No |
| `bearing` | `varchar` | Compass direction faced or served by the stop, such as N, SW or E. | compass_bearing | Yes | No | No |
| `nptglocalitycode` | `varchar` | National Public Transport Gazetteer code for the stop's locality. | locality_identifier | Yes | No | No |
| `localityname` | `varchar` | NPTG locality name associated with the stop. | locality_name | Yes | Yes | No |
| `parentlocalityname` | `varchar` | Name of the parent locality containing the stop locality. | parent_locality_name | Yes | No | No |
| `grandparentlocalityname` | `varchar` | Name of the higher-level locality containing the parent locality. | grandparent_locality_name | Yes | No | No |
| `town` | `varchar` | Town or settlement recorded for the stop location. | town_name | Yes | Yes | No |
| `townlang` | `varchar` | Language code for the town name, such as EN. | language_code | Yes | No | No |
| `suburb` | `varchar` | Suburb or neighbourhood recorded for the stop. | suburb_name | Yes | Yes | No |
| `suburblang` | `varchar` | Language code for the suburb name. | language_code | Yes | No | No |
| `localitycentre` | `varchar` | Boolean indicator showing whether the stop represents a locality centre. | locality_centre_flag | Yes | No | No |
| `gridtype` | `varchar` | Coordinate grid system used for the stop location, such as UKOS. | coordinate_system_code | Yes | No | No |
| `easting` | `real` | Easting coordinate in metres in the dataset's projected coordinate reference system. | x_coordinate | Yes | No | No |
| `northing` | `real` | Northing coordinate in metres in the dataset's projected coordinate reference system. | y_coordinate | Yes | No | No |
| `longitude` | `real` | Longitude coordinate, normally expressed in decimal degrees. | longitude | Yes | No | No |
| `latitude` | `real` | Latitude coordinate, normally expressed in decimal degrees. | latitude | Yes | No | No |
| `stoptype` | `varchar` | NaPTAN stop-classification code identifying the transport stop or access-point type. | stop_type_code | Yes | No | No |
| `busstoptype` | `varchar` | NaPTAN bus-stop subtype, such as marked, hail-and-ride, flexible or unmarked. | bus_stop_type_code | Yes | No | No |
| `timingstatus` | `varchar` | Operational timing-point status used in public transport scheduling. | timing_status | Yes | No | No |
| `defaultwaittime` | `varchar` | Default interchange waiting time recorded for the stop. | default_wait_time | Yes | No | No |
| `notes` | `varchar` | Additional publisher note about the stop record. | note | Yes | Yes | No |
| `noteslang` | `varchar` | Language code for the stop notes. | language_code | Yes | No | No |
| `administrativeareacode` | `integer` | NPTG administrative-area code responsible for the stop record. | administrative_area_code | Yes | No | No |
| `creationdatetime` | `timestamp` | Date and time when the stop record was created. | record_creation_datetime | Yes | No | No |
| `modificationdatetime` | `timestamp` | Date and time when the stop record was last modified. | record_update_datetime | Yes | No | No |
| `revisionnumber` | `integer` | Revision sequence number of the NaPTAN record. | record_revision | Yes | No | No |
| `modification` | `varchar` | Change action represented by the record, such as new, revise or delete. | change_action | Yes | No | No |
| `status` | `varchar` | Lifecycle status of the stop record, such as active, inactive or pending. | record_status | Yes | No | No |
| `stop_pk` | `integer` | Internal primary-key value for the imported stop record. | record_identifier | Yes | No | No |
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

- Use ATCOCode as the persistent stop identifier; local plate and public codes may differ.
- Inactive or deleted records should be excluded when identifying currently usable stops.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
