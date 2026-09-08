# BGS Geology 625K - Faults

## Overview

- **Identifier:** `a_british_geological_survey/625k_faults`
- **Source organisation:** British Geological Survey
- **Product:** BGS geological data
- **Source:** https://www.bgs.ac.uk/geological-data/
- **Local dataset version:** 5.17 (released 23 April 2008)
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **WGS84 extent:** `[-8.097029, 49.967884, 0.781719, 60.836755]`
- **Topic category:** geoscientificInformation
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Equivalent scale:** 1:625,000
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update
- **Schema:** `a_british_geological_survey`
- **Table:** `625k_faults`
- **Geometry:** MULTILINESTRING
- **CRS:** EPSG:27700
- **Rows:** 2741
- **Columns:** 14
- **Metadata status:** context_curated

## Description

Generalised 1:625,000-scale linework representing mapped geological faults and thrust faults in Great Britain.

## Lineage

Published by British Geological Survey as part of BGS geological data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `category` | `varchar(32)` | Map-series category assigned to the fault feature, such as 625k. |
| `feature` | `varchar(60)` | Fault feature type, such as a fault or thrust fault with hanging-wall barbs. |
| `feature_d` | `varchar(100)` | Human-readable description associated with the corresponding coded attribute. |
| `fltname_c` | `varchar(6)` | Source code for the named fault, where a recognised fault name is available. |
| `fltname_d` | `varchar(100)` | Human-readable description associated with the corresponding coded attribute. |
| `sheet` | `varchar(60)` | Name of the source geological map sheet or digital layer. |
| `version` | `varchar(10)` | Version number of the published BGS dataset. |
| `released` | `varchar(10)` | Date on which this version of the dataset was released. |
| `nom_scale` | `varchar(10)` | Nominal map scale denominator, such as 625000 for 1:625,000 mapping. |
| `nom_os_yr` | `varchar(10)` | Nominal year or edition of the Ordnance Survey base mapping. |
| `nom_bgs_yr` | `varchar(10)` | Nominal year of the BGS geological compilation. |
| `mslink` | `bigint` | Internal source-system link identifier used by the original mapping database. |
| `625f_pk` | `integer` | Primary-key value for a 1:625,000 fault feature. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
