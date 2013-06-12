============
Requirements
============

Hazards
-------

|project_name| is designed to generate impact scenarios by combining the
level of any hazard with a range of exposure data including building (points
or footprints), population density grids and roads. For the purpose of this
plan the focus will be on:

**Flood impact on**

* Buildings, irrespective of their construction and based on the levels
  defined in |BNPB|’s guidelines (Perka 2) where available e.g. < 1m, 1-3m, >3m
* Population (counts based on a threshold to be decided) and the associated
  needs for clean water, rice, sanitary facilities etc as defined in the |BNPB|
  standards (Perka 7).

**Tsunami impact on**

* Buildings  (as with flood)
* Population  (as with flood)

**Earthquake impact**

* Buildings damage and estimates of financial losses,
  depending on their structure type where available, and according to the
  Perka 2 guidelines.
* Population fatalities

**Real-time Earthquake Impact** (see also functionality listed below)

* Replace existing real time earthquake impact prototype currently running at
  |BNPB| with new version, based on |project_name| and using the earthquake
  impact function specified above.

**Categorised Hazard**

* Buildings, irrespective of their construction and based on the Category
  specified by the hazard
* Population count within specified categories

Specific requirements suggested by users
----------------------------------------

This is feedback obtained from |project_name| trainers,
November 2012 workshop in Yogyakarta and discussions with staff at University
of Gaja Madah throughout second half of 2012. An overarching principle that
was decided on in the workshop was that |project_name| should not
reimplement functionality that can be done easily with QGIS. Rather this
should become the topic of advanced training. |project_name| should focus on
simple, repetitive tasks aimed at non-GIS experts and the ability to produce
customised reports and maps. The user feedback is grouped loosely by themes.
Resource estimates (day, week, month) and priorities (low, medium,
high) are given in brackets.

Error messages and warnings
...........................

Although |project_name| has an ethos of producing error messages that
provide the end user with information on how to resolve issues,
the feedback suggests that more needs to be done:

* Audit error reporting: https://github.com/AIFDR/inasafe/issues/431:
  [week,high]
* Use GUI to show limitations: https://github.com/AIFDR/inasafe/issues/433:
  [day, high]
* Turn reproject-on-the-fly on by default:
  https://github.com/AIFDR/inasafe/issues/460: [hour, high] - Done

Documentation
.............

In addition to the available static documentation, there is a need for online
help - especially in understanding the variety of available impact functions

* Context help on impact functions:
  https://github.com/AIFDR/inasafe/issues/422: [week, high]
* Finish documenting impact functions:
  https://github.com/AIFDR/inasafe/issues/186: [week, high]
* https://github.com/AIFDR/inasafe/issues/487
* User documentation in Bahasa Indonesia: Under contract with UGM
* Training material in English (and put into Sphinx): Under contract with UGM

Workflows
.........

Suggestions relating to workflows in using |project_name| and managing data

* Wizard for novice user: https://github.com/AIFDR/inasafe/issues/410:
  [months,  high]
* Bundle results in one folder: https://github.com/AIFDR/inasafe/issues/425
  [medium]
* Aggregation: https://github.com/AIFDR/inasafe/issues/423 [In progress!]
* Construct action plan:  https://github.com/AIFDR/inasafe/issues/418 [low]
* More than one hazard:  https://github.com/AIFDR/inasafe/issues/419 [low]

Easier access and ways of loading input data
............................................

Crucial to impact modelling is ease of accessing input data sets whether they
reside on the local system or remotely such as data from OpenStreetMap

* OSM loader: https://github.com/AIFDR/inasafe/issues/415 [month, high]
* Ability to work with other standards:
  https://github.com/AIFDR/inasafe/issues/432 [low]

Better styling and reporting
............................

As an important part of |project_name|’s output takes the form of map layers
it is important that they are automatically styled well.

* Legend on results section: https://github.com/AIFDR/inasafe/issues/421:
  [month, medium]
* Show aggregated results in charts:
  https://github.com/AIFDR/inasafe/issues/420 [3 months?, medium]
* Terminology in translations: https://github.com/AIFDR/inasafe/issues/456
  [month, high]

Suggested new impact calculations
.................................

This is a list of new impact calculations suggested by users

* Estimate population from buildings:
  https://github.com/AIFDR/inasafe/issues/488:    [week, low]
* Earthquake polygon hazard:
  https://github.com/AIFDR/inasafe/issues/489 [week, low]
* Ability to locate safe places:
  https://github.com/AIFDR/inasafe/issues/411 [medium]
* IDP camps:
  https://github.com/AIFDR/inasafe/issues/412 [medium]
* Land use analysis:
  https://github.com/AIFDR/inasafe/issues/417 [medium, ?]
* Impact on roads:
  https://github.com/AIFDR/inasafe/issues/416 1 [6 months, high]
* Tornado and Landslide:
  https://github.com/AIFDR/inasafe/issues/457 [medium]
* Take an input layer of number of people evacuated and calculate the minimum
  required assistance https://github.com/AIFDR/inasafe/issues/491 [high]

Installation
............

Suggestions to do with installing and managing |project_name|

* Ability to downgrade:
  https://github.com/AIFDR/inasafe/issues/427 [low]
* Repackage |project_name| with QGIS:
  https://github.com/AIFDR/inasafe/issues/426 [week, low]

Requirements suggested by development team
------------------------------------------

These are suggestions identified by the developers that would make
|project_name| better positioned for further development.

Change the internal representation of layers to use QGIS data structures.
.........................................................................

For historical reasons, |project_name| uses a Python wrapper around the GDAL
bindings for representing raster and vector layers. The advantage of this is
that what constitutes the computational core of |project_name| can exist and
run independently of QGIS and for instance be used by web based applications
such as the geonode-safe project. However, this separation also have some
adverse effects on |project_name|:

* Working with two internal representations leads to excessive reading and
  writing of intermediate results and hence suboptimal performance
* The impact functions work with abstract layer representations that have no
  access to functionality available in QGIS. This limits the calculations that
  can be made available to the end user.
* The current representation of layers does not allow for blockwise
  read/write operations which requires all layers and results to fit in
  physical memory. QGIS layers provide this functionality and would
  potentially allow |project_name| to work with larger datasets if made
  available.

If a move to QGIS layers was effectuated it would require

* Complete refactor of the current storage package. On path could be to keep
  the current |project_name| layer objects, but replace the low level GDAL
  functionality with equivalent QGIS calls.
* QGIS layer objects must have the ability to provide spatial data in Python
  and numpy data structures as appropriate for impact calculations.
* Make zonal statistics from QGIS available to impact functions (e.g through
  the call assign_hazard_level_to_exposure_data)


Resolution of impact layer
..........................

Where both hazard and exposure layers are rasters, the resolution of the
Impact layer is currently chosen to be that of the hazard layer - mainly for
aesthetic reasons. There are other options: Use

#. hazard resolution
#. exposure resolution
#. arbitrary
#. finest of the two input layer

* Impact function writer’s guide:
  https://github.com/AIFDR/inasafe/issues/487
* More developer documentation of |project_name|’s core
* Show metadata such as filenames and impact functions for each run in
  impact report (issue #22)
