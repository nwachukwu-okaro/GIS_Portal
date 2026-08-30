# Highest Level Qualification Intzones

## Overview

- **Identifier:** `a_nrs_scotland/highest_level_qualification_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `highest_level_qualification_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Highest Level Qualification Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to highest level qualification intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `all_people_aged_16_and_over` | `double precision` | Count or numeric value for all people aged 16 and over in the represented area. | statistical_value | Yes | No | No |
| `no_qualifications` | `double precision` | Count or numeric value for number qualifications in the represented area. | statistical_value | Yes | No | No |
| `lower_school_qualifications` | `double precision` | Count or numeric value for lower school qualifications in the represented area. | statistical_value | Yes | No | No |
| `upper_school_qualifications` | `double precision` | Count or numeric value for upper school qualifications in the represented area. | statistical_value | Yes | No | No |
| `apprenticeship_qualifications` | `double precision` | Count or numeric value for apprenticeship qualifications in the represented area. | statistical_value | Yes | No | No |
| `further_education_and_sub_degree_higher_education_qualificat` | `double precision` | Count or numeric value for further education and sub degree higher education qualificat in the represented area. | statistical_value | Yes | No | No |
| `degree_level_qualifications_or_above` | `double precision` | Count or numeric value for degree level qualifications or above in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
