Introduction and Overview of InaSAFE
====================================

Concept
-------
To effectively prepare for future floods, earthquakes or tsunami you must first understand the likely 
impacts that need to be managed. For example, to prepare contingency plans for a severe flood in Jakarta, 
emergency managers need to answer questions like:

- what are the areas likely to be affected;
- how many people will need to be evacuated and sheltered;
- which schools will be closed;
- which hospitals can still take patients; and
- which roads will be closed?

Conceptually InaSAFE combines one exposure layer (e.g. buildings) with one hazard scenario
(e.g. flooding) and returns an impact layer along with textual staticial summary.

.. image:: docs/resources/en/socialisation/inasafe_concept.png

InaSAFE is framed around questions such as:

"In the event of **a flood similar to the 2007 Jakarta event** how many **people** might need 
**evacuating**."

Background
----------

As one of the most hazard-prone and densely populated countries in the world, Indonesia faces 
significant risk of loss of lives and challenges to development progress as a result of natural disasters.  
The development of contingency plans is seen as an important step to strengthen disaster risk reduction programs. 
However this can only be effective when contingency plans utilises realistic hazard scenario. 
Realistic hazard scenarios require scientific, sound and up-to-date data related to sources of hazard 
and elements of exposure.  Such map-based contingency plans offer accurate and comprehensive results 
in calculating minimum relief items, identifying safe places, and sectorial planning.

InaSAFE is free and open source software that provides a simple but rigorous way to combine the data 
from scientists, local governments and communities to provide insights into the likely impacts of 
future disaster events. The software is focused on examining, in detail, the impacts by a single 
hazard would have on specific sectors. For example location of primary schools and estimated number 
of students affected by a possible tsunami in Maumere (when it happened during the school hours).
InaSAFE has been developed as a QuantumGIS plugin to enable end users to do scenario development 
using their collected hazard and exposure data. The software has been designed as a simple user 
interface in a hope that disaster managers and end users can easily use it for creating disaster 
scenario maps in Indonesia easily.

InaSAFE was preliminarily launched by Dr Agus Wibowo, the Head of Indonesian Disaster Management 
Agency’s Data Centre, at the Understanding Risk Forum in Cape Town on 3 July, 2012. There were over 
300 downloads of the software within the first three weeks of its preliminary launch.

InaSAFE (Version 1.0) was officially launched at the 5th Asian Ministerial Conference for Disaster 
Risk Reduction in Yogyakarta, 23–25 October 2012, by Mr Dodi Ruswandi, the Deputy for disaster reduction 
and preparedness from Indonesia’s Disaster Management Agency (BNPB), Mr Abhas Jha,  Disaster risk 
management coordinator for East Asia and the Pacific from the World Bank, and Dr Matt Hayne 
co-director of the Australian Government funded Australia-Indonesia Facility for Disaster Reduction.

InaSAFE is now being taught across 6 provinces in Indonesia as one of the 3 open source software 
tools used to enable development of realistic disaster scenarios for contingency planning. The other 2 tools are:

#. OpenStreetMap  (OSM): is a free map of the world that anyone can add to and edit.  Utilizing community mapping allows for more detailed information that can be fed into InaSAFE (i.e. How many houses will be affected by a specific hazard).
#. QuantumGIS  (QGIS): an open source Geographical Information System software that allows users to spatially analyse their data. It is also the platform on which InaSAFE is built.

InaSAFE was selected as a 2012 Open Source Rookie of the Year by Black Duck, the trusted partner for
open source software adoption, management and governance.  InaSAFE, along with projects from groups 
such as Yahoo! and Twitter, was selected for this prestigious award from amongst 1,000’s of open 
source programs that were started in 2012.

Input Data
----------

Effectively preparing for a disaster requires people from a wide range of sectors and backgrounds to 
effectively work together and share their experience, expertise, and resources. Using InaSAFE to develop 
a scenario requires the same spirit of cooperation and sharing of expertise and data.

InaSAFE is designed to use and combine existing data from science agencies, local governments, and 
communities themselves. Normally, information on the location of people and important assets are 
provided by local communities and government departments responsible for each sector, often through 
a facilitated part of a disaster preparedness and planning exercise.

Where appropriate spatial data doesn’t yet exist, external tools such as OpenStreetMap (see ) 
can allow governments and communities to quickly and easily map their assets that are important to them.

.. note:: It is important to note that InaSAFE is not a hazard modelling tool. Information on hazards needs to be provided either by technical experts, often from Government agencies, universities or technical consultants, or from communities themselves based on their previous experiences.

The more communities, scientists and governments share data and knowledge, the more realistic and 
useful the InaSAFE scenario will be. InaSAFE accepts three types of Input data, Hazard, Exposure and 
Aggregation.

Hazard
......

Hazard can be seen as a condition, phenomenon, or human activity that potentially cause victims, 
losses or destruction to social structure and environment. Events or phenomena that frequently are 
seen as hazard potentials include earthquakes, tsunamis, floods, landslides, tornadoes etc.

For InaSAFE, hazard data refers to a singular disaster scenario (i.e. a Mw 7.8 earthquake or a 
volcanic eruption) that has been developed through scientific modelled software for infrequent events, 
for more frequent events such as floods it can either be modelled by scientist or mapped by the community. 
The hazard must be accompanied by specific units:

+-------------------+-------------------------------------------+--------------------+ 
|       Hazard      |                  Modelled                 |     Footprints     | 
+===================+===========================================+====================+ 
| Earthquake        | MMI (shakemap)                            |                    | 
+-------------------+-------------------------------------------+--------------------+ 
| Tsunami           | Max depth in Meters                       |                    |
+-------------------+-------------------------------------------+--------------------+
| Volcanic Eruption | ash load (kg\ :sup:`2` \/m\ :sup:`2` \)   | Hazard Zones       |
+-------------------+-------------------------------------------+--------------------+
| Flood             | Max depth in Meters                       | Flood prone areas  |
+-------------------+-------------------------------------------+--------------------+
| \*Landslide       |                                           | Hazard Zone        |
+-------------------+-------------------------------------------+--------------------+
| \*Bush Fire       |                                           | Hazard Zone        |
+-------------------+-------------------------------------------+--------------------+
| \*Cyclone/Tornado |                                           |                    |
+-------------------+-------------------------------------------+--------------------+

*\*To come in future version of InaSAFE*

The input Hazard layer must have:

- a coordinates/location identifier
- specific hazard intensity (e.g. flood depth, earthquake’s MMI)
- temporal information when the event occurred or is expected to occur

Exposure
........

For InaSAFE, exposure data is refers to as population density (number of people found in a certain area)
or important infrastructure (buildings, bridges etc). that become a focus of interest when calculating 
the impact of a specific hazard.







