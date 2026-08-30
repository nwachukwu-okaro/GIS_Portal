# Census Area Explorer Migration Data 2021 Lgd

## Overview

- **Identifier:** `a_nisra_nireland/census_area_explorer_migration_data_2021_lgd`
- **Source organisation:** Northern Ireland Statistics and Research Agency
- **Source:** https://www.nisra.gov.uk/statistics/geography/geographic-data
- **Geographic coverage:** Northern Ireland
- **Schema:** `a_nisra_nireland`
- **Table:** `census_area_explorer_migration_data_2021_lgd`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 22
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Census Area Explorer Migration Data 2021 Lgd is an authoritative dataset published by Northern Ireland Statistics and Research Agency. It contains records relating to census area explorer migration data 2021 lgd.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geocode` | `text` | Publisher-assigned geocode for the record. | source_identifier | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `year` | `bigint` | Count or numeric value for year in the represented area. | statistical_value | Yes | No | No |
| `population` | `text` | Publisher-supplied population for the represented feature or record. | source_attribute | Yes | No | No |
| `address_one_year_ago_different_address_outside_northern_ireland` | `text` | Publisher-supplied address one year ago different address outside northern ireland for the represented feature or record. | source_attribute | Yes | No | No |
| `address_one_year_ago_different_address_within_northern_ireland` | `text` | Publisher-supplied address one year ago different address within northern ireland for the represented feature or record. | source_attribute | Yes | No | No |
| `address_one_year_ago_lived_at_same_address` | `text` | Publisher-supplied address one year ago lived at same address for the represented feature or record. | source_attribute | Yes | No | No |
| `year_of_arrival_to_live_in_ni_arrived_2001_2010` | `text` | Publisher-supplied year of arrival to live in ni arrived 2001 2010 for the represented feature or record. | source_attribute | Yes | No | No |
| `year_of_arrival_to_live_in_ni_arrived_2011_2021` | `text` | Publisher-supplied year of arrival to live in ni arrived 2011 2021 for the represented feature or record. | source_attribute | Yes | No | No |
| `year_of_arrival_to_live_in_ni_arrived_before_2001` | `text` | Publisher-supplied year of arrival to live in ni arrived before 2001 for the represented feature or record. | source_attribute | Yes | No | No |
| `year_of_arrival_to_live_in_ni_born_in_northern_ireland` | `text` | Publisher-supplied year of arrival to live in ni born in northern ireland for the represented feature or record. | source_attribute | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
