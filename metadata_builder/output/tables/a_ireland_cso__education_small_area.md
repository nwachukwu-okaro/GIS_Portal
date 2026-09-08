# Education Small Area

## Overview

- **Identifier:** `a_ireland_cso/education_small_area`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_ireland_cso`
- **Table:** `education_small_area`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 18920
- **Columns:** 80
- **Metadata status:** source_mapped

## Description

Education Small Area is an authoritative dataset published by Central Statistics Office Ireland. It contains records relating to education small area.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `guid` | `text` | Publisher-assigned guid for the record. |
| `geogid` | `text` | Publisher-assigned geogid for the record. |
| `geogdesc` | `text` | Publisher-supplied geogdesc for the represented feature or record. |
| `ur_category` | `double precision` | Count or numeric value for ur category in the represented area. |
| `ur_category_desc` | `text` | Publisher-supplied ur category description for the represented feature or record. |
| `age_under_15_males` | `bigint` | Count or numeric value for age under 15 males in the represented area. |
| `age_15_males` | `bigint` | Count or numeric value for age 15 males in the represented area. |
| `age_16_males` | `bigint` | Count or numeric value for age 16 males in the represented area. |
| `age_17_males` | `bigint` | Count or numeric value for age 17 males in the represented area. |
| `age_18_males` | `bigint` | Count or numeric value for age 18 males in the represented area. |
| `age_19_males` | `bigint` | Count or numeric value for age 19 males in the represented area. |
| `age_20_males` | `bigint` | Count or numeric value for age 20 males in the represented area. |
| `age_21_and_over_males` | `bigint` | Count or numeric value for age 21 and over males in the represented area. |
| `not_stated_males` | `bigint` | Count or numeric value for not stated males in the represented area. |
| `total_males` | `bigint` | Count or numeric value for total males in the represented area. |
| `age_under_15_females` | `bigint` | Count or numeric value for age under 15 females in the represented area. |
| `age_15_females` | `bigint` | Count or numeric value for age 15 females in the represented area. |
| `age_16_females` | `bigint` | Count or numeric value for age 16 females in the represented area. |
| `age_17_females` | `bigint` | Count or numeric value for age 17 females in the represented area. |
| `age_18_females` | `bigint` | Count or numeric value for age 18 females in the represented area. |
| `age_19_females` | `bigint` | Count or numeric value for age 19 females in the represented area. |
| `age_20_females` | `bigint` | Count or numeric value for age 20 females in the represented area. |
| `age_21_and_over_females` | `bigint` | Count or numeric value for age 21 and over females in the represented area. |
| `not_stated_females` | `bigint` | Count or numeric value for not stated females in the represented area. |
| `total_females` | `bigint` | Count or numeric value for total females in the represented area. |
| `age_under_15_total` | `bigint` | Count or numeric value for age under 15 total in the represented area. |
| `age_15_total` | `bigint` | Count or numeric value for age 15 total in the represented area. |
| `age_16_total` | `bigint` | Count or numeric value for age 16 total in the represented area. |
| `age_17_total` | `bigint` | Count or numeric value for age 17 total in the represented area. |
| `age_18_total` | `bigint` | Count or numeric value for age 18 total in the represented area. |
| `age_19_total` | `bigint` | Count or numeric value for age 19 total in the represented area. |
| `age_20_total` | `bigint` | Count or numeric value for age 20 total in the represented area. |
| `age_21_and_over_total` | `bigint` | Count or numeric value for age 21 and over total in the represented area. |
| `not_stated_total` | `bigint` | Count or numeric value for not stated total in the represented area. |
| `total` | `bigint` | Count or numeric value for total in the represented area. |
| `still_at_school_or_college_males` | `bigint` | Count or numeric value for still at school or college males in the represented area. |
| `other_males` | `bigint` | Count or numeric value for other males in the represented area. |
| `still_at_school_or_college_females` | `bigint` | Count or numeric value for still at school or college females in the represented area. |
| `other_females` | `bigint` | Count or numeric value for other females in the represented area. |
| `still_at_school_or_college_total` | `bigint` | Count or numeric value for still at school or college total in the represented area. |
| `other_total` | `bigint` | Count or numeric value for other total in the represented area. |
| `no_formal_education_males` | `bigint` | Count or numeric value for number formal education males in the represented area. |
| `primary_education_males` | `bigint` | Count or numeric value for primary education males in the represented area. |
| `lower_secondary_males` | `bigint` | Count or numeric value for lower secondary males in the represented area. |
| `upper_secondary_males` | `bigint` | Count or numeric value for upper secondary males in the represented area. |
| `technical_or_vocational_qualification_males` | `bigint` | Count or numeric value for technical or vocational qualification males in the represented area. |
| `advanced_certificatecompleted_apprenticeship_males` | `bigint` | Count or numeric value for advanced certificatecompleted apprenticeship males in the represented area. |
| `higher_certificate_males` | `bigint` | Count or numeric value for higher certificate males in the represented area. |
| `ordinary_bachelor_degree_or_national_diploma_males` | `bigint` | Count or numeric value for ordinary bachelor degree or national diploma males in the represented area. |
| `honours_bachelor_degree_professional_qualification_or_both_male` | `bigint` | Count or numeric value for honours bachelor degree professional qualification or both male in the represented area. |
| `postgraduate_diploma_or_degree_males` | `bigint` | Count or numeric value for postgraduate diploma or degree males in the represented area. |
| `doctoratephd_or_higher_males` | `bigint` | Count or numeric value for doctoratephd or higher males in the represented area. |
| `not_stated_males_1` | `bigint` | Count or numeric value for not stated males 1 in the represented area. |
| `total_males_1` | `bigint` | Count or numeric value for total males 1 in the represented area. |
| `no_formal_education_females` | `bigint` | Count or numeric value for number formal education females in the represented area. |
| `primary_education_females` | `bigint` | Count or numeric value for primary education females in the represented area. |
| `lower_secondary_females` | `bigint` | Count or numeric value for lower secondary females in the represented area. |
| `upper_secondary_females` | `bigint` | Count or numeric value for upper secondary females in the represented area. |
| `technical_or_vocational_qualification_females` | `bigint` | Count or numeric value for technical or vocational qualification females in the represented area. |
| `advanced_certificatecompleted_apprenticeship_females` | `bigint` | Count or numeric value for advanced certificatecompleted apprenticeship females in the represented area. |
| `higher_certificate_females` | `bigint` | Count or numeric value for higher certificate females in the represented area. |
| `ordinary_bachelor_degree_or_national_diploma_females` | `bigint` | Count or numeric value for ordinary bachelor degree or national diploma females in the represented area. |
| `honours_bachelor_degree_professional_qualification_or_both_fema` | `bigint` | Count or numeric value for honours bachelor degree professional qualification or both fema in the represented area. |
| `postgraduate_diploma_or_degree_females` | `bigint` | Count or numeric value for postgraduate diploma or degree females in the represented area. |
| `doctoratephd_or_higher_females` | `bigint` | Count or numeric value for doctoratephd or higher females in the represented area. |
| `not_stated_females_1` | `bigint` | Count or numeric value for not stated females 1 in the represented area. |
| `total_females_1` | `bigint` | Count or numeric value for total females 1 in the represented area. |
| `no_formal_education_total` | `bigint` | Count or numeric value for number formal education total in the represented area. |
| `primary_education_total` | `bigint` | Count or numeric value for primary education total in the represented area. |
| `lower_secondary_total` | `bigint` | Count or numeric value for lower secondary total in the represented area. |
| `upper_secondary_total` | `bigint` | Count or numeric value for upper secondary total in the represented area. |
| `technical_or_vocational_qualification_total` | `bigint` | Count or numeric value for technical or vocational qualification total in the represented area. |
| `advanced_certificatecompleted_apprenticeship_total` | `bigint` | Count or numeric value for advanced certificatecompleted apprenticeship total in the represented area. |
| `higher_certificate_total` | `bigint` | Count or numeric value for higher certificate total in the represented area. |
| `ordinary_bachelor_degree_or_national_diploma_total` | `bigint` | Count or numeric value for ordinary bachelor degree or national diploma total in the represented area. |
| `honours_bachelor_degree_professional_qualification_or_both_tota` | `bigint` | Count or numeric value for honours bachelor degree professional qualification or both tota in the represented area. |
| `postgraduate_diploma_or_degree_total` | `bigint` | Count or numeric value for postgraduate diploma or degree total in the represented area. |
| `doctoratephd_or_higher_total` | `bigint` | Count or numeric value for doctoratephd or higher total in the represented area. |
| `not_stated_total_1` | `bigint` | Count or numeric value for not stated total 1 in the represented area. |
| `total_1` | `bigint` | Count or numeric value for total 1 in the represented area. |
