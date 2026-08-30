# Education Establishments

## Overview

- **Identifier:** `a_department_for_education/education_establishments`
- **Source organisation:** Department for Education
- **Source:** https://www.get-information-schools.service.gov.uk/
- **Official dataset page:** https://get-information-schools.service.gov.uk/Downloads
- **Local dataset version:** 20251203 (3 December 2025)
- **Geographic coverage:** England
- **Schema:** `a_department_for_education`
- **Table:** `education_establishments`
- **Geometry:** Non-spatial
- **CRS:** Not applicable or unknown
- **Rows:** 52152
- **Columns:** 135
- **Metadata status:** context_curated

## Description

Locations and administrative details of education establishments from the Department for Education's Get Information about Schools service, including identifiers, status dates, pupil statistics, addresses, leadership, inspection links and specialist provision.

## Columns

| Column | Data type | Meaning | Semantic role | Filter | Search | Join |
|---|---|---|---|---|---|---|
| `urn` | `bigint` | Unique Reference Number assigned by the Department for Education to the establishment. | education_establishment_identifier | Yes | No | No |
| `la_code` | `bigint` | Code assigned by the source dataset. | code | Yes | No | No |
| `la_name` | `varchar(35)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `establishmentnumber` | `bigint` | DfE establishment number used with the local-authority code to identify a school. | establishment_number | Yes | No | No |
| `establishmentname` | `varchar(96)` | Official name of the education establishment. | feature_name | Yes | Yes | No |
| `typeofestablishment_code` | `bigint` | Code assigned by the source dataset. | code | Yes | No | No |
| `typeofestablishment_name` | `varchar(49)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `establishmenttypegroup_code` | `bigint` | Code assigned by the source dataset. | code | Yes | No | No |
| `establishmenttypegroup_name` | `varchar(34)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `establishmentstatus_code` | `bigint` | Code assigned by the source dataset. | code | Yes | No | No |
| `establishmentstatus_name` | `varchar(27)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `reasonestablishmentopened_code` | `bigint` | Code assigned by the source dataset. | code | Yes | No | No |
| `reasonestablishmentopened_name` | `varchar(29)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `opendate` | `varchar(10)` | Date on which the establishment opened in its current registered form. | opening_date | Yes | No | No |
| `reasonestablishmentclosed_code` | `bigint` | Code assigned by the source dataset. | code | Yes | No | No |
| `reasonestablishmentclosed_name` | `varchar(39)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `closedate` | `varchar(10)` | Date on which the establishment closed; empty for establishments not recorded as closed. | closure_date | Yes | No | No |
| `phaseofeducation_code` | `bigint` | Code assigned by the source dataset. | code | Yes | No | No |
| `phaseofeducation_name` | `varchar(23)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `statutorylowage` | `bigint` | Lowest statutory age of pupils admitted by the establishment. | minimum_pupil_age | Yes | No | No |
| `statutoryhighage` | `bigint` | Highest statutory age of pupils admitted by the establishment. | maximum_pupil_age | Yes | No | No |
| `boarders_code` | `bigint` | Code assigned by the source dataset. | code | Yes | No | No |
| `boarders_name` | `varchar(38)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `nurseryprovision_name` | `varchar(19)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `officialsixthform_code` | `bigint` | Code assigned by the source dataset. | code | Yes | No | No |
| `officialsixthform_name` | `varchar(26)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `gender_code` | `bigint` | Code assigned by the source dataset. | code | Yes | No | No |
| `gender_name` | `varchar(14)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `religiouscharacter_code` | `bigint` | Code assigned by the source dataset. | code | Yes | No | No |
| `religiouscharacter_name` | `varchar(56)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `religiousethos_name` | `varchar(56)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `diocese_code` | `varchar(4)` | Code assigned by the source dataset. | code | Yes | No | No |
| `diocese_name` | `varchar(40)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `admissionspolicy_code` | `bigint` | Code assigned by the source dataset. | code | Yes | No | No |
| `admissionspolicy_name` | `varchar(14)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `schoolcapacity` | `bigint` | Recorded number of pupil places available at the establishment. | pupil_capacity | Yes | No | No |
| `specialclasses_code` | `bigint` | Code assigned by the source dataset. | code | Yes | No | No |
| `specialclasses_name` | `varchar(19)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `censusdate` | `varchar(10)` | School census date to which pupil counts and related statistics apply. | reference_date | Yes | No | No |
| `numberofpupils` | `bigint` | Total pupils recorded on roll at the census date. | pupil_count | Yes | No | No |
| `numberofboys` | `bigint` | Number of boys recorded on roll at the census date. | male_pupil_count | Yes | No | No |
| `numberofgirls` | `bigint` | Number of girls recorded on roll at the census date. | female_pupil_count | Yes | No | No |
| `percentagefsm` | `real` | Percentage of pupils eligible for free school meals. | free_school_meals_percentage | Yes | No | No |
| `trustschoolflag_code` | `bigint` | Code assigned by the source dataset. | code | Yes | No | No |
| `trustschoolflag_name` | `varchar(35)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `trusts_code` | `bigint` | Code assigned by the source dataset. | code | Yes | No | No |
| `trusts_name` | `varchar(78)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `schoolsponsorflag_name` | `varchar(19)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `schoolsponsors_name` | `varchar(76)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `federationflag_name` | `varchar(25)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `federations_code` | `varchar(23)` | Code assigned by the source dataset. | code | Yes | No | No |
| `federations_name` | `varchar(122)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `ukprn` | `bigint` | UK Provider Reference Number assigned to the education provider. | provider_identifier | Yes | No | No |
| `feheidentifier` | `bigint` | Identifier used for a further- or higher-education provider. | further_higher_education_identifier | Yes | No | No |
| `furthereducationtype_name` | `varchar(41)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `lastchangeddate` | `varchar(10)` | Date on which the establishment record was last changed. | record_update_date | Yes | No | No |
| `street` | `varchar(73)` | Street component of the establishment's postal address. | address_street | Yes | No | No |
| `locality` | `varchar(53)` | Locality component of the establishment's postal address. | address_locality | Yes | No | No |
| `address3` | `varchar(94)` | Additional address line supplied for the establishment. | address_line | Yes | No | No |
| `town` | `varchar(30)` | Postal town or city of the establishment. | address_town | Yes | No | No |
| `county_name` | `varchar(45)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `postcode` | `varchar(8)` | Postcode of the establishment's registered site. | postcode | Yes | No | No |
| `schoolwebsite` | `varchar(123)` | Website address published for the establishment. | website_url | Yes | No | No |
| `telephonenum` | `numeric` | Telephone number published for the establishment. | telephone_number | Yes | No | No |
| `headtitle_name` | `varchar(16)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `headfirstname` | `varchar(50)` | Given name of the recorded headteacher or establishment leader. | headteacher_given_name | Yes | No | No |
| `headlastname` | `varchar(67)` | Family name of the recorded headteacher or establishment leader. | headteacher_family_name | Yes | No | No |
| `headpreferredjobtitle` | `varchar(50)` | Preferred job title of the recorded establishment leader. | headteacher_job_title | Yes | No | No |
| `bsoinspectoratename_name` | `varchar(32)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `inspectoratereport` | `varchar(215)` | URL of the establishment's published inspectorate report where available. | inspection_report_url | Yes | No | No |
| `dateoflastinspectionvisit` | `varchar(10)` | Date of the most recent recorded inspection visit. | last_inspection_date | Yes | No | No |
| `nextinspectionvisit` | `varchar(1)` | Source indicator for the next inspection visit where one is recorded. | next_inspection_indicator | Yes | No | No |
| `teenmoth_name` | `varchar(40)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `teenmothplaces` | `bigint` | Number of places provided specifically for teenage mothers. | teenage_mother_place_count | Yes | No | No |
| `ccf_name` | `varchar(35)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `senpru_name` | `varchar(35)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `ebd_name` | `varchar(31)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `placespru` | `bigint` | Number of places recorded for pupil referral unit provision. | pru_place_count | Yes | No | No |
| `ftprov_name` | `varchar(34)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `edbyother_name` | `varchar(42)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `section41approved_name` | `varchar(14)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `sen1_name` | `varchar(48)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `sen2_name` | `varchar(48)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `sen3_name` | `varchar(48)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `sen4_name` | `varchar(48)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `sen5_name` | `varchar(48)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `sen6_name` | `varchar(48)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `sen7_name` | `varchar(48)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `sen8_name` | `varchar(48)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `sen9_name` | `varchar(48)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `sen10_name` | `varchar(48)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `sen11_name` | `varchar(48)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `sen12_name` | `varchar(48)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `sen13_name` | `varchar(48)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `typeofresourcedprovision_name` | `varchar(32)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `resourcedprovisiononroll` | `bigint` | Pupils on roll in designated resourced special-educational-needs provision. | resourced_provision_pupil_count | Yes | No | No |
| `resourcedprovisioncapacity` | `bigint` | Recorded capacity of designated resourced special-educational-needs provision. | resourced_provision_capacity | Yes | No | No |
| `senunitonroll` | `bigint` | Pupils on roll in the establishment's special educational needs unit. | sen_unit_pupil_count | Yes | No | No |
| `senunitcapacity` | `bigint` | Recorded pupil capacity of the special educational needs unit. | sen_unit_capacity | Yes | No | No |
| `gor_code` | `varchar(1)` | Code assigned by the source dataset. | code | Yes | No | No |
| `gor_name` | `varchar(24)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `districtadministrative_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `districtadministrative_name` | `varchar(35)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `administrativeward_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `administrativeward_name` | `varchar(53)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `parliamentaryconstituency_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `parliamentaryconstituency_name` | `varchar(40)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `urbanrural_code` | `varchar(4)` | Code assigned by the source dataset. | code | Yes | No | No |
| `urbanrural_name` | `varchar(71)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `gsslacode_name` | `varchar(9)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `easting` | `double precision` | Easting coordinate in metres in the dataset's projected coordinate reference system. | x_coordinate | Yes | No | No |
| `northing` | `double precision` | Northing coordinate in metres in the dataset's projected coordinate reference system. | y_coordinate | Yes | No | No |
| `msoa_name` | `varchar(40)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `lsoa_name` | `varchar(45)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `inspectoratename_name` | `varchar(28)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `senstat` | `bigint` | Pupils with a statement of SEN or an Education, Health and Care plan. | statutory_sen_pupil_count | Yes | No | No |
| `sennostat` | `bigint` | Pupils receiving SEN support without a statement or Education, Health and Care plan. | nonstatutory_sen_pupil_count | Yes | No | No |
| `boardingestablishment_name` | `varchar(22)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `propsname` | `varchar(70)` | Name of the proprietor or owning body recorded for the establishment. | proprietor_name | Yes | Yes | No |
| `previousla_code` | `bigint` | Code assigned by the source dataset. | code | Yes | No | No |
| `previousla_name` | `varchar(35)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `previousestablishmentnumber` | `bigint` | Previous DfE establishment number associated with this record. | previous_establishment_number | Yes | No | No |
| `country_name` | `varchar(22)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `uprn` | `numeric` | Unique Property Reference Number for the establishment site. | property_identifier | Yes | No | No |
| `sitename` | `varchar(39)` | Name used to identify the establishment site or premises. | site_name | Yes | Yes | No |
| `qabname_code` | `bigint` | Code assigned by the source dataset. | code | Yes | No | No |
| `qabname_name` | `varchar(14)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `establishmentaccredited_code` | `bigint` | Code assigned by the source dataset. | code | Yes | No | No |
| `establishmentaccredited_name` | `varchar(14)` | Name associated with the represented feature. | feature_name | Yes | Yes | No |
| `qabreport` | `varchar(6)` | Quality-assurance or inspection body associated with the published report, such as Ofsted. | inspection_body | Yes | No | No |
| `chnumber` | `bigint` | Companies House number recorded for the proprietor or operating organisation. | company_identifier | Yes | No | No |
| `msoa_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `lsoa_code` | `varchar(9)` | Code assigned by the source dataset. | code | Yes | No | No |
| `fsm` | `bigint` | Number of pupils recorded as eligible for free school meals. | free_school_meals_count | Yes | No | No |
| `accreditationexpirydate` | `varchar(10)` | Date on which the establishment's recorded accreditation expires. | accreditation_expiry_date | Yes | No | No |

## Supported operations

- filter
- select
- attribute_join
- export

## Metadata warnings

- Pupil statistics relate to the stated census date and may not represent current enrolment.
- Check GIAS for the latest establishment status and contact details.

## Provenance

Technical facts were extracted from PostGIS. Publisher information was inherited from the curated schema source registry.
