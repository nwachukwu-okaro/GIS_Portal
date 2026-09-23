# Places

## Overview

- **Identifier:** `a_overture_maps/places`
- **Source organisation:** Overture Maps Foundation
- **Product:** Overture Maps
- **Source:** https://docs.overturemaps.org/
- **Geographic coverage:** Global
- **WGS84 extent:** `[-10.656273, 49.300012, 2.880000, 63.233627]`
- **Topic category:** location
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_overture_maps`
- **Table:** `places`
- **Geometry:** MULTIPOINT
- **CRS:** EPSG:4326
- **Rows:** 3507636
- **Columns:** 14
- **Metadata status:** source_mapped

## Description

Places is part of Overture Maps, published by Overture Maps Foundation. It represents places features using multipoint geometry.

## Lineage

Published by Overture Maps Foundation as part of Overture Maps. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `varchar` | Primary-key identifier for records in places. |
| `categories.primary` | `varchar` |  |
| `confidence` | `double precision` |  |
| `brand.wikidata` | `varchar` |  |
| `brand.names.primary` | `varchar` |  |
| `names.primary` | `varchar` |  |
| `basic_category` | `varchar` |  |
| `taxonomy.primary` | `varchar` |  |
| `version` | `integer` |  |
| `filename` | `varchar` |  |
| `theme` | `varchar` |  |
| `type` | `varchar` |  |
| `addresses` | `json` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
