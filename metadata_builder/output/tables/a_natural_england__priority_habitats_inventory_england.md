# Priority Habitats Inventory England

## Overview

- **Identifier:** `a_natural_england/priority_habitats_inventory_england`
- **Source organisation:** Natural England
- **Source:** https://naturalengland-defra.opendata.arcgis.com/
- **Schema:** `a_natural_england`
- **Table:** `priority_habitats_inventory_england`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 799637
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

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `mainhabs` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `habcodes` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `featdesc` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `featcodes` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `otherclass` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `addhabs` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `primsource` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `areaha` | `real` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `version` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `uid` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `globalid` | `varchar` | Source attribute; its precise meaning has not yet been documented. | Unclassified | Yes | No | No |
| `objectid` | `bigint` | Source-system object identifier. | identifier | Yes | No | No |
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

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
