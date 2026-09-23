# Occupations Csolea

## Overview

- **Identifier:** `a_ireland_cso/occupations_csolea`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_ireland_cso`
- **Table:** `occupations_csolea`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 167
- **Columns:** 36
- **Metadata status:** source_mapped

## Description

Occupations Csolea is an authoritative dataset published by Central Statistics Office Ireland. It contains records relating to occupations csolea.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `guid` | `text` | UUID-formatted identifier associated with the record; persistence across releases is not confirmed. |
| `geogid` | `text` | Code identifying the geographical area represented by the row. |
| `geogdesc` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `managers_directors_and_senior_officials_males` | `bigint` |  |
| `professional_occupations_males` | `bigint` |  |
| `associate_professional_and_technical_occupations_males` | `bigint` |  |
| `administrative_and_secretarial_occupations_males` | `bigint` |  |
| `skilled_trades_occupations_males` | `bigint` |  |
| `caring_leisure_and_other_service_occupations_males` | `bigint` |  |
| `sales_and_customer_service_occupations_males` | `bigint` |  |
| `process_plant_and_machine_operatives_males` | `bigint` |  |
| `elementary_occupations_males` | `bigint` |  |
| `not_stated_males` | `bigint` |  |
| `total_males` | `bigint` | Census total for males in the represented geographical area; measurement unit requires the table documentation. |
| `managers_directors_and_senior_officials_females` | `bigint` |  |
| `professional_occupations_females` | `bigint` |  |
| `associate_professional_and_technical_occupations_females` | `bigint` |  |
| `administrative_and_secretarial_occupations_females` | `bigint` |  |
| `skilled_trades_occupations_females` | `bigint` |  |
| `caring_leisure_and_other_service_occupations_females` | `bigint` |  |
| `sales_and_customer_service_occupations_females` | `bigint` |  |
| `process_plant_and_machine_operatives_females` | `bigint` |  |
| `elementary_occupations_females` | `bigint` |  |
| `not_stated_females` | `bigint` |  |
| `total_females` | `bigint` | Census total for females in the represented geographical area; measurement unit requires the table documentation. |
| `managers_directors_and_senior_officials_total` | `bigint` |  |
| `professional_occupations_total` | `bigint` |  |
| `associate_professional_and_technical_occupations_total` | `bigint` |  |
| `administrative_and_secretarial_occupations_total` | `bigint` |  |
| `skilled_trades_occupations_total` | `bigint` |  |
| `caring_leisure_and_other_service_occupations_total` | `bigint` |  |
| `sales_and_customer_service_occupations_total` | `bigint` |  |
| `process_plant_and_machine_operatives_total` | `bigint` |  |
| `elementary_occupations_total` | `bigint` |  |
| `not_stated_total` | `bigint` |  |
| `total` | `bigint` |  |
