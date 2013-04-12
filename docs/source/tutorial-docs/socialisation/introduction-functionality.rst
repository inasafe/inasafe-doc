InaSAFE Functionality
=====================
Before we dive into using QGIS and InaSAFE, this chapter will explain InaSAFE current functionality, the functionality we will touch on today as well as the spatial datasets we will be using (located on your USB sticks).

Current Functionality of InaSAFE
--------------------------------
As explained in the previous section, InaSAFE needs to have a hazard layer and a exposure layer to create an impact layer. Currently InaSAFE has been designed for the following datasets:

Hazard
......

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

Exposure
........

=============  ================  =================  ==================  =======================   
**Exposure**   **Spatial Type**  **Exposure Type**  **Attribute Name**  **Hazard Units/Fields**
-------------  ----------------  -----------------  ------------------  -----------------------
Population     Raster            Density            N/A                 People per pixel 
Structures     Polygon           Structure type     type                text
Structures     Point             Structure type     type                text
=============  ================  =================  ==================  =======================

InaSAFE is a dynamic tool that can easily be adapted to other types of hazard and exposure layers.  The beauty of InaSAFE being open source, is that anyone that has a background in programming would be able to make their own Impact function.
If you dont, see page 55 for more details.
Please see the InaSAFE website for more information. http://inasafe.org

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
:InaSAFE name: people
:Source: http://asiapop.org
:Lisense: Creative Commons by Attribution (CCbyA)
:Coverage: ASEAN +
:About: High resolution, contemporary data on human population distributions are a prerequisite for the accurate measurement of the impacts of population growth, for monitoring changes and for planning interventions. The AsiaPop project was initiated in July 2011 with an aim of producing detailed and freely-available population distribution maps for the whole of Asia.
The raster pixel size is 100m by 100m.

.. image:: /static/socialisation/asiapop.jpeg
   :align: center

Structures
..........

:Name: OpenStreetMap(OSM)
:InaSAFE name: buildings
:Source: http://openstreetmap.org
:license: Open Data Commons Open Database License (ODbL)
:Coverage: World - incomplete
:About:  OpenStreetMap is a collaborative project to create a free editable map of the world. Two major driving forces behind the establishment and growth of OSM have been restrictions on use or availability of map information across much of the world and the advent of inexpensive portable satellite navigation devices.

.. image:: /static/socialisation/openstreetmap.png
   :align: center
   
AusAID has been working with the Humanitarian OpenStreetMap Team over the last 2 years in piloting and training OpenStreetMap in Indonesia.  The result so far is over 800,000 buildings have been mapped.  
The scenarios we will look at within this workshop are situated in Jakarta, Merapi (Central Java and Yogyakarta), Sumatra (specifically Padang) and Maumere, Flores. Each one of these areas has a different OpenStreetMap data collection methodology. Below will explain the methodologies used in Jakarta and Padang.

:Jakarta: BPBD DKI Jakarta (Regional Disaster Managers) and BNPB (Nationals Disaster Managers) with assistance from AIFDR (Australia-Indonesia Facility for Disaster Reduction), the World Bank, UNOCHA, Humanitarian OpenStreetMap Team and University of Indonesia held workshops in each of Jakarta’s 6 Districts in order to help Village Heads map their community boundaries and major infrastructure. Over 500 representatives from Jakarta’s 267 Villages participated in these workshops – and have mapped an impressive 6,000 buildings and all 2,668 sub-village boundaries (Rukun Warga-RW). http://www.aifdr.org/?p=619
:Padang: Post Hati’s earthquake in 2010, there was a huge effort to map Hati through OSM, coordinating this effort was very hard, and hence AusAID subsequently funded the creation of OSM tasking Server.  The OSM tasking server is a web-base tool where you are able to select your own square to map.  The first pilot of the web-tool was in Padang, the specified area is now 100% finished with over 95,000 buildings mapped. However the buildings are purely footprints, an on the ground mapping effort is needed to record what type of building it is.  The tool is now being used across world to coordinate OSM mapping efforts. http://tasks.hotosm.org/

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

:Name:  HKL Flood Model
:InaSAFE name:  a flood similar to the 2007 Jakarta event
:Source: HKL - http://deltares.nl
:license: Creative Commons by Attribution (CCbyA)
:Coverage: Jakarta
:About: The Flood model was created by scientist/engineers in coordination with DKI Jakarta Public Works based on the 2007 flood conditions.  The water depth is the maximum depth occurring across the entire flooding period.

Flood Footprint
...............

:Name:  Jakarta flood areas on the 18/1/2013
:InaSAFE name:  Jakarta flooding on the 18th January 2013
:Source: OpenStreetMap and BPBD DKI Jakarta
:license: Creative Commons by Attribution (CCbyA)
:Coverage: Jakarta
:About: Based on the subvillage boundaries that were map during the DKI mapping project, we were able to use this dataset during the recent floods to identify the areas that had been flooded based on information provided by the villages.

.. image:: /static/socialisation/floodmodel.png
   :align: left

.. image:: /static/socialisation/floodfootprint.png
   :align: right
   
Volcano
.......

:Name:  Global Volcanism Program
:InaSAFE name:  volcano
:Source: Smithsonian  http://volcano.si.edu
:license: United States Copyright
:Coverage: World
:About: The Smithsonian’s Global Volcanism Program seeks better understanding of all volcanoes through documenting their eruptions — small as well as large — during the past 10,000 years. Through their website you are able to download a spreadsheet of all the recorded volcanoes.  This spreadsheet also has the volcano location, which has been turned into a point file.

.. image:: /static/socialisation/volcano.png
   :align: center

Earthquake
..........

:Name:  Shakemap of Pandang 2009 earthquake
:InaSAFE name: an earthquake in Padang like 2009
:Source: Badan Geologi and AIFDR
:license: Creative Commons by Attribution
:Coverage: Padang
:About: A shakemap is a representation of ground shaking produced by an earthquake.  This particular scenario was modelled based on the 30 September 2009 Mw 7.9 earthquake in Padang.
ShakeMaps are generated automatically following moderate and large earthquakes by USGS.
http://earthquake.usgs.gov/earthquakes/map/
Pre-event / scenario based shakemaps need to be modelled by earthquake specialist.

.. image:: /static/socialisation/padang_earthquake.png
   :align: center

Tsunami
.......

:Name:  Maumere Tsunami
:InaSAFE name:  A tsunami in maumere (Mw 8.1)
:Source: AIFDR and Badan Geologi
:license: Creative Commons by Attribution
:Coverage: Maumere, Flores
:About: In September 2011 the Indonesian government held a national exercise in Maumere, Flores. AIFDR assisted Badan Geologi in developing a tsunami model for Maumere based on an Mw 8.1 earthquake.  The Tsunami was modelled using the an open source software called ANUGA and elevation from NEXTMap. The water depth is the maximum depth occurring across the entire tsunami event. http://anuga.anu.edu.au/ and http://intermap.com/

.. image:: /static/socialisation/tsunami.png
   :align: center
   











   
   
   
















 
      




  