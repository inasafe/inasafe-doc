.. image:: /static/training/qgis/1_000.*

..  _ch8-using-inasafe:

Chapter 8 Using InaSAFE 
=======================

**Learning Objectives**

-  Understand Hazard, Exposure and Impact
-  Learn InaSAFE interface
-  Run InaSAFE for Infrastructure
-  Use InaSAFE OpenStreetMap downloader
-  Add keyword metadata
-  Set outline impact analysis
-  Run InaSAFE for Population
-  Use aggregation layer
-  Customize minimum needs
-  Print InaSAFE Result
-  Save Impact Result data into new layer

InaSAFE provides overviews of potential disaster scenarios, of their outcomes, as well as map 
which can aid decision makers when disaster strikes. In this chapter we will learn about 
how to use InaSAFE along with other usefull features in InaSAFE for flood hazard scenario. 
If you interest to learn more about InaSAFE with other hazard beside flood, 
you go and learn in `InaSAFE website <http://www.inasafe.org>`_.

8.1 Hazards, Exposure and Impact
---------------------------------

Let’s begin by reviewing he inputs and outputs of InaSAFE – **hazard**; **exposure**; and 
**impact**. These terms are important for you to remember because the analysis process depend on
these three things.

**Hazards** (also called disasters) are what we call the data layers that describe the extent and
magnitude of natural events (such as earthquakes, tsunamis, volcanic eruptions) 
that could potentially cause an event or series of events that threaten and disrupt the lives and
livelihoods of people.

In general, the hazards data we use in InaSAFE represents a single hazard scenario. 
A scenario means that the hazard:

-  is at a particular location
-  has a measured intensity
-  has a measured duration
-  has a certain time frame

**Exposure** data represents things that are at risk when faced with a potential hazard. 
This can be man-made features such as public buildings, houses, roads and bridges, 
or it can be so-called natural features, such as population, rice paddies and lakes. 
These exposed elements can be divided into various categories, including physical elements 
(houses, power lines), economic elements (agricultural land, access to employment), 
social elements (vulnerable groups, population count), and environmental elements 
(air, water, plants and animals).

**Impact** is the result we get after InaSAFE processes the effect of the hazard data upon 
the exposure data. For example, if there is an earthquake model in Lembang, 
and we process it against building data in Bandung, our impact layer may show those houses 
that would be severely damaged, those somewhat damaged, and those mildly damaged. 
In other words, what goes in to InaSAFE are hazards and exposure. What comes out is impact.

8.2 The InaSAFE Interface
--------------------------

Before we run any scenarios, let’s take a closer look at the InaSAFE interface.

1. First, make sure you’ve installed the InaSAFE plugins. Follow the plugin instructions 
   in :ref:`chapter 3 <ch3-basic-of-qgis>`. Find and install the plugin called InaSAFE.

2. Open a new project in QGIS.

3. If the InaSAFE toolbar is not visible, right-click on the toolbars and make sure 
   that :guilabel:`InaSAFE` plugin is checked. The toolbar looks like this:

.. image:: /static/training/qgis/8_001.*
   :align: center

4. To show the InaSAFE panel, click on the :guilabel:`Toggle InaSAFE dock` button.

.. image:: /static/training/qgis/8_002.*
   :align: center

.. note:: Just like QGIS toolbars, you can drag and drop the InaSAFE dock panel 
    to change its position on the QGIS interface. You can pull it away as a separate window, 
    or place it below the Layers panel. It’s convenient in its location on the right side 
    of QGIS, so we will leave it there.

.. image:: /static/training/qgis/8_003.*
   :align: center

The InaSAFE panel consists of three parts: Questions, Results and Buttons. The questions are mixed
in with dropdown boxes - this is where we establish our input data and define the scenario 
that we want InaSAFE to process. The purpose of InaSAFE is to make your impact analysis 
very simple and easy to do. The Questions section provides a simple way for you 
to formulate what you want to know. All questions are created in the following format:

In the event of [**hazard**] how many [**exposure**] might [**impact**]?

For example: "In the event of an earthquake how many buildings might be destroyed?"

The Results section is filled in with information after InaSAFE is run, as we shall see. 
The buttons at the bottom allow us to run a scenario, print and access help.

8.3 Run InaSAFE for Infrastructure
----------------------------------

8.3.1 Adding Hazard Data
........................

We will learn about how to using InaSAFE to run impact scenario based on Infrastructure data.
Before we started let start how to add hazard data. Hazards can be represented by vector layers or
by raster layers. Remember that raster layers are like images with many pixels, 
and each pixel represents some data about an area on the ground. A raster that shows elevation,
for example, will contain pixels with different values based on the altitude of the location.
Similarly, a raster that represents a flood will contain the depth of the flood in every pixel in
the raster.

Let’s begin by adding our hazard layer to QGIS. It’s a raster model of flood in Jakarta.

1. Click the :guilabel:`Add Raster Layer` button.

.. image:: /static/training/qgis/8_004.*
   :align: center

2. Open :file:`flood_hkv_current.tif`. This data is raster data (in .tif format) which represents
   the flood prone area. The layer will look like this:

.. image:: /static/training/qgis/8_005.*
   :align: center

You will notice that the hazard drop-down box has been automatically filled in the InaSAFE panel.
This is because the data file has already been prepared for us with keyword metadata 
(fancy words for settings) that tells InaSAFE whether it’s a hazard or exposure layer. 
When we add the exposure data, we will learn how to add these InaSAFE keywords ourselves.

8.3.2 Adding Exposure Data
...........................

We can get the data from OpenStreetMap using OpenStreetMap Downloader. 
We will get any OpenStreetMap data based on the current map extent in QGIS. 
If your map extent displaying Indonesia, it will take a whole day according of 
our internet connection. It better to zoom in in specific location to minimize the bandwidth.
Let’s learn how to use OpenStreetMap Downloader in QGIS to get OpenStreetMap data.

1. Click on :guilabel:`OpenStreetMap Downloader` button.

.. image:: /static/training/qgis/8_006.*
   :align: center

2. In the *Feature Types* you can choose all the OpenStreetMap data or specific data 
   that you want download such as :guilabel:`building polygons` and :guilabel:`Roads`. 
   Also you can download :guilabel:`political boundaries` and select level administration 
   in your area such as RW Jakarta is level 8.

3. Set you *output directory* to the destination you want by clicking “…” button on the right side.

.. image:: /static/training/qgis/8_007.*
   :align: center

4. If you want to use some prefix, for example :kbd:`jakarta` you can type in 
   :guilabel:`File name prefix` area.

5. We can download all the map canvas extent but it takes a long time. 
   Otherwise if you want to download specific area, click on :guilabel:`Drag on Map` button and
   create a bounding box by dragging it to set download area

6. Click on :guilabel:`OK` and wait until download finish.

.. image:: /static/training/qgis/8_008.*
   :align: center

7. You can hide the **Roads** by clicking the box next to :guilabel:`Roads` layer list.

8.3.3 Adding Keyword Metadata
..............................

In order for InaSAFE to know that our layers are hazard or exposure datasets, 
we need to assign keywords to the layers using the InaSAFE keyword tool. 
Let’s take a look at the keywords that have already been created on the hazard layer.

1. Select the :guilabel:`buildings` layer in the Layers panel, and click on the 
   :guilabel:`Keywords Creation Wizard` button.

.. image:: /static/training/qgis/8_009.*
   :align: center

2. In the *InaSAFE Keywords Creation Wizard* window, we can follow the existing instructions 
   step by step and change several keyword fields.

.. image:: /static/training/qgis/8_010.*
   :align: center

3. Click :guilabel:`OK`.

4. Select the :guilabel:`Roads` layer and open again the keyword editor.

5. Notice that the layer now appears in the InaSAFE panel.

.. image:: /static/training/qgis/8_011.*
   :align: center

8.3.4 Set Outline Impact Analysis
..................................

If you have a laptop with small ram, run InaSAFE for large area with so many data will takes 
a long time to finish. To solve that, we can set the analysis area to smaller area 
to make the analysis quicker.

1. Select :guilabel:`Toggle Scenario Outlines` to showing analysis outline area.

.. image:: /static/training/qgis/8_012.*
   :align: center

It will showing green box around in the map canvas.

.. image:: /static/training/qgis/8_013.*
   :align: center

This green box is the analysis area that InaSAFE will calculate all the data inside the green box.

2. To change the analysis area, click :guilabel:`Set analysis area` button.

.. image:: /static/training/qgis/8_014.*
   :align: center

3. Click :guilabel:`Use intersections of hazard, exposure and this bounding box` and click on 
   :guilabel:`Drag on map` button and create a box to set analysis area. 
   This will create blue box around map canvas.

.. image:: /static/training/qgis/8_015.*
   :align: center

4. After that click :guilabel:`OK`.

8.3.5 Impact Analysis
......................

Now our hazard and exposure data are set in the InaSAFE panel, 
because the appropriate keywords have been added to our layers. 
Note that if we were to add a second exposure layer to our project, 
we would be able to choose which exposure layer we wanted from the InaSAFE drop-down menu. 
The same applies to hazard layers.

The third drop-down box is the impact function (“Might”). This concludes our question, 
and defines the function that InaSAFE will run behind the scenes. 
InaSAFE developers have written many of these functions to analyse all sorts of hazard and
exposure layers. The function that is selected for us here will process 
the hazard and exposure layers spatially to determine how the exposure layer will “be flooded.”

Click the :guilabel:`Run` button at the bottom to start the impact analysis. 
At the end of the process, the statistics will be displayed in the Results section, 
and a new layer will be added to the Layers panel that describes the result of the analysis.
The map will distinguish between buildings that are affected and those that are not.

.. image:: /static/training/qgis/8_016.*
   :align: center

8.4 Run InaSAFE for Population
-------------------------------

In this section we will learn how to run impact analysis for population data with InaSAFE. 
We still use raster hazard data for flood in Jakarta but we will add another exposure data which
is population from AsiaPop.

8.4.1 Adding Exposure Data
...........................

We already learn about how to symbolise this data in previous chapter (chapter 6), 
so if you think the colour of this AsiaPop’s data different than yours, 
you may need to symbolise it.

1. Click :guilabel:`Add Raster Layer` button and add :file:`popmap10_all`.

2. Change the layer order like this:

.. image:: /static/training/qgis/8_017.*
   :align: center

3. You can hide the vector data such as roads and building to create more clear view in map canvas.

8.4.2 Adding Keyword Data for Population
.........................................

1. Select the **popmap10\_all** layer in the Layers panel, and click on the 
   :guilabel:`Keywords Creation Wizard` button.

.. image:: /static/training/qgis/8_018.*
   :align: center

2. In the *Keywords Creation Wizard* window choose exposure as category layer, 
   we can follow the existing instructions step by step and change several keyword fields. 
   The last step, you can fill the :guilabel:`Title` with :kbd:`people`.

.. image:: /static/training/qgis/8_019.*
   :align: center

3. Click :guilabel:`OK`.

4. Notice that the layer now appears in the InaSAFE panel.

.. image:: /static/training/qgis/8_020.*
   :align: center

8.4.3 Using boundary as aggregation layer
..........................................

We can let InaSAFE to give impact result to us according whole area or divide it 
by administration boundary. It mean that the InaSAFE will provide impact analyst result 
into each administration area that we provide. This method will help us 
to know more specific result for each area, so we can know how many people 
that might be affected and how many logistic we should prepare for each administration area. 
To do this, we need to define aggregation layer first using :guilabel:`Keyword Creation Wizard`.

1. Click :guilabel:`Add Vector Layer` button and add :file:`Jakarta_District_Boundary_WGS84.shp`.

2. Select the :file:`district_osm_jakarta.shp` layer in the Layers panel, and click on the 
   :guilabel:`Keywords Creation Wizard` button.

3. In the *Keywords Creation Wizard* window choose aggregation as category layer.

4. After that, you can follow the existing instructions step by step 
   and change several keyword fields. The last step, you can give the Title with 
   :kbd:`District Jakarta`.

.. image:: /static/training/qgis/8_021.*
   :align: center

8.4.4 Set Outline Analysis
...........................

We already set the analysis area for calculating impact for building.
This time we will set the analysis area for population data.

1. Right click on :guilabel:`flood_hkv_current_jakarta` layer and click :guilabel:`Zoom to Layer`

2. Select :guilabel:`Toggle Scenario Outlines` to showing analysis outline area.

.. image:: /static/training/qgis/8_022.*
   :align: center

It will showing green box around in the map canvas.

.. image:: /static/training/qgis/8_023.*
   :align: center

This green box is the analysis area that InaSAFE will calculate all the data inside the green box.

3. To change the analysis area, click *Set analysis area* button.

.. image:: /static/training/qgis/8_024.*
   :align: center

-  Click :guilabel:`Drag on map` button and create a box to set around the
   **flood\_hkv\_current\_jakarta** area. This will create blue box around map canvas.

.. image:: /static/training/qgis/8_025.*
   :align: center

-  After that click :guilabel:`OK`.

-  We will run InaSAFE with Jakarta boundary as aggregation layer. To do this, simply change 
   :guilabel:`aggregate result by` in InaSAFE panel into district boundary.

.. image:: /static/training/qgis/8_026.*
   :align: center

-  Now click, :guilabel:`Run` to calculate impact analysis and wait for a moment.

.. image:: /static/training/qgis/8_027.*
   :align: center

You will get impact result in the InaSAFE panel in the right side divided 
by 5 municipal in Jakarta.

.. image:: /static/training/qgis/8_028.*
   :align: center

8.4.5 Configure Minimum Needs
..............................

When you scroll impact result from running InaSAFE scenario, you will notice 
that there are some statistic that show how many rice, drinking water, clean water, family kits
and toilet for each municipals in Jakarta. It called minimum needs per week
for each people evacuated. The purpose of this minimum needs is to provide quick method calculating
support requirements (in terms of food, water, etc) for displaced persons.

The minimum needs (by default) are based on ‘Perka 7/2008’ BNPB 
according to the following default formulas:

-  400g rice per person per day (2.8 kg per week)
-  2.5l drinking water per person per day (17.51 L per week)
-  15l clean water per person per day (105 L per week)
-  One family kits per family per week (assumes five people per families
   which not specified in perka)
-  20 people per toilet

If you feel not satisfied with these configuration, you can define your custom minimum needs 
for your own area using *Minimum Needs Configuration*

1. Click in :menuselection:`Plugin → InaSAFE → Minimum Needs Configuration`

.. image:: /static/training/qgis/8_029.*
   :align: center

2. *Minimum Needs Manager* Window will appear. You can see in the
   :guilabel:`Profile` selection there are 3 profile that already defined,
   **BNPB_en**, **Philippine Minimum Needs_en**, **BNPB_id**, and **Tanzania**.

.. image:: /static/training/qgis/8_030.*
   :align: center

3. If you want to change the default minimum needs for each item in each profile, 
   simply select an item that you want to change and click

.. image:: /static/training/qgis/8_031.*
   :align: center

button in the right upper side of the window.

4. You will enter *Resource editor* and from these editor, you can add
   or modify resource by fill each field that you think it’s important

5. Click :guilabel:`Save Resource` if you already change the value from an item or
   click :guilabel:`Discard Changes` if you didn’t change anything.

6. If you want to create your own custom minimum needs, click :guilabel:`New` in the bottom side
   of the window and you can start adding new item by click :guilabel:`+` button 
   in the right upper side of the window to open *Resource editor.*

7. Click :guilabel:`Save` after you add several item to your custom minimum needs.

8.4.6 Run Impact Analyst with Modified Minimum Needs
......................................................

After you create your custom minimum needs you can run InaSAFE with your own minimum needs:

1. Go to :menuselection:`Plugins ‣ InaSAFE ‣ Minimum Needs Configuration`

2. In *Minimum Needs Manager* Window, select your custom profile in Profile selector. 
   After that close the *Minimum Needs Manager* Window.

3. Click :guilabel:`Options…` in InaSAFE Panel to open *InaSAFE impact function configuration*

.. image:: /static/training/qgis/8_032.*
   :align: center

4. Click :guilabel:`Minimum Needs` tab to see if your own Custom Minimum Needs already set.

5. Click :guilabel:`Run` to see the InaSAFE result with your custom minimum needs.

8.5 Print InaSAFE Result
-------------------------

The data displayed on the screen can be saved to a PDF file by clicking
:guilabel:`Print` at the bottom of the InaSAFE panel. Before we print the InaSAFE result, 
we can improve our impact map by editing the symbology in QGIS. Styles can be changed, 
other relevant layers can be added, and the layout can be changed using the Print Composer.

1. Click on the InaSAFE result layer and click :guilabel:`Print`.

2. A window will appear in which you can choose the extent to be printed. 
   Choose :guilabel:`Analysis extent` if you want to print the entire map extent, or choose 
   :guilabel:`Current extent` to print the analysis based on the current view of the map.

3. You may also choose a custom print template *a3-landscape-blue, a3-landscape-orange, a3-portrait-blue, a3-portrait-orange, a4-landscape-blue, a4-landscape-orange, a4-portrait-blue, and a4-portrait-orange*.

.. image:: /static/training/qgis/8_033.*
   :align: center

4. If you want to add additional information before printing, click :guilabel:`Open Composer`.

5. To save it in PDF format for printing, click :guilabel:`Open PDF`.

6. Choose your save location and click :guilabel:`Save`.

.. image:: /static/training/qgis/8_034.*
   :align: center

7. After you wait for a while, InaSAFE will create 2 pdf output, first one is the **map based** 
   on your extent view and the second one is the **statistics data**.

.. image:: /static/training/qgis/8_035.*
   :align: center

8.6 Save Your Results
----------------------

You can save the impact layer that InaSAFE created, and you can save the QGIS project 
to come back to it later, but note that the InaSAFE’s symbology style cannot be saved. 
It will show you only black and white layer and you need to symbolise again.

8.6.1 Save your InaSAFE result style
.....................................

To get the style from your InaSAFE result, you need to save the InaSAFE result’s style first.

1. Right click on :guilabel:`Population which need evacuation`, and go to
   :guilabel:`Properties`.

2. Go to :guilabel:`Style` button on the bottom side the properties window and
   click :guilabel:`Save Style …`.

.. image:: /static/training/qgis/8_036.*
   :align: center

3. Save your symbology style as :kbd:`population_result_style` and click :guilabel:`Save button`.

.. image:: /static/training/qgis/8_037.*
   :align: center

4. To save the newly generated layer, right-click on it in the Layers panel. Click 
   :guilabel:`Save As …`

8.6.2 Save InaSAFE Result layer
................................

After you saved your InaSAFE result style now you can save your InaSAFE result layer 
and get the same style like the InaSAFE Result.

1. Right click on :guilabel:`Population which need evacuation`, and go to 
   :guilabel:`Save As…`

2. Click on :guilabel:`Browse` button and select a name and location for the file.
   Click :guilabel:`OK`.

3. Load your saved layer using :guilabel:`Add Raster Layer` button.

4. You will see black and white layer in map extent. Open the properties of your saved layer 
   to resolve this.

5. Go to :guilabel:`Style` button on the bottom side the properties window and 
   click :guilabel:`Load Style…`

.. image:: /static/training/qgis/8_038.*
   :align: center

6. Select your :file:`population_result_style` and click :guilabel:`Open` button.

7. Now your saved layer will have the same style with your temporary InaSAFE result layer.

8. To use this style as default style you can click :guilabel:`Save as Default`
   under :guilabel:`Style` button.

.. image:: /static/training/qgis/8_039.*
   :align: center

8.6.3 Save Project
...................

1. Click :guilabel:`Save As` button in toolbar.

.. image:: /static/training/qgis/8_040.*
   :align: center

2. Give a name to the project and put it in the directory where you want to save your work. 
   Then click :guilabel:`Save`.

.. image:: /static/training/qgis/8_041.*
   :align: center

Now you already learn about how to use InaSAFE from using InaSAFE Keyword Wizard 
to define keyword attribute, how to run InaSAFE with InaSAFE dock and Impact Function Wizard, 
how to modify minimum needs, and how to use OSM Downloader to download OpenStreetMap data directly.
InaSAFE it’s really help use to know the impact of disaster 
and how we can create some plan if the disaster happen in real life.