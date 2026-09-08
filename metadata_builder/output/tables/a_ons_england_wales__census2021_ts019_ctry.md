# Census2021 Ts019 Ctry

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts019_ctry`
- **Source organisation:** Office for National Statistics
- **Source:** https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries
- **Licence:** [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- **Geographic coverage:** England and Wales
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Use constraints:** Open Government Licence v3.0 — https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **Conformity:** Not evaluated — internal use
- **UK GEMINI2 compliance tier:** 1
- **Missing for full compliance:** temporal_extent, dataset_reference_date, frequency_of_update
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts019_ctry`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 3
- **Columns:** 8
- **Metadata status:** source_mapped

## Description

Census2021 Ts019 Ctry is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts019 ctry.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `date` | `bigint` | Count or numeric value for date in the represented area. |
| `geography` | `text` | Publisher-supplied geography for the represented feature or record. |
| `geography_code` | `text` | Code assigned by the source dataset. |
| `total_all_usual_residents` | `bigint` | Count or numeric value for total all usual residents in the represented area. |
| `address_one_year_ago_is_the_same_as_the_address_of_enumeration` | `bigint` | Count or numeric value for address one year ago is the same as the address of enumeration in the represented area. |
| `address_one_year_ago_is_student_term_time_or_boarding_school_ad` | `bigint` | Count or numeric value for address one year ago is student term time or boarding school ad in the represented area. |
| `migrant_from_within_the_uk_address_one_year_ago_was_in_the_uk` | `bigint` | Count or numeric value for migrant from within the uk address one year ago was in the uk in the represented area. |
| `migrant_from_outside_the_uk_address_one_year_ago_was_outside_th` | `bigint` | Count or numeric value for migrant from outside the uk address one year ago was outside th in the represented area. |
