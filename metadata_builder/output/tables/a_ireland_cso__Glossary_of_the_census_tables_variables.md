# Glossary Of The Census Tables Variables

## Overview

- **Identifier:** `a_ireland_cso/Glossary_of_the_census_tables_variables`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_ireland_cso`
- **Table:** `Glossary_of_the_census_tables_variables`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 790
- **Columns:** 5
- **Metadata status:** source_mapped

## Description

Glossary Of The Census Tables Variables is an authoritative dataset published by Central Statistics Office Ireland. It contains records relating to glossary of the census tables variables.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | `integer` | Count or numeric value for identifier in the represented area. |
| `themes` | `varchar` | Publisher-supplied themes for the represented feature or record. |
| `tables within themes` | `varchar` | Publisher-supplied tables within themes for the represented feature or record. |
| `column names` | `varchar` | Publisher-supplied column names for the represented feature or record. |
| `description of field` | `varchar` | Publisher-supplied description of field for the represented feature or record. |
