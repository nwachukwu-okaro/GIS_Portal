# Household Type Alt Intzones

## Overview

- **Identifier:** `a_nrs_scotland/household_type_alt_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `household_type_alt_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 11
- **Metadata status:** source_mapped

## Description

Household Type Alt Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to household type alt intzones.

## Lineage

Published by National Records of Scotland as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `all_households` | `double precision` | Count or numeric value for all households in the represented area. |
| `one_person_household` | `double precision` | Count or numeric value for one person household in the represented area. |
| `married_or_civil_partnership_couple_household_no_dependent_c` | `double precision` | Count or numeric value for married or civil partnership couple household number dependent c in the represented area. |
| `married_or_civil_partnership_couple_household_with_dependent` | `double precision` | Count or numeric value for married or civil partnership couple household with dependent in the represented area. |
| `cohabiting_couple_household_no_dependent_children` | `double precision` | Count or numeric value for cohabiting couple household number dependent children in the represented area. |
| `cohabiting_couple_household_with_dependent_children` | `double precision` | Count or numeric value for cohabiting couple household with dependent children in the represented area. |
| `lone_parent_household_no_dependent_children` | `double precision` | Numeric lone parent household number dependent children value recorded for the feature. |
| `lone_parent_household_with_dependent_children` | `double precision` | Numeric lone parent household with dependent children value recorded for the feature. |
| `multi_person_household_all_full_time_students` | `double precision` | Count or numeric value for multi person household all full time students in the represented area. |
| `multi_person_household_other` | `double precision` | Count or numeric value for multi person household other in the represented area. |
