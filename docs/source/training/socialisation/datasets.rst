.. _datasets:


The data used in this course is available for download at
`data.inasafe.org  <http://data.inasafe.org/>`_. Ask your trainer what data you 
will need to download for the course, if it is not provided.

If you are working through the training independently, use the following data
packages:
`data.inasafe.org - Run Basic InaSAFEv3.2.zip <http://data.inasafe.org/TrainingDataPackages/RunBasicInaSAFEv3.2.zip>`_
`data.inasafe.org - Run Intermediate InaSAFEv3.2.zip <http://data.inasafe.org/TrainingDataPackages/RunIntermediateInaSAFEv3.2.zip>`_
`data.inasafe.org - Other Hazards v3.2.zip <http://data.inasafe.org/TrainingDataPackages/OtherHazardsv3.2.zip>`_

Hazard data
===========
Flood Model
...........

:File name:  Jakarta_Flood_HKV_WGS84.tif
:Training data name:  A flood similar to the 2007 Jakarta event
:Geometry: Raster
:Data Type: Continuous
:Scenario: Single event
:Unit: metres
:Source: HKV
:URL: http://deltares.nl
:Date: 2012
:Licence: `Creative Commons by Attribution (CCbyA) <http://creativecommons.org/>`_
:Coverage: Jakarta
:Data description: The flood model was created by scientists/engineers in coordination
    with DKI Jakarta Public Works based on the 2007 flood conditions. The
    water depth is the maximum depth occurring across the entire flooding
    period.

.. image:: /static/training/socialisation/005_data_flood_model.png
   :align: center

Flood Footprint
...............

:File name:  Jakarta_Flood_WGS84.shp
:Training data name:  A flood in Jakarta like 2013
:Geometry: Polygon
:Data Type: Classied
:Scenario: Single event
:Attribute field: FLOODPRONE
:Attribute value: Wet (Yes), Dry (No)
:Source: |OSM| and BPBD DKI Jakarta
:Date: 18 January 2013
:Licence: `Creative Commons by Attribution (CCbyA) <http://creativecommons.org/>`_
:Coverage: Jakarta
:Data description: Along with sub-village boundaries that were mapped during the DKI
    mapping project, this dataset was used to identify flood areas
    based on information provided by the villages.

.. image:: /static/training/socialisation/005_data_flood_footprint.png
   :align: center

Earthquake
..........

:File name:  Padang_EQ_2009_WGS84.tif
:Training data name: Earthquake in Padang 2009
:Geometry: Raster
:Data type: Continuous
:Scenario: Single event
:Unit: MMI
:Source: Badan Geologi and |GoA|
:Date: 2012
:Licence: `Creative Commons by Attribution (CCbyA) <http://creativecommons.org/>`_
:Coverage: Padang
:About: A shakemap is a representation of ground shaking produced by an
    earthquake. This particular scenario was modelled based on the 30th
    September 2009 Mw 7.9 earthquake in Padang. ShakeMaps are generated
    automatically following moderate and large earthquakes by USGS. For more
    information go to http://earthquake.usgs.gov/earthquakes/map/. Pre-event /
    scenario based shakemaps must be modelled by earthquake specialists.

.. image:: /static/training/socialisation/005_data_earthquake.png
   :align: center

Tsunami
.......

:File name:  Maumere_Tsunami_WGS84.tif
:Training data name:  Tsunami in Maumere (Mw 8.1)
:Geometry: Raster
:Data type: Continuous
:Scenario: Single event
:Source: |GoA| and Badan Geologi
:Date: 2012
:Licence: `Creative Commons by Attribution (CCbyA) <http://creativecommons.org/>`_
:Coverage: Maumere, Flores
:About: In September 2011, the Indonesian government held a national exercise
    in Maumere, Flores. |AIFDR| and |GoA| assisted Badan Geology in developing a
    tsunami model for Maumere based on an Mw 8.1 earthquake. The Tsunami was
    modelled using open source software called ANUGA and elevation data
    from NEXTMap. The water depth is the maximum depth occurring across the
    entire tsunami event. For more information visit http://anuga.anu.edu.au/
    and http://intermap.com/

.. image:: /static/training/socialisation/005_data_tsunami.png
   :align: center

Volcano
.......

:File name:  Sinabung_Hazard_Map_2015_WGS84.shp
:Training data name:  Sinabung Hazard Map
:Geometry: Polygon
:Data type: Classified
:Scenario: Multiple event
:Attribute field: KRB
:Attribute value: Kawasan rawan bencana III - High; Kawasan rawan bencana II - Medium; Kawasan rawan bencana I - Low
:Source: PVMG
:URL: http://www.vsi.esdm.go.id/galeri/index.php/Peta-Kawasan-Rawan-Bencana-Gunungapi-01/Wilayah-Sumatera/KRB-G_-Sinabung (publish map)
:Date: 2015
:Licence:
:Coverage: Sinabung
:Data description: This map contains information about the hazard level for
    each zone, so that can be used to identify the potential impacted.

.. image:: /static/training/socialisation/005_data_volcano_hazard.*
   :align: center

Volcano Point
............

:File name:  Sinabung_Mount_WGS84.shp
:Training data name:  Sinabung Mt
:Geometry: Point
:Data type: Classified
:Scenario: Multiple event
:Attribute field: Name
:Attribute value: Sinabung
:Source: PVMG
:URL: http://www.vsi.esdm.go.id/galeri/index.php/Peta-Kawasan-Rawan-Bencana-Gunungapi-01/Wilayah-Sumatera/KRB-G_-Sinabung (publish map)
:Date: 2015
:Licence:
:Coverage: Sinabung
:Data description: The data locate the peak of Mount Sinabung.

.. image:: /static/training/socialisation/005_data_volcano_sinabung.*
   :align: center

Volcanic Ash
............

:File name:  Sinabung_Volcanic_Ash_WGS84.shp
:Training data name:  Sinabung Volcanic Ash
:Geometry: Polygon
:Data type: Classified
:Scenario: Single event
:Attribute field: KRB
:Attribute value: High, Medium, Low
:Source: PVMG - BNPB
:URL:
:Date: 2014
:Licence:
:Coverage: Sinabung region
:Data description: The data show the spread of volcanic ash from Mount
    Sinabung during the 2014 eruption.

.. image:: /static/training/socialisation/005_data_volcanic_ash.*
   :align: center

Landslide
............

:File name:  NGK_Landslide_Vulnerability_WGS84.shp
:Training data name:  Landslide Hazard Zone
:Geometry: Polygon
:Data type: Classified
:Scenario: Single event
:Attribute field: KRB
:Attribute value: High Landslide Vulnerability Zone - High; Moderate Landslide Vulnerability Zone - Medium; Low Landslide Vulnerability Zone - Low
:Source: PVMBG
:URL: http://vsi.esdm.go.id/galeri/index.php/Peta-Zona-Kerentanan-Gerakan-Tanah-01/Peta-Zona-Kerentanan-Gerakan-Tanah/Prov-NTT (publish map)
:Date: 2009
:Licence:
:Coverage:
:Data description: Landslide vulnerability maps show the regions where
    landslides may occur. Topographic and landuse changes after mapping can
    change the landslide zone in the map.
    The high vulnerability zone is to be avoided for settlement area or
    strategic infrastructure. If it can't avoided, build on the moderate zone,
    but detailed research is needed to avoid landslide happen. In moderate
    zone, detailed research is also needed when planning to cut the slope.

.. image:: /static/training/socialisation/005_data_landslide_zones.*
   :align: center


Exposure data
=============

Population
..........

:Name: AsiaPop
:Training data name: population
:Geometry: Raster
:Data type: Continuous
:Unit: Count
:Source: World Pop
:URL: http://worldpop.org.uk
:Date: 2010
:Licence: `Creative Commons by Attribution (CCbyA) <http://creativecommons.org/>`_
:Coverage: ASEAN +
:Data description: High resolution (1 pixel represents 100m x 100m),
    contemporary data on human population distributions are a prerequisite
    for the accurate measurement of the impacts of population growth, for
    monitoring changes and for planning interventions. The AsiaPop project
    was initiated in July 2011 with an aim of producing detailed and
    freely-available population distribution maps for the whole of Asia.

.. image:: /static/training/socialisation/005_data_asiapop.png
   :height: 500pt
   :align: center

The raster pixel size is approximately 100m by 100m.

Buildings
.........

:Name: OSM Buildings
:Training data name: Buildings
:Geometry: Polygon and point
:Data type: Classified
:Attribute field: Type
:Attribute value: types of buildings; hospital, school etc
:Source: OpenStreetMap
:URL: http://openstreetmap.org
:Date: July 2015
:Licence: `Open Data Commons Open Database License (ODbL) <http://opendatacommons.org/licenses/odbl/>`_
:Coverage: World - incomplete
:Data description:  OpenStreetMap is a collaborative project to create a free
    editable map of the world. Two major driving forces behind the
    establishment and growth of OSM have been restrictions on use or
    availability of map information across much of the world and the advent
    of inexpensive portable satellite navigation devices.

.. image:: /static/training/socialisation/005_data_osm_building.png
   :align: center

|GoA| has been working with the Humanitarian OpenStreetMap Team (HOT) since 2011 
in piloting and training OpenStreetMap in Indonesia.
So far over 4 million buildings have been mapped.
Some of the scenarios we use in this training are situated in Jakarta, Yogyakarta
(Merapi), Sumatra (Padang) and Flores (Maumere).
Each one of these areas has a different OpenStreetMap data collection
methodology.
Below the data collection methodologies used in Jakarta and Padang are explained:

:Jakarta: BPBD DKI Jakarta (Regional Disaster Managers) and |BNPB| (National
    Disaster Managers) with assistance from |GoA|, the World Bank,
    UNOCHA, HOT and University of Indonesia, held
    workshops in each of Jakarta's six districts in order to help village heads
    map their community boundaries and major infrastructure.
    Over 500 representatives from Jakarta's 267 villages participated in these
    workshops and have mapped an impressive 6,000 buildings and all 2,668
    sub-village boundaries (Rukun Warga-RW).
    For more information go to `AIFDR Website <http://www.aifdr.org/?p=619>`_

:Padang: After the Haiti earthquake in 2010, there was a large effort to map Haiti
    through OSM. Coordinating this effort was difficult,
    and so |GoA| funded the creation of the OSM Tasking Manager.
    The OSM Tasking Manager is a web-based tool in which a designated area is
    easily divided into a grid, and individual users can select one piece at a time
    to quickly work together and digitally map the target area. The tool was
    first piloted in Padang, where contributors from around the world helped
    digitise over 95,000 buildings. However, the buildings are only footprints - 
    an on the ground mapping effort is needed to record attributes about each building. 
    The tool is now being used across the world to coordinate OSM mapping efforts. 
    It is available at `tasks.hotosm.org <http://tasks.hotosm.org/>`_

Roads
.....

:Name: OSM Roads
:Training data name: Roads
:Geometry: Line
:Data type: Classified
:Attribute field: Type
:Attribute value: types of roads
:Source: OpenStreetMap
:URL: http://openstreetmap.org
:Date: July 2015
:Licence: `Open Data Commons Open Database License (ODbL) <http://opendatacommons.org/licenses/odbl/>`_
:Coverage: World - incomplete
:Data description:  OpenStreetMap is a collaborative project to create a free
    editable map of the world. Two major driving forces behind the
    establishment and growth of OSM have been restrictions on use or
    availability of map information across much of the world and the advent
    of inexpensive portable satellite navigation devices.

.. image:: /static/training/socialisation/005_data_osm_road.png
   :align: center

Aggregation Data
================

Administrative Boundary
.......................

:Name: Administrative Boundary
:Training data name: District / Subdistrict / village
:Geometry: Polygon
:Data type: Classified
:Attribute field: Kabupaten / Kecamatan / Desa
:Attribute value: toponymy of the area
:Source: BPS
:URL:
:Date: 2010
:Licence:
:Coverage:
:Data description:  The data represent administrative boundaries in Indonesia





:ref:`Go to next module --> <run_basic_inasafe>`
