# Qgis Projects

## Overview

- **Identifier:** `a_british_geological_survey/qgis_projects`
- **Source organisation:** British Geological Survey
- **Product:** BGS geological data
- **Source:** https://www.bgs.ac.uk/geological-data/
- **Licence:** [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** Great Britain
- **Topic category:** geoscientificInformation
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update
- **Schema:** `a_british_geological_survey`
- **Table:** `qgis_projects`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1
- **Columns:** 3
- **Metadata status:** source_mapped

## Description

Qgis Projects is part of BGS geological data, published by British Geological Survey. It contains records relating to qgis projects.

## Lineage

Published by British Geological Survey as part of BGS geological data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `name` | `text` | Official or publisher-assigned name of the represented feature. |
| `metadata` | `jsonb` |  |
| `content` | `bytea` |  |
