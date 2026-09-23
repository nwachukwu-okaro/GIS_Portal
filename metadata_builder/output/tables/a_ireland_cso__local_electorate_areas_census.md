# Local Electorate Areas Census

## Overview

- **Identifier:** `a_ireland_cso/local_electorate_areas_census`
- **Source organisation:** Central Statistics Office Ireland
- **Source:** https://www.cso.ie/en/databases/
- **Geographic coverage:** Ireland
- **Topic category:** boundaries
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, column_descriptions, frequency_of_update, spatial_resolution_or_equivalent_scale
- **Schema:** `a_ireland_cso`
- **Table:** `local_electorate_areas_census`
- **Geometry:** GEOMETRY
- **CRS:** EPSG:27700
- **Rows:** 167
- **Columns:** 794
- **Metadata status:** source_mapped

## Description

Local Electorate Areas Census is an authoritative dataset published by Central Statistics Office Ireland. It represents local electorate areas census features using geometry geometry.

## Lineage

Published by Central Statistics Office Ireland as open statistics and census data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `guid` | `varchar(36)` | UUID-formatted identifier associated with the record; persistence across releases is not confirmed. |
| `geogid` | `varchar(8)` | Code identifying the geographical area represented by the row. |
| `geogdesc` | `varchar(29)` | Name or descriptive label of the geographical area represented by the row. |
| `t1_1age0m` | `bigint` | Census count of males aged 0 in the represented area. |
| `t1_1age1m` | `bigint` | Census count of males aged 1 in the represented area. |
| `t1_1age2m` | `bigint` | Census count of males aged 2 in the represented area. |
| `t1_1age3m` | `bigint` | Census count of males aged 3 in the represented area. |
| `t1_1age4m` | `bigint` | Census count of males aged 4 in the represented area. |
| `t1_1age5m` | `bigint` | Census count of males aged 5 in the represented area. |
| `t1_1age6m` | `bigint` | Census count of males aged 6 in the represented area. |
| `t1_1age7m` | `bigint` | Census count of males aged 7 in the represented area. |
| `t1_1age8m` | `bigint` | Census count of males aged 8 in the represented area. |
| `t1_1age9m` | `bigint` | Census count of males aged 9 in the represented area. |
| `t1_1age10m` | `bigint` | Census count of males aged 10 in the represented area. |
| `t1_1age11m` | `bigint` | Census count of males aged 11 in the represented area. |
| `t1_1age12m` | `bigint` | Census count of males aged 12 in the represented area. |
| `t1_1age13m` | `bigint` | Census count of males aged 13 in the represented area. |
| `t1_1age14m` | `bigint` | Census count of males aged 14 in the represented area. |
| `t1_1age15m` | `bigint` | Census count of males aged 15 in the represented area. |
| `t1_1age16m` | `bigint` | Census count of males aged 16 in the represented area. |
| `t1_1age17m` | `bigint` | Census count of males aged 17 in the represented area. |
| `t1_1age18m` | `bigint` | Census count of males aged 18 in the represented area. |
| `t1_1age19m` | `bigint` | Census count of males aged 19 in the represented area. |
| `t1_1age20_24m` | `bigint` | Census count of males aged 20 to 24 in the represented area. |
| `t1_1age25_29m` | `bigint` | Census count of males aged 25 to 29 in the represented area. |
| `t1_1age30_34m` | `bigint` | Census count of males aged 30 to 34 in the represented area. |
| `t1_1age35_39m` | `bigint` | Census count of males aged 35 to 39 in the represented area. |
| `t1_1age40_44m` | `bigint` | Census count of males aged 40 to 44 in the represented area. |
| `t1_1age45_49m` | `bigint` | Census count of males aged 45 to 49 in the represented area. |
| `t1_1age50_54m` | `bigint` | Census count of males aged 50 to 54 in the represented area. |
| `t1_1age55_59m` | `bigint` | Census count of males aged 55 to 59 in the represented area. |
| `t1_1age60_64m` | `bigint` | Census count of males aged 60 to 64 in the represented area. |
| `t1_1age65_69m` | `bigint` | Census count of males aged 65 to 69 in the represented area. |
| `t1_1age70_74m` | `bigint` | Census count of males aged 70 to 74 in the represented area. |
| `t1_1age75_79m` | `bigint` | Census count of males aged 75 to 79 in the represented area. |
| `t1_1age80_84m` | `bigint` | Census count of males aged 80 to 84 in the represented area. |
| `t1_1agege_85m` | `bigint` |  |
| `t1_1agetm` | `bigint` |  |
| `t1_1age0f` | `bigint` | Census count of females aged 0 in the represented area. |
| `t1_1age1f` | `bigint` | Census count of females aged 1 in the represented area. |
| `t1_1age2f` | `bigint` | Census count of females aged 2 in the represented area. |
| `t1_1age3f` | `bigint` | Census count of females aged 3 in the represented area. |
| `t1_1age4f` | `bigint` | Census count of females aged 4 in the represented area. |
| `t1_1age5f` | `bigint` | Census count of females aged 5 in the represented area. |
| `t1_1age6f` | `bigint` | Census count of females aged 6 in the represented area. |
| `t1_1age7f` | `bigint` | Census count of females aged 7 in the represented area. |
| `t1_1age8f` | `bigint` | Census count of females aged 8 in the represented area. |
| `t1_1age9f` | `bigint` | Census count of females aged 9 in the represented area. |
| `t1_1age10f` | `bigint` | Census count of females aged 10 in the represented area. |
| `t1_1age11f` | `bigint` | Census count of females aged 11 in the represented area. |
| `t1_1age12f` | `bigint` | Census count of females aged 12 in the represented area. |
| `t1_1age13f` | `bigint` | Census count of females aged 13 in the represented area. |
| `t1_1age14f` | `bigint` | Census count of females aged 14 in the represented area. |
| `t1_1age15f` | `bigint` | Census count of females aged 15 in the represented area. |
| `t1_1age16f` | `bigint` | Census count of females aged 16 in the represented area. |
| `t1_1age17f` | `bigint` | Census count of females aged 17 in the represented area. |
| `t1_1age18f` | `bigint` | Census count of females aged 18 in the represented area. |
| `t1_1age19f` | `bigint` | Census count of females aged 19 in the represented area. |
| `t1_1age20_24f` | `bigint` | Census count of females aged 20 to 24 in the represented area. |
| `t1_1age25_29f` | `bigint` | Census count of females aged 25 to 29 in the represented area. |
| `t1_1age30_34f` | `bigint` | Census count of females aged 30 to 34 in the represented area. |
| `t1_1age35_39f` | `bigint` | Census count of females aged 35 to 39 in the represented area. |
| `t1_1age40_44f` | `bigint` | Census count of females aged 40 to 44 in the represented area. |
| `t1_1age45_49f` | `bigint` | Census count of females aged 45 to 49 in the represented area. |
| `t1_1age50_54f` | `bigint` | Census count of females aged 50 to 54 in the represented area. |
| `t1_1age55_59f` | `bigint` | Census count of females aged 55 to 59 in the represented area. |
| `t1_1age60_64f` | `bigint` | Census count of females aged 60 to 64 in the represented area. |
| `t1_1age65_69f` | `bigint` | Census count of females aged 65 to 69 in the represented area. |
| `t1_1age70_74f` | `bigint` | Census count of females aged 70 to 74 in the represented area. |
| `t1_1age75_79f` | `bigint` | Census count of females aged 75 to 79 in the represented area. |
| `t1_1age80_84f` | `bigint` | Census count of females aged 80 to 84 in the represented area. |
| `t1_1agege_85f` | `bigint` |  |
| `t1_1agetf` | `bigint` |  |
| `t1_1age0t` | `bigint` | Census count of persons aged 0 in the represented area. |
| `t1_1age1t` | `bigint` | Census count of persons aged 1 in the represented area. |
| `t1_1age2t` | `bigint` | Census count of persons aged 2 in the represented area. |
| `t1_1age3t` | `bigint` | Census count of persons aged 3 in the represented area. |
| `t1_1age4t` | `bigint` | Census count of persons aged 4 in the represented area. |
| `t1_1age5t` | `bigint` | Census count of persons aged 5 in the represented area. |
| `t1_1age6t` | `bigint` | Census count of persons aged 6 in the represented area. |
| `t1_1age7t` | `bigint` | Census count of persons aged 7 in the represented area. |
| `t1_1age8t` | `bigint` | Census count of persons aged 8 in the represented area. |
| `t1_1age9t` | `bigint` | Census count of persons aged 9 in the represented area. |
| `t1_1age10t` | `bigint` | Census count of persons aged 10 in the represented area. |
| `t1_1age11t` | `bigint` | Census count of persons aged 11 in the represented area. |
| `t1_1age12t` | `bigint` | Census count of persons aged 12 in the represented area. |
| `t1_1age13t` | `bigint` | Census count of persons aged 13 in the represented area. |
| `t1_1age14t` | `bigint` | Census count of persons aged 14 in the represented area. |
| `t1_1age15t` | `bigint` | Census count of persons aged 15 in the represented area. |
| `t1_1age16t` | `bigint` | Census count of persons aged 16 in the represented area. |
| `t1_1age17t` | `bigint` | Census count of persons aged 17 in the represented area. |
| `t1_1age18t` | `bigint` | Census count of persons aged 18 in the represented area. |
| `t1_1age19t` | `bigint` | Census count of persons aged 19 in the represented area. |
| `t1_1age20_24t` | `bigint` | Census count of persons aged 20 to 24 in the represented area. |
| `t1_1age25_29t` | `bigint` | Census count of persons aged 25 to 29 in the represented area. |
| `t1_1age30_34t` | `bigint` | Census count of persons aged 30 to 34 in the represented area. |
| `t1_1age35_39t` | `bigint` | Census count of persons aged 35 to 39 in the represented area. |
| `t1_1age40_44t` | `bigint` | Census count of persons aged 40 to 44 in the represented area. |
| `t1_1age45_49t` | `bigint` | Census count of persons aged 45 to 49 in the represented area. |
| `t1_1age50_54t` | `bigint` | Census count of persons aged 50 to 54 in the represented area. |
| `t1_1age55_59t` | `bigint` | Census count of persons aged 55 to 59 in the represented area. |
| `t1_1age60_64t` | `bigint` | Census count of persons aged 60 to 64 in the represented area. |
| `t1_1age65_69t` | `bigint` | Census count of persons aged 65 to 69 in the represented area. |
| `t1_1age70_74t` | `bigint` | Census count of persons aged 70 to 74 in the represented area. |
| `t1_1age75_79t` | `bigint` | Census count of persons aged 75 to 79 in the represented area. |
| `t1_1age80_84t` | `bigint` | Census count of persons aged 80 to 84 in the represented area. |
| `t1_1agege_85t` | `bigint` |  |
| `t1_1agett` | `bigint` |  |
| `t1_2sglm` | `bigint` |  |
| `t1_2marm` | `bigint` |  |
| `t1_2sepm` | `bigint` |  |
| `t1_2divm` | `bigint` |  |
| `t1_2widm` | `bigint` |  |
| `t1_2tm` | `bigint` |  |
| `t1_2sglf` | `bigint` |  |
| `t1_2marf` | `bigint` |  |
| `t1_2sepf` | `bigint` |  |
| `t1_2divf` | `bigint` |  |
| `t1_2widf` | `bigint` |  |
| `t1_2tf` | `bigint` |  |
| `t1_2sglt` | `bigint` |  |
| `t1_2mart` | `bigint` |  |
| `t1_2sept` | `bigint` |  |
| `t1_2divt` | `bigint` |  |
| `t1_2widt` | `bigint` |  |
| `t1_2t` | `bigint` |  |
| `t2_1iebp` | `bigint` |  |
| `t2_1ukbp` | `bigint` |  |
| `t2_1plbp` | `bigint` |  |
| `t2_1inbp` | `bigint` |  |
| `t2_1eubp` | `bigint` |  |
| `t2_1rwbp` | `bigint` |  |
| `t2_1tbp` | `bigint` |  |
| `t2_1iec` | `bigint` |  |
| `t2_1ukc` | `bigint` |  |
| `t2_1plc` | `bigint` |  |
| `t2_1inc` | `bigint` |  |
| `t2_1euc` | `bigint` |  |
| `t2_1rwc` | `bigint` |  |
| `t2_1nsc` | `bigint` |  |
| `t2_1tc` | `bigint` |  |
| `t2_2wi` | `bigint` |  |
| `t2_2wit` | `bigint` |  |
| `t2_2ow` | `bigint` |  |
| `t2_2bbi` | `bigint` |  |
| `t2_2aai` | `bigint` |  |
| `t2_2oth` | `bigint` |  |
| `t2_2ns` | `bigint` |  |
| `t2_2t` | `bigint` |  |
| `t2_3sa` | `bigint` |  |
| `t2_3ec` | `bigint` |  |
| `t2_3ei` | `bigint` |  |
| `t2_3oi` | `bigint` |  |
| `t2_3t` | `bigint` |  |
| `t2_4ca` | `bigint` |  |
| `t2_4or` | `bigint` |  |
| `t2_4nr` | `bigint` |  |
| `t2_4ns` | `bigint` |  |
| `t2_4t` | `bigint` |  |
| `t2_5pl` | `bigint` |  |
| `t2_5fr` | `bigint` |  |
| `t2_5es` | `bigint` |  |
| `t2_5oth` | `bigint` |  |
| `t2_5t` | `bigint` |  |
| `t2_6vw` | `bigint` |  |
| `t2_6w` | `bigint` |  |
| `t2_6nw` | `bigint` |  |
| `t2_6naa` | `bigint` |  |
| `t2_6ns` | `bigint` |  |
| `t2_6t` | `bigint` |  |
| `t3_1yes` | `bigint` |  |
| `t3_1no` | `bigint` |  |
| `t3_1ns` | `bigint` |  |
| `t3_1t` | `bigint` |  |
| `t3_2dim` | `bigint` |  |
| `t3_2didom` | `bigint` |  |
| `t3_2diwom` | `bigint` |  |
| `t3_2diloom` | `bigint` |  |
| `t3_2dinom` | `bigint` |  |
| `t3_2doesm` | `bigint` |  |
| `t3_2woesm` | `bigint` |  |
| `t3_2looesm` | `bigint` |  |
| `t3_2noesm` | `bigint` |  |
| `t3_2nsm` | `bigint` |  |
| `t3_2allm` | `bigint` |  |
| `t3_2dif` | `bigint` |  |
| `t3_2didof` | `bigint` |  |
| `t3_2diwof` | `bigint` |  |
| `t3_2diloof` | `bigint` |  |
| `t3_2dinof` | `bigint` |  |
| `t3_2doesf` | `bigint` |  |
| `t3_2woesf` | `bigint` |  |
| `t3_2looesf` | `bigint` |  |
| `t3_2noesf` | `bigint` |  |
| `t3_2nsf` | `bigint` |  |
| `t3_2allf` | `bigint` |  |
| `t3_2dit` | `bigint` |  |
| `t3_2didot` | `bigint` |  |
| `t3_2diwot` | `bigint` |  |
| `t3_2diloot` | `bigint` |  |
| `t3_2dinot` | `bigint` |  |
| `t3_2doest` | `bigint` |  |
| `t3_2woest` | `bigint` |  |
| `t3_2looest` | `bigint` |  |
| `t3_2noest` | `bigint` |  |
| `t3_2nst` | `bigint` |  |
| `t3_2allt` | `bigint` |  |
| `t4_1_2pf` | `bigint` |  |
| `t4_1_3pf` | `bigint` |  |
| `t4_1_4pf` | `bigint` |  |
| `t4_1_5pf` | `bigint` |  |
| `t4_1_gre_6pf` | `bigint` |  |
| `t4_1_tf` | `bigint` |  |
| `t4_1_2pp` | `bigint` |  |
| `t4_1_3pp` | `bigint` |  |
| `t4_1_4pp` | `bigint` |  |
| `t4_1_5pp` | `bigint` |  |
| `t4_1_gre_6pp` | `bigint` |  |
| `t4_1_tp` | `bigint` |  |
| `t4_1_2pc` | `bigint` |  |
| `t4_1_3pc` | `bigint` |  |
| `t4_1_4pc` | `bigint` |  |
| `t4_1_5pc` | `bigint` |  |
| `t4_1_gre_6pc` | `bigint` |  |
| `t4_1_tc` | `bigint` |  |
| `t4_2_1cu15` | `bigint` |  |
| `t4_2_2cu15` | `bigint` |  |
| `t4_2_3cu15` | `bigint` |  |
| `t4_2_4cu15` | `bigint` |  |
| `t4_2_ge5cu15` | `bigint` |  |
| `t4_2_tcu15` | `bigint` |  |
| `t4_2_1co15` | `bigint` |  |
| `t4_2_2co15` | `bigint` |  |
| `t4_2_3co15` | `bigint` |  |
| `t4_2_4co15` | `bigint` |  |
| `t4_2_ge5co15` | `bigint` |  |
| `t4_2_tco15` | `bigint` |  |
| `t4_2_2cuo15` | `bigint` |  |
| `t4_2_3cuo15` | `bigint` |  |
| `t4_2_4cuo15` | `bigint` |  |
| `t4_2_ge5cuo15` | `bigint` |  |
| `t4_2_tcuo15` | `bigint` |  |
| `t4_2_nct` | `bigint` |  |
| `t4_2_1ct` | `bigint` |  |
| `t4_2_2ct` | `bigint` |  |
| `t4_2_3ct` | `bigint` |  |
| `t4_2_4ct` | `bigint` |  |
| `t4_2_ge5ct` | `bigint` |  |
| `t4_2_tct` | `bigint` |  |
| `t4_3fccu15` | `bigint` |  |
| `t4_3fcco15` | `bigint` |  |
| `t4_3fccuo15` | `bigint` |  |
| `t4_3fcct` | `bigint` |  |
| `t4_3fopmcu15` | `bigint` |  |
| `t4_3fopmco15` | `bigint` |  |
| `t4_3fopmcuo15` | `bigint` |  |
| `t4_3fopmct` | `bigint` |  |
| `t4_3fopfcu15` | `bigint` |  |
| `t4_3fopfco15` | `bigint` |  |
| `t4_3fopfcuo15` | `bigint` |  |
| `t4_3fopfct` | `bigint` |  |
| `t4_3cccu15` | `bigint` |  |
| `t4_3ccco15` | `bigint` |  |
| `t4_3cccuo15` | `bigint` |  |
| `t4_3ccct` | `bigint` |  |
| `t4_3copmcu15` | `bigint` |  |
| `t4_3copmco15` | `bigint` |  |
| `t4_3copmcuo15` | `bigint` |  |
| `t4_3copmct` | `bigint` |  |
| `t4_3copfcu15` | `bigint` |  |
| `t4_3copfco15` | `bigint` |  |
| `t4_3copfcuo15` | `bigint` |  |
| `t4_3copfct` | `bigint` |  |
| `t4_4age0_4f` | `bigint` | Census count of females aged 0 to 4 in the represented area. |
| `t4_4age5_9f` | `bigint` | Census count of females aged 5 to 9 in the represented area. |
| `t4_4age10_14f` | `bigint` | Census count of females aged 10 to 14 in the represented area. |
| `t4_4age15_19f` | `bigint` | Census count of females aged 15 to 19 in the represented area. |
| `t4_4age_ge20f` | `bigint` |  |
| `t4_4tf` | `bigint` |  |
| `t4_4age0_4p` | `bigint` |  |
| `t4_4age5_9p` | `bigint` |  |
| `t4_4age10_14p` | `bigint` |  |
| `t4_4age15_19p` | `bigint` |  |
| `t4_4age_ge20p` | `bigint` |  |
| `t4_4tp` | `bigint` |  |
| `t4_5pff` | `bigint` |  |
| `t4_5enf` | `bigint` |  |
| `t4_5rf` | `bigint` |  |
| `t4_5psf` | `bigint` |  |
| `t4_5esf` | `bigint` |  |
| `t4_5paf` | `bigint` |  |
| `t4_5adof` | `bigint` |  |
| `t4_5aduf` | `bigint` |  |
| `t4_5tf` | `bigint` |  |
| `t4_5pfp` | `bigint` |  |
| `t4_5enp` | `bigint` |  |
| `t4_5rp` | `bigint` |  |
| `t4_5psp` | `bigint` |  |
| `t4_5esp` | `bigint` |  |
| `t4_5pap` | `bigint` |  |
| `t4_5adop` | `bigint` |  |
| `t4_5adup` | `bigint` |  |
| `t4_5tp` | `bigint` |  |
| `t5_1op_h` | `bigint` |  |
| `t5_1mc_h` | `bigint` |  |
| `t5_1cc_h` | `bigint` |  |
| `t5_1mcc_h` | `bigint` |  |
| `t5_1ccc_h` | `bigint` |  |
| `t5_1opfc_h` | `bigint` |  |
| `t5_1opmc_h` | `bigint` |  |
| `t5_1co_h` | `bigint` |  |
| `t5_1cco_h` | `bigint` |  |
| `t5_1opfco_h` | `bigint` |  |
| `t5_1opmco_h` | `bigint` |  |
| `t5_1getfu_h` | `bigint` |  |
| `t5_1nhr_h` | `bigint` |  |
| `t5_1genp_h` | `bigint` |  |
| `t5_1t_h` | `bigint` |  |
| `t5_1op_p` | `bigint` |  |
| `t5_1mc_p` | `bigint` |  |
| `t5_1cc_p` | `bigint` |  |
| `t5_1mcc_p` | `bigint` |  |
| `t5_1ccc_p` | `bigint` |  |
| `t5_1opfc_p` | `bigint` |  |
| `t5_1opmc_p` | `bigint` |  |
| `t5_1co_p` | `bigint` |  |
| `t5_1cco_p` | `bigint` |  |
| `t5_1opfco_p` | `bigint` |  |
| `t5_1opmco_p` | `bigint` |  |
| `t5_1getfu_p` | `bigint` |  |
| `t5_1nhr_p` | `bigint` |  |
| `t5_1genp_p` | `bigint` |  |
| `t5_1t_p` | `bigint` |  |
| `t5_2_1ph` | `bigint` |  |
| `t5_2_2ph` | `bigint` |  |
| `t5_2_3ph` | `bigint` |  |
| `t5_2_4ph` | `bigint` |  |
| `t5_2_5ph` | `bigint` |  |
| `t5_2_6ph` | `bigint` |  |
| `t5_2_7ph` | `bigint` |  |
| `t5_2_ge8ph` | `bigint` |  |
| `t5_2_th` | `bigint` |  |
| `t5_2_1pp` | `bigint` |  |
| `t5_2_2pp` | `bigint` |  |
| `t5_2_3pp` | `bigint` |  |
| `t5_2_4pp` | `bigint` |  |
| `t5_2_5pp` | `bigint` |  |
| `t5_2_6pp` | `bigint` |  |
| `t5_2_7pp` | `bigint` |  |
| `t5_2_ge8pp` | `bigint` |  |
| `t5_2_tp` | `bigint` |  |
| `t6_1_hb_h` | `bigint` |  |
| `t6_1_fa_h` | `bigint` |  |
| `t6_1_bs_h` | `bigint` |  |
| `t6_1_cm_h` | `bigint` |  |
| `t6_1_th` | `bigint` |  |
| `t6_1_hb_p` | `bigint` |  |
| `t6_1_fa_p` | `bigint` |  |
| `t6_1_bs_p` | `bigint` |  |
| `t6_1_cm_p` | `bigint` |  |
| `t6_1_tp` | `bigint` |  |
| `t6_2_pre19h` | `bigint` |  |
| `t6_2_19_45h` | `bigint` |  |
| `t6_2_46_60h` | `bigint` |  |
| `t6_2_61_70h` | `bigint` |  |
| `t6_2_71_80h` | `bigint` |  |
| `t6_2_81_90h` | `bigint` |  |
| `t6_2_91_00h` | `bigint` |  |
| `t6_2_01_10h` | `bigint` |  |
| `t6_2_11_15h` | `bigint` |  |
| `t6_2_16lh` | `bigint` |  |
| `t6_2_nsh` | `bigint` |  |
| `t6_2_th` | `bigint` |  |
| `t6_2_pre19p` | `bigint` |  |
| `t6_2_19_45p` | `bigint` |  |
| `t6_2_46_60p` | `bigint` |  |
| `t6_2_61_70p` | `bigint` |  |
| `t6_2_71_80p` | `bigint` |  |
| `t6_2_81_90p` | `bigint` |  |
| `t6_2_91_00p` | `bigint` |  |
| `t6_2_01_10p` | `bigint` |  |
| `t6_2_11_15p` | `bigint` |  |
| `t6_2_16lp` | `bigint` |  |
| `t6_2_nsp` | `bigint` |  |
| `t6_2_tp` | `bigint` |  |
| `t6_3_omlh` | `bigint` |  |
| `t6_3_ooh` | `bigint` |  |
| `t6_3_rplh` | `bigint` |  |
| `t6_3_rlah` | `bigint` |  |
| `t6_3_rvchbh` | `bigint` |  |
| `t6_3_ofrh` | `bigint` |  |
| `t6_3_nsh` | `bigint` |  |
| `t6_3_th` | `bigint` |  |
| `t6_3_omlp` | `bigint` |  |
| `t6_3_oop` | `bigint` |  |
| `t6_3_rplp` | `bigint` |  |
| `t6_3_rlap` | `bigint` |  |
| `t6_3_rvchbp` | `bigint` |  |
| `t6_3_ofrp` | `bigint` |  |
| `t6_3_nsp` | `bigint` |  |
| `t6_3_tp` | `bigint` |  |
| `t6_4_1rh` | `bigint` |  |
| `t6_4_2rh` | `bigint` |  |
| `t6_4_3rh` | `bigint` |  |
| `t6_4_4rh` | `bigint` |  |
| `t6_4_5rh` | `bigint` |  |
| `t6_4_6rh` | `bigint` |  |
| `t6_4_7rh` | `bigint` |  |
| `t6_4_ge8rh` | `bigint` |  |
| `t6_4_nsh` | `bigint` |  |
| `t6_4_th` | `bigint` |  |
| `t6_4_1rp` | `bigint` |  |
| `t6_4_2rp` | `bigint` |  |
| `t6_4_3rp` | `bigint` |  |
| `t6_4_4rp` | `bigint` |  |
| `t6_4_5rp` | `bigint` |  |
| `t6_4_6rp` | `bigint` |  |
| `t6_4_7rp` | `bigint` |  |
| `t6_4_ge8rp` | `bigint` |  |
| `t6_4_nsp` | `bigint` |  |
| `t6_4_tp` | `bigint` |  |
| `t6_5_nch` | `bigint` |  |
| `t6_5_och` | `bigint` |  |
| `t6_5_ngch` | `bigint` |  |
| `t6_5_ech` | `bigint` |  |
| `t6_5_cch` | `bigint` |  |
| `t6_5_pch` | `bigint` |  |
| `t6_5_lpgch` | `bigint` |  |
| `t6_5_wch` | `bigint` |  |
| `t6_5_oth` | `bigint` |  |
| `t6_5_ns` | `bigint` |  |
| `t6_5_t` | `bigint` |  |
| `t6_6_pm` | `bigint` |  |
| `t6_6_gsla` | `bigint` |  |
| `t6_6_gsp` | `bigint` |  |
| `t6_6_op` | `bigint` |  |
| `t6_6_n` | `bigint` |  |
| `t6_6_ns` | `bigint` |  |
| `t6_6_t` | `bigint` |  |
| `t6_7_ps` | `bigint` |  |
| `t6_7_ist` | `bigint` |  |
| `t6_7_oit` | `bigint` |  |
| `t6_7_oth` | `bigint` |  |
| `t6_7_nsf` | `bigint` |  |
| `t6_7_ns` | `bigint` |  |
| `t6_7_t` | `bigint` |  |
| `t6_8_o` | `bigint` |  |
| `t6_8_ta` | `bigint` |  |
| `t6_8_uhh` | `bigint` |  |
| `t6_8_ovd` | `bigint` |  |
| `t6_8_t` | `bigint` |  |
| `t6_9_0brh` | `bigint` |  |
| `t6_9_1brh` | `bigint` |  |
| `t6_9_2brh` | `bigint` |  |
| `t6_9_3brh` | `bigint` |  |
| `t6_9_4brh` | `bigint` |  |
| `t6_9_ge5brh` | `bigint` |  |
| `t6_9_th` | `bigint` |  |
| `t6_9_0brp` | `bigint` |  |
| `t6_9_1brp` | `bigint` |  |
| `t6_9_2brp` | `bigint` |  |
| `t6_9_3brp` | `bigint` |  |
| `t6_9_4brp` | `bigint` |  |
| `t6_9_ge5brp` | `bigint` |  |
| `t6_9_tp` | `bigint` |  |
| `t6_9_nsp` | `bigint` |  |
| `t6_9_nsh` | `bigint` |  |
| `t6_10_re` | `bigint` |  |
| `t6_10_nore` | `bigint` |  |
| `t6_10_ns` | `bigint` |  |
| `t6_10_t` | `bigint` |  |
| `t6_11_ge1sa` | `bigint` |  |
| `t6_11_nosa` | `bigint` |  |
| `t6_11_ns` | `bigint` |  |
| `t6_11_t` | `bigint` |  |
| `t7_1_vol` | `bigint` |  |
| `t8_1_wm` | `bigint` |  |
| `t8_1_lffjm` | `bigint` |  |
| `t8_1_stum` | `bigint` |  |
| `t8_1_ltum` | `bigint` |  |
| `t8_1_sm` | `bigint` |  |
| `t8_1_lahfm` | `bigint` |  |
| `t8_1_rm` | `bigint` |  |
| `t8_1_utwsdm` | `bigint` |  |
| `t8_1_othm` | `bigint` |  |
| `t8_1_tm` | `bigint` |  |
| `t8_1_wf` | `bigint` |  |
| `t8_1_lffjf` | `bigint` |  |
| `t8_1_stuf` | `bigint` |  |
| `t8_1_ltuf` | `bigint` |  |
| `t8_1_sf` | `bigint` |  |
| `t8_1_lahff` | `bigint` |  |
| `t8_1_rf` | `bigint` |  |
| `t8_1_utwsdf` | `bigint` |  |
| `t8_1_othf` | `bigint` |  |
| `t8_1_tf` | `bigint` |  |
| `t8_1_wt` | `bigint` |  |
| `t8_1_lffjt` | `bigint` |  |
| `t8_1_stut` | `bigint` |  |
| `t8_1_ltut` | `bigint` |  |
| `t8_1_st` | `bigint` |  |
| `t8_1_lahft` | `bigint` |  |
| `t8_1_rt` | `bigint` |  |
| `t8_1_utwsdt` | `bigint` |  |
| `t8_1_otht` | `bigint` |  |
| `t8_1_tt` | `bigint` |  |
| `t9_1_pwm` | `bigint` |  |
| `t9_1_mtm` | `bigint` |  |
| `t9_1_nmm` | `bigint` |  |
| `t9_1_sm` | `bigint` |  |
| `t9_1_ssm` | `bigint` |  |
| `t9_1_usm` | `bigint` |  |
| `t9_1_othgeum` | `bigint` |  |
| `t9_1_tm` | `bigint` |  |
| `t9_1_pwf` | `bigint` |  |
| `t9_1_mtf` | `bigint` |  |
| `t9_1_nmf` | `bigint` |  |
| `t9_1_sf` | `bigint` |  |
| `t9_1_ssf` | `bigint` |  |
| `t9_1_usf` | `bigint` |  |
| `t9_1_othgeuf` | `bigint` |  |
| `t9_1_tf` | `bigint` |  |
| `t9_1_pwt` | `bigint` |  |
| `t9_1_mtt` | `bigint` |  |
| `t9_1_nmt` | `bigint` |  |
| `t9_1_st` | `bigint` |  |
| `t9_1_sst` | `bigint` |  |
| `t9_1_ust` | `bigint` |  |
| `t9_1_othgeut` | `bigint` |  |
| `t9_1_tt` | `bigint` |  |
| `t9_2_ha` | `bigint` |  |
| `t9_2_hb` | `bigint` |  |
| `t9_2_hc` | `bigint` |  |
| `t9_2_hd` | `bigint` |  |
| `t9_2_he` | `bigint` |  |
| `t9_2_hf` | `bigint` |  |
| `t9_2_hg` | `bigint` |  |
| `t9_2_hh` | `bigint` |  |
| `t9_2_hi` | `bigint` |  |
| `t9_2_hj` | `bigint` |  |
| `t9_2_hz` | `bigint` |  |
| `t9_2_ht` | `bigint` |  |
| `t9_2_pa` | `bigint` |  |
| `t9_2_pb` | `bigint` |  |
| `t9_2_pc` | `bigint` |  |
| `t9_2_pd` | `bigint` |  |
| `t9_2_pe` | `bigint` |  |
| `t9_2_pf` | `bigint` |  |
| `t9_2_pg` | `bigint` |  |
| `t9_2_ph` | `bigint` |  |
| `t9_2_pi` | `bigint` |  |
| `t9_2_pj` | `bigint` |  |
| `t9_2_pz` | `bigint` |  |
| `t9_2_pt` | `bigint` |  |
| `t10_1_lt15m` | `bigint` |  |
| `t10_1_15m` | `bigint` |  |
| `t10_1_16m` | `bigint` |  |
| `t10_1_17m` | `bigint` |  |
| `t10_1_18m` | `bigint` |  |
| `t10_1_19m` | `bigint` |  |
| `t10_1_20m` | `bigint` |  |
| `t10_1_ge21m` | `bigint` |  |
| `t10_1_nsm` | `bigint` |  |
| `t10_1_tm` | `bigint` |  |
| `t10_1_lt15f` | `bigint` |  |
| `t10_1_15f` | `bigint` |  |
| `t10_1_16f` | `bigint` |  |
| `t10_1_17f` | `bigint` |  |
| `t10_1_18f` | `bigint` |  |
| `t10_1_19f` | `bigint` |  |
| `t10_1_20f` | `bigint` |  |
| `t10_1_ge21f` | `bigint` |  |
| `t10_1_nsf` | `bigint` |  |
| `t10_1_tf` | `bigint` |  |
| `t10_1_lt15t` | `bigint` |  |
| `t10_1_15t` | `bigint` |  |
| `t10_1_16t` | `bigint` |  |
| `t10_1_17t` | `bigint` |  |
| `t10_1_18t` | `bigint` |  |
| `t10_1_19t` | `bigint` |  |
| `t10_1_20t` | `bigint` |  |
| `t10_1_ge21t` | `bigint` |  |
| `t10_1_nst` | `bigint` |  |
| `t10_1_tt` | `bigint` |  |
| `t10_2_sasm` | `bigint` |  |
| `t10_2_othm` | `bigint` |  |
| `t10_2_sasf` | `bigint` |  |
| `t10_2_othf` | `bigint` |  |
| `t10_2_sast` | `bigint` |  |
| `t10_2_otht` | `bigint` |  |
| `t10_4_nfm` | `bigint` |  |
| `t10_4_pm` | `bigint` |  |
| `t10_4_lsm` | `bigint` |  |
| `t10_4_usm` | `bigint` |  |
| `t10_4_tvm` | `bigint` |  |
| `t10_4_accam` | `bigint` |  |
| `t10_4_hcm` | `bigint` |  |
| `t10_4_odndm` | `bigint` |  |
| `t10_4_hdpqm` | `bigint` |  |
| `t10_4_pdm` | `bigint` |  |
| `t10_4_dm` | `bigint` |  |
| `t10_4_nsm` | `bigint` |  |
| `t10_4_tm` | `bigint` |  |
| `t10_4_nff` | `bigint` |  |
| `t10_4_pf` | `bigint` |  |
| `t10_4_lsf` | `bigint` |  |
| `t10_4_usf` | `bigint` |  |
| `t10_4_tvf` | `bigint` |  |
| `t10_4_accaf` | `bigint` |  |
| `t10_4_hcf` | `bigint` |  |
| `t10_4_odndf` | `bigint` |  |
| `t10_4_hdpqf` | `bigint` |  |
| `t10_4_pdf` | `bigint` |  |
| `t10_4_df` | `bigint` |  |
| `t10_4_nsf` | `bigint` |  |
| `t10_4_tf` | `bigint` |  |
| `t10_4_nft` | `bigint` |  |
| `t10_4_pt` | `bigint` |  |
| `t10_4_lst` | `bigint` |  |
| `t10_4_ust` | `bigint` |  |
| `t10_4_tvt` | `bigint` |  |
| `t10_4_accat` | `bigint` |  |
| `t10_4_hct` | `bigint` |  |
| `t10_4_odndt` | `bigint` |  |
| `t10_4_hdpqt` | `bigint` |  |
| `t10_4_pdt` | `bigint` |  |
| `t10_4_dt` | `bigint` |  |
| `t10_4_nst` | `bigint` |  |
| `t10_4_tt` | `bigint` |  |
| `t11_1_fw` | `bigint` |  |
| `t11_1_biw` | `bigint` |  |
| `t11_1_buw` | `bigint` |  |
| `t11_1_tdlw` | `bigint` |  |
| `t11_1_mw` | `bigint` |  |
| `t11_1_cdw` | `bigint` |  |
| `t11_1_cpw` | `bigint` |  |
| `t11_1_vw` | `bigint` |  |
| `t11_1_othw` | `bigint` |  |
| `t11_1_wmfhw` | `bigint` |  |
| `t11_1_nsw` | `bigint` |  |
| `t11_1_tw` | `bigint` |  |
| `t11_1_fsccc` | `bigint` |  |
| `t11_1_bisccc` | `bigint` |  |
| `t11_1_busccc` | `bigint` |  |
| `t11_1_tdlsccc` | `bigint` |  |
| `t11_1_msccc` | `bigint` |  |
| `t11_1_cdsccc` | `bigint` |  |
| `t11_1_cpsccc` | `bigint` |  |
| `t11_1_vsccc` | `bigint` |  |
| `t11_1_othsccc` | `bigint` |  |
| `t11_1_wmfhsccc` | `bigint` |  |
| `t11_1_nssccc` | `bigint` |  |
| `t11_1_tsccc` | `bigint` |  |
| `t11_1_ft` | `bigint` |  |
| `t11_1_bit` | `bigint` |  |
| `t11_1_but` | `bigint` |  |
| `t11_1_tdlt` | `bigint` |  |
| `t11_1_mt` | `bigint` |  |
| `t11_1_cdt` | `bigint` |  |
| `t11_1_cpt` | `bigint` |  |
| `t11_1_vt` | `bigint` |  |
| `t11_1_otht` | `bigint` |  |
| `t11_1_wmfht` | `bigint` |  |
| `t11_1_nst` | `bigint` |  |
| `t11_1_tt` | `bigint` |  |
| `t11_2_t1` | `bigint` |  |
| `t11_2_t2` | `bigint` |  |
| `t11_2_t3` | `bigint` |  |
| `t11_2_t4` | `bigint` |  |
| `t11_2_t5` | `bigint` |  |
| `t11_2_t6` | `bigint` |  |
| `t11_2_t7` | `bigint` |  |
| `t11_2_t8` | `bigint` |  |
| `t11_2_ns` | `bigint` |  |
| `t11_2_t` | `bigint` |  |
| `t11_3_d1` | `bigint` |  |
| `t11_3_d2` | `bigint` |  |
| `t11_3_d3` | `bigint` |  |
| `t11_3_d4` | `bigint` |  |
| `t11_3_d5` | `bigint` |  |
| `t11_3_d6` | `bigint` |  |
| `t11_3_ns` | `bigint` |  |
| `t11_3_t` | `bigint` |  |
| `t11_4_wfh` | `bigint` |  |
| `t11_4_nwfh` | `bigint` |  |
| `t11_4_ns` | `bigint` |  |
| `t11_4_t` | `bigint` |  |
| `t11_5_cc_age0_4` | `bigint` |  |
| `t11_5_cc_age5_14` | `bigint` |  |
| `t11_5_cc_t` | `bigint` |  |
| `t12_1_m` | `bigint` |  |
| `t12_1_f` | `bigint` |  |
| `t12_1_t` | `bigint` |  |
| `t12_2_m` | `bigint` |  |
| `t12_2_f` | `bigint` |  |
| `t12_2_t` | `bigint` |  |
| `t12_3_vgm` | `bigint` |  |
| `t12_3_vgf` | `bigint` |  |
| `t12_3_vgt` | `bigint` |  |
| `t12_3_gm` | `bigint` |  |
| `t12_3_gf` | `bigint` |  |
| `t12_3_gt` | `bigint` |  |
| `t12_3_fm` | `bigint` |  |
| `t12_3_ff` | `bigint` |  |
| `t12_3_ft` | `bigint` |  |
| `t12_3_bm` | `bigint` |  |
| `t12_3_bf` | `bigint` |  |
| `t12_3_bt` | `bigint` |  |
| `t12_3_vbm` | `bigint` |  |
| `t12_3_vbf` | `bigint` |  |
| `t12_3_vbt` | `bigint` |  |
| `t12_3_nsm` | `bigint` |  |
| `t12_3_nsf` | `bigint` |  |
| `t12_3_nst` | `bigint` |  |
| `t12_3_tm` | `bigint` |  |
| `t12_3_tf` | `bigint` |  |
| `t12_3_tt` | `bigint` |  |
| `t12_4_yes` | `bigint` |  |
| `t12_4_no` | `bigint` |  |
| `t12_4_ns` | `bigint` |  |
| `t12_4_t` | `bigint` |  |
| `t13_1_mdsom` | `bigint` |  |
| `t13_1_pom` | `bigint` |  |
| `t13_1_aptom` | `bigint` |  |
| `t13_1_asom` | `bigint` |  |
| `t13_1_stom` | `bigint` |  |
| `t13_1_closom` | `bigint` |  |
| `t13_1_scsom` | `bigint` |  |
| `t13_1_ppmom` | `bigint` |  |
| `t13_1_eom` | `bigint` |  |
| `t13_1_nsm` | `bigint` |  |
| `t13_1_tm` | `bigint` |  |
| `t13_1_mdsof` | `bigint` |  |
| `t13_1_pof` | `bigint` |  |
| `t13_1_aptof` | `bigint` |  |
| `t13_1_asof` | `bigint` |  |
| `t13_1_stof` | `bigint` |  |
| `t13_1_closof` | `bigint` |  |
| `t13_1_scsof` | `bigint` |  |
| `t13_1_ppmof` | `bigint` |  |
| `t13_1_eof` | `bigint` |  |
| `t13_1_nsf` | `bigint` |  |
| `t13_1_tf` | `bigint` |  |
| `t13_1_mdsot` | `bigint` |  |
| `t13_1_pot` | `bigint` |  |
| `t13_1_aptot` | `bigint` |  |
| `t13_1_asot` | `bigint` |  |
| `t13_1_stot` | `bigint` |  |
| `t13_1_closot` | `bigint` |  |
| `t13_1_scsot` | `bigint` |  |
| `t13_1_ppmot` | `bigint` |  |
| `t13_1_eot` | `bigint` |  |
| `t13_1_nst` | `bigint` |  |
| `t13_1_tt` | `bigint` |  |
| `t14_1_affm` | `bigint` |  |
| `t14_1_bcm` | `bigint` |  |
| `t14_1_mim` | `bigint` |  |
| `t14_1_ctm` | `bigint` |  |
| `t14_1_tcm` | `bigint` |  |
| `t14_1_pam` | `bigint` |  |
| `t14_1_psm` | `bigint` |  |
| `t14_1_othm` | `bigint` |  |
| `t14_1_tm` | `bigint` |  |
| `t14_1_afff` | `bigint` |  |
| `t14_1_bcf` | `bigint` |  |
| `t14_1_mif` | `bigint` |  |
| `t14_1_ctf` | `bigint` |  |
| `t14_1_tcf` | `bigint` |  |
| `t14_1_paf` | `bigint` |  |
| `t14_1_psf` | `bigint` |  |
| `t14_1_othf` | `bigint` |  |
| `t14_1_tf` | `bigint` |  |
| `t14_1_afft` | `bigint` |  |
| `t14_1_bct` | `bigint` |  |
| `t14_1_mit` | `bigint` |  |
| `t14_1_ctt` | `bigint` |  |
| `t14_1_tct` | `bigint` |  |
| `t14_1_pat` | `bigint` |  |
| `t14_1_pst` | `bigint` |  |
| `t14_1_otht` | `bigint` |  |
| `t14_1_tt` | `bigint` |  |
| `t15_1_nc` | `bigint` |  |
| `t15_1_1c` | `bigint` |  |
| `t15_1_2c` | `bigint` |  |
| `t15_1_3c` | `bigint` |  |
| `t15_1_ge4c` | `bigint` |  |
| `t15_1_nsc` | `bigint` |  |
| `t15_1_tc` | `bigint` |  |
| `t15_2_bb` | `bigint` |  |
| `t15_2_oic` | `bigint` |  |
| `t15_2_no` | `bigint` |  |
| `t15_2_ns` | `bigint` |  |
| `t15_2_t` | `bigint` |  |
| `geom` | `geometry` | Spatial geometry of the represented feature. |
