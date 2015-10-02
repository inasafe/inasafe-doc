.. _run_intermediate_inasafe:

.. image:: /static/training/socialisation/inasafe_logo.*

Run Intermediate |project_name|
===============================

Introduction
------------

In `Run Basic InaSAFE <http://docs.inasafe.org/en/training/socialisation/run_basic_inasafe.html/>`__ we learned how to run flood analysis on
population and buildings, understand flood impact default settings and
impact summary report, and how to change analysis threshold. We also
learned how to save our work and generate a pdf of the analysis results.
In this exercise we will learn more techniques such as how to run
|project_name| with aggregation data to produce more specific results. And we
will learn how to download data using the OpenStreetMap downloader and
how to run |project_name| analysis on the downloaded building points and roads.
Last but not least, we will learn how to define the analysis area.

Learning Objective
------------------

To improve participant’s understanding of the |project_name| function and
features. By the end of this exercise, participants will be able to:

- Define keywords using the |project_name| keyword wizard

- Run |project_name| with aggregation data

- Use the OpenStreetMap Downloader to download data for |project_name| and

- Set the |project_name| analysis area using the |project_name| analysis area tool.

Data for this exercise
----------------------

DKI Jakarta.zip from `|project_name| Training
Data <http://data.inasafe.org/TrainingDataPackages/>`__ and we will use
the following data:

1. Jakarta Flood 18113 WGS84

2. Jakarta District Boundary WGS84

3. Jakarta Subdistrict Boundary WGS84

4. Jakarta Population WGS84

Exercise
--------

Run |project_name| for Population Data
......................................

A. Add and symbolize vector data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before we start, click :guilabel:`Open` and select :file:`DKI Jakarta Intermediate.qgs`.
If there is notification to save the current project, you can choose
either to save the project or not. It will look like this:

.. image:: /static/training/socialisation/intermediate_inasafe_01.*
   :align: center
   :width: 300 pt

Next, add :file:`Jakarta Flood 18113 WGS84` data from :file:`Run Intermediate InaSAFE > DKI Jakarta > 01 Hazard Data`. This is the flood hazard data
for Jakarta from an actual flood event. During Jakarta floods in January
2013, provincial disaster manager collects information about flood,
including the location of flooded areas by sub-village boundary
(`see more about this data at… <http://docs.inasafe.org/en/training/socialisation/datasets.html>`__).

Let us symbolize this layer so that it shows only affected areas (if you
forget how to symbolize, you can go to `Introduction to QGIS <http://docs.inasafe.org/en/training/socialisation/introduction_to_qgis.html/>`__).
The layer should look like this:

.. image:: /static/training/socialisation/intermediate_inasafe_02.*
   :align: center
   :width: 300 pt

Now we already know which area in Jakarta categorized as
flooded/affected area. Next, we will analyze the data using |project_name|.
When you see on the right side, you will notice that the hazard is not
there and only exposure data (population) that is available there, even
though you already turn ON the data layer. Do you know why |project_name| did
not put the Jakarta Flood Vector Hazard data to the dock? The answer
will be provided in the next section.

B. Define keyword for hazard data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|project_name| need some keyword to figure out what type of data that a user
provide for analysis (hazard data, exposure data or aggregation data).
If the data provided does not have a keyword, it will show a warning
message “Layer Keyword Missing” in |project_name| Dock. Try select :guilabel:`A Flood in
Jakarta like 2013` layer and look at the |project_name| dock, you will see
like this:

.. image:: /static/training/socialisation/intermediate_inasafe_03.*
   :align: center
   :width: 300 pt

As you can see from the picture above, this layer keywords is missing
and we need to open the keyword wizard to solve this problem. The
keywords wizard will take you through a step-by-step process of
assigning keywords to your data.

Select **A Flood in Jakarta like 2013** layer first and click :guilabel:`Keyword Creation Wizard`.
A window will appear and then you can follow the steps
provided by :guilabel:`Keyword Creation Wizard.` If you get stuck, you can follow
the diagram below to understand the steps and the choices you will be
offered.

Starting at the top of the diagram and working down; in the first step
you get to choose if your data are hazard, exposure or aggregation data.
Depending on the choice you make you will be offered the next option.
You can always go back and change things later.

If you choose hazard or exposure, you will need to select the type of
hazard or exposure and after that you need to choose the layer mode
whether continuous or classified (if you forget about what is continuous
or classified, you can go to `Key Concept of Disaster Management
section <http://docs.inasafe.org/en/training/socialisation/inasafe_concepts.html>`__).
Both hazard and exposure type have the same step after you define the
layer mode, you then need to define which unit or attribute that
represent the hazard.

The steps will be different for aggregation data. After you define the
data as aggregation data, you need to select the attribute to represent
the names of aggregation areas. After you select it, you will be asked
to define the population ratio. In the end, you will need to enter the
source of data and the name of your layer that will be displayed in
|project_name| dock.

.. image:: /static/training/socialisation/intermediate_inasafe_04.*
   :align: center
   :width: 300 pt

.. image:: /static/training/socialisation/intermediate_inasafe_05.*
   :align: center
   :width: 300 pt

After you put the keyword using keyword wizard, you can see in the
|project_name| panel on the right side that the layer keyword already set. Does
it look like the image below? If not, you need to go back and try to
define the keyword again. and in the hazard panel, the data already put
on.

.. image:: /static/training/socialisation/intermediate_inasafe_06.*
   :align: center
   :width: 300 pt

After you set the keyword to match the image above, the hazard data will
appear in hazard panel of |project_name| Dock.

.. image:: /static/training/socialisation/intermediate_inasafe_07.*
   :align: center
   :width: 300 pt

Now all the keyword data already set and we can move into the next
section to run |project_name| with population data.

C. Run |project_name| for population with aggregation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We have seen the result of |project_name| on buildings and populations with
raster hazard data and right now we will run |project_name| analysis using
flood vector hazard data and raster population as exposure data. But
this time we will use aggregation data. |project_name| allows us to add
administrative data with specific boundary that we can use as an
aggregate. Using |project_name| with aggregation data will help you to get
detailed result since the aggregation data can provide detailed
information of specific area or by administration boundary.

To do this, look at the Layer List and make sure to turn ON the
**Jakarta District** layer. Next, take a look at |project_name| dock especially
in *Aggregate results by*.

.. image:: /static/training/socialisation/intermediate_inasafe_08.*
   :align: center
   :width: 300 pt

Why we can not see the **Jakarta District** layer that we just turned ON
before? Check the layer by selecting it on the Layer List. Did you see
the keyword? The problem why this layer did not appear in |project_name| Dock
is because it did not have keyword data inside. So, let us put the
keyword for **Jakarta District** using :guilabel:`Keyword Creation Wizard` and for
your reference, you can see the keyword diagram explained before.

Now you can select **Jakarta District** as aggregation data in |project_name|
Dock. The |project_name| Dock should look like this now:

.. image:: /static/training/socialisation/intermediate_inasafe_09.*
   :align: center
   :width: 300 pt

Let us click :guilabel:`Run` and wait until |project_name| finish analyzing the data, a new
impact layer will be added to Layer List. When you look at the result,
it looks the same as |project_name| analysis result without aggregation, but if
you scroll down more to the bottom you will see the detailed result. As
explained before, using aggregation will let you get detailed
information into specific area or by administration boundary.

.. image:: /static/training/socialisation/intermediate_inasafe_10.*
   :align: center
   :width: 300 pt

In the picture above we got detailed impact result divided by each
district in Jakarta for detailed gender report, detailed age report and
detailed minimum needs report. You can also use *jakarta subdistrict*
as aggregation data if you want to get more detail result rather than
using *jakarta distrct*. Try to run the analysis again but right now
you will use *jakarta subdistrict*. Not only for population,
aggregation option in |project_name| also can be applied for building and road.
In the next exercise, we will learn to run |project_name| to road and building.

2. Run |project_name| for road and building
...........................................

A. Download building polygons and roads with OpenStreetMap Downloader
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We already run |project_name| for vector hazard data with population and now we
will try to run |project_name| for vector hazard data with another exposure
data which is road and building polygons data. We will get these data
from one of |project_name| features, :guilabel:`OpenStreetMap Downloader`.
:guilabel:`OpenStreetMap Downloader` is a feature that allows you to download OpenStreetMap data
and load it in QGIS directly. This feature requires an internet
connection as it fetches the data via web service. Once downloaded, it
will be available as shapefiles and symbolized neatly (more information
at `OpenStreetMap Downloader
page <http://docs.inasafe.org/en/user-docs/application-help/openstreetmap_downloader.html>`__).

To use this feature for our next exercise, follow these steps:

1. :guilabel:`Zoom in` to the any flooded area that you prefer.

2. Click :guilabel:`OpenStreetMap Downloader` icon.

3. Select :guilabel:`Building Polygons` and :guilabel:`Roads` for feature types that we will
   download.

4. Click :guilabel:`Drag on Map` to select boundary box for downloaded area.

5. Choose your output directory, where OSM data will be stored. You may
   also need to put prefix name so that it would be easier to identify the data.

.. image:: /static/training/socialisation/intermediate_inasafe_11.*
   :align: center
   :width: 300 pt

6. Click :guilabel:`OK`.

It may take a while to download all the data in the given area based on
how big the area is (generally dataset at city level and below should
work well). After you download the data, a new layer will appear in the
Layer List. The amount of data available depends on the OpenStreetMap
data available in the downloaded region. If you want to get more data in
your area, you can participate in OpenStreetMap and start map the area.

Since the data already downloaded, we are ready to run |project_name| analysis.
But can |project_name| run the data for only the small part of the whole hazard
data? We will find the answer in the next section.

B. Define your custom analysis area
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|project_name| have feature that allows you to set your analysis area. You can
specify exactly which area should be used for your analysis. So, if you
have exposure data that is not in the same size, you can use this
feature to define your own analysis area.

1. Click :guilabel:`Set Analysis Area` to show set analysis extent feature.

2. Select :guilabel:`Use intersection of hazard, exposure and this bounding box`.

3. Click :guilabel:`Drag on Map` to draw the bounding box around building point
   and road.

4. Click :guilabel:`OK`

.. note:: if you click Draw on Map, the window will be temporarily hidden
		  so that you can drag a rectangle on the map. After you have finished
		  dragging the rectangle, the window will reappear.

.. image:: /static/training/socialisation/intermediate_inasafe_12.*
   :align: center
   :width: 300 pt

Now that you already set the bounding box of your analysis area, to
check whether your analysis area already defined or not,
click :guilabel:`Toggle Scenario Outlines`. A green box will appear around your data.

.. image:: /static/training/socialisation/intermediate_inasafe_13.*
   :align: center
   :width: 300 pt

.. note:: Using Toggle Scenario Outlines help you understand which area for |project_name|
        to analyze. It is also an important step before run |project_name|
        analysis because not all of the data you put in the Layer List will be
        automatically defined by |project_name|.

Take a look at the |project_name| panel dock to make sure building polygons and
roads already have keyword, if not, you can define it using :guilabel:`InaSAFE Keyword Wizard`.
After the keyword already set, we are ready to run |project_name| for building polygons and roads.

C. Run |project_name| analysis for building polygons
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let us run analysis for building polygons first. Make sure you set the
|project_name| dock as pictured below:

.. image:: /static/training/socialisation/intermediate_inasafe_14.*
   :align: center
   :width: 300 pt

We will run |project_name| for flood vector hazard and building polygons with
aggregation data. Click :guilabel:`Run` to begin |project_name| analysis. After that you
will find the impact result layer in Layer List.

.. image:: /static/training/socialisation/intermediate_inasafe_15.*
   :align: center
   :width: 300 pt

Look at **Detailed building type report**, in the picture above we only get
two districts in Jakarta (Jakarta Timur and Jakarta Selatan). It may be
different with your result since it depends on the analysis area and
also aggregation layer that you use for analysis.

|project_name| did not separate the impact result into three categories as in
the `Run Basic InaSAFE <http://docs.inasafe.org/en/training/socialisation/run_basic_inasafe.html/>`__ because in the
previous exercise we have raster data contains flood depth in each pixel
yet in this exercise, the hazard data that we use only shows affected
area. So |project_name| will calculate how many buildings inside the affected
area.

We just succeeded running |project_name| on flood vector hazard with building
polygon. Next, we will try to run |project_name| for roads. What are the result
that you expect to get when you run |project_name| for roads?

D. Run |project_name| for roads
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this last exercise, we will run |project_name| on roads data that we got
from OpenStreetMap previously. Make sure that you select road as
exposure data in the |project_name| dock like this screenshot below:

.. image:: /static/training/socialisation/intermediate_inasafe_16.*
   :align: center
   :width: 300 pt

Click :guilabel:`Run` to start |project_name| analysis. A new impact layer will be added
to your Layer List and in map canvas you can see green road as not
flooded and red as flooded. Select **Flooded roads** layer to see the
statistic from |project_name| analysis.

.. image:: /static/training/socialisation/intermediate_inasafe_17.*
   :align: center
   :width: 300 pt

In this analysis, |project_name| will generate how many road temporary closed
in the affected area and also breakdown of the result by road type. And
if you are using aggregation, there will be detailed result divided by
aggregation data. For action checklist, you will see several questions
that can be use for point of discussion related to road impact, for
example *Which roads can be used to evacuate people or distribute
logistics?*

Summary
-------

In this exercise you have learned how to run |project_name| analysis with
different hazard data format and with new type of exposure data. You
also have learned two fundamental steps that you need to remember before
you run |project_name|.

First, you learned how to define a keyword for your data so it can be
analyzed with |project_name|. Without a keyword, |project_name| would not recognize
your data, so you need to define it whether the data is hazard, exposure
or aggregation data. You can set the keyword
using :guilabel:`|project_name| Keyword Wizard` feature.

Second, it is important to see the analysis area using *Toggle Scenario
Outline* before you run |project_name| analysis. Because, |project_name| sometimes did
not automatically set analysis area according to intersection of hazard
and exposure data. If |project_name| did not set the analysis area, you need to
define it manually using :guilabel:`Set Analysis Area` feature.

In this exercise, you also have learned how to download buildings and
roads data from OpenStreetMap using :guilabel:`OpenStreetMap Downloader`. With
this feature you can define how wide the area that you want to download
and what type of data you want to download. The availability of the data
are depend on how complete the data in OpenStreetMap.

In the next section, you will learn how to run |project_name| with other type
of hazard data such as tsunami, earthquake, volcano and generic data.
