# Boundary Census Sexual Orientation Data 2021 Dea

## Overview

- **Identifier:** `a_nisra_nireland/boundary_census_sexual_orientation_data_2021_dea`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **WGS84 extent:** `[-8.177502, 54.022724, -5.432789, 55.312984]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_nisra_nireland`
- **Table:** `boundary_census_sexual_orientation_data_2021_dea`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:4326
- **Rows:** 80
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Boundary Census Sexual Orientation Data 2021 Dea is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It represents boundary census sexual orientation data 2021 dea features using multipolygon geometry.

## Lineage

Published by the Northern Ireland Statistics and Research Agency as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geocode` | `text` | Publisher-assigned geocode for the record. |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `year` | `bigint` | Count or numeric value for year in the represented area. |
| `population` | `text` | Publisher-supplied population for the represented feature or record. |
| `sexual_orientation_gay_lesbian_bisexual_or_other_sexual_orienta` | `text` | Publisher-supplied sexual orientation gay lesbian bisexual or other sexual orienta for the represented feature or record. |
| `sexual_orientation_prefer_not_to_say_or_not_stated` | `text` | Publisher-supplied sexual orientation prefer not to say or not stated for the represented feature or record. |
| `sexual_orientation_straight_or_heterosexual` | `text` | Publisher-supplied sexual orientation straight or heterosexual for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
