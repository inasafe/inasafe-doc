.. _socialisation_overview:

Overview
========

Concept
-------
To effectively prepare for future floods, earthquakes or tsunamis one must
first understand the likely impacts that need to be managed.
For example, to prepare a contingency plan for a severe flood in Jakarta,
emergency managers need to answer questions like:

- what are the areas likely to be affected?
- how many people will need to be evacuated and sheltered?
- which schools will be closed?
- which hospitals can still take patients?
- which roads will be closed?

|project_name| combines one exposure data layer (e.g. location of
buildings) with one hazard scenario (e.g. the footprint of a flood) and returns a spatial impact layer along with a statistical summary and action
questions.

|project_name| is framed around questions such as:

"In the event of **a flood similar to the 2007 Jakarta event** how many
**people** might need **evacuating**."

.. image:: /static/training/socialisation/001_inasafe_concept.png

|project_name| is also able to aggregate the impact results by administration
boundary and provide a breakdown of information about the gender and age of
affected people.

Background
----------

As one of the most hazard-prone and densely populated countries in the world,
Indonesia faces significant risk of loss of lives and challenges to
development progress as a result of natural disasters.
The development of contingency plans is seen as an important step to
strengthen disaster risk reduction programs.
However, this can only be effective when contingency plans utilize realistic
hazard scenarios.
Realistic hazard scenarios require scientific, sound and up-to-date data
hazard information as well as up-to-date, scale appropriate exposure data.
Such map-based contingency plans offer accurate and comprehensive results in
calculating minimum relief items, identifying safe places,
and sectorial planning.

|project_name| is free and open source software that provides a simple but
rigorous way to combine the data from scientists, local governments and
communities to provide insights into the likely impacts of future disaster
events.
The software is focused on examining, in detail, the impacts that a single
hazard would have on specific sectors.
For example, |project_name| can help users examine the location of primary schools and estimated number of students who would be affected by a possible tsunami in Maumere, Indonesia (when it happened during school
hours).
|project_name| has been developed as a QGIS plugin to enable end users to not
only complete a disaster impact analysis, but to also conduct further geographic analysis using the suite of QGIS tools that are available.
The software includes a simple-to-use interface in the hope that
disaster managers and other end users can easily create impact maps to inform contingency planning.

|project_name| was preliminarily launched by Dr. Agus Wibowo, Head of the Data
Center at the Indonesia’s Disaster Management Agency (|BNPB|),
at the Understanding Risk Forum in Cape Town on 3 July,2012.
There were over 300 downloads of the software within the first three weeks of
its preliminary launch.

|project_name| (Version 1.0) was officially launched at the 5th Asian
Ministerial Conference for Disaster Risk Reduction in Yogyakarta,
23–25 October 2012, by Mr. Dodi Ruswandi, the Deputy for disaster reduction
and preparedness, |BNPB|, Mr. Abhas Jha,  Disaster risk management coordinator
for East Asia and the Pacific from the World Bank,
and Dr. Matt Hayne co-director of Australia-Indonesia Facility for Disaster
Reduction (|AIFDR|).

|project_name| (Version 2.0) was officially launched at the opening of
the InaDRTG center in Jakarta in March 2014 by |BNPB|.

|project_name| is being taught across 6 provinces in Indonesia as one of
the 3 open source software tools used to enable development of realistic
disaster scenarios for contingency planning.
The other 2 tools are:

#. OpenStreetMap (|OSM|): a free map of the world that anyone can add to
   and edit.
   Utilizing community mapping allows for more detailed information that can
   be fed into |project_name| (e.g. how many houses will be affected by a
   specific hazard).
#. |QGIS|: an open source Geographical Information System software that
   allows users to spatially analyse their data.
   It is also the platform on which |project_name| is built.

|project_name| was selected as a 2012 Open Source Rookie of the Year by Black
Duck, the trusted partner for open source software adoption,
management and governance.
|project_name|, along with projects from groups such as Yahoo! and Twitter,
was selected for this prestigious award from amongst 1000’s of open source
programs that were started in 2012.

Input Data
----------

Effectively preparing for a disaster requires people from a wide range of
sectors and backgrounds to effectively work together and share their
experience, expertise, and resources.
Using |project_name| to develop a scenario requires the same spirit of
cooperation and sharing of expertise and data.

|project_name| is designed to use and combine existing data from science
agencies, local governments, and communities themselves.
Normally, information on the location of people and important assets are
provided by local communities and government departments responsible for each
sector, often through a facilitated part of a disaster preparedness and
planning exercise.

If the spatial data does not yet exist, external tools such as OpenStreetMap
(|OSM|) can allow governments and communities to quickly and easily map
their assets that are important to them.

.. note:: It is important to note that |project_name| is not a hazard
   modelling tool.
   Information on hazards needs to be provided either by technical experts,
   often from government agencies, universities or technical consultants,
   or from communities themselves based on their previous experiences.

The more communities, scientists and governments share data and knowledge,
the more realistic and useful the |project_name| scenario will be.
|project_name| accepts three types of Input data: Hazard, Exposure and
Aggregation.

Hazard
......

Hazard can be seen as a condition, phenomenon, or human activity that
potentially cause victims, losses or destruction to social structure and
environment.
Events or phenomena that are seen as hazard potentials include disasters such as earthquakes, tsunamis, floods, landslides and tornadoes.

For |project_name|, hazard data refers to a singular disaster scenario, such as a Mw 7.8 earthquake or volcanic eruption. Data for such infrequent events is created with scientific modeling software. For more frequently occurring disaster scenarios such as floods, the hazard data can be either modeled by scientists or directly mapped by the local community.

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

\* *To come in a future version of |project_name|*

The input hazard layer must have:

- a coordinates/location identifier
- specific hazard intensity (e.g. flood depth, earthquake’s MMI)
- temporal information when the event occurred or is expected to occur

Exposure
........

For |project_name|, exposure data may represent population density (number
of people found in a certain area) or important infrastructure (buildings,
bridges) that becomes a focus of interest when calculating the impact of
a specific hazard.

+--------------------------+-------------------------------------------+
|       Exposure           |                  Type                     |
+==========================+===========================================+
| Population               | Density (people/units\ :sup:`2` \)        |
+--------------------------+-------------------------------------------+
| Buildings                | Schools, Hospitals                        |
+--------------------------+-------------------------------------------+
| Other man-made structures| Bridges, telecommunications               |
+--------------------------+-------------------------------------------+
| \* Roads                 | major, minor                              |
+--------------------------+-------------------------------------------+
| \† Landslide             | Agriculture, industrial                   |
+--------------------------+-------------------------------------------+

\* *Is available for hazard layer footprints only; the next version of |project_name| will allow for modelled hazards.*

\† *To come in a future version of |project_name|.*

The input exposure layer must have:

- a coordinate/location identifier
- temporal information about when the data was collected
- type, if available

Aggregation
............

|project_name| prides itself on simplicity, but with each question answered a
new one arises.
"In the event of **<hazard>** how many **<exposure>** will be affected?",
is the core question that is answered by |project_name|. Aggregation data adds to this by providing options to divide your results by area, such as by province boundaries.
Instead of knowing only the total number of people affected by the hazard,
|project_name| is able to aggregate the results allowing the user to
understand how many people are affected in a certain administrative area.
This can aid local governments in understanding the impact specific to their district.

Impact Function
---------------

|project_name| is capable of having multiple impact functions specific to the input data.
Typically an impact function deals with the combination of one hazard
layer and one exposure layer.
The way the data is combined is specific to the impact function.
It could be a simple overlay of the two layers, or it could be a complicated
function that calculates if a building would fall down in an earthquake based
on building structure information.

The output of the impact function will usually have a spatial component (i
.e. a GIS layer which automatically loads into the map canvas) and a
non-spatial component (i.e. a list of estimates of disaster risk reduction
elements such as how many kilos of rice to make available,
or a list of actions you may want to consider carrying out) which will be
found in the |project_name| pane.

Impact functions can be written for any contingency planning purpose. One 
example is the minimum needs (minimum quantity of relief items per
person) that need to be supplied to refugees during/after a disaster.
The Indonesian Disaster Management Agency (|BNPB|) have identified these needs
per day, and |project_name| uses these numbers to calculate how much
food, water, toilets, family kits, and other resources are need during/after the disaster
based on the number of evacuated people.
This output directly informs contingency planners how much of each item is
needed to respond to a major disaster.

Additionally, an impact function can be configured ‘on the fly’ during the
analysis.
This will be touched on during the training exercise.
:ref:`impact_functions`

Keywords
........

An impact function is automatically chosen depending on the keywords
that have been allocated to the input layers.
The purpose of the keywords file is to provide additional metadata needed by
the impact functions.
For example, the keywords file will indicate whether a given dataset should be
treated as a hazard or an exposure layer.
It is also used to indicate the context of the layer (e.g. flood,
earthquake). This is discussed in more detail in :ref:`keywords_system`.

Available Impact Functions*
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

*\*This is not the complete list of impact functions currently in*
|project_name|

Output Data
-----------
Impact calculation produces an output layer representing potential damages or
losses of affected exposure.
The output layer will come out once the impact calculation process is
finished successfully.
If the aggregation feature is used, this output layer could be organized by
administrative boundaries.

In a typical impact analysis, the output data will include both a spatial layer (e.g., 
indicating where people are by density) and a non-spatial layer which will contain
statistics on the minimum needs of the number of people that ‘need evacuating’.

.. image:: /static/training/socialisation/002_output_data.png
