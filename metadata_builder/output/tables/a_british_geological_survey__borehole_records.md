# BGS Borehole Records

## Overview

- **Identifier:** `a_british_geological_survey/borehole_records`
- **Source organisation:** British Geological Survey
- **Product:** BGS geological data
- **Source:** https://www.bgs.ac.uk/geological-data/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-7.497121, 49.911488, 1.762133, 60.828252]`
- **Topic category:** geoscientificInformation
- **Temporal extent:** 1955-01-01 to 2026-03-30
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** dataset_reference_date, frequency_of_update
- **Schema:** `a_british_geological_survey`
- **Table:** `borehole_records`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:27700
- **Rows:** 1351536
- **Columns:** 16
- **Metadata status:** context_curated

## Description

Point index of BGS borehole records, providing registration references, National Grid locations, drilling length and date information, confidentiality status and links to available online records or logs.

## Lineage

Published by British Geological Survey as part of BGS geological data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `qs` | `varchar(6)` | BGS quarter-sheet code locating the borehole record, such as HP60NW. |
| `numb` | `integer` | Sequential borehole number within the BGS map-sheet reference. |
| `bsuff` | `varchar(4)` | Suffix used to distinguish boreholes sharing the same sheet and sequence number. |
| `regno` | `varchar(51)` | BGS borehole registration number, formed from the sheet code, number and optional suffix. |
| `rt` | `varchar(2)` | BGS code identifying the borehole record type, such as BJ, OE or SE. |
| `grid_refer` | `varchar(14)` | Ordnance Survey National Grid Reference for the borehole location. |
| `confidenti` | `varchar(1)` | Y/N flag indicating whether access to the borehole record is confidential. |
| `strtheight` | `real` | Ground or start elevation of the borehole location relative to the recorded vertical datum. |
| `name` | `varchar(150)` | Official or publisher-assigned name of the represented feature. |
| `length` | `double precision` | Recorded drilled length or total depth of the borehole, normally in metres. |
| `bgs_id` | `integer` | Identifier assigned by the source dataset. |
| `date_known` | `integer` | Recorded borehole date or year value where the drilling date is known. |
| `date_k_typ` | `varchar(68)` | Qualifier describing the borehole date, such as DRILLED DATE, CIRCA, PRE or NOT ENTERED. |
| `date_enter` | `date` | Date on which the borehole record was entered into the source database. |
| `ags_log_ur` | `varchar(254)` | URL for viewing the corresponding BGS borehole record or AGS log online. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
