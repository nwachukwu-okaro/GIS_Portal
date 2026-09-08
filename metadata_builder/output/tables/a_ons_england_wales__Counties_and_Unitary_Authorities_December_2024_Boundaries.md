# Counties And Unitary Authorities December 2024 Boundaries

## Overview

- **Identifier:** `a_ons_england_wales/Counties_and_Unitary_Authorities_December_2024_Boundaries`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **WGS84 extent:** `[-8.650007, 49.864798, 1.763680, 60.860745]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence v3.0 — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ons_england_wales`
- **Table:** `Counties_and_Unitary_Authorities_December_2024_Boundaries`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 218
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Counties And Unitary Authorities December 2024 Boundaries is an authoritative dataset published by Office for National Statistics. It represents counties and unitary authorities december 2024 boundaries features using multipolygon geometry.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `ctyua24cd` | `varchar(9)` |  |
| `ctyua24nm` | `varchar(36)` |  |
| `ctyua24nmw` | `varchar(24)` |  |
| `bng_e` | `integer` | Count or numeric value for bng e in the represented area. |
| `bng_n` | `integer` | Count or numeric value for bng n in the represented area. |
| `long` | `double precision` | Numeric long value recorded for the feature. |
| `lat` | `double precision` | Numeric lat value recorded for the feature. |
| `globalid` | `varchar(38)` | Publisher-assigned globalid for the record. |
