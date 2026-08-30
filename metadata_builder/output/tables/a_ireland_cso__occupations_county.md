# Occupations County

## Overview

- **Identifier:** `a_ireland_cso/occupations_county`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **Schema:** `a_ireland_cso`
- **Table:** `occupations_county`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 32
- **Columns:** 36
- **Metadata status:** source_mapped

## Description

Occupations County is an authoritative dataset published by Central Statistics Office Ireland. It contains records relating to occupations county.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `guid` | `text` | Publisher-assigned guid for the record. | source_identifier | Yes | No | No |
| `geogid` | `text` | Publisher-assigned geogid for the record. | source_identifier | Yes | No | No |
| `geogdesc` | `text` | Publisher-supplied geogdesc for the represented feature or record. | source_attribute | Yes | No | No |
| `managers_directors_and_senior_officials_males` | `bigint` | Count or numeric value for managers directors and senior officials males in the represented area. | statistical_value | Yes | No | No |
| `professional_occupations_males` | `bigint` | Count or numeric value for professional occupations males in the represented area. | statistical_value | Yes | No | No |
| `associate_professional_and_technical_occupations_males` | `bigint` | Count or numeric value for associate professional and technical occupations males in the represented area. | statistical_value | Yes | No | No |
| `administrative_and_secretarial_occupations_males` | `bigint` | Count or numeric value for administrative and secretarial occupations males in the represented area. | statistical_value | Yes | No | No |
| `skilled_trades_occupations_males` | `bigint` | Count or numeric value for skilled trades occupations males in the represented area. | statistical_value | Yes | No | No |
| `caring_leisure_and_other_service_occupations_males` | `bigint` | Count or numeric value for caring leisure and other service occupations males in the represented area. | statistical_value | Yes | No | No |
| `sales_and_customer_service_occupations_males` | `bigint` | Count or numeric value for sales and customer service occupations males in the represented area. | statistical_value | Yes | No | No |
| `process_plant_and_machine_operatives_males` | `bigint` | Count or numeric value for process plant and machine operatives males in the represented area. | statistical_value | Yes | No | No |
| `elementary_occupations_males` | `bigint` | Count or numeric value for elementary occupations males in the represented area. | statistical_value | Yes | No | No |
| `not_stated_males` | `bigint` | Count or numeric value for not stated males in the represented area. | statistical_value | Yes | No | No |
| `total_males` | `bigint` | Count or numeric value for total males in the represented area. | statistical_value | Yes | No | No |
| `managers_directors_and_senior_officials_females` | `bigint` | Count or numeric value for managers directors and senior officials females in the represented area. | statistical_value | Yes | No | No |
| `professional_occupations_females` | `bigint` | Count or numeric value for professional occupations females in the represented area. | statistical_value | Yes | No | No |
| `associate_professional_and_technical_occupations_females` | `bigint` | Count or numeric value for associate professional and technical occupations females in the represented area. | statistical_value | Yes | No | No |
| `administrative_and_secretarial_occupations_females` | `bigint` | Count or numeric value for administrative and secretarial occupations females in the represented area. | statistical_value | Yes | No | No |
| `skilled_trades_occupations_females` | `bigint` | Count or numeric value for skilled trades occupations females in the represented area. | statistical_value | Yes | No | No |
| `caring_leisure_and_other_service_occupations_females` | `bigint` | Count or numeric value for caring leisure and other service occupations females in the represented area. | statistical_value | Yes | No | No |
| `sales_and_customer_service_occupations_females` | `bigint` | Count or numeric value for sales and customer service occupations females in the represented area. | statistical_value | Yes | No | No |
| `process_plant_and_machine_operatives_females` | `bigint` | Count or numeric value for process plant and machine operatives females in the represented area. | statistical_value | Yes | No | No |
| `elementary_occupations_females` | `bigint` | Count or numeric value for elementary occupations females in the represented area. | statistical_value | Yes | No | No |
| `not_stated_females` | `bigint` | Count or numeric value for not stated females in the represented area. | statistical_value | Yes | No | No |
| `total_females` | `bigint` | Count or numeric value for total females in the represented area. | statistical_value | Yes | No | No |
| `managers_directors_and_senior_officials_total` | `bigint` | Count or numeric value for managers directors and senior officials total in the represented area. | statistical_value | Yes | No | No |
| `professional_occupations_total` | `bigint` | Count or numeric value for professional occupations total in the represented area. | statistical_value | Yes | No | No |
| `associate_professional_and_technical_occupations_total` | `bigint` | Count or numeric value for associate professional and technical occupations total in the represented area. | statistical_value | Yes | No | No |
| `administrative_and_secretarial_occupations_total` | `bigint` | Count or numeric value for administrative and secretarial occupations total in the represented area. | statistical_value | Yes | No | No |
| `skilled_trades_occupations_total` | `bigint` | Count or numeric value for skilled trades occupations total in the represented area. | statistical_value | Yes | No | No |
| `caring_leisure_and_other_service_occupations_total` | `bigint` | Count or numeric value for caring leisure and other service occupations total in the represented area. | statistical_value | Yes | No | No |
| `sales_and_customer_service_occupations_total` | `bigint` | Count or numeric value for sales and customer service occupations total in the represented area. | statistical_value | Yes | No | No |
| `process_plant_and_machine_operatives_total` | `bigint` | Count or numeric value for process plant and machine operatives total in the represented area. | statistical_value | Yes | No | No |
| `elementary_occupations_total` | `bigint` | Count or numeric value for elementary occupations total in the represented area. | statistical_value | Yes | No | No |
| `not_stated_total` | `bigint` | Count or numeric value for not stated total in the represented area. | statistical_value | Yes | No | No |
| `total` | `bigint` | Count or numeric value for total in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
