.. image:: /static/training/beginner/qgis-inasafe/image7.*

Module 12: Understanding InaSAFE
================================

**Learning Objectives**

- Explaining the concept of Hazard, Exposure, and Impact data
- Explaining how to get Impact
- Explaining InaSAFE’s interface
- Adding hazard data
- Adding unprocessed exposure data (vector and raster)
- Using keywords editor
- Analyzing Impact
- Improving InaSAFE Output Map
- Saving and Printing scenario result

We have already seen InaSAFE in action. We’ve installed the plugin and have run
a disaster analysis on a Jakarta flood scenario. We learned about hazard and
exposure data. In this chapter, we’ll review what we’ve learned and go a bit
further. By now you should be pretty comfortable with QGIS, and your knowledge
will continue to grow as you practice your new skills. We will work through a
disaster scenario more slowly to better understand InaSAFE, and in Unit 4 we
will go to even deeper.

**1. Hazards, Exposures and Impact**

Let’s being by reviewing what we the inputs and outputs of InaSAFE - **hazard**,
**exposure**, and **impact**.  These terms are important for you to remember
because the analysis process will always depend on these three things.

**Hazards** (also called disasters) are what we call the data layers (layers)
that describe the extent and magnitude of natural events (such as earthquakes,
tsunamis, volcanic eruptions) that could potentially cause an event or series
of events that threaten and disrupt the lives and livelihoods of people.

Generally, hazards that we model:

- are at a particular location
- have a measured intensity
- have a measured duration
- have a certain time frame

In our previous look at InaSAFE we used a flood in Jakarta as our hazard.  In
this chapter we will use a dataset modelled from an earthquake in Lembang.

**Exposure** data represents things that are at risk when faced with a potential
hazard.  This can be man-made features such as public buildings, houses, roads,
and bridges, or it can be so-called natural features, such as population, rice
paddies, and lakes.  These exposed elements can be divided into various
categories, including physical elements (houses, power lines), economic elements
(agricultural land, access to employment), social elements (vulnerable groups,
population density), and environmental elements (air, water, plants and animals).

Previously we ran InaSAFE with exposure data consisting of population data from
AsiaPop, and building data from OpenStreetMap.  In this chapter’s analysis we
will once again use OSM data.

**Impact** is the result we get after InaSAFE processes the effect of the hazard
data upon the exposure data.  For example, if there is an earthquake model in
Lembang, and we process it against building data in Bandung, our impact layer
may show those houses that would be severely damaged, those somewhat damaged,
and those mildly damaged.  In other words, what goes in to InaSAFE are hazards
and exposure.  What comes out is impact.

**2. The InaSAFE Interface**

Before we run any scenarios, let’s take a closer look at the InaSAFE interface.
Make sure you’ve installed InaSAFE plugins (see Module 4 for reference if
you forgot how to do it) Open a new project in QGIS.

- If the InaSAFE toolbar is not visible, :guilabel:`right-click` on the
  **toolbars** and make sure that :guilabel:`Plugins` is checked.  The
  toolbar looks like this:

.. image:: /static/training/beginner/qgis-inasafe/image278.*
   :align: center

- To show the InaSAFE panel, click on the button named
  :guilabel:`Toggle InaSAFE dock`.

.. image:: /static/training/beginner/qgis-inasafe/image279.*
   :align: center

.. note:: That just like QGIS toolbars, you can drag and drop the InaSAFE dock
   panel to change its position on the QGIS interface.  You can pull it away as
   a separate window, or place it below the Layers list.  It’s quite convenient
   in its location on the right side of QGIS, so we will leave it there.

.. image:: /static/training/beginner/qgis-inasafe/image280.*
   :align: center

The InaSAFE panel consists of three parts: Questions, Results and Buttons.  The
questions are mixed in with dropdown boxes - this is where we establish our
input data and define the scenario that we want InaSAFE to process.  The purpose
of InaSAFE is to make your impact analysis very simple and easy to do.  The
Questions section provides a simple way for you to formulate what you want to
know.  All questions are created in the following format:

*In the event of [hazard] how many [exposure] might [impact]?
For example:"In the event of an earthquake how many buildings might be closed?"*

The other parts of the InaSAFE we have seen in action.  The Results section is
filled in with information once InaSAFE is run, and the Buttons allow us to run
a scenario, print, and access help.

**3.  Adding Hazard Data**

**Hazards** can be represented by vector layers or by raster layers.  Remember
that raster layers are like images with many pixels, and each pixel represents
some data about an area on the ground.  A raster that shows elevation, for
example, will contain pixels with different values based on the altitude of the
location.  Similarly, a raster that represents an earthquake will contain the
magnitude of the earthquake at the time of the event in every pixel in
the raster.

An earthquake can also be modelled with vector data, although the detail of the
data will most likely be lower.  In this case vector polygons will represent the
area where the earthquake occurred, and possibly various polygons will show
areas of differing magnitudes.

Let’s begin by adding our hazard layer to QGIS.  It’s a raster model of an
earthquake in Lembang.

- Click the :guilabel:`Add Raster Layer` button.

.. image:: /static/training/beginner/qgis-inasafe/image281.*
   :align: center

- Navigate to the :file:`../qgis/Bandung` folder and add
  **Lembang_Earthquake_Scenario.asc**. This data is raster data (in ASCII
  format) which represents the magnitude of the earthquake. The layer will
  look like this:

.. image:: /static/training/beginner/qgis-inasafe/image282.*
   :align: center

Try to change the layer band into Singleband Pseudocolor until the layer
look like this image below (refer to Modul 8, if you forgot how to do it!):

.. image:: /static/training/beginner/qgis-inasafe/image283.*
   :align: center

You will notice that the hazard dropdown box has been automatically filled in
the InaSAFE panel.  This is because the data file has already been prepared for
us with keyword metadata (fancy words for settings) that tells InaSAFE whether
it’s a hazard or exposure layer.  When we add the exposure data, we will learn
how to do inform InaSAFE ourselves.

**4. Exposure**

**Exposure** can also be represented by vectors or rasters.  In fact we’ve
already seen this in the Jakarta flood scenario.  When we ran that analysis our
population layer was a raster, with each pixel representing the population of a
given area on the Earth.  Our buildings on the other hand, were vectors.

Let’s add our exposure data to QGIS - once again we will be using buildings
obtained from OpenStreetMap.

- Click on the :guilabel:`Add Vector Layer` button.

.. image:: /static/training/beginner/qgis-inasafe/image284.*
   :align: center

- Add the file Bangunan_Bandung.shp, which is located
  in the qgis/Bandung folder.

.. image:: /static/training/beginner/qgis-inasafe/image285.*
   :align: center

- Notice that unlike the hazard layer, it does not appear automatically in
  InaSAFE!

**5. Adding Keyword Metadata**

In order for InaSAFE to know that our layers are hazard or exposure datasets,
we need to assign keywords to the layers using the InaSAFE keyword tool.  Let’s
take a look at the keywords that have already been created on the hazard layer.

- :guilabel:`Select` the **earthquake** layer in the Layers list, and click on
  the :guilabel:`InaSAFE Keyword Editor` button.

.. image:: /static/training/beginner/qgis-inasafe/image286.*
   :align: center

- You can see that this layer has already been assigned some keyword information
  for InaSAFE, including its title, a category, and a subcategory.

.. image:: /static/training/beginner/qgis-inasafe/image287.*
   :align: center

- Click :guilabel:`OK`, and now :guilabel:`select` the **Bangunan_Bandung**
  layer and open the keyword editor.

.. image:: /static/training/beginner/qgis-inasafe/image288.*
   :align: center

- You’ll notice that title and category are set, but not the subcategory!
- Change this to :guilabel:`structure`, and then click :guilabel:`OK`.
- Notice that the layer now appears in the InaSAFE dock panel.

.. image:: /static/training/beginner/qgis-inasafe/image289.*
   :align: center

- Click :guilabel:`Run` to calculate impact analysis and wait for a moment

.. image:: /static/training/beginner/qgis-inasafe/image290.*
   :align: center

**6. Impact Analysis**

Now our hazard and exposure data are set in the InaSAFE panel, because the
appropriate keywords have been added to our layers.
Note that if we were to add a second exposure layer to our project,
we would be able to choose which exposure layer we wanted from the InaSAFE
dropdown menu.
The same applies to hazard layers.

The third dropdown box is the impact function (“Might”).
This concludes our question, and defines the function that InaSAFE will run
behind the scenes.
InaSAFE developers have written many of these functions to analyze all sorts of
hazard and exposure layers.
The function that is selected for us here will process the hazard and
exposure layers spatially to determine how the exposure layer will “be
affected.”

- Click the :guilabel:`Run` button at the bottom to start the impact analysis.
  At the end of the process, the statistics will be displayed in the Results
  section, and a new layer will be added to the Layers list that describes
  the result of the analysis.
  The map will distinguish between buildings that are affected and those that
  are not.

.. image:: /static/training/beginner/qgis-inasafe/image291.*
   :align: center

**7. Improve the InaSAFE Output Map**

We can improve our impact map by editing
the symbology in QGIS.  Styles can be changed, other relevant layers can be
added, and the layout can be changed using the Print Composer.

Let’s add Bing aerial imagery as a background for our map.

- Go to :menuselection:`Plugins ‣ OpenLayers plugin ‣ Add Bing Aerial layer`.
- Drag the layer below your new impact layer.  If the buildings don’t show
  correctly above the imagery, :guilabel:`right-click` on the layer and select
  :guilabel:`Update drawing order`.

.. image:: /static/training/beginner/qgis-inasafe/image292.*
   :align: center

**8.  Using the Print Button**

The data displayed on the screen can be saved to a PDF file by clicking Print at
the bottom of the InaSAFE panel.

- Klik on InaSAFE result layer, then click :guilabel:`Print`
- A window will show up, you can choose the extent that you want to be printed.

  1. *Analysis extent* if you want to print all the analysis result
  2. *Current extent* if you want to print analysis result based on QGIS
     map canvas

- You also can pick the template (basic or InaSAFE). If you have QGIS
  composer template file (.qpt format), you also can use it. For now,
  let’s choose Basic.

.. image:: /static/training/beginner/qgis-inasafe/image293.*
   :align: center

- If you want to add additional information on your layout before it will
  be printed, you can click :guilabel:`Open Composer`. If you want to save
  it in PDF format to print it, click :guilabel:`Open PDF`
- Choose your save location and click :guilabel:`Save`.


.. image:: /static/training/beginner/qgis-inasafe/image294.*
   :align: center

.. image:: /static/training/beginner/qgis-inasafe/image295.*
   :align: center

.. image:: /static/training/beginner/qgis-inasafe/image296.*
   :align: center



**9. Save Your Results**

You can save the impact layer that InaSAFE created, and you can save the QGIS
project to come back to it later, but note that the InaSAFE statistics cannot be
saved (except when you save them in a PDF).  To get the statistics again in
QGIS, you will need to run the analysis again.

- To save the newly generated layer, :guilabel:`right-click` on it in the
  **Layers list**.
- Click :guilabel:`Save As`...
- Select a name and location for the file.  Click :guilabel:`OK`.

To save the project:

- Click on the :guilabel:`Save Project` button at the top of QGIS.

.. image:: /static/training/beginner/qgis-inasafe/image297.*
   :align: center

- Give a name to the project and put it in the directory you want to save your
  work. Then click :guilabel:`Save`.

.. image:: /static/training/beginner/qgis-inasafe/image298.*
   :align: center
