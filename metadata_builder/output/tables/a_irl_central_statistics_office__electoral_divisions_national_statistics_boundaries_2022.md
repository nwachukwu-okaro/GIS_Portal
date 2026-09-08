# Electoral Divisions National Statistics Boundaries 2022

## Overview

- **Identifier:** `a_irl_central_statistics_office/electoral_divisions_national_statistics_boundaries_2022`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **WGS84 extent:** `[-10.662960, 51.419897, -5.996278, 55.446580]`
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_irl_central_statistics_office`
- **Table:** `electoral_divisions_national_statistics_boundaries_2022`
- **Geometry:** MULTIPOLYGON
- **CRS:** EPSG:2157
- **Rows:** 3420
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

CSO Electoral Divisions - National Statistical Boundaries - 2022 - Generalised 50mCSO EDs are a statistical geography that aligns closely with the official ED boundary. EDs are comprised of whole Small Areas. In a small number of cases, CSO EDs do not align with the official boundary, where EDs are amalgamated to ensure statistical confidentiality or where a change was required to ensure better CSO ED/CSO alignment.Creation of generalised versions of Published ED boundaries. Using Douglas-Peucker algorithm with tolerances of 20m, 50m, 100m and writes out features classes. Uses topology and option of preserving common boundaries to ensure output does not generalise differently on common boundaries.Update Notice: 4th August 2023: ED and LEA attributes changed on 15 SAs.  As a result of the changes to SAs, CSO ED has one additional ED and the number of CSO EDs is 3420 and there is a change to 2 CSO LEAs. The ED and LEAs impacted are <o:p></o:p>

ED 2ae19629-1d37-13a3-e055-000000000001 renamed to DALKEY-COLIEMORE<o:p></o:p>

ED 94b26e15-6ed2-44c2-a0b0-207c369a2da8 SHANKILL-RATHSALLAGH added<o:p></o:p>

LEA 40aece0e-a19d-4e78-af9d-e129f5557496  DÚN LAOGHAIRE redrawn<o:p></o:p>

LEA d65ef6e7-75e6-49d9-bda9-d4690e8f68dc KILLINEY-SHANKILL redrawn<o:p></o:p>

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `ed_guid` | `text` | Publisher-assigned ed guid for the record. |
| `ed_official` | `text` | Publisher-supplied ed official for the represented feature or record. |
| `ed_english` | `text` | Publisher-supplied ed english for the represented feature or record. |
| `ed_gaeilge` | `text` | Publisher-supplied ed gaeilge for the represented feature or record. |
| `ed_id_str` | `text` | Publisher-supplied ed identifier str for the represented feature or record. |
| `ed_part_count` | `smallint` | Count or numeric value for ed part count in the represented area. |
| `county_code` | `text` | Code assigned by the source dataset. |
| `county_english` | `text` | Publisher-supplied county english for the represented feature or record. |
| `county_gaeilge` | `text` | Publisher-supplied county gaeilge for the represented feature or record. |
| `cso_lea` | `text` | Publisher-supplied cso lea for the represented feature or record. |
| `objectid` | `integer` | Source-system row identifier; useful internally but not guaranteed to remain stable between data releases. |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
