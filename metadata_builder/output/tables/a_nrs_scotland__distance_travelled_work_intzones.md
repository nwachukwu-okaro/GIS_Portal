# Distance Travelled Work Intzones

## Overview

- **Identifier:** `a_nrs_scotland/distance_travelled_work_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Schema:** `a_nrs_scotland`
- **Table:** `distance_travelled_work_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1282
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Distance Travelled Work Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to distance travelled work intzones.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. | source_attribute | Yes | No | No |
| `all_people_aged_16_and_over_in_employment_the_week_before_the_c` | `text` | Publisher-supplied all people aged 16 and over in employment the week before the c for the represented feature or record. | source_attribute | Yes | No | No |
| `mainly_work_from_home` | `text` | Publisher-supplied mainly work from home for the represented feature or record. | source_attribute | Yes | No | No |
| `less_than_2km` | `text` | Publisher-supplied less than 2km for the represented feature or record. | source_attribute | Yes | No | No |
| `t_2km_to_less_than_5km` | `text` | Publisher-supplied t 2km to less than 5km for the represented feature or record. | source_attribute | Yes | No | No |
| `t_5km_to_less_than_10km` | `text` | Publisher-supplied t 5km to less than 10km for the represented feature or record. | source_attribute | Yes | No | No |
| `t_10km_to_less_than_20km` | `text` | Publisher-supplied t 10km to less than 20km for the represented feature or record. | source_attribute | Yes | No | No |
| `t_20km_to_less_than_30km` | `double precision` | Count or numeric value for t 20km to less than 30km in the represented area. | statistical_value | Yes | No | No |
| `t_30km_to_less_than_40km` | `double precision` | Count or numeric value for t 30km to less than 40km in the represented area. | statistical_value | Yes | No | No |
| `t_40km_to_less_than_60km` | `double precision` | Count or numeric value for t 40km to less than 60km in the represented area. | statistical_value | Yes | No | No |
| `t_60km_and_over` | `double precision` | Count or numeric value for t 60km and over in the represented area. | statistical_value | Yes | No | No |
| `other_no_fixed_place_of_work_or_working_outside_the_uk` | `double precision` | Count or numeric value for other number fixed place of work or working outside the uk in the represented area. | statistical_value | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Licence has not yet been verified.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
