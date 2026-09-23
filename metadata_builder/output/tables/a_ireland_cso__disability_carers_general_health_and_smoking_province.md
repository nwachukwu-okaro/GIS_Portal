# Disability Carers General Health And Smoking Province

## Overview

- **Identifier:** `a_ireland_cso/disability_carers_general_health_and_smoking_province`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_ireland_cso`
- **Table:** `disability_carers_general_health_and_smoking_province`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 5
- **Columns:** 34
- **Metadata status:** source_mapped

## Description

Disability Carers General Health And Smoking Province is an authoritative dataset published by Central Statistics Office Ireland. It contains records relating to disability carers general health and smoking province.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `guid` | `text` |  |
| `geogid` | `text` | Code identifying the geographical area represented by the row. |
| `geogdesc` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `males` | `bigint` |  |
| `females` | `bigint` |  |
| `total_perons` | `bigint` |  |
| `males_1` | `bigint` |  |
| `females_1` | `bigint` |  |
| `total` | `bigint` |  |
| `very_good_males` | `bigint` |  |
| `very_good_females` | `bigint` |  |
| `very_good_total` | `bigint` |  |
| `good_males` | `bigint` |  |
| `good_females` | `bigint` |  |
| `good_total` | `bigint` |  |
| `fair_males` | `bigint` |  |
| `fair_females` | `bigint` |  |
| `fair_total` | `bigint` |  |
| `bad_males` | `bigint` |  |
| `bad_females` | `bigint` |  |
| `bad_total` | `bigint` |  |
| `very_bad_males` | `bigint` |  |
| `very_bad_females` | `bigint` |  |
| `very_bad_total` | `bigint` |  |
| `not_stated_males` | `bigint` |  |
| `not_stated_females` | `bigint` |  |
| `not_stated_total` | `bigint` |  |
| `total_males` | `bigint` | Census total for males in the represented geographical area; measurement unit requires the table documentation. |
| `total_females` | `bigint` | Census total for females in the represented geographical area; measurement unit requires the table documentation. |
| `total_1` | `bigint` |  |
| `persons_who_smoke` | `bigint` |  |
| `persons_who_dont_smoke` | `bigint` |  |
| `non_stated` | `bigint` |  |
| `total_persons` | `bigint` |  |
