.. _inasafe_concepts:

Key concepts in disaster management planning with |project_name|
================================================================
In this section we explain the basic concepts of |project_name| and the merits
of disaster management planning.

Definitions:
------------
Before we start, here are some definitions you may find useful.

**Risk assessment:**  *“A methodology to determine the nature and extent of risk
by analysing potential hazards and evaluating existing conditions of
vulnerability that together could potentially harm exposed people, property,
services, livelihoods and the environment on which they depend. ”*
Source `<http://www.unisdr.org/we/inform/terminology>`_


**Contingency planning:**  *“A management process that analyses specific
potential events or emerging situations that might threaten society or the
environment and establishes arrangements in advance to enable timely,
effective and appropriate responses to such events and situations.”*
Source: `<http://www.unisdr.org/we/inform/terminology>`_

**Response:** *“The provision of emergency services and public assistance during
or immediately after a disaster in order to save lives, reduce health impacts,
ensure public safety and meet the basic subsistence needs of the people
affected.”*
Source: `<http://www.unisdr.org/we/inform/terminology>`_

In the context of disaster management, the expected ‘normal’ situation is that
there is no disaster in progress, and people are going about their normal
daily lives. Disaster managers need to plan for the occasions when the ‘normal’
situation has been replaced by a disaster and people can no longer go about
their normal daily lives. In order to prepare for such situations, disaster
managers need to have a basic understanding of questions like:
- how many people might be in the affected area?

- how might those people be impacted?

For example are they likely to be injured, stranded, deceased, or unable to
continue with their normal economic activities;  have they lost access to
food and water?

- how will roads in the affected area be impacted?

- how many dwellings in the affected will be affected? And to what degree?

For example in a flood are buildings dry, wet (but still possibly habitable)
or flooded (with occupants evacuated)?

- if people are affected, how many of them are likely to be women, children, pregnant, elderly etc.?


Knowing the likely answers to these questions can be helpful to disaster
managers. For example if you are aware of how many people live in flood prone
areas you can estimate how many temporary shelters might be needed in the
event of a disaster, how many provisions should be stockpiled in order to
provide for the daily needs of affected people and so on. Having demographic
breakdowns for the people likely to be affected, can help disaster managers
include things like special dietary requirements for lactating women in their
disaster management planning.

This planning might also take into account expected impacts on
infrastructure - for example by planning to have sufficient rescue boats
should all the local roads be flooded.

What is a hazard?
-----------------
.. image:: /static/training/socialisation/004_hazard.png
   :align: center

In the context of |project_name| a hazard is any natural or human caused event
or series of events that may negatively impact the population, infrastructure
or resources in an area.

Some examples of natural hazards:

- a flood (caused by overflowing rivers, storm surge, localised precipitation that cannot drain effectively, or by engineering failure such as a dam or levee breach)

- an earthquake and the resulting ground shaking that is produced by it

- a volcano and the resulting lava flow from a volcano

- ash fall from a volcano

- a tsunami

Some examples of non-natural hazards:

- a chemical spill

- a nuclear plant failure

- an industrial fire / explosion

It is important to note that |project_name| is not a hazard modelling tool.
That means that you need to obtain your hazard data from elsewhere and bring
it along ready to use in |project_name|. In this training course we will
focus on natural hazards, so we will take a moment here to explain how
hazard datasets might be made.

.. image:: /static/training/socialisation/004_jakarta_flood.png
   :align: center

There are three main ways that can be used to generate hazard datasets:

- Local knowledge

- Modelling

- Mapping

Local Knowledge
...............

This is probably the most practical way to gather hazard data quickly.
One approach that has been effective in Indonesia is to hold mapping
workshops where village chiefs and local officials are invited. The officials
are asked to indicate which villages and sub-villages within their area of
responsibility flood regularly.

Instead of simply mapping which areas are flooded, it is also possible to
take another approach and map each flood event, using the same boundaries
(village / sub-village). During the event community officials can use online
systems to update the status of the flood waters in their area.

A key requirement for any local knowledge based process is that there are
suitable mapping units available to use for deciding if an area is flood
prone or not. In some cases participants may need to capture these, in other
cases village or sub-village boundaries can be used. Using administrative
boundaries may not always be ideal since the flood extents are unlikely to
align well with the boundaries, but it may be sufficient for broad
planning purposes; especially when response activities are managed at the
same administrative level.

Modelling
.........

Modelling floods is an entire discipline in it’s own right. Flood modelling
can be carried out by combining factors such as precipitation, geology and
runoff characteristics, terrain etc. to derive a model of impending or
current flood. Modelling can use data interpolation techniques - e.g. by
taking flood depth readings manually or using telemetry from various sites
around the flood prone area, flood depths can be interpolated to estimate
the depth at places that were not sampled.

Another modelling approach used by engineers is to install depth sensors
upstream of the catchment and then try to model how much water is coming into
the catchment area based on depth and flow rates. This has the potential
advantage of giving early warning before floods enter the flood prone area,
although it also has the disadvantage that localised rainfall may not be
accurately considered in the model.

Using a digital elevation model (DEM) and a stream network, it is also
possible to generate a simple model of which areas might be inundated by a
water rise in the river network of a certain amount. DEM cells adjacent to
the stream network which are below the flood-rise threshold will be
considered flooded and then those cell neighbours can in turn be considered
so as to ensure that only contiguous areas in the DEM are flagged as inundated.
There are various other approaches that can be used to model flood potential
that involve using a DEM.

One advantage of using a modelling approach is that it allows us to do
forecasting for abnormal events. For example, there may not be localised
knowledge about 50 or 100 year flood events and their impacts, but these
can be estimated using modelling techniques.

Single-event versus multiple-event hazards
------------------------------------------
Hazard data used in |project_name| can be either single-event or
multiple-event. Single event hazards are useful when you want to estimate
scenarios like *‘how many people would be affected if we had another flood
like in 2013’.* A single event hazard covers a short span of time - like a
single flood or earthquake event. Single event data is also the most suitable
to use for events which are stochastic e.g. earthquakes which seldom occur
at the same place and with the same intensity more than once.

Multiple-event data are useful when you would like to plan for disasters
that repeatedly affect the same area. For example over the course of 10 years,
the same districts or sub-districts may get flooded, though not on every event.
Flood and volcano eruptions may be good candidates for using multiple-event
data in your disaster management planning.


Requirements for using flood data in |project_name|


+--------+---------------------------------------------------------------------+
|        |   **Key notes for floods**                                          |
+========+=====================================================================+
|Format  |  Vector polygon data or raster data                                 |
+--------+---------------------------------------------------------------------+
|Vector  | A field representing whether the polygon is flood prone or not.     |
+--------+---------------------------------------------------------------------+
|Raster  | A simple grid with cell values that represent water depth           |
+--------+---------------------------------------------------------------------+
|Source  | Can be obtained from community mapping or a national mapping agency |
+--------+---------------------------------------------------------------------+

What is exposure?
-----------------
.. image:: /static/training/socialisation/004_exposure.png
   :align: center

In the context of |project_name|, exposure refers to people, infrastructure
or land areas that may be affected by a disaster. Currently |project_name|
supports three kinds of exposure data:

- roads

- buildings

- population / people

Roads data
..........

.. image:: /static/training/socialisation/icon_road.png
   :align: left

Road datasets are a useful data source when you want to understand the impact
of a flood on roads infrastructure. With the |project_name| flood on roads
impact functions; you can calculate which roads of which type might be
impacted by a flood.

Very often there will be national datasets available for roads.  In this case
you should contact your national mapping agency for up-to-date datasets.
The OpenStreetMap project is an excellent source of exposure data. The data
is freely available, generally well maintained and a vital resource for
disaster management planners. There are numerous ways to download
OpenStreetMap roads data, but our recommended way is to download the data
using the OSM download tool provided with |project_name|.


+--------+---------------------------------------------------------------------+
|        |   **Key notes for road data**                                       |
+========+=====================================================================+
|Format  |  Vector line data                                                   |
+--------+---------------------------------------------------------------------+
|Field   | A field representing road type                                      |
+--------+---------------------------------------------------------------------+
|Notes   | Topologically correct data are best but not essential               |
+--------+---------------------------------------------------------------------+
|Source  | Can be obtained from community mapping or a national mapping agency |
+--------+---------------------------------------------------------------------+


Buildings (structure) data
..........................

.. image:: /static/training/socialisation/icon_building.png
   :align: left

Like roads, buildings footprints can be a useful dataset to have for
understanding the impacts of a flood. For example you may wish to know
‘how many buildings might be flooded, and what types of buildings are they?’.
In |project_name|  you do not need to use engineering quality data.
We are more concerned with the numbers and types of structures affected by a
disaster and do not work at engineering tolerances needed when, for example,
planning a new water mains system.

+--------+---------------------------------------------------------------------+
|        |   **Key notes for building data**                                   |
+========+=====================================================================+
|Format  |  Vector polygon data                                                |
+--------+---------------------------------------------------------------------+
|Field   | A field representing building type                                  |
+--------+---------------------------------------------------------------------+
|Notes   | |project_name| does not need 'engineering quality' data             |
+--------+---------------------------------------------------------------------+
|Source  | Can be obtained from community mapping or a national mapping agency |
+--------+---------------------------------------------------------------------+

Population data
...............
.. image:: /static/training/socialisation/icon_people.png
   :align: left

Population data can often be obtained from your census bureau or through
various online data sources. One problem with population data is that it is
often quite coarse (represented using a raster with a large pixel size) and
so analysis at large scales (e.g. a small neighbourhood) using population
data may not always be the best idea. Currently |project_name|  only supports
raster based census data, but in the near future we will be releasing a
version that supports assigning population estimates to buildings using
census data. One of the nicest online resources for population data is
‘WorldPop’ - a project that aims to provide population data for anywhere
in the globe produced in a standardised and rigorous way.

+--------------+---------------------------------------------------------------+
|              |   **Key notes for population data**                           |
+==============+===============================================================+
|Format        |  Raster 'cell' data                                           |
+--------------+---------------------------------------------------------------+
|Requirements  | Currently the data should be in EPSG:4326 CRS                 |
+--------------+---------------------------------------------------------------+
|Notes         | Make sure you know if your data represent density or count    |
+--------------+---------------------------------------------------------------+
|Source        | WorldPop or from a  national census agency                    |
+--------------+---------------------------------------------------------------+

What is aggregation?
--------------------
Aggregation is the process whereby we group the results of the analysis by
district so that you can see how many people, roads or buildings were
affected in each area. This will help you to understand where the most
critical needs are, and to generate reports as shown in the image below.
Aggregation is optional in |project_name| - if you do not use aggregation,
the entire analysis area will be used for the data summaries.
Typically aggregation layers in |project_name| have as attributes the name
of the district or reporting area. It is also possible to use extended
attributes to indicate the ratio of men and women, children, adults and
elderly living in each area. Where these are provided and the exposure layer
is population, |project_name| will provide a demographic breakdown per
aggregation area indicating how many men, women etc were probably affected
in that area.

.. image:: /static/training/socialisation/004_BengawanSolo.png
   :align: left

What is contextual data?
------------------------

