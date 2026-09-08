# Tenure People Intzones

## Overview

- **Identifier:** `a_nrs_scotland/tenure_people_intzones`
- **Source organisation:** National Records of Scotland
- **Source:** https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products
- **Geographic coverage:** Scotland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_nrs_scotland`
- **Table:** `tenure_people_intzones`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 1284
- **Columns:** 12
- **Metadata status:** source_mapped

## Description

Tenure People Intzones is an authoritative dataset published by National Records of Scotland. It contains records relating to tenure people intzones.

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
| `all_occupied_households` | `double precision` | Count or numeric value for all occupied households in the represented area. |
| `owned_total` | `double precision` | Count or numeric value for owned total in the represented area. |
| `owned_owned_outright` | `double precision` | Count or numeric value for owned owned outright in the represented area. |
| `owned_owned_with_a_mortgage_or_loan` | `double precision` | Count or numeric value for owned owned with a mortgage or loan in the represented area. |
| `owned_shared_ownership_part_owned_and_part_rented` | `double precision` | Count or numeric value for owned shared ownership part owned and part rented in the represented area. |
| `owned_shared_equity_e_g_lift_or_help_to_buy` | `double precision` | Count or numeric value for owned shared equity e g lift or help to buy in the represented area. |
| `social_rented_council_la_or_housing_association_registered_s` | `double precision` | Count or numeric value for social rented council la or housing association registered s in the represented area. |
| `private_rented_total` | `double precision` | Count or numeric value for private rented total in the represented area. |
| `private_rented_private_landlord_or_letting_agency` | `double precision` | Count or numeric value for private rented private landlord or letting agency in the represented area. |
| `private_rented_other` | `double precision` | Count or numeric value for private rented other in the represented area. |
| `lives_rent_free` | `double precision` | Count or numeric value for lives rent free in the represented area. |
