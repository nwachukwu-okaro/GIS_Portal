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
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
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
| `id` | `varchar` | Publisher-assigned identifier for the record. |
| `categories.primary` | `varchar` | Publisher-supplied categories primary for the represented feature or record. |
| `confidence` | `double precision` | Count or numeric value for confidence in the represented area. |
| `brand.wikidata` | `varchar` | Publisher-supplied brand wikidata for the represented feature or record. |
| `brand.names.primary` | `varchar` | Publisher-supplied brand names primary for the represented feature or record. |
| `names.primary` | `varchar` | Publisher-supplied names primary for the represented feature or record. |
| `basic_category` | `varchar` | Publisher-supplied basic category for the represented feature or record. |
| `taxonomy.primary` | `varchar` | Publisher-supplied taxonomy primary for the represented feature or record. |
| `version` | `integer` | Count or numeric value for version in the represented area. |
| `filename` | `varchar` | Publisher-supplied filename for the represented feature or record. |
| `theme` | `varchar` | Publisher-supplied theme for the represented feature or record. |
| `type` | `varchar` | Publisher-supplied type for the represented feature or record. |
| `addresses` | `json` | Publisher-supplied addresses for the represented feature or record. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
