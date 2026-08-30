# Census2021 Ts063 Msoa

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts063_msoa`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts063_msoa`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 7264
- **Columns:** 13
- **Metadata status:** source_mapped

## Description

Census2021 Ts063 Msoa is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts063 msoa.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. | statistical_value | Yes | No | No |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `geography_code` | `text` | Code assigned by the source dataset. | code | Yes | No | No |
| `total_all_usual_residents_aged_16_years_and_over_in_employment` | `bigint` | Count or numeric value for total all usual residents aged 16 years and over in employment in the represented area. | statistical_value | Yes | No | No |
| `col_1_managers_directors_and_senior_officials` | `bigint` | Count or numeric value for col 1 managers directors and senior officials in the represented area. | statistical_value | Yes | No | No |
| `col_2_professional_occupations` | `bigint` | Count or numeric value for col 2 professional occupations in the represented area. | statistical_value | Yes | No | No |
| `col_3_associate_professional_and_technical_occupations` | `bigint` | Count or numeric value for col 3 associate professional and technical occupations in the represented area. | statistical_value | Yes | No | No |
| `col_4_administrative_and_secretarial_occupations` | `bigint` | Count or numeric value for col 4 administrative and secretarial occupations in the represented area. | statistical_value | Yes | No | No |
| `col_5_skilled_trades_occupations` | `bigint` | Count or numeric value for col 5 skilled trades occupations in the represented area. | statistical_value | Yes | No | No |
| `col_6_caring_leisure_and_other_service_occupations` | `bigint` | Count or numeric value for col 6 caring leisure and other service occupations in the represented area. | statistical_value | Yes | No | No |
| `col_7_sales_and_customer_service_occupations` | `bigint` | Count or numeric value for col 7 sales and customer service occupations in the represented area. | statistical_value | Yes | No | No |
| `col_8_process_plant_and_machine_operatives` | `bigint` | Count or numeric value for col 8 process plant and machine operatives in the represented area. | statistical_value | Yes | No | No |
| `col_9_elementary_occupations` | `bigint` | Count or numeric value for col 9 elementary occupations in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
