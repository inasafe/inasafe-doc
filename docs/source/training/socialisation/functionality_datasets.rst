.. _functionality-datasets:

Functionality and Datasets
==========================

Before we dive into using QGIS and |project_name|, this chapter will explain
|project_name|  current functionality, the functionality we will touch on
during this short |project_name| course as well as the spatial datasets we
will be using.

Current Functionality of |project_name|
---------------------------------------

As explained in the previous section, |project_name| needs to have a hazard
layer and a exposure layer to create an impact layer.
Currently |project_name| impact functions relies on the following datasets:

**Hazard:**

==========  ================  ===============  ==================  ======================  ===============
**Hazard**  **Spatial Type**  **Hazard Type**  **Attribute Name**  **Hazard Units/field**  **Parameters**
----------  ----------------  ---------------  ------------------  ----------------------  ---------------
Flood       Raster            Depth            N/A                  m                      Threshold (m)
Flood       Polygon           Wet/Dry          affected             1/0                    Threshold (%)
Volcano     Raster            Ash Load         N/A                  kg/m2
Volcano     Polygon           Category         KRB                  text
Volcano     Point             Distance         Name                 text                   Radius (km)
Earthquake  Raster            Shakemap         N/A                  MMI                    H/M/L value
Tsunami     Raster            Depth            N/A                  m                      Threshold (m)
==========  ================  ===============  ==================  ======================  ===============

KRB = Kawansan Rawan Bencana (Volcano Hazard level)

**Exposure:**

=============  ================  ==================  ==================  =======================
**Exposure**   **Spatial Type**  **Exposure Type**   **Attribute Name**  **Exposure Units/Fields**
-------------  ----------------  ------------------  ------------------  -----------------------
Population     Raster            Density             N/A                 People per pixel
Structures     Polygon           Structure type      type                text
Structures     Point             Structure type      type                text
=============  ================  ==================  ==================  =======================

.. note:: For information on what is a Raster or a Vector,
   as well as the difference between Vector objects please go to
   :doc:`rastervsvector`

|project_name| is a dynamic tool that can easily be adapted to other types of
hazard and exposure layers.
The beauty of |project_name| being open source, is that anyone that has a
background in programming would be able to make their own Impact function.
For more information see take a look at :ref:`impact_function_tutorial`

Exposure Layers Used in Practical
---------------------------------

============  ================  =================  ==================  =======================
**Exposure**  **Spatial Type**  **Exposure Type**  **Attribute Name**  **Hazard Units/Fields**
------------  ----------------  -----------------  ------------------  -----------------------
Population    Raster            Density            N/A                 People per Pixel
Structures    Polygon           Structure type     type                text
============  ================  =================  ==================  =======================

Population
..........

:Name: AsiaPop
:InaSAFE: people
:Source: http://asiapop.org
:License: `Creative Commons by Attribution (CCbyA) <http://creativecommons.org/>`_
:Coverage: ASEAN +
:About: High resolution, contemporary data on human population distributions
    are a prerequisite for the accurate measurement of the impacts of
    population growth, for monitoring changes and for planning interventions.
    The AsiaPop project was initiated in July 2011 with an aim of producing
    detailed and freely-available population distribution maps for the whole
    of Asia.

.. image:: /static/training/socialisation/003_asia_pop.png
   :height: 500pt
   :align: center

The raster pixel size is 100m by 100m.

Structures
..........

:Name: |OSM|
:InaSAFE: buildings
:Source: http://openstreetmap.org
:License: `Open Data Commons Open Database License (ODbL) <http://opendatacommons.org/licenses/odbl/>`_
:Coverage: World - incomplete
:About:  OpenStreetMap is a collaborative project to create a free
    editable map of the world.
    Two major driving forces behind the establishment and growth of |OSM|
    have been restrictions on use or availability of map information across
    much of the world and the advent of inexpensive portable satellite
    navigation devices.

.. image:: /static/training/socialisation/004_openstreetmap.png
   :align: center

|AusAID| has been working with the Humanitarian OpenStreetMap Team over the
last 2 years in piloting and training OpenStreetMap in Indonesia.
The result so far is over 1,300,000 buildings have been mapped.
The scenarios we will look at within this workshop are situated in Jakarta,
Merapi (Central Java and Yogyakarta), Sumatra (specifically Padang) and
Maumere, Flores.
Each one of these areas has a different OpenStreetMap data collection
methodology.
Below will explain the methodologies used in Jakarta and Padang.

:Jakarta: BPBD DKI Jakarta (Regional Disaster Managers) and |BNPB| (Nationals
    Disaster Managers) with assistance from |AIFDR|, |AusAID|, the World Bank,
    UNOCHA, Humanitarian OpenStreetMap Team and University of Indonesia held
    workshops in each of Jakarta's 6 Districts in order to help Village Heads
    map their community boundaries and major infrastructure.
    Over 500 representatives from Jakarta's 267 Villages participated in these
    workshops and have mapped an impressive 6,000 buildings and all 2,668
    sub-village boundaries (Rukun Warga-RW).
    Go to `AIFDR Website <http://www.aifdr.org/?p=619>`_

:Padang: Post Haiti's earthquake in 2010, there was a huge effort to map Haiti
    through |OSM|, coordinating this effort was very hard,
    and hence |AusAID| subsequently funded the creation of OSM tasking Server.
    The OSM tasking server is a web-base tool where you are able to select
    your own square to map.  The first pilot of the web-tool was in Padang,
    the specified area is now 100% finished with over 95,
    000 buildings mapped. However the buildings are purely footprints,
    an on the ground mapping effort is needed to record what type of building
    it is. The tool is now being used across world to coordinate OSM
    mapping efforts. Go to `OSM Tasking Manager <http://tasks.hotosm.org/>`_

Hazard Layers used in Practical
-------------------------------

===========  ================  ===============  ==================  ======================  ===============
**Hazard**   **Spatial Type**  **Hazard Type**  **Attribute Name**  **Hazard Units/field**  **Parameters**
-----------  ----------------  ---------------  ------------------  ----------------------  ---------------
Flood        Raster            Depth            N/A                 m                       Threshold (m)
Flood        Polygon           Wet/Dry          affected            1/0                     Threshold (%)
Volcano      Point             Distance         Name                text                    Radius (km)
Earthquake   Raster            Shakemap         N/A                 MMI                     H/M/L value
Tsunami      Raster            Depth            N/A                 m                       Threshold (m)
===========  ================  ===============  ==================  ======================  ===============

Flood Model
...........

:Name:  HKV Flood Model
:InaSAFE:  a flood similar to the 2007 Jakarta event
:Source: `HKV <http://deltares.nl>`_
:License: `Creative Commons by Attribution (CCbyA) <http://creativecommons.org/>`_
:Coverage: Jakarta
:About: The Flood model was created by scientist/engineers in coordination
    with DKI Jakarta Public Works based on the 2007 flood conditions. The
    water depth is the maximum depth occurring across the entire flooding
    period.

.. image:: /static/training/socialisation/005_floodmodel.png
   :align: center

Flood Footprint
...............

:Name:  Jakarta flood areas on the 18/1/2013 by sub village boundaries
:InaSAFE:  Jakarta flooding on the 18th January 2013
:Source: |OSM| and BPBD DKI Jakarta
:License: `Creative Commons by Attribution (CCbyA) <http://creativecommons.org/>`_
:Coverage: Jakarta
:About: Based on the sub-village boundaries that were map during the DKI
    mapping project, we were able to use this dataset during the recent
    floods to identify the areas that had been flooded based on information
    provided by the villages.

.. image:: /static/training/socialisation/006_floodfootprint.png
   :align: center

Volcano
.......

:Name:  Global Volcanism Program
:InaSAFE:  volcano
:Source: Smithsonian from http://volcano.si.edu
:License: `United States Copyright <http://www.copyright.gov/title17/>`_
:Coverage: World
:About: The Smithsonian's Global Volcanism Program seeks better understanding
    of all volcanoes through documenting their eruptions-small as well as
    large-during the past 10,000 years. Through their website you are able to
    download a spreadsheet of all the recorded volcanoes.  This spreadsheet
    also has the volcano location, which has been turned into a point file.

.. image:: /static/training/socialisation/007_volcano.png
   :align: center


Earthquake
..........

:Name:  Shakemap of Pandang 2009 earthquake
:InaSAFE: an earthquake in Padang like 2009
:Source: Badan Geologi and |AIFDR|, |AusAID|
:License: `Creative Commons by Attribution (CCbyA) <http://creativecommons.org/>`_
:Coverage: Padang
:About: A shakemap is a representation of ground shaking produced by an
    earthquake.  This particular scenario was modelled based on the 30
    September 2009 Mw 7.9 earthquake in Padang. ShakeMaps are generated
    automatically following moderate and large earthquakes by USGS. Go to
    http://earthquake.usgs.gov/earthquakes/map/

Pre-event / scenario based shakemaps need to be modelled by earthquake
specialists.

.. image:: /static/training/socialisation/008_earthquake.png
   :align: center

Tsunami
.......

:Name:  Maumere Tsunami
:InaSAFE:  A tsunami in maumere (Mw 8.1)
:Source: |AIFDR|, |AusAID| and Badan Geologi
:License: `Creative Commons by Attribution (CCbyA) <http://creativecommons.org/>`_
:Coverage: Maumere, Flores
:About: In September 2011 the Indonesian government held a national exercise
    in Maumere, Flores. |AIFDR| and |AusAID| assisted Badan Geology in developing a
    tsunami model for Maumere based on an Mw 8.1 earthquake.  The Tsunami was
    modelled using the an open source software called ANUGA and elevation
    from NEXTMap. The water depth is the maximum depth occurring across the
    entire tsunami event. Go to http://anuga.anu.edu.au/
    and http://intermap.com/

.. image:: /static/training/socialisation/009_tsunami.png
   :align: center
