# Job Density Ctry

## Overview

- **Identifier:** `a_ons_england_wales/job_density_ctry`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence v3.0 — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update
- **Schema:** `a_ons_england_wales`
- **Table:** `job_density_ctry`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 40
- **Columns:** 9
- **Metadata status:** source_mapped

## Description

Job Density Ctry is an authoritative dataset published by Office for National Statistics. It contains records relating to job density ctry.

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
| `date` | `integer` | Count or numeric value for date in the represented area. |
| `england` | `double precision` |  |
| `england and wales` | `double precision` |  |
| `great britain` | `double precision` |  |
| `northern ireland` | `varchar` |  |
| `scotland` | `double precision` |  |
| `united kingdom` | `varchar` |  |
| `wales` | `double precision` |  |
