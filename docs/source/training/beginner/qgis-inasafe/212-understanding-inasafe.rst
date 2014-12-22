.. image:: /static/training/beginner/qgis-inasafe/image7.*

..  _understanding-inasafe:

Module 12: Understanding |project_name|
=======================================

**Learning Objectives**

- Understand the concept of hazard, exposure and impact data
- Understand how to determine impact
- Understand the |project_name| interface
- Add hazard data
- Add unprocessed exposure data (vector and raster)
- Use the keywords editor
- Analyse impact
- Improve |project_name| output map
- Save and print scenario results
>>>>>>> upstream/develop


1. Hazards, exposure and impact
-------------------------------

Let’s begin by reviewing the inputs and outputs of |project_name| -
**hazard**, **exposure**, and **impact**.
These terms are important for you to remember because the analysis process
depends on these three things.

**Hazards** (also called disasters) are what we call the data layers
that describe the extent and magnitude of natural events (such as earthquakes,
tsunamis and volcanic eruptions) that could potentially cause an event or series
of events that threaten and disrupt the lives and livelihoods of people.

In general, the hazard data we use in |project_name| represents a single 
hazard scenario. A scenario means that the hazard:

- is at a particular location
- has a measured intensity
- has a measured duration
- has a certain time frame

In this module we will use a dataset modelled from an earthquake in Lembang.

.. note:: The earthquake modelling was done by experts. |project_name| is not 
   a hazard modelling tool.

**Exposure** data represents things that are at risk when faced with a potential
hazard.
This can be man-made features such as public buildings, houses, roads
and bridges, or it can be so-called natural features, such as population, rice
paddies and lakes.
These exposed elements can be divided into various categories,
including physical elements (houses, power lines),
economic elements (agricultural land, access to employment),
social elements (vulnerable groups, population count),
and environmental elements (air, water, plants and animals).

**Impact** is the result we get after |project_name| processes the effect of
the hazard data upon the exposure data.
For example, if there is an earthquake model in Lembang,
and we process it against building data in Bandung, our impact layer may show
those houses that would be severely damaged, those somewhat damaged,
and those mildly damaged.
In other words, what goes in to |project_name| are hazards and exposure.
What comes out is impact.

2. The InaSAFE interface
------------------------

Before we run any scenarios, let’s take a closer look at the |project_name|
interface.

1. First make sure that you’ve installed the |project_name| plugin. Follow the
   plugin instructions in :ref:`module 4 <installing-plugins>`. Find and
   install the plugin called |project_name|.

2. Open a new project in QGIS.

3. If the |project_name| toolbar is not visible, right-click on the
   toolbars and make sure that :guilabel:`Plugins` is checked.
   The toolbar looks like this:

.. image:: /static/training/beginner/qgis-inasafe/image278.*
   :align: center

4. To show the |project_name| panel, click on the 
   :guilabel:`Toggle InaSAFE dock` button.

.. image:: /static/training/beginner/qgis-inasafe/image279.*
   :align: center

.. note:: Just like QGIS toolbars, you can drag and drop the
   |project_name| dock panel to change its position in the QGIS interface.
   You can pull it away as a separate window, or place it below the Layers
   panel.
   It’s convenient in its location on the right side of QGIS,
   so we will leave it there.

.. image:: /static/training/beginner/qgis-inasafe/image280.*
   :align: center

The |project_name| panel consists of three parts: Questions,
Results and Buttons.
The questions are mixed in with drop-down boxes - this is where we establish our
input data and define the scenario that we want |project_name| to process.
The purpose of |project_name| is to make your impact analysis very simple and
easy to do.
The Questions section provides a simple way for you to formulate what you
want to know.
All questions are created in the following format:

*In the event of [hazard] how many [exposure] might [impact]?*

For example: "In the event of an earthquake how many buildings might be
destroyed?"

The Results section is filled in with information after |project_name| is run,
as we shall see. The buttons at the bottom allow us to run a scenario, print
and access help.

3. Adding hazard data
----------------------

**Hazards** can be represented by vector layers or by raster layers.
Remember that raster layers are like images with many pixels,
and each pixel represents some data about an area on the ground.
A raster that shows elevation, for example, will contain pixels with
different values based on the altitude of the location.
Similarly, a raster that represents an earthquake will contain the
magnitude of the earthquake at the time of the event in every pixel in the
raster.

An earthquake can also be modelled with vector data, although the detail of the
data will most likely be lower.
In this case vector polygons represent the area where the earthquake
occurred, and various polygons may show areas of differing
magnitudes.

Let’s begin by adding our hazard layer to QGIS.
It’s a raster model of an earthquake in Lembang.

5. Click the :guilabel:`Add Raster Layer` button.

.. image:: /static/training/beginner/qgis-inasafe/image281.*
   :align: center

6. Navigate to the :file:`qgis/Bandung/` folder and add
   :file:`Lembang_Earthquake_Scenario.asc`.
   This data is raster data (in ASCII format) which represents the magnitude
   of the earthquake.
   The layer will look like this:

.. image:: /static/training/beginner/qgis-inasafe/image282.*
   :align: center

7. Try to change the layer band into Singleband Pseudocolor so that the layer
   looks like the image below (refer to :ref:`module 8 <changing-raster-symbology>`, 
   if you forgot how!):

.. image:: /static/training/beginner/qgis-inasafe/image283.*
   :align: center

You will notice that the hazard drop-down box has been automatically filled in
the |project_name| panel.
This is because the data file has already been prepared for us with keyword
metadata (fancy words for settings) that tells |project_name| whether it’s a
hazard or exposure layer.
When we add the exposure data, we will learn how to do add these |project_name|
keywords ourselves.

4. Exposure
-----------

**Exposure** can also be represented by vectors or rasters.

Let’s add our exposure data to QGIS - we will be using buildings
obtained from OpenStreetMap.

8. Click on the :guilabel:`Add Vector Layer` button.

.. image:: /static/training/beginner/qgis-inasafe/image284.*
   :align: center

9. Add the file :file:`Bangunan_Bandung.shp`, which is located in the 
   :file:`qgis/Bandung/` folder.

.. image:: /static/training/beginner/qgis-inasafe/image285.*
   :align: center

10. Notice that unlike the hazard layer, it does not appear automatically in
    |project_name|!

5. Adding keyword metadata
--------------------------

In order for |project_name| to know that our layers are hazard or exposure
datasets, we need to assign keywords to the layers using the |project_name|
keyword tool.
Let’s take a look at the keywords that have already been created on the
hazard layer.

11. Select the earthquake layer in the Layers panel, and click on
    the :guilabel:`InaSAFE Keyword Editor` button. 

.. image:: /static/training/beginner/qgis-inasafe/image286.*
   :align: center

12. You can see that this layer has already been assigned some keyword 
    information for |project_name|, including its title, a category 
    and a subcategory.

.. image:: /static/training/beginner/qgis-inasafe/image287.*
   :align: center

13. Click :guilabel:`OK`.

14. Select the :guilabel:`Bangunan_Bandung` layer and open the keyword editor.

.. image:: /static/training/beginner/qgis-inasafe/image288.*
   :align: center

15. Notice that title and category are set, but not the subcategory.

16. Change the subcategory to :guilabel:`structure`, and click :guilabel:`OK`.

17. Notice that the layer now appears in the |project_name| panel.

.. image:: /static/training/beginner/qgis-inasafe/image289.*
   :align: center

6. Impact Analysis
------------------

Now our hazard and exposure data are set in the |project_name| panel,
because the appropriate keywords have been added to our layers.
Note that if we were to add a second exposure layer to our project,
we would be able to choose which exposure layer we wanted from the
|project_name| drop-down menu.
The same applies to hazard layers.

The third drop-down box is the impact function (“Might”).
This concludes our question, and defines the function that |project_name|
will run behind the scenes.
|project_name| developers have written many of these functions to analyse all
sorts of hazard and exposure layers.
The function that is selected for us here will process the hazard and
exposure layers spatially to determine how the exposure layer will “be
affected.”

18. Click the :guilabel:`Run` button at the bottom to start the impact analysis.
    At the end of the process, the statistics will be displayed in the Results
    section, and a new layer will be added to the Layers panel that describes
    the result of the analysis.
    The map will distinguish between buildings that are affected and those that
    are not.

.. image:: /static/training/beginner/qgis-inasafe/image291.*
   :align: center

7. Improve the InaSAFE output map
---------------------------------

We can improve our impact map by editing the symbology in QGIS.
Styles can be changed, other relevant layers can be added,
and the layout can be changed using the Print Composer.

Let’s add Bing aerial imagery as a background for our map.

19. Go to :menuselection:`Plugins ‣ OpenLayers plugin ‣ Add Bing Aerial layer`.

20. Drag the layer below your new impact layer.
    If the buildings don’t show correctly above the imagery,
    right-click on the layer and click
    :guilabel:`Update drawing order`.

.. image:: /static/training/beginner/qgis-inasafe/image292.*
   :align: center

8. Using the print button
-------------------------

The data displayed on the screen can be saved to a PDF file by clicking 
:guilabel:`Print` at the bottom of the |project_name| panel.

21. Click on the |project_name| result layer and then click :guilabel:`Print`.

22. A window will appear in which you can choose the extent to be printed.
    Choose :guilabel:`Analysis extent` if you want to print the entire map 
    extent, or choose :guilabel:`Current extent` to print the analysis 
    based on the current view of the map.

23. You may also choose a custom print template (basic or |project_name|).
    For now, choose :guilabel:`basic`.

.. image:: /static/training/beginner/qgis-inasafe/image293.*
   :align: center

24. If you want to add additional information before printing,
    click :guilabel:`Open Composer`.
    
25. To save it in PDF format for printing, click :guilabel:`Open PDF`.

26. Choose your save location and click :guilabel:`Save`.

.. image:: /static/training/beginner/qgis-inasafe/image294.*
   :align: center

.. image:: /static/training/beginner/qgis-inasafe/image295.*
   :align: center

.. image:: /static/training/beginner/qgis-inasafe/image296.*
   :align: center

9. Save your results
--------------------

You can save the impact layer that |project_name| created,
and you can save the QGIS project to come back to it later,
but note that the |project_name| statistics cannot be saved (except when you
save them in a PDF).
To get the statistics again in QGIS, you will need to run the analysis again.

27. To save the newly generated layer, right-click on it in the
    Layers panel. Click :guilabel:`Save As...`

28. Select a name and location for the file. Click :guilabel:`OK`.

29. To save the project, click on the :guilabel:`Save Project` button at the 
    top of QGIS.

.. image:: /static/training/beginner/qgis-inasafe/image297.*
   :align: center

30. Give a name to the project and put it in the directory where you want to 
    save your work.
    Then click :guilabel:`Save`.

.. image:: /static/training/beginner/qgis-inasafe/image298.*
   :align: center


:ref:`Go to next module --> <getting-support>` 
