# Priority Habitats Inventory England

## Overview

- **Identifier:** `a_natural_england/priority_habitats_inventory_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England
- **WGS84 extent:** `[-6.401221, 49.869904, 1.757372, 55.811098]`
- **Topic category:** environment
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_natural_england`
- **Table:** `priority_habitats_inventory_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 799637
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Version: 20251118
Source: https://www.data.gov.uk/dataset/4b6ddab7-6c0f-4407-946e-d6499f19fcde/priority-habitats-inventory-england

Attribution:
© Natural England 2025.
Contains OS data © Crown copyright and database rights 2022. OS
AC0000851168.
Contains data supplied by and reproduced with permission of Arnside
and Silverdale AONB and Lancaster City Council.
Contains data created and provided by Cumbria Biodiversity Data
Centre on behalf of Cumbria Wildlife Trust. The data has been
extracted from Cumbria Wildlife Trust’s Grassland Inventory and is used
under a CC BY 4.0 International Licence.
Contains, or is based on, information supplied by the Forestry
Commission. © Crown copyright and database right 2022. Ordnance
Survey 100021242.
Contains data created and provided by the National Trust, used under a
CC BY 4.0 International Licence.
Contains Environment Agency data © Environment Agency copyright
and/or database right 2015. All rights reserved. Contains Ordnance
Survey data © Crown copyright and database right 2014.
Contains Northumberland National Park Authority data licenced under
the Open Government Licence v3.0.
Contains, or is derived from, information supplied by Natural England
and the Ordnance Survey. © Crown copyright and database rights 2022.
Ordnance Survey AC0000851168.
© Natural England 2021 © Crown Copyright and database rights 2021.
Ordnance Survey AC0000851168. © Environment Agency 2021.
Contains, or is derived from, Rural Payments Agency data. © Rural
Payments Agency. Contains Ordnance Survey data. Crown copyright
and database right 2023.
Contains North Yorkshire Council data © North Yorkshire Council.

## Lineage

Published by Natural England as open environmental and conservation data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `mainhabs` | `varchar` | Publisher-supplied mainhabs for the represented feature or record. |
| `habcodes` | `varchar` | Publisher-supplied habcodes for the represented feature or record. |
| `featdesc` | `varchar` | Publisher-supplied featdesc for the represented feature or record. |
| `featcodes` | `varchar` | Publisher-supplied featcodes for the represented feature or record. |
| `otherclass` | `varchar` | Publisher-supplied otherclass for the represented feature or record. |
| `addhabs` | `varchar` | Publisher-supplied addhabs for the represented feature or record. |
| `primsource` | `varchar` | Publisher-supplied primsource for the represented feature or record. |
| `areaha` | `real` | Numeric areaha value recorded for the feature. |
| `version` | `varchar` | Publisher-supplied version for the represented feature or record. |
| `uid` | `varchar` | Publisher-assigned uid for the record. |
| `globalid` | `varchar` | Publisher-assigned globalid for the record. |
| `objectid` | `bigint` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
