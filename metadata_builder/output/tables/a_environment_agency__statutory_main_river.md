# Statutory Main Rivers

## Overview

- **Identifier:** `a_environment_agency/statutory_main_river`
- **Source organisation:** Environment Agency
- **Source:** https://environment.data.gov.uk/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-5.703383, 49.986932, 1.756276, 55.707770]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_environment_agency`
- **Table:** `statutory_main_river`
- **Geometry:** MULTICURVE
- **CRS:** EPSG:27700
- **Rows:** 183911
- **Columns:** 5
- **Metadata status:** context_curated

## Description

Line network of watercourses legally designated as Main River in England, where the Environment Agency has permissive powers for flood-risk management.

## Lineage

Published by Environment Agency as open environmental data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
| `status` | `text` | Legal or operational classification of the watercourse, such as Main River. |
| `length_km` | `double precision` | Calculated length of the watercourse feature in kilometres. |
| `shape_length` | `double precision` | Source GIS length measurement for the line geometry in dataset units. |
