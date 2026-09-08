# Education Establishments

## Overview

- **Identifier:** `a_department_for_education/education_establishments`
- **Source organisation:** Department for Education
- **Source:** https://www.get-information-schools.service.gov.uk/
- **Official dataset page:** https://get-information-schools.service.gov.uk/Downloads
- **Local dataset version:** 20251203 (3 December 2025)
- **Geographic coverage:** England
- **Topic category:** society
- **Dataset language:** eng
- **Metadata language:** eng
- **Conformity:** Not evaluated — internal use
- **Missing for full compliance:** access_constraints, licence_name, temporal_extent, dataset_reference_date, use_constraints, frequency_of_update
- **Schema:** `a_department_for_education`
- **Table:** `education_establishments`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 52152
- **Columns:** 135
- **Metadata status:** context_curated

## Description

Locations and administrative details of education establishments from the Department for Education's Get Information about Schools service, including identifiers, status dates, pupil statistics, addresses, leadership, inspection links and specialist provision.

## Lineage

Published by Department for Education as open education data. Loaded into Systra PostGIS database without transformation.

## Metadata point of contact

- **Organisation:** Systra UK and Ireland
- **Email:** gis_uk@systra.com
- **Role:** pointOfContact

## Columns

| Column | Type | Description |
|---|---|---|
| `urn` | `bigint` | Unique Reference Number assigned by the Department for Education to the establishment. |
| `la_code` | `bigint` | Code assigned by the source dataset. |
| `la_name` | `varchar(35)` | Name associated with the represented feature. |
| `establishmentnumber` | `bigint` | DfE establishment number used with the local-authority code to identify a school. |
| `establishmentname` | `varchar(96)` | Official name of the education establishment. |
| `typeofestablishment_code` | `bigint` | Code assigned by the source dataset. |
| `typeofestablishment_name` | `varchar(49)` | Name associated with the represented feature. |
| `establishmenttypegroup_code` | `bigint` | Code assigned by the source dataset. |
| `establishmenttypegroup_name` | `varchar(34)` | Name associated with the represented feature. |
| `establishmentstatus_code` | `bigint` | Code assigned by the source dataset. |
| `establishmentstatus_name` | `varchar(27)` | Name associated with the represented feature. |
| `reasonestablishmentopened_code` | `bigint` | Code assigned by the source dataset. |
| `reasonestablishmentopened_name` | `varchar(29)` | Name associated with the represented feature. |
| `opendate` | `varchar(10)` | Date on which the establishment opened in its current registered form. |
| `reasonestablishmentclosed_code` | `bigint` | Code assigned by the source dataset. |
| `reasonestablishmentclosed_name` | `varchar(39)` | Name associated with the represented feature. |
| `closedate` | `varchar(10)` | Date on which the establishment closed; empty for establishments not recorded as closed. |
| `phaseofeducation_code` | `bigint` | Code assigned by the source dataset. |
| `phaseofeducation_name` | `varchar(23)` | Name associated with the represented feature. |
| `statutorylowage` | `bigint` | Lowest statutory age of pupils admitted by the establishment. |
| `statutoryhighage` | `bigint` | Highest statutory age of pupils admitted by the establishment. |
| `boarders_code` | `bigint` | Code assigned by the source dataset. |
| `boarders_name` | `varchar(38)` | Name associated with the represented feature. |
| `nurseryprovision_name` | `varchar(19)` | Name associated with the represented feature. |
| `officialsixthform_code` | `bigint` | Code assigned by the source dataset. |
| `officialsixthform_name` | `varchar(26)` | Name associated with the represented feature. |
| `gender_code` | `bigint` | Code assigned by the source dataset. |
| `gender_name` | `varchar(14)` | Name associated with the represented feature. |
| `religiouscharacter_code` | `bigint` | Code assigned by the source dataset. |
| `religiouscharacter_name` | `varchar(56)` | Name associated with the represented feature. |
| `religiousethos_name` | `varchar(56)` | Name associated with the represented feature. |
| `diocese_code` | `varchar(4)` | Code assigned by the source dataset. |
| `diocese_name` | `varchar(40)` | Name associated with the represented feature. |
| `admissionspolicy_code` | `bigint` | Code assigned by the source dataset. |
| `admissionspolicy_name` | `varchar(14)` | Name associated with the represented feature. |
| `schoolcapacity` | `bigint` | Recorded number of pupil places available at the establishment. |
| `specialclasses_code` | `bigint` | Code assigned by the source dataset. |
| `specialclasses_name` | `varchar(19)` | Name associated with the represented feature. |
| `censusdate` | `varchar(10)` | School census date to which pupil counts and related statistics apply. |
| `numberofpupils` | `bigint` | Total pupils recorded on roll at the census date. |
| `numberofboys` | `bigint` | Number of boys recorded on roll at the census date. |
| `numberofgirls` | `bigint` | Number of girls recorded on roll at the census date. |
| `percentagefsm` | `real` | Percentage of pupils eligible for free school meals. |
| `trustschoolflag_code` | `bigint` | Code assigned by the source dataset. |
| `trustschoolflag_name` | `varchar(35)` | Name associated with the represented feature. |
| `trusts_code` | `bigint` | Code assigned by the source dataset. |
| `trusts_name` | `varchar(78)` | Name associated with the represented feature. |
| `schoolsponsorflag_name` | `varchar(19)` | Name associated with the represented feature. |
| `schoolsponsors_name` | `varchar(76)` | Name associated with the represented feature. |
| `federationflag_name` | `varchar(25)` | Name associated with the represented feature. |
| `federations_code` | `varchar(23)` | Code assigned by the source dataset. |
| `federations_name` | `varchar(122)` | Name associated with the represented feature. |
| `ukprn` | `bigint` | UK Provider Reference Number assigned to the education provider. |
| `feheidentifier` | `bigint` | Identifier used for a further- or higher-education provider. |
| `furthereducationtype_name` | `varchar(41)` | Name associated with the represented feature. |
| `lastchangeddate` | `varchar(10)` | Date on which the establishment record was last changed. |
| `street` | `varchar(73)` | Street component of the establishment's postal address. |
| `locality` | `varchar(53)` | Locality component of the establishment's postal address. |
| `address3` | `varchar(94)` | Additional address line supplied for the establishment. |
| `town` | `varchar(30)` | Postal town or city of the establishment. |
| `county_name` | `varchar(45)` | Name associated with the represented feature. |
| `postcode` | `varchar(8)` | Postcode of the establishment's registered site. |
| `schoolwebsite` | `varchar(123)` | Website address published for the establishment. |
| `telephonenum` | `numeric` | Telephone number published for the establishment. |
| `headtitle_name` | `varchar(16)` | Name associated with the represented feature. |
| `headfirstname` | `varchar(50)` | Given name of the recorded headteacher or establishment leader. |
| `headlastname` | `varchar(67)` | Family name of the recorded headteacher or establishment leader. |
| `headpreferredjobtitle` | `varchar(50)` | Preferred job title of the recorded establishment leader. |
| `bsoinspectoratename_name` | `varchar(32)` | Name associated with the represented feature. |
| `inspectoratereport` | `varchar(215)` | URL of the establishment's published inspectorate report where available. |
| `dateoflastinspectionvisit` | `varchar(10)` | Date of the most recent recorded inspection visit. |
| `nextinspectionvisit` | `varchar(1)` | Source indicator for the next inspection visit where one is recorded. |
| `teenmoth_name` | `varchar(40)` | Name associated with the represented feature. |
| `teenmothplaces` | `bigint` | Number of places provided specifically for teenage mothers. |
| `ccf_name` | `varchar(35)` | Name associated with the represented feature. |
| `senpru_name` | `varchar(35)` | Name associated with the represented feature. |
| `ebd_name` | `varchar(31)` | Name associated with the represented feature. |
| `placespru` | `bigint` | Number of places recorded for pupil referral unit provision. |
| `ftprov_name` | `varchar(34)` | Name associated with the represented feature. |
| `edbyother_name` | `varchar(42)` | Name associated with the represented feature. |
| `section41approved_name` | `varchar(14)` | Name associated with the represented feature. |
| `sen1_name` | `varchar(48)` | Name associated with the represented feature. |
| `sen2_name` | `varchar(48)` | Name associated with the represented feature. |
| `sen3_name` | `varchar(48)` | Name associated with the represented feature. |
| `sen4_name` | `varchar(48)` | Name associated with the represented feature. |
| `sen5_name` | `varchar(48)` | Name associated with the represented feature. |
| `sen6_name` | `varchar(48)` | Name associated with the represented feature. |
| `sen7_name` | `varchar(48)` | Name associated with the represented feature. |
| `sen8_name` | `varchar(48)` | Name associated with the represented feature. |
| `sen9_name` | `varchar(48)` | Name associated with the represented feature. |
| `sen10_name` | `varchar(48)` | Name associated with the represented feature. |
| `sen11_name` | `varchar(48)` | Name associated with the represented feature. |
| `sen12_name` | `varchar(48)` | Name associated with the represented feature. |
| `sen13_name` | `varchar(48)` | Name associated with the represented feature. |
| `typeofresourcedprovision_name` | `varchar(32)` | Name associated with the represented feature. |
| `resourcedprovisiononroll` | `bigint` | Pupils on roll in designated resourced special-educational-needs provision. |
| `resourcedprovisioncapacity` | `bigint` | Recorded capacity of designated resourced special-educational-needs provision. |
| `senunitonroll` | `bigint` | Pupils on roll in the establishment's special educational needs unit. |
| `senunitcapacity` | `bigint` | Recorded pupil capacity of the special educational needs unit. |
| `gor_code` | `varchar(1)` | Code assigned by the source dataset. |
| `gor_name` | `varchar(24)` | Name associated with the represented feature. |
| `districtadministrative_code` | `varchar(9)` | Code assigned by the source dataset. |
| `districtadministrative_name` | `varchar(35)` | Name associated with the represented feature. |
| `administrativeward_code` | `varchar(9)` | Code assigned by the source dataset. |
| `administrativeward_name` | `varchar(53)` | Name associated with the represented feature. |
| `parliamentaryconstituency_code` | `varchar(9)` | Code assigned by the source dataset. |
| `parliamentaryconstituency_name` | `varchar(40)` | Name associated with the represented feature. |
| `urbanrural_code` | `varchar(4)` | Code assigned by the source dataset. |
| `urbanrural_name` | `varchar(71)` | Name associated with the represented feature. |
| `gsslacode_name` | `varchar(9)` | Name associated with the represented feature. |
| `easting` | `double precision` | Easting coordinate in metres in the dataset's projected coordinate reference system. |
| `northing` | `double precision` | Northing coordinate in metres in the dataset's projected coordinate reference system. |
| `msoa_name` | `varchar(40)` | Name associated with the represented feature. |
| `lsoa_name` | `varchar(45)` | Name associated with the represented feature. |
| `inspectoratename_name` | `varchar(28)` | Name associated with the represented feature. |
| `senstat` | `bigint` | Pupils with a statement of SEN or an Education, Health and Care plan. |
| `sennostat` | `bigint` | Pupils receiving SEN support without a statement or Education, Health and Care plan. |
| `boardingestablishment_name` | `varchar(22)` | Name associated with the represented feature. |
| `propsname` | `varchar(70)` | Name of the proprietor or owning body recorded for the establishment. |
| `previousla_code` | `bigint` | Code assigned by the source dataset. |
| `previousla_name` | `varchar(35)` | Name associated with the represented feature. |
| `previousestablishmentnumber` | `bigint` | Previous DfE establishment number associated with this record. |
| `country_name` | `varchar(22)` | Name associated with the represented feature. |
| `uprn` | `numeric` | Unique Property Reference Number for the establishment site. |
| `sitename` | `varchar(39)` | Name used to identify the establishment site or premises. |
| `qabname_code` | `bigint` | Code assigned by the source dataset. |
| `qabname_name` | `varchar(14)` | Name associated with the represented feature. |
| `establishmentaccredited_code` | `bigint` | Code assigned by the source dataset. |
| `establishmentaccredited_name` | `varchar(14)` | Name associated with the represented feature. |
| `qabreport` | `varchar(6)` | Quality-assurance or inspection body associated with the published report, such as Ofsted. |
| `chnumber` | `bigint` | Companies House number recorded for the proprietor or operating organisation. |
| `msoa_code` | `varchar(9)` | Code assigned by the source dataset. |
| `lsoa_code` | `varchar(9)` | Code assigned by the source dataset. |
| `fsm` | `bigint` | Number of pupils recorded as eligible for free school meals. |
| `accreditationexpirydate` | `varchar(10)` | Date on which the establishment's recorded accreditation expires. |
