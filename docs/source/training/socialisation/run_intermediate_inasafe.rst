.. image:: /static/training/socialisation/inasafe_logo.*

.. _run_intermediate_inasafe:

Run Intermediate |project_name|
===============================

Introduction
------------

In `Run Basic InaSAFE <http://docs.inasafe.org/en/training/socialisation/run_basic_inasafe.html/>`__ we learned how to run a flood analysis on
population and buildings, adjust the flood impact default settings and analyze
impact summary report, and change analysis threshold. We also
learned how to save our work and generate a pdf of the analysis results.
In this exercise we will learn more techniques such as how to run
|project_name| with aggregation data to produce reports broken down by districts or regions. We
will also learn how to download data using the OpenStreetMap downloader and
how to run |project_name| analysis on the downloaded building polygons and roads.
Last but not least, we will learn how to define the analysis area.

Learning Objective
------------------

To improve the participant’s understanding of additional |project_name| function and
features. By the end of this exercise, participants will be able to:

- Define keywords using the |project_name| keyword wizard

- Run |project_name| with aggregation data

- Use the OpenStreetMap Downloader to download data for |project_name|

- Set the |project_name| analysis area using the |project_name| analysis area tool.

Data for this exercise
----------------------

The data for this exercise are available in DKI Jakarta.zip which can be downloaded from `InaSAFE Training Data <http://data.inasafe.org/TrainingDataPackages/>`__. We will use
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

Click :guilabel:`Open` and select :file:`DKI Jakarta Intermediate.qgs`.
There is a notification to save the current project, choose
whether to save your current work or discard your current work. Once :file:`DKI_Jakarta_Intermediate` is opened, you will see the following:

.. image:: /static/training/socialisation/intermediate_inasafe_01.*
   :align: center
   :width: 300 pt

Next, add :file:`Jakarta Flood 18113 WGS84` data from :file:`Run Intermediate InaSAFE > DKI Jakarta > 01 Hazard Data`. This is the flood hazard data
for Jakarta from an actual flood event. During Jakarta floods in January
2013, the provincial disaster manager collected information about the flood,
including the location of flooded areas by sub-village boundary
(see more about this data at :ref:`datasets`.)

Let us symbolize this layer so that it shows only affected areas (if you
forget how to symbolize, you can go to :ref:`introduction_to_qgis`.)
The layer should look like this:

.. image:: /static/training/socialisation/intermediate_inasafe_02.*
   :align: center
   :width: 300 pt

Using this layer, we will be able to see which area in Jakarta are categorized as
flooded/affected area by analyzing the data using |project_name|.
On the InaSAFE Dock, you will notice that the hazard is not
there and only exposure data (population) is visible, even
though you already turned ON the data layer.

.. image:: /static/training/socialisation/intermediate_inasafe_18.*
   :align: center
   :width: 300 pt

Do you know why |project_name| did not display the Jakarta Flood Vector Hazard data on the dock?
The answer will be provided in the next section.

B. Define keyword for hazard data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|project_name| need a keyword to determine what type of data the user
provide for analysis (hazard data, exposure data or aggregation data).
If the data provided does not have a keyword, it will show a warning
message “Layer Keyword Missing” in the |project_name| Dock. Try selecting :guilabel:`A Flood in
Jakarta like 2013` layer and look at the |project_name| dock, You will see
the following:

.. image:: /static/training/socialisation/intermediate_inasafe_03.*
   :align: center
   :width: 300 pt

As you can see from the picture above, this layer keywords are missing
and we need to open the keyword wizard to solve this problem. The
keywords wizard will take you through a step-by-step process of
assigning keywords to your data.

Select **A Flood in Jakarta like 2013** layer and click :guilabel:`Keyword Creation Wizard`.
A window will appear and follow the steps
provided by the :guilabel:`Keyword Creation Wizard.` If you get stuck, you can follow
the diagram below to understand the steps and the choices you will be
offered.

Steps in the Keyword Creation Wizard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Starting at the top of the diagram and working down; in the first step
you will choose if your data are hazard, exposure or aggregation data.
Your choice will determine the next options offered. 
You can always go back and change things later.

If you choose Hazard or Exposure, you will need to select the type of
hazard or exposure. Next, you will choose whether the layer mode
is continuous or classified (if you forget what Continuous
or Classified means, you can reference the `Key Concept of Disaster Management
section <http://docs.inasafe.org/en/training/socialisation/inasafe_concepts.html>`__).
Both Hazard and Exposure types have the same step after you define the
layer mode: defining which unit or attribute
represents the hazard.

The steps will be different for aggregation data. After you define the
data as aggregation data, you will select the attribute to represent
the names of aggregation areas. After you select it, you will be asked
to define the population ratio. Finally, you will need to enter the
source of data and the name of your layer to be displayed in the
|project_name| dock.

.. image:: /static/training/socialisation/intermediate_inasafe_04.*
   :align: center
   :width: 300 pt

.. image:: /static/training/socialisation/intermediate_inasafe_05.*
   :align: center
   :width: 300 pt

After you set the keyword using the Keyword Wizard, you can see in the
|project_name| panel on the right side that the layer keyword has been set.
Verify that it looks like the image below? If it does not, you should go back and try to
define the keyword again.

.. image:: /static/training/socialisation/intermediate_inasafe_06.*
   :align: center
   :width: 300 pt

After you set the keyword to match the image above, the hazard data will
appear in the hazard panel of the |project_name| Dock.

.. image:: /static/training/socialisation/intermediate_inasafe_07.*
   :align: center
   :width: 300 pt

Now all the keyword data has been set and we can move into the next
section to run |project_name| with population data.

C. Run |project_name| for population with aggregation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We have seen the result of |project_name| on buildings and populations with
raster hazard data. Now we will run |project_name| analysis using
flood vector hazard data and raster population as exposure data. This time, however, we will use aggregated data. Using |project_name| with aggregated data will help you to get
detailed result since the aggregated data can provide detailed
information on specific administrative (or other) area. |project_name| allow us to add administrative data with specific boundaries that we can use to aggregate results.

To do this, look at the Layer List and make sure to turn ON the
**Jakarta District** layer. Next, take a look at the |project_name| dock under the heading *Aggregate results by*.

.. image:: /static/training/socialisation/intermediate_inasafe_08.*
   :align: center
   :width: 300 pt

Why are we not able to see the **Jakarta District** layer that we just turned ON
before? Check the layer by selecting it on the Layer List. Did you see
the keyword? The reason why this layer did not appear in the |project_name| Dock
is because it did not have keyword data defube. Go ahead and add a
keyword for **Jakarta District** using the :guilabel:`Keyword Creation Wizard`. For
your reference, refer to the keyword diagram as explained above.

Now you will able to select **Jakarta District** under 'Aggregate results by' in the |project_name|
Dock. The |project_name| Dock should look like this:

.. image:: /static/training/socialisation/intermediate_inasafe_09.*
   :align: center
   :width: 300 pt

Click :guilabel:`Run` and wait until |project_name| finishes analyzing the data. A new
impact layer will be added to the Layer List. When you look at the result,
it looks the same as |project_name| analysis result without aggregation, but if
you scroll down to the bottom you will see the detailed result. As
explained before, using aggregation will let you get detailed
information for a specific area or administration region.

.. image:: /static/training/socialisation/intermediate_inasafe_10.*
   :align: center
   :width: 300 pt

In the screenshot above, we see detailed impact results for each
district in Jakarta for the detailed gender report, the detailed age report and the
detailed minimum needs report. You can also use *jakarta subdistrict*
rather than using *jakarta_district* for aggregation if you want to get more detailed results.
Try running the analysis again using *jakarta subdistrict*. The
aggregation option in |project_name| can also be applied for buildings and roads (in addition to population).
In the next exercise, we will learn to run |project_name| for roads and buildings.

2. Running |project_name| for roads and buildings
..................................................

A. Download building polygons and roads with OpenStreetMap Downloader
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We have completed running |project_name| with population and vector hazard data. Now, we
will run |project_name| with different type of vector exposure
data: roads and buildings polygons. We will obtain these dataset using
one of |project_name| features, :guilabel:`OpenStreetMap Downloader`.
:guilabel:`OpenStreetMap Downloader` is a feature that enables downloading OpenStreetMap data
and directly loading it into QGIS. This feature requires an internet
connection as it fetches the data via a web service. Once downloaded, the data
will be available as shapefiles and symbolized neatly (more information
at `OpenStreetMap Downloader
page <http://docs.inasafe.org/en/user-docs/application-help/openstreetmap_downloader.html>`__).

To use this feature for our next exercise, follow these steps:

1. :guilabel:`Zoom in` to any flooded area that you prefer.

2. Click the :guilabel:`OpenStreetMap Downloader` icon.

3. Select :guilabel:`Building Polygons` and :guilabel:`Roads` as the feature types to download.

4. Click :guilabel:`Drag on Map` to select the boundary box from which data will be downloaded.

5. Choose the your output directory, where OSM data will be stored. Adding a file name prefix makes it easier to identify the data downloaded.

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

|project_name| has a feature that allows you specify exactly
which area should be used for your analysis. If you
have exposure data that is not the same size, you can use this
feature to define your own analysis area.

1. Click :guilabel:`Set Analysis Area` to show set analysis extent feature.

2. Select :guilabel:`Use intersection of hazard, exposure and this bounding box`.

3. Click :guilabel:`Drag on Map` to draw the bounding box around building polygons
   and roads.

4. Click :guilabel:`OK`

.. note:: if you click Draw on Map, the window will be temporarily hidden
		  so that you can drag a rectangle on the map. After you have finished
		  dragging the rectangle, the window will reappear.

.. image:: /static/training/socialisation/intermediate_inasafe_12.*
   :align: center
   :width: 300 pt

To verify that your analysis area has been successfully defined,
click :guilabel:`Toggle Scenario Outlines`. A green box will appear around your data.

.. image:: /static/training/socialisation/intermediate_inasafe_13.*
   :align: center
   :width: 300 pt

.. note:: Using Toggle Scenario Outlines help you understand which area that |project_name|
        will analyze. It is also an important step before running |project_name|
        analysis because not all of the data you put in the Layer List will be
        automatically defined by |project_name|.

Take a look at the |project_name| panel dock to make sure building polygons and
roads have a keyword defined. If they do not you can define one using :guilabel:`InaSAFE Keyword Wizard`.
After the keyword has been already set, we are ready to run |project_name| for building polygons and roads.

C. Run |project_name| analysis for building polygons
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let us run analysis for building polygons first. Make sure you set the
|project_name| dock as pictured below:

.. image:: /static/training/socialisation/intermediate_inasafe_14.*
   :align: center
   :width: 300 pt

We will run |project_name| for flood vector hazard and building polygons with data aggregated by Jakarta district
Click :guilabel:`Run` to begin |project_name| analysis. After running, you
will find the impact result layer in Layer List.

.. image:: /static/training/socialisation/intermediate_inasafe_15.*
   :align: center
   :width: 300 pt

Looking at the **Detailed building type report** (pictured above) we only see
two districts in Jakarta (Jakarta Timur and Jakarta Selatan). Your results may differ
since it depend on the analysis area selected and
also the aggregation layer that you used for analysis.

|project_name| did not separate the impact result into three categories as in
the :ref:`Run Basic InaSAFE <run_basic_inasafe>` because in the
previous exercise we used raster data containing flood depth in each pixel
yet in this exercise, the hazard data that we use only depicts affected
areas. Therefore, |project_name| will calculate how many buildings are inside the affected
area but not level of impact on each building.

We just succeeded running |project_name| on flood vector hazard with building
polygon. Next, we will run |project_name| for roads. What are the results
that you expect to get when you run |project_name| for roads?

D. Run |project_name| for roads
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this last exercise, we will run |project_name| on roads data that we previously downloaded
from OpenStreetMap. Make sure that you select roads as
exposure data in the |project_name| dock, as shown in the screenshot below:

.. image:: /static/training/socialisation/intermediate_inasafe_16.*
   :align: center
   :width: 300 pt

Click :guilabel:`Run` to start |project_name| analysis. A new impact layer will be added
to your Layer List and in the map canvas you will see green roads as not
flooded and red as flooded. Select the **Flooded roads** layer to see
statistics from the |project_name| analysis.

.. image:: /static/training/socialisation/intermediate_inasafe_17.*
   :align: center
   :width: 300 pt

In this analysis, |project_name| will generate statistics on how many roads are temporarily closed
in the affected area and also a breakdown of the result by road type.
If you are using aggregation, there will be detailed results for each aggregation.
In the action checklist, you will see several questions
that can be used for points of discussion related to road impact, and disaster logistics planning,
for example: *Which roads can be used to evacuate people or to distribute relief items?*

Summary
-------

In this exercise, you have learned how to run |project_name| analysis with
different hazard data formats and with new type of exposure data. You have also
learned two fundamental steps to remember before you run |project_name|:

First, you learned how to define a keyword for your data so it can be
analyzed with |project_name|. Without a keyword, |project_name| will not recognize
your data, so you need to define it whether the data is hazard, exposure
or aggregation data. You can set the keyword
using the :guilabel:`Keyword Creation Wizard` feature.

Second, it is important to review the analysis area using *Toggle Scenario
Outline* before you run |project_name| analysis. This is because, |project_name| sometimes does
not automatically set the analysis area according to the intersection of hazard
and exposure data. If |project_name| did not set the analysis area, you need to
define it manually using the :guilabel:`Set Analysis Area` feature.

In this exercise, you have learned how to download buildings and
roads data from OpenStreetMap using :guilabel:`OpenStreetMap Downloader`. With
this feature you can define the size of the area
and what type of data you want to download. The availability of the data
depend on how complete the data are in OpenStreetMap.

In the next section, you will learn how to run |project_name| with other type
of hazard data such as tsunami, earthquake, volcano and generic data.
