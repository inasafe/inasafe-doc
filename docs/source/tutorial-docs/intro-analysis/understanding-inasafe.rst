Understanding InaSAFE
=====================

Learning Objectives
--------------------
* Understand the concept of Hazard and Exposure data
* Know how to derive an impact
* Add pre-prepared hazard data (vector and raster) and exposure data
* Use the keywords editor
* Understand the results of InaSAFE
* Save and print the results of a scenario


Introduction
--------------
We have already seen InaSAFE in action. We’ve installed the plugin and have run a disaster analysis on a Jakarta flood scenario.  We learned about hazard and exposure data.  In this chapter, we’ll review what we’ve learned and go a bit further.  By now you should be pretty comfortable with QGIS, and your knowledge will continue to grow as you practice your new skills.  We will work through a disaster scenario more slowly to better understand InaSAFE, and in Unit 4 we will go to even deeper.


### 1.  Hazards, Exposures and Impact

Let’s being by reviewing what we the inputs and outputs of InaSAFE - **hazard**, **exposure**, and **impact**.  These terms are important for you to remember because the analysis process will always depend on these three things.


**Hazards** (also called disasters) are what we call the data layers (layers) that describe the extent and magnitude of natural events (such as earthquakes, tsunamis, volcanic eruptions) that could potentially cause an event or series of events that threaten and disrupt the lives and livelihoods of people.


Generally, hazards that we model:

* are at a particular location
* have a measured intensity
* have a measured duration
* have a certain time frame


In our previous look at InaSAFE we used a flood in Jakarta as our hazard.  In this chapter we will use a dataset modelled from an earthquake in Lembang.


**Exposure** data represents things that are at risk when faced with a potential hazard.  This can be man-made features such as public buildings, houses, roads, and bridges, or it can be so-called natural features, such as population, rice paddies, and lakes.  These exposed elements can be divided into various categories, including physical elements (houses, power lines), economic elements (agricultural land, access to employment), social elements (vulnerable groups, population density), and environmental elements (air, water, plants and animals).


Previously we ran InaSAFE with exposure data consisting of population data from AsiaPop, and building data from OpenStreetMap.  In this chapter’s analysis we will once again use OSM data.


**Impact** is the result we get after InaSAFE processes the effect of the hazard data upon the exposure data.  For example, if there is an earthquake model in Lembang, and we process it against building data in Bandung, our impact layer may show those houses that would be severely damaged, those somewhat damaged, and those mildly damaged.  In other words, what goes in to InaSAFE are hazards and exposure.  What comes out is impact.


### 2.  The InaSAFE Interface

Before we run any scenarios, let’s take a closer look at the InaSAFE interface. Open a new project in QGIS.

* If the InaSAFE toolbar is not visible, right-click on the toolbars and make sure that “Plugins” is checked.  The toolbar looks like this:<br>
<img src="\tutorial\intro-analysis\12_inasafetoolbar.png" />
* To show the InaSAFE panel, click on the button named “Toggle InaSAFE dock.”<br>
<img src="\tutorial\intro-analysis\12_inasafedock.png" />
* Note that just like QGIS toolbars, you can drag and drop the InaSAFE dock panel to change its position on the QGIS interface.  You can pull it away as a separate window, or place it below the Layers list.  It’s quite convenient in its location on the right side of QGIS, so we will leave it there.<br>
<img src="\tutorial\intro-analysis\12_inasafebox.png" />


The InaSAFE panel consists of three parts: Questions, Results and Buttons.  The questions are mixed in with dropdown boxes - this is where we establish our input data and define the scenario that we want InaSAFE to process.  The purpose of InaSAFE is to make your impact analysis very simple and easy to do.  The Questions section provides a simple way for you to formulate what you want to know.  All questions are created in the following format:


In the event of [**hazard**] how many [**exposure**] might [**impact**]?
For example: "In the event of an earthquake how many buildings might be closed?"


The other parts of the InaSAFE we have seen in action.  The Results section is filled in with information once InaSAFE is run, and the Buttons allow us to run a scenario, print, and access help.


### 3.  Adding Hazard Data

Hazards can be represented by vector layers or by raster layers.  Remember that raster layers are like images with many pixels, and each pixel represents some data about an area on the ground.  A raster that shows elevation, for example, will contain pixels with different values based on the altitude of the location.  Similarly, a raster that represents an earthquake will contain the magnitude of the earthquake at the time of the event in every pixel in the raster.


An earthquake can also be modelled with vector data, although the detail of the data will most likely be lower.  In this case vector polygons will represent the area where the earthquake occurred, and possibly various polygons will show areas of differing magnitudes.


Let’s begin by adding our hazard layer to QGIS.  It’s a raster model of an earthquake in Lembang.

* Click the “Add Raster Layer” button.<br>
<img src="\tutorial\intro-analysis\12_rasterlayer.png" />
* Navigate to the **qgis/Bandung** folder and add **Lembang_Earthquake_Scenario.asc.** This data is raster data (in ASCII format) which represents the magnitude of the earthquake. The layer will look like this:<br>
<img src="\tutorial\intro-analysis\12_hazarddata.png" />


You will notice that the hazard dropdown box has been automatically filled in the InaSAFE panel.  This is because the data file has already been prepared for us with keyword metadata (fancy words for settings) that tells InaSAFE whether it’s a hazard or exposure layer.  When we add the exposure data, we will learn how to do inform InaSAFE ourselves.


### 4.  Exposure

Exposure can also be represented by vectors or rasters.  In fact we’ve already seen this in the Jakarta flood scenario.  When we ran that analysis our population layer was a raster, with each pixel representing the population of a given area on the Earth.  Our buildings on the other hand, were vectors.


Let’s add our exposure data to QGIS - once again we will be using buildings obtained from OpenStreetMap.

* Click on the “Add Vector Layer” button.<br>
<img src="\tutorial\intro-analysis\12_vectorlayer.png" />
* Add the file **Bangunan_Bandung.shp**, which is located in the **qgis/Bandung** folder.<br>
<img src="\tutorial\intro-analysis\12_layerbox.png" />
* Notice that unlike the hazard layer, it does not appear automatically in InaSAFE!

### 5.  Adding Keyword Metadata

In order for InaSAFE to know that our layers are hazard or exposure datasets, we need to assign keywords to the layers using the InaSAFE keyword tool.  Let’s take a look at the keywords that have already been created on the hazard layer.

* Select the earthquake layer in the Layers list, and click on the “InaSAFE Keyword Editor” button.<br>
<img src="\tutorial\intro-analysis\12_inasafeeditor.png" />
* You can see that this layer has already been assigned some keyword information for InaSAFE, including its title, a category, and a subcategory.<br>
<img src="\tutorial\intro-analysis\12_keywordeditor1.png" />


* Click OK, and now select the Bangunan_Bandung layer and open the keyword editor.<br>
<img src="\tutorial\intro-analysis\12_keywordeditor2.png" />


* You’ll notice that title and category are set, but not the subcategory!
* Change this to “structure,” and then click OK.
* Notice that the layer now appears in the InaSAFE dock panel.<br>
<img src="\tutorial\intro-analysis\12_inasafefinal.png" />

### 6.  Impact Analysis

Now our hazard and exposure data are set in the InaSAFE panel, because the appropriate keywords have been added to our layers.  Note that if we were to add a second exposure layer to our project, we would be able to choose which exposure layer we wanted from the InaSAFE dropdown menu.  The same applies to hazard layers.


The third dropdown box is the impact function (“Might”).  This concludes our question, and defines the function that InaSAFE will run behind the scenes.  InaSAFE developers have written many of these functions to analyze all sorts of hazard and exposure layers.  The function that is selected for us here will process the hazard and exposure layers spatially to determine how the exposure layer will “be affected.”


* Click the “Run” button at the bottom to start the impact analysis.  At the end of the process, the statistics will be displayed in the Results section, and a new layer will be added to the Layers list that describes the result of the analysis.  The map will distinguish between buildings that are affected and those that are not.<br>
<img src="\tutorial\intro-analysis\12_impactanalyst1.png" /><br>
<img src="\tutorial\intro-analysis\12_impactanalyst2.png" />


### 7.  Improve the InaSAFE Output Map

We can improve our impact map by editing the symbology in QGIS.  Styles can be changed, other relevant layers can be added, and the layout can be changed using the Print Composer.


Let’s add Bing aerial imagery as a background for our map.

* Go to Plugins ? OpenLayers plugin ? Add Bing Aerial layer.
* Drag the layer below your new impact layer.  If the buildings don’t show correctly above the imagery, right-click on the layer and select “Update drawing order.”<br>
<img src="\tutorial\intro-analysis\12_bingimagery.png" />


### 8.  Using the Print Button

The data displayed on the screen can be saved to a PDF file by clicking Print at the bottom of the InaSAFE panel.  As we’ve seen already, two files will be created, one containing the map and another the data.  Note that you can adjust the print out of your map by adding layers and changing symbologies, and also by zooming to areas of your choosing.<br>
<img src="\tutorial\intro-analysis\12_printbutton.png" />


### 9.  Save Your Results

You can save the impact layer that InaSAFE created, and you can save the QGIS project to come back to it later, but note that the InaSAFE statistics cannot be saved (except when you save them in a PDF).  To get the statistics again in QGIS, you will need to run the analysis again.

* To save the newly generated layer, right-click on it in the Layers list.
* Click Save As...
* Select a name and location for the file.  Click OK.


To save the project:

* Click on the “Save Project” button at the top of QGIS.<br>
<img src="\tutorial\intro-analysis\12_disket.png" />
* Give a name to the project and put it in the directory you want to save your work. Then click Save.<br>
<img src="\tutorial\intro-analysis\12_projectbox.png" />
 


**Summary**
Now you have a firm understanding of how to use to conduct your own impact analysis, using available hazard and exposure data.  In this chapter we’ve learned how to define keywords for each layer so that they can be automatically understood by InaSAFE, and we’ve gone through another disaster scenario, understanding each step more clearly.  By now, you should feel pretty comfortable running a scenario with InaSAFE.  In Unit 4 we will go even further, and you’ll be a pro!