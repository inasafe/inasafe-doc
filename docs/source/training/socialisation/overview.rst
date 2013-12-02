.. _socialisation_overview:

Overview
========

Concept
-------
To effectively prepare for future floods, earthquakes or tsunami you must
first understand the likely impacts that need to be managed. For example,
to prepare a contingency plan for a severe flood in Jakarta,
emergency managers need to answer questions like:

- what are the areas likely to be affected;
- how many people will need to be evacuated and sheltered;
- which schools will be closed;
- which hospitals can still take patients; and
- which roads will be closed?

Conceptually |project_name| combines one exposure layer (e.g. location of buildings) with
one hazard scenario (e.g. flooding footprint) and returns a spatial impact layer along
with textual statistical summary and action questions.

|project_name| is framed around questions such as:

"In the event of **a flood similar to the 2007 Jakarta event** how many
**people** might need **evacuating**."

.. image:: /static/training/socialisation/001_inasafe_concept.png

|project_name| is also able to aggregate the impact results by administration
boundary and provided breakdown information about gender and age of affected people.

Background
----------

As one of the most hazard-prone and densely populated countries in the world,
Indonesia faces significant risk of loss of lives and challenges to
development progress as a result of natural disasters. The development of
contingency plans is seen as an important step to strengthen disaster risk
reduction programs. However this can only be effective when contingency plans
utilise realistic hazard scenario. Realistic hazard scenarios require
scientific, sound and up-to-date data hazard information as well as up-to-date, scale
appropriate exposure.  Such map-based contingency plans offer accurate and
comprehensive results in calculating minimum relief items,
identifying safe places, and sectorial planning.

|project_name| is free and open source software that provides a simple but
rigorous way to combine the data from scientists, local governments and
communities to provide insights into the likely impacts of future disaster
events. The software is focused on examining, in detail,
the impacts by a single hazard would have on specific sectors. For example
location of primary schools and estimated number of students affected by a
possible tsunami in Maumere (when it happened during the school hours).
|project_name| has been developed as a QuantumGIS plugin to enable end users
to not only complete an InaSAFE analysis, but to also analysis the result using
the suite of QGIS tools that are available. The software has been designed as a
simple user interface in a hope that disaster managers and end users can easily
use |project_name| for creating impact maps to inform contingency planning.

|project_name| was preliminarily launched by Dr Agus Wibowo, Head of the Data
Center at the Indonesia’s Disaster Management Agency (|BNPB|),
at the Understanding Risk Forum in Cape Town on 3 July,2012. There were over 300
downloads of the software within the first three weeks of its preliminary launch.

|project_name| (Version 1.0) was officially launched at the 5th Asian
Ministerial Conference for Disaster Risk Reduction in Yogyakarta,
23–25 October 2012, by Mr Dodi Ruswandi, the Deputy for disaster reduction
and preparedness, |BNPB|, Mr Abhas Jha,  Disaster risk management coordinator
for East Asia and the Pacific from the World Bank, and Dr Matt Hayne co-director
of Australia-Indonesia Facility for Disaster Reduction (|AIFDR|).

|project_name| is now being taught across 6 provinces in Indonesia as one of
the 3 open source software tools used to enable development of realistic
disaster scenarios for contingency planning. The other 2 tools are:

#. OpenStreetMap (|OSM|): is a free map of the world that anyone can add to
   and edit. Utilizing community mapping allows for more detailed information
   that can be fed into |project_name| (i.e. How many houses will be affected
   by a specific hazard).
#. QuantumGIS (|QGIS|): an open source Geographical Information System
   software that allows users to spatially analyse their data. It is also the
   platform on which |project_name| is built.

|project_name| was selected as a 2012 Open Source Rookie of the Year by Black
Duck, the trusted partner for open source software adoption,
management and governance. |project_name|, along with projects from groups
such as Yahoo! and Twitter, was selected for this prestigious award from
amongst 1,000’s of open source programs that were started in 2012.

Input Data
----------

Effectively preparing for a disaster requires people from a wide range of
sectors and backgrounds to effectively work together and share their
experience, expertise, and resources. Using |project_name| to develop a
scenario requires the same spirit of cooperation and sharing of expertise and
data.

|project_name| is designed to use and combine existing data from science
agencies, local governments, and communities themselves. Normally,
information on the location of people and important assets are provided by
local communities and government departments responsible for each sector,
often through a facilitated part of a disaster preparedness and planning
exercise.

If the spatial data does not yet exist, external tools such as OpenStreetMap
(|OSM|) can allow governments and communities to quickly and easily map
their assets that are important to them.

.. note:: It is important to note that |project_name| is not a hazard
   modelling tool. Information on hazards needs to be provided either by
   technical experts, often from Government agencies,
   universities or technical consultants, or from communities themselves
   based on their previous experiences.

The more communities, scientists and governments share data and knowledge,
the more realistic and useful the |project_name| scenario will be.
|project_name| accepts three types of Input data, Hazard, Exposure and
Aggregation.

Hazard
......

Hazard can be seen as a condition, phenomenon, or human activity that
potentially cause victims, losses or destruction to social structure and
environment. Events or phenomena that frequently are seen as hazard
potentials include earthquakes, tsunamis, floods, landslides, tornadoes etc.

For |project_name|, hazard data refers to a singular disaster scenario (i.e.
a Mw 7.8 earthquake or a volcanic eruption) that has been developed through
scientific modelled software for infrequent events, for more frequent events
such as floods it can either be modelled by scientist or mapped by the
community.

The hazard must be accompanied by specific units:

+------------------------+-----------------------------------------+----------------------+
|       Hazard           |                  Modelled               |     Footprints       |
+========================+=========================================+======================+
| Earthquake             | MMI (shakemap)                          |                      |
+------------------------+-----------------------------------------+----------------------+
| Tsunami                | Max depth in Meters                     |                      |
+------------------------+-----------------------------------------+----------------------+
| Volcanic Eruption      | ash load (kg\ :sup:`2` \/m\ :sup:`2` \) | Hazard Zones         |
+------------------------+-----------------------------------------+----------------------+
| Flood                  | Max depth in Meters                     | Flood prone areas    |
+------------------------+-----------------------------------------+----------------------+
| \*Landslide            |                                         | Hazard Zone          |
+------------------------+-----------------------------------------+----------------------+
| \*Bush Fire            |                                         | Hazard Zone          |
+------------------------+-----------------------------------------+----------------------+
| \*Cyclone/Tornado      |                                         |                      |
+------------------------+-----------------------------------------+----------------------+

*\*To come in future version of InaSAFE*

The input Hazard layer must have:

- a coordinates/location identifier
- specific hazard intensity (e.g. flood depth, earthquake’s MMI)
- temporal information when the event occurred or is expected to occur

Exposure
........

For |project_name|, exposure data is refers to as population density (number
of people found in a certain area) or important infrastructure (buildings,
bridges etc). that become a focus of interest when calculating the impact of
a specific hazard.

+--------------------------+-------------------------------------------+
|       Exposure           |                  Type                     |
+==========================+===========================================+
| Population               | Density (people/units\ :sup:`2` \)        |
+--------------------------+-------------------------------------------+
| Buildings                | Schools, Hospitals                        |
+--------------------------+-------------------------------------------+
| Other Man-made structure | Bridges, telecommunications               |
+--------------------------+-------------------------------------------+
| \*Roads                  | major, minor                              |
+--------------------------+-------------------------------------------+
| \*Landslide              | Agriculture, industrial                   |
+--------------------------+-------------------------------------------+

*\*To come in future version of InaSAFE*

The input Exposure layer must have:

- a coordinate/location identifier
- temporal information when the data was collected
- type, if available

Aggregation
............

|project_name| prides itself on simplicity, but with each question answered a
new one arises. “In the event of **<hazard>** how many **<exposure>** will be
affected?“, is the core question that is answered by InaSAFE, but aggregation
adds to this by providing options to divide your results by area such as
province boundaries. Instead of just knowing the total number of people affected
by the hazard, |project_name| is able to aggregate
allowing the user know how many people are affected in a certain administration
area. Hence the local governments will be able understand the impact to their
specific area.


Impact Function
---------------

The core to |project_name| is its capability of having multiple Impact
functions specific to the input data. An impact function generally only deals
with the combination of 1 hazard layer with 1 exposure layer. The way it is
combined is specific to the impact function, it could be a simple overlay of
the 2 layer, or it could be a complicated function that calculate if a building
would fall down in an earthquake based on building structure information

The output of the impact function will typically have a spatial component (e.g. a
GIS layer which automatically loads into the map canvas) and a non-spatial
component (e.g. a list of estimates of disaster risk reduction elements such as
how many kilos of rice to make available, or a list of actions you may want to
consider carrying out) which will be found in the InaSAFE window panel.

Impact functions can be written for any contingency planning purpose,
one example is the minimum needs (minimum quantity of relief items per per
person) that need to be supplied to refugees during/after a disaster. The
Indonesian Disaster Management Agency (|BNPB|) have identified these needs
per day, and |project_name| has used these numbers to calculate how much
food, water, toilets, family kits etc are need during/after the disaster
based on the number of evacuated people. This output directly informs
contingency planners how much of each item is needed to withstand a major
disaster.

Additionally an impact functions can be configured ‘on the fly’ during the
analysis.  This will be touched on during the training exercise.
:ref:`impact_functions`


Keywords
........

An Impact function will automatically be chosen depending on the keywords
that has been allocated to the input layers. The purpose of the keywords file
is to provide additional metadata needed by the impact functions. For
example, the keywords file will indicate whether a given dataset should be
treated as a hazard or an exposure layer. It is also used to indicate the
context of the layer (e.g. flood, earthquake). :ref:`keywords_system`

Available Impact Functions
..........................

+-------------------+----------------+--------------------------+--------------------------------------------------------------------+
|       Hazard      |   How many     |         might            |                              output                                |
+===================+================+==========================+====================================================================+
| Earthquake        | People         | die or be displaced      | Number of people dead or displaced                                 |
+-------------------+----------------+--------------------------+--------------------------------------------------------------------+
| Earthquake        | Buildings      | be affected              | Number of buildings affected                                       |
+-------------------+----------------+--------------------------+--------------------------------------------------------------------+
| Flood             | People         | need evacuating          | Number of people affected and Number of people needing evacuation  |
+-------------------+----------------+--------------------------+--------------------------------------------------------------------+
| Flood             | Buildings      | be affected              | Number of buildings affected                                       |
+-------------------+----------------+--------------------------+--------------------------------------------------------------------+
| Tsunami           | People         | need evacuating          | Hazard Zone                                                        |
+-------------------+----------------+--------------------------+--------------------------------------------------------------------+
| Tsunami           | Buildings      | be affected              | Number of buildings affected                                       |
+-------------------+----------------+--------------------------+--------------------------------------------------------------------+
| Volcano           | People         | need evacuating          | Number of people affected and Number of people needing evacuation  |
+-------------------+----------------+--------------------------+--------------------------------------------------------------------+
| Volcano           | Buildings      | be affected              | Number of buildings affected                                       |
+-------------------+----------------+--------------------------+--------------------------------------------------------------------+

*\*This is not the complete list of Impact functions currently in InaSAFE.*

Output Data
-----------
Impact calculation produces an output layer representing potential damages or
losses of affected exposure. The output layer will come out once the impact
calculation process is finished successfully. As previously indicated this
output layer could potentially be aggregated by administration boundaries.

Using the example explained in Impact functions about the minimum needs,
the output data will be both a spatial layer indicating where people are (by
density) and the non-spatial layer will have statistics on the minimum needs
based on the number of people that ‘need evacuating’.

.. image:: /static/training/socialisation/002_output_data.png


