# Inspire Polygons

## Overview

- **Identifier:** `a_hm_land_registry/inspire_polygons`
- **Source organisation:** HM Land Registry
- **Source:** https://use-land-property-data.service.gov.uk/
- **WGS84 extent:** `[-6.418949, 49.864637, 1.763316, 55.811678]`
- **Topic category:** planningCadastre
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_hm_land_registry`
- **Table:** `inspire_polygons`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:27700
- **Rows:** 24422678
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Inspire Polygons is an authoritative dataset published by HM Land Registry. It represents inspire polygons features using multipolygon geometry.

## Lineage

Published by HM Land Registry as open land and property data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `ogc_fid` | `integer` | Internal OGC feature identifier assigned during publication. |
| `gml_id` | `text` | Identifier assigned by the source dataset. |
| `inspireid` | `integer` | INSPIRE identifier assigned to the cadastral parcel feature. |
| `label` | `integer` | Numeric label used to identify or display the cadastral parcel. |
| `nationalcadastralreference` | `integer` | National cadastral reference associated with the parcel polygon. |
| `validfrom` | `text` | Date and time from which the cadastral feature is valid in the source dataset. |
| `beginlifespanversion` | `text` | Date and time when this version of the INSPIRE feature began its lifecycle. |
| `fid` | `bigint` | Feature identifier assigned by the source or import process. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
