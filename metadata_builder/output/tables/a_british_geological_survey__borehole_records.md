# BGS Borehole Records

## Overview

- **Identifier:** `a_british_geological_survey/borehole_records`
- **Source organisation:** British Geological Survey
- **Product:** BGS geological data
- **Source:** https://www.bgs.ac.uk/geological-data/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-7.497121, 49.911488, 1.762133, 60.828252]`
- **Schema:** `a_british_geological_survey`
- **Table:** `borehole_records`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:27700
- **Rows:** 1351536
- **Columns:** 16
- **Metadata status:** context_curated

## Description

Point index of BGS borehole records, providing registration references, National Grid locations, drilling length and date information, confidentiality status and links to available online records or logs.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `qs` | `varchar(6)` | BGS quarter-sheet code locating the borehole record, such as HP60NW. | map_sheet_code | Yes | No | No |
| `numb` | `integer` | Sequential borehole number within the BGS map-sheet reference. | borehole_number | Yes | No | No |
| `bsuff` | `varchar(4)` | Suffix used to distinguish boreholes sharing the same sheet and sequence number. | borehole_suffix | Yes | No | No |
| `regno` | `varchar(51)` | BGS borehole registration number, formed from the sheet code, number and optional suffix. | borehole_identifier | Yes | No | No |
| `rt` | `varchar(2)` | BGS code identifying the borehole record type, such as BJ, OE or SE. | borehole_record_type_code | Yes | No | No |
| `grid_refer` | `varchar(14)` | Ordnance Survey National Grid Reference for the borehole location. | geographic_reference | Yes | No | No |
| `confidenti` | `varchar(1)` | Y/N flag indicating whether access to the borehole record is confidential. | confidentiality_flag | Yes | No | No |
| `strtheight` | `real` | Ground or start elevation of the borehole location relative to the recorded vertical datum. | borehole_start_elevation | Yes | No | No |
| `name` | `varchar(150)` | Official or publisher-assigned name of the represented feature. | feature_name | Yes | Yes | No |
| `length` | `double precision` | Recorded drilled length or total depth of the borehole, normally in metres. | borehole_length | Yes | No | No |
| `bgs_id` | `integer` | Identifier assigned by the source dataset. | identifier | Yes | No | No |
| `date_known` | `integer` | Recorded borehole date or year value where the drilling date is known. | borehole_date_value | Yes | No | No |
| `date_k_typ` | `varchar(68)` | Qualifier describing the borehole date, such as DRILLED DATE, CIRCA, PRE or NOT ENTERED. | borehole_date_qualifier | Yes | No | No |
| `date_enter` | `date` | Date on which the borehole record was entered into the source database. | record_entry_date | Yes | No | No |
| `ags_log_ur` | `varchar(254)` | URL for viewing the corresponding BGS borehole record or AGS log online. | source_record_url | Yes | No | No |
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

- A map point identifies a borehole record location and does not describe subsurface conditions by itself.
- Some records or logs may be confidential or unavailable online.
- Verify reuse terms against the individual BGS product licence.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
