.. _functionality-datasets:

Functionality and Datasets
==========================

Before we begin using QGIS and |project_name|, this module will explain
|project_name| current functionality, the functionality that will be covered in
this short course and the spatial datasets we will be using.

The data used in this course is available for download at
`data.inasafe.org  <http://data.inasafe.org/>`_. Ask your trainer what data you 
will need to download for the course, if they do not provide it for you directly.

If you are working through the training independently, use the following data package: `data.inasafe.org -
InaSAFEv2.0.zip <http://data.inasafe.org/TrainingDataPackages/InaSAFEv2.0.zip>`_.

The data used in this course is available for download on
`data.inasafe.org <http://data.inasafe.org/>`_.
Ask your trainer which data you will need to download or your trainer will
give you the data on a USB-Stick anyway.

Current Functionality of |project_name|
---------------------------------------

As explained in the previous section, |project_name| needs to have a hazard
layer and an exposure layer to create an impact layer.
Currently |project_name| impact functions rely on the following datasets:

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

=============  ================  ==================  ==================  =========================
**Exposure**   **Spatial Type**  **Exposure Type**   **Attribute Name**  **Exposure Units/Fields**
-------------  ----------------  ------------------  ------------------  -------------------------
Population     Raster            Population count    N/A                 People per pixel
Structures     Polygon           Structure type      type                text
Structures     Point             Structure type      type                text
=============  ================  ==================  ==================  =========================

.. note:: For information on what is a raster or a vector,
     as well as the differences between vector objects please go to
     :doc:`rastervsvector`

|project_name| is a dynamic tool that can easily be adapted to other types of
hazard and exposure layers.
The beauty of |project_name| being open source, is that anyone who has a
background in programming is able to make their own impact functions.

Exposure Layers Used in Practical
---------------------------------

============  ================  =================  ==================  =========================
**Exposure**  **Spatial Type**  **Exposure Type**  **Attribute Name**  **Exposure Units/Fields**
------------  ----------------  -----------------  ------------------  -------------------------
Population    Raster            Population count   N/A                 People per Pixel
Structures    Polygon           Structure type     type                text
============  ================  =================  ==================  =========================

Population
..........

:Name: AsiaPop
:InaSAFE: people
:Source: http://worldpop.org.uk
:Licence: `Creative Commons by Attribution (CCbyA) <http://creativecommons.org/>`_
:Download: `Indonesia Population Download <http://www.worldpop.org.uk/data/summary/?contselect=Asia&countselect=Indonesia&typeselect=Population>`_
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
:Licence: `Open Data Commons Open Database License (ODbL) <http://opendatacommons.org/licenses/odbl/>`_
:Coverage: World - incomplete
:About:  OpenStreetMap is a collaborative project to create a free
    editable map of the world.
    Two major driving forces behind the establishment and growth of OSM
    have been restrictions on use or availability of map information across
    much of the world and the advent of inexpensive portable satellite
    navigation devices.

.. image:: /static/training/socialisation/004_openstreetmap.png
   :align: center

|GoA| has been working with the Humanitarian OpenStreetMap Team (HOT) since 2011 
in piloting and training OpenStreetMap in Indonesia.
Thus far over 1,300,000 buildings have been mapped.
The scenarios we will look at within this workshop are situated in Jakarta,
Central Java and Yogyakarta (Merapi), Sumatra (Padang) and
Flores (Maumere).
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

Hazard Layers used in Practical
---------------------------------

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
:Licence: `Creative Commons by Attribution (CCbyA) <http://creativecommons.org/>`_
:Coverage: Jakarta
:About: The flood model was created by scientists/engineers in coordination
    with DKI Jakarta Public Works based on the 2007 flood conditions. The
    water depth is the maximum depth occurring across the entire flooding
    period.

.. image:: /static/training/socialisation/005_floodmodel.png
   :align: center

Flood Footprint
...............

:Name:  Jakarta flood areas on 18/1/2013 by sub village boundaries
:InaSAFE:  Jakarta flooding on the 18th January 2013
:Source: |OSM| and BPBD DKI Jakarta
:Licence: `Creative Commons by Attribution (CCbyA) <http://creativecommons.org/>`_
:Coverage: Jakarta
:About: Along with sub-village boundaries that were mapped during the DKI
    mapping project, this dataset was used to identify flood areas 
    based on information provided by the villages.

.. image:: /static/training/socialisation/006_floodfootprint.png
   :align: center

Volcano
.......

:Name:  Global Volcanism Program
:InaSAFE:  volcano
:Source: Smithsonian from http://volcano.si.edu
:Licence: `United States Copyright <http://www.copyright.gov/title17/>`_
:Coverage: World
:About: The Smithsonian's Global Volcanism Program seeks better understanding
    of all volcanoes through documenting their eruptions - small as well as
    large-during the past 10,000 years. Through their website you are able to
    download a spreadsheet of all the recorded volcanoes. This spreadsheet
    also has the volcano location, which has been converted into a point file.

.. image:: /static/training/socialisation/007_volcano.png
   :align: center


Earthquake
..........

:Name:  Shakemap of Padang 2009 earthquake
:InaSAFE: an earthquake in Padang like 2009
:Source: Badan Geologi and |AIFDR|, |GoA|
:Licence: `Creative Commons by Attribution (CCbyA) <http://creativecommons.org/>`_
:Coverage: Padang
:About: A shakemap is a representation of ground shaking produced by an
    earthquake. This particular scenario was modelled based on the 30th
    September 2009 Mw 7.9 earthquake in Padang. ShakeMaps are generated
    automatically following moderate and large earthquakes by USGS. For more
    information go to http://earthquake.usgs.gov/earthquakes/map/. Pre-event / 
    scenario based shakemaps must be modelled by earthquake specialists.

.. image:: /static/training/socialisation/008_earthquake.png
   :align: center

Tsunami
.......

:Name:  Maumere Tsunami
:InaSAFE:  A tsunami in Maumere (Mw 8.1)
:Source: |AIFDR|, |GoA| and Badan Geologi
:Licence: `Creative Commons by Attribution (CCbyA) <http://creativecommons.org/>`_
:Coverage: Maumere, Flores
:About: In September 2011, the Indonesian government held a national exercise
    in Maumere, Flores. |AIFDR| and |GoA| assisted Badan Geology in developing a
    tsunami model for Maumere based on an Mw 8.1 earthquake. The Tsunami was
    modelled using open source software called ANUGA and elevation data
    from NEXTMap. The water depth is the maximum depth occurring across the
    entire tsunami event. For more information visit http://anuga.anu.edu.au/
    and http://intermap.com/

.. image:: /static/training/socialisation/009_tsunami.png
   :align: center


:ref:`Go to next module --> <introduction-to-qgis>`
