# Flood Zones 2 and 3 - Rivers and Sea

## Overview

- **Identifier:** `a_environment_agency/flood_zones_2_3_rivers_and_sea`
- **Source organisation:** Environment Agency
- **Source:** https://environment.data.gov.uk/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.366581, 49.882243, 1.763602, 55.811634]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_environment_agency`
- **Table:** `flood_zones_2_3_rivers_and_sea`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 12804126
- **Columns:** 5
- **Metadata status:** context_curated

## Description

Modelled Flood Zone 2 and Flood Zone 3 extents showing land at risk from flooding from rivers or the sea, without accounting for defences.

## Lineage

Published by Environment Agency as open environmental data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `origin` | `text` | Evidence or modelling source used to define the flood-zone extent. |
| `flood_zone` | `text` | Flood-zone class, such as FZ2 or FZ3. |
| `flood_source` | `text` | Source of flooding represented, such as river, sea or surface water. |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
