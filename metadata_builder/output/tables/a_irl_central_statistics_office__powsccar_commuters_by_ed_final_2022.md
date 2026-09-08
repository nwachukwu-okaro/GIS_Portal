# Powsccar Commuters By Ed Final 2022

## Overview

- **Identifier:** `a_irl_central_statistics_office/powsccar_commuters_by_ed_final_2022`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_irl_central_statistics_office`
- **Table:** `powsccar_commuters_by_ed_final_2022`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 339607
- **Columns:** 10
- **Metadata status:** source_mapped

## Description

Using information coded from Question 36 What is the FULL NAME and ADDRESS of your place of work, school, college or childcare? in Census 2022 for POWSCCAR, CSO has developed a set of aggregate commuting counts. These counts are presented at CSO Electoral Division (ED) and county level.

The counts are based on origin and destination EDs for workers, students and children who are usually resident in Ireland. The counts include persons who work/study from home and persons who had no fixed place of work.

Journeys by workers/students and childcare from the Republic of Ireland to destinations in both Northern Ireland and overseas are included.

In order to maintain confidentiality, the following measures have been taken prior to publication:

Electoral divisions to which fewer than 10 persons commuted have been suppressed.
Records where no work, school, college or childcare was codable for a worker, student or child have been removed.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `cbef_pk` | `integer` | Surrogate primary key for the row |
| `residence_csoed_guid` | `varchar` | Geographic Unique Identification (GUID) Code for origin CSO Electoral Division (ED) |
| `residence_csoed_label` | `varchar` | Name of origin CSO ED |
| `residence_county` | `varchar` | County code for origin county |
| `residence_county_label` | `varchar` | Name of origin county |
| `powscc_csoed_guid` | `varchar` | GUID for destination CSO ED (LGD code for Northern Ireland or 98 for Overseas) |
| `powscc_csoed_label` | `varchar` | Name of destination CSO ED (LGD name for Northern Ireland or Overseas) |
| `powscc_county` | `varchar` | County code for destination county (NI for Northern Ireland or 98 for Overseas) |
| `powscc_county_label` | `varchar` | Name of destination county (Northern Ireland or Overseas) |
| `count` | `smallint` | Number of persons commuting |
