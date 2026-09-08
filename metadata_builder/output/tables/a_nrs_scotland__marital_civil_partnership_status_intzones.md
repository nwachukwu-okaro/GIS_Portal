# Marital Civil Partnership Status Intzones

## Overview

- **Identifier:** `a_nrs_scotland/marital_civil_partnership_status_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `marital_civil_partnership_status_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 7
- **Metadata status:** source_mapped

## Description

Marital Civil Partnership Status Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to marital civil partnership status intzones.

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
| `all_people_aged_16_and_over` | `double precision` | Count or numeric value for all people aged 16 and over in the represented area. |
| `never_married_and_never_registered_in_a_civil_partnership` | `double precision` | Count or numeric value for never married and never registered in a civil partnership in the represented area. |
| `married_or_in_a_registered_civil_partnership` | `double precision` | Count or numeric value for married or in a registered civil partnership in the represented area. |
| `separated_but_still_legally_married_or_still_legally_in_a_ci` | `double precision` | Count or numeric value for separated but still legally married or still legally in a ci in the represented area. |
| `divorced_or_civil_partnership_dissolved` | `double precision` | Count or numeric value for divorced or civil partnership dissolved in the represented area. |
| `widowed_or_surviving_civil_partnership_partner` | `double precision` | Count or numeric value for widowed or surviving civil partnership partner in the represented area. |
