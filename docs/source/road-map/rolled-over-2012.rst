=================================================================
Items rolled over from 2012 plan
=================================================================

These are ongoing items that were flagged and/or started in the 2012 road map https://docs.google.com/document/d/1QjYmVRNSTWvvJR48hSAa0V5B6wagrn7KT0Xj8BBwUbc/edit
In some cases, they were raised again in user requirements.

New features
------------

Real time earthquake impact system 
..................................

Replacement of prototype earthquake impact system which has been running at BPNB since August 2011. The replacement will address some shortcomings of the prototype to do with appearance of automatically generated map, extensibility and maintenance. The transition to |project_name| also allows for the inclusion of fatality estimates. The replacement was developed by Tim Sutton in Q3/Q4 of 2012 and is running at AIFDR. Still outstanding is obtaining feedback from BNPB on the design and deployment at BNPB.

**Resource Estimate**
Skills: QGIS, Python, Unix
FTE: 1 month

Offline / Online Integration []
...............................

Hazard and exposure data are collected and generated in different places.
Data is therefore hosted and maintained by different organisations. If data is hosted online according to established protocols, |project_name| should be able to ingest such remote data sets and combine them to compute impact estimates. Examples of data sources include PostGIS, GeoServer, GeoNode, etc


**Resource Estimate**
Skills: Web services, REST, QGIS, Python
FTE: 3 months
Resourcing: 
Tickets: https://github.com/AIFDR/inasafe/issues?milestone=12

Ability to analyse impact on roads 
..................................

Analysis of impact to roads (and indeed also railways, powerlines, etc) from a range of hazards important to contingency planning. |project_name| must therefore be able to assign hazard levels to line exposure data from raster and polygon hazard data. The functionality has been implemented in principle using Python with numpy. However, due to the irregular nature of the problem (e.g. individual line segments will be cut by polygon boundaries but must be brought back to the line item they belong to) it not fast enough for real life complex polygons and lines. 

This implementation is invoked here: https://github.com/AIFDR/inasafe/blob/new_std_doc/safe/engine/interpolation.py#L505
and its high level tests are: 
https://github.com/AIFDR/inasafe/blob/new_std_doc/safe/engine/test_engine.py#L2115
https://github.com/AIFDR/inasafe/blob/new_std_doc/safe/engine/test_engine.py#L2223
https://github.com/AIFDR/inasafe/blob/new_std_doc/safe/engine/test_engine.py#L2350

The underlying routine is :
https://github.com/AIFDR/inasafe/blob/new_std_doc/safe/common/polygon.py#L594
and its high level tests are from
https://github.com/AIFDR/inasafe/blob/new_std_doc/safe/common/test_polygon.py#L1200
to 
https://github.com/AIFDR/inasafe/blob/new_std_doc/safe/common/test_polygon.py#L1200


Options to reimplement this functionality include:
#. Use libraries from GDAL, GEOS, QGIS or shapely etc
#. Rewrite the time consuming Python code in C (that’d be the routines in polygon.py)
#. Reimplement the time consuming code using Cython (http://cython.org)

Option a would be the most attractive if possible, followed by c which is a fairly recent possibilty the finally c which requires a bit more work, maintenance and delivery of compiled C-code with |project_name|.


**Resource Estimate**
Skills: Python, numpy, algorithms, GDAL, GEOS, Shapely, C, Cython, gcc,
FTE: 6 months
Resourcing: 
Tickets: https://github.com/AIFDR/inasafe/issues?milestone=9

Raster and Styles in QGIS [FUTURE]
..................................

QGIS is currently able to access vector data remotely using WFS (Web Feature Service).  However raster data, needs WCS (Web Coverage Service) support, which is currently not implemented in QGIS. The standard format for styling data layers created by the OGC is called SLD (Styled Layer Descriptor). QGIS needs to transparently work with SLDs when available.

**Resource Estimate**
Skills: Python, GIS, OGC, REST, WxS
FTE: 2 months
Resourcing: TBA
Tickets: https://github.com/AIFDR/inasafe/issues?milestone=18


Software maintenance and bug fixing 
....................................

To make any software system functional it is essential to allocate resources for fixing bugs as they emerge. This task also contains the requirement to monitor and maintain the quality of the software (adherence to standards, continued regression testing, tracking of issues, etc). 

**Resource Estimate**
Skills: Software engineering, Python, QGIS, |project_name|
FTE:
Resourcing: 
Tickets: https://github.com/AIFDR/inasafe/issues?milestone=15 

|project_name| Core development (30 June 2013)
.......................................

A significant number of outstanding issues remain for |project_name| to be finished and it is very likely that more will appear as a result of the planned trials in the form of new or improved features.

**Resource Estimate**
Skills: Software engineering, Python, QGIS, GDAL, |project_name|
FTE: 6 months
Resourcing: GFDRR, $105k contract to Linfiniti, $5k contract to Software Engineer
Tickets: https://github.com/AIFDR/inasafe/issues?milestone=16

Development and Maintenance of Documentation (31 March 2013)
............................................................

Documentation is essential for any software project. This must not only be produced while it is being developed but also maintained to reflect changes as the occur. This will include documentation of the real time earthquake work.

**Resource Estimate**
Skills: Communication, |project_name|, Restructured Text
FTE: 2 months
Resourcing: AIFDR, $5k contract to Linfinity, $5k contract to Software Engineer, $10k contract to technical writer, Edi Dewanto
Tickets: https://github.com/AIFDR/inasafe/issues?milestone=11

Training of software developers (30 June 2013)
...............................................

To facilitate an active development community around |project_name| it is essential to provide training for potential contributors to the project. 

**Resource Estimate**
Skills: Communication, DRR, |project_name|
FTE: 6 months
Resourcing: AIFDR, $5k contract to software engineer, $5k contract to Linfiniti
Tickets: 

Communication materials and events (31 Mar 2013)
................................................

Development of material for the media and events, including launch of version 1.0.0 

**Resource Estimate**
Skills: Communication, DRR, |project_name|
FTE: 1 months
Resourcing: AIFDR, BNPB
Tickets: 



