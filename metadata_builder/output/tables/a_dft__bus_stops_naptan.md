# NaPTAN Bus Stops

## Overview

- **Identifier:** `a_dft/bus_stops_naptan`
- **Source organisation:** Department for Transport
- **Source:** https://www.data.gov.uk/search?filters%5Bpublisher%5D=Department+for+Transport
- **WGS84 extent:** `[-7.557160, 49.766807, 3.187673, 60.825872]`
- **Topic category:** transportation
- **Temporal extent:** 1899-12-30T00:00:00 to 2106-02-07T00:00:00
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_dft`
- **Table:** `bus_stops_naptan`
- **Geometry:** POINT
- **CRS:** EPSG:27700
- **Rows:** 433655
- **Columns:** 45
- **Metadata status:** context_curated

## Description

Point locations and reference attributes for bus stops from the National Public Transport Access Nodes dataset, including national identifiers, passenger-facing names, locality hierarchy, stop classifications, timing status and record lifecycle information.

## Lineage

Published by Department for Transport as open transport data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `atcocode` | `varchar` | Unique national ATCO identifier for the stop point. |
| `naptancode` | `varchar` | Short public-facing NaPTAN code printed or displayed for the stop. |
| `platecode` | `varchar` | Local code shown on the physical stop plate where supplied. |
| `cleardowncode` | `varchar` | Code used by some operators to clear or identify the stop in operational systems. |
| `commonname` | `varchar` | Primary name by which the stop is publicly known. |
| `commonnamelang` | `varchar` | Language code for the primary stop name. |
| `shortcommonname` | `varchar` | Abbreviated public name for the stop where supplied. |
| `shortcommonnamelang` | `varchar` | Language code for the abbreviated stop name. |
| `landmark` | `varchar` | Nearby landmark used to help passengers locate the stop. |
| `landmarklang` | `varchar` | Language code for the landmark text. |
| `street` | `varchar` | Street or road on which the stop is located. |
| `streetlang` | `varchar` | Language code for the street name. |
| `crossing` | `varchar` | Nearby crossing or intersecting street used to describe the stop location. |
| `crossinglang` | `varchar` | Language code for the crossing description. |
| `indicator` | `varchar` | Location indicator distinguishing the stop, such as a stand, bay, direction or outside landmark. |
| `indicatorlang` | `varchar` | Language code for the stop indicator. |
| `bearing` | `varchar` | Compass direction faced or served by the stop, such as N, SW or E. |
| `nptglocalitycode` | `varchar` | National Public Transport Gazetteer code for the stop's locality. |
| `localityname` | `varchar` | NPTG locality name associated with the stop. |
| `parentlocalityname` | `varchar` | Name of the parent locality containing the stop locality. |
| `grandparentlocalityname` | `varchar` | Name of the higher-level locality containing the parent locality. |
| `town` | `varchar` | Town or settlement recorded for the stop location. |
| `townlang` | `varchar` | Language code for the town name, such as EN. |
| `suburb` | `varchar` | Suburb or neighbourhood recorded for the stop. |
| `suburblang` | `varchar` | Language code for the suburb name. |
| `localitycentre` | `varchar` | Boolean indicator showing whether the stop represents a locality centre. |
| `gridtype` | `varchar` | Coordinate grid system used for the stop location, such as UKOS. |
| `easting` | `real` | Easting coordinate in metres in the dataset's projected coordinate reference system. |
| `northing` | `real` | Northing coordinate in metres in the dataset's projected coordinate reference system. |
| `longitude` | `real` | Longitude coordinate, normally expressed in decimal degrees. |
| `latitude` | `real` | Latitude coordinate, normally expressed in decimal degrees. |
| `stoptype` | `varchar` | NaPTAN stop-classification code identifying the transport stop or access-point type. |
| `busstoptype` | `varchar` | NaPTAN bus-stop subtype, such as marked, hail-and-ride, flexible or unmarked. |
| `timingstatus` | `varchar` | Operational timing-point status used in public transport scheduling. |
| `defaultwaittime` | `varchar` | Default interchange waiting time recorded for the stop. |
| `notes` | `varchar` | Additional publisher note about the stop record. |
| `noteslang` | `varchar` | Language code for the stop notes. |
| `administrativeareacode` | `integer` | NPTG administrative-area code responsible for the stop record. |
| `creationdatetime` | `timestamp` | Date and time when the stop record was created. |
| `modificationdatetime` | `timestamp` | Date and time when the stop record was last modified. |
| `revisionnumber` | `integer` | Revision sequence number of the NaPTAN record. |
| `modification` | `varchar` | Change action represented by the record, such as new, revise or delete. |
| `status` | `varchar` | Lifecycle status of the stop record, such as active, inactive or pending. |
| `stop_pk` | `integer` | Internal primary-key value for the imported stop record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
