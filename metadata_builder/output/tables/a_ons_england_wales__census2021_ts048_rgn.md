# Census2021 Ts048 Rgn

## Overview

- **Identifier:** `a_ons_england_wales/census2021_ts048_rgn`
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
- **Missing for full compliance:** temporal_extent, dataset_reference_date, column_descriptions, frequency_of_update
- **Schema:** `a_ons_england_wales`
- **Table:** `census2021_ts048_rgn`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 10
- **Columns:** 36
- **Metadata status:** source_mapped

## Description

Census2021 Ts048 Rgn is an authoritative dataset published by Office for National Statistics. It contains records relating to census2021 ts048 rgn.

## Lineage

Published by the Office for National Statistics as part of their digital boundary products. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `date` | `bigint` |  |
| `geography` | `text` | Name or descriptive label of the geographical area represented by the row. |
| `geography_code` | `text` | Code assigned by the source dataset. |
| `total_all_usual_residents_in_communal_establishments` | `bigint` | Recorded census measure for the category "total all usual residents in communal establishments" in the represented area. Units and population base require the source table. |
| `medical_and_care_establishment` | `bigint` |  |
| `medical_and_care_establishment_nhs` | `bigint` |  |
| `medical_and_care_establishment_nhs_general_hospital` | `bigint` |  |
| `medical_and_care_establishment_nhs_mental_health_hospital_or_un` | `bigint` |  |
| `medical_and_care_establishment_nhs_other_hospital` | `bigint` |  |
| `medical_and_care_establishment_local_authority` | `bigint` |  |
| `medical_and_care_establishment_local_authority_children_s_home` | `bigint` |  |
| `medical_and_care_establishment_local_authority_care_home_with_n` | `bigint` |  |
| `medical_and_care_establishment_local_authority_care_home_withou` | `bigint` |  |
| `medical_and_care_establishment_local_authority_other_home` | `bigint` |  |
| `medical_and_care_establishment_registered_social_landlord_or_ho` | `bigint` |  |
| `medical_and_care_establishment_registered_social_landlord_or_1` | `bigint` |  |
| `medical_and_care_establishment_other` | `bigint` |  |
| `medical_and_care_establishment_other_care_home_with_nursing` | `bigint` |  |
| `medical_and_care_establishment_other_care_home_without_nursing` | `bigint` |  |
| `medical_and_care_establishment_other_children_s_home_including` | `bigint` |  |
| `medical_and_care_establishment_other_mental_health_hospital_or` | `bigint` |  |
| `medical_and_care_establishment_other_other_hospital` | `bigint` |  |
| `medical_and_care_establishment_other_other_establishment` | `bigint` |  |
| `other_establishment` | `bigint` |  |
| `other_establishment_defence` | `bigint` |  |
| `other_establishment_prison_service` | `bigint` |  |
| `other_establishment_approved_premises_probation_or_bail_hostel` | `bigint` |  |
| `other_establishment_detention_centres_and_other_detention` | `bigint` |  |
| `other_establishment_education` | `bigint` |  |
| `other_establishment_hotel_guest_house_bandb_or_youth_hostel` | `bigint` |  |
| `other_establishment_hostel_or_temporary_shelter_for_the_homeles` | `bigint` |  |
| `other_establishment_holiday_accommodation` | `bigint` |  |
| `other_establishment_other_travel_or_temporary_accommodation` | `bigint` |  |
| `other_establishment_religious` | `bigint` |  |
| `other_establishment_staff_or_worker_accommodation_or_other` | `bigint` |  |
| `establishment_not_stated` | `bigint` |  |
