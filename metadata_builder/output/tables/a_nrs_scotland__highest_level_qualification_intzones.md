# Highest Level Qualification Intzones

## Overview

- **Identifier:** `a_nrs_scotland/highest_level_qualification_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `highest_level_qualification_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Highest Level Qualification Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to highest level qualification intzones.

## Lineage

Published by National Records of Scotland as open statistics and boundary data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `all_people_aged_16_and_over` | `double precision` | Recorded census measure for the category "all people aged 16 and over" in the represented area. Units and population base require the source table. |
| `no_qualifications` | `double precision` |  |
| `lower_school_qualifications` | `double precision` |  |
| `upper_school_qualifications` | `double precision` |  |
| `apprenticeship_qualifications` | `double precision` |  |
| `further_education_and_sub_degree_higher_education_qualificat` | `double precision` |  |
| `degree_level_qualifications_or_above` | `double precision` |  |
