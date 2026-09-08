# Migration Data 2021 Dea

## Overview

- **Identifier:** `a_nisra_nireland/migration_data_2021_dea`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_nisra_nireland`
- **Table:** `migration_data_2021_dea`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 80
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Migration Data 2021 Dea is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It contains records relating to migration data 2021 dea.

## Lineage

Published by the Northern Ireland Statistics and Research Agency as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geocode` | `text` | Publisher-assigned geocode for the record. |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `year` | `bigint` | Count or numeric value for year in the represented area. |
| `address_one_year_ago_different_address_outside_northern_ireland` | `text` | Publisher-supplied address one year ago different address outside northern ireland for the represented feature or record. |
| `address_one_year_ago_different_address_within_northern_ireland` | `text` | Publisher-supplied address one year ago different address within northern ireland for the represented feature or record. |
| `address_one_year_ago_lived_at_same_address` | `text` | Publisher-supplied address one year ago lived at same address for the represented feature or record. |
| `year_of_arrival_to_live_in_ni_arrived_2001_2010` | `text` | Publisher-supplied year of arrival to live in ni arrived 2001 2010 for the represented feature or record. |
| `year_of_arrival_to_live_in_ni_arrived_2011_2021` | `text` | Publisher-supplied year of arrival to live in ni arrived 2011 2021 for the represented feature or record. |
| `year_of_arrival_to_live_in_ni_arrived_before_2001` | `text` | Publisher-supplied year of arrival to live in ni arrived before 2001 for the represented feature or record. |
| `year_of_arrival_to_live_in_ni_born_in_northern_ireland` | `text` | Publisher-supplied year of arrival to live in ni born in northern ireland for the represented feature or record. |
