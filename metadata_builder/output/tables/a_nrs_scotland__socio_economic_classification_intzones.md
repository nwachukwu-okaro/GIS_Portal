# Socio Economic Classification Intzones

## Overview

- **Identifier:** `a_nrs_scotland/socio_economic_classification_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `socio_economic_classification_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 18
- **Metadata status:** source_mapped

## Description

Socio Economic Classification Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to socio economic classification intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `all_people_aged_16_and_over` | `double precision` | Count or numeric value for all people aged 16 and over in the represented area. | statistical_value | Yes | No | No |
| `l1_employers_in_large_establishments` | `double precision` | Count or numeric value for l1 employers in large establishments in the represented area. | statistical_value | Yes | No | No |
| `l2_higher_managerial_and_administrative_occupations` | `double precision` | Count or numeric value for l2 higher managerial and administrative occupations in the represented area. | statistical_value | Yes | No | No |
| `l3_higher_professional_occupations` | `double precision` | Count or numeric value for l3 higher professional occupations in the represented area. | statistical_value | Yes | No | No |
| `l4_lower_professional_and_higher_technical_occupations` | `double precision` | Count or numeric value for l4 lower professional and higher technical occupations in the represented area. | statistical_value | Yes | No | No |
| `l5_lower_managerial_and_administrative_occupations` | `double precision` | Count or numeric value for l5 lower managerial and administrative occupations in the represented area. | statistical_value | Yes | No | No |
| `l6_higher_supervisory_occupations` | `double precision` | Count or numeric value for l6 higher supervisory occupations in the represented area. | statistical_value | Yes | No | No |
| `l7_intermediate_occupations` | `double precision` | Count or numeric value for l7 intermediate occupations in the represented area. | statistical_value | Yes | No | No |
| `l8_employers_in_small_establishments` | `double precision` | Count or numeric value for l8 employers in small establishments in the represented area. | statistical_value | Yes | No | No |
| `l9_own_account_workers` | `double precision` | Count or numeric value for l9 own account workers in the represented area. | statistical_value | Yes | No | No |
| `l10_lower_supervisory_occupations` | `double precision` | Count or numeric value for l10 lower supervisory occupations in the represented area. | statistical_value | Yes | No | No |
| `l11_lower_technical_occupations` | `double precision` | Count or numeric value for l11 lower technical occupations in the represented area. | statistical_value | Yes | No | No |
| `l12_semi_routine_occupations` | `double precision` | Count or numeric value for l12 semi routine occupations in the represented area. | statistical_value | Yes | No | No |
| `l13_routine_occupations` | `double precision` | Count or numeric value for l13 routine occupations in the represented area. | statistical_value | Yes | No | No |
| `l14_1_never_worked` | `double precision` | Count or numeric value for l14 1 never worked in the represented area. | statistical_value | Yes | No | No |
| `l14_2_long_term_unemployed` | `double precision` | Numeric l14 2 long term unemployed value recorded for the feature. | measure | Yes | No | No |
| `l15_full_time_students` | `double precision` | Count or numeric value for l15 full time students in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
