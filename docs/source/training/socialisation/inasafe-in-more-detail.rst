=============================
|project_name| in More Detail
=============================

**Objectives:**

* To interrogate the results using simple GIS tools (Zoom in, Zoom full,
  Information and Measurement tools)
* To add a new hazard layer, read its attribute table, and symbolize based on
  attribute
* To create a keyword for the new hazard layer
* To Run |project_name| with the new hazard layer
* To Run |project_name| and add the percentage of affected people who will need
  evacuation
* To aggregate the results  

**Expected Results:**

Participants are able to:

* use simple GIS tools like zoom in, zoom full, information and measurement
  tools and interrogate its attribute table
* add a new vector layer and symbolised based on attribute
* create a keyword file for a hazard layer
* understand the difference between a model hazard and a footprint hazard
* input the percentage of people that will need evacuating for a flood
  footprint hazard
* aggregate impact results by administration areas  


Interrogating the Output Data
-----------------------------

You will now have 3 or 4 layer that have been generated through |project_name|

* 2 - *Population which need evacuating* - Raster Data

* 1or2 - *Estimated building affected* - Vector Data

We are now going to use the basic QGIS tools to examine the datasets.

============================================    ====================================
**Symbol**										**Name**
--------------------------------------------	------------------------------------
.. image:: /static/general/icon_identify		Identify Features
.. image:: /static/general/icon_attribute		Open Attribute Table
.. image:: /static/general/icon_line			Measure Line
.. image:: /static/general/icon_area			Measure Area
.. image:: /static/general/icon_zoomlayer		Zoom to Layer
.. image:: /static/general/icon_zoomin			Zoom In
.. image:: /static/general/add_vector			Add Vector Layer
--------------------------------------------	------------------------------------


About Estimate Building Affected
................................

1. Using the :guilabel:`Zoom In` tool, zoom to a cluster of buildings

Here we have zoomed into 2 rivers going through the middle of Jakarta.

.. image:: /static/training/socialisation/042_buildings_zoom.png
   :align: center
   
.. note:: That the red buildings are situated in water greater than 1 meter
   and the green building are determined not affected as they are in waters
   less than 1 meter deep.

2. :guilabel:`Select` *Estimate buildings affected* in the **Layer List** to highlight
   the layer. It should now be in blue.

.. image:: /static/training/socialisation/043_highlight.png
   :align: center

3. Use the :guilabel:`Identify Features` tool to select a building

Here I clicked on the building circled in the above picture, the results are below.
This buildings has a lot of information recorded about it.

.. image:: /static/training/socialisation/044_identifyresults.png
   :align: center
.. note:: As mentioned before, this information was gathered by the
   Provincial disaster managers, through an OpenStreetMap  data collection
   program.  They collect important structures and essential information
   about the building, such as name, address, type and building structural
   information.  Also included was if the building had roof access.

4. Click on :guilabel:`Zoom to Layer` - this will get you back to extent of 
*Estimate building affected*


About Population which needs evacuation
.......................................

5. In the **Layer list** :guilabel:`Uncheck` the *Estimated buildings affected* and
   :guilabel:`Check` one of  the *Population which Need evacuation*

6. :guilabel:`Select` *Population which Need evacuation* in the **Layer List** to highlight
   the layer. It should now be in blue.

7. :guilabel:`Zoom In` to an area of your choice

8. Use the :guilabel:`Identify Features` tool to select a pixel (square) of the 
selected *Population which Need evacuation*

Here I clicked on the :guilabel:`light green area` , to find that there is a
value of 80.6411, which means there are approximately 80 people in one pixel
(square).

.. image:: /static/training/socialisation/045_examineraster.png
   :align: center
   
.. note:: In this dataset a pixel is 100m by 100m

9.  Use the :guilabel:`Identify Features` tool to select other pixels to find out 
their value.

10. :guilabel:`Close` the **Identify Results** box

11. Is each pixel really 100m by 100m? lets check. Use the :guilabel:`Measure Line` tool

.. note:: It maybe easier to measure one pixel by zooming in further.

The answer is yes, a pixel is 100 meter across, and if you measure from top
to bottom it will also be 100 meter.

.. image:: /static/training/socialisation/046_measuretest.png
   :align: center

As you can see I got 102 meters but this is only because its very hard to
click on one corner of the pixel and then the other, unless I zoom in real
close!

12. :guilabel:`Close` the **Measure** box

13. Use the :guilabel:`Zoom to Layer` to go back to the full extent of the select layer.

14. :guilabel:`Uncheck` all layers except:

* buildings
* people


Flood Footprint in |project_name|
---------------------------------

Adding a Vector Layer
.....................

15. Select on the :guilabel:`Add Vector` tool

16. Use :guilabel:`Browse` to navigate to the *data* folder within *InaSAFE Projects*, 
:guilabel:`Select` *flood_osm_bpbd18113_jakarta.shp*, :guilabel:`Open` in the **Open an 
OGR Support** window and :guilabel:`Open` again in the **Source** window.

.. image:: /static/training/socialisation/047_jakarta18113.png
   :align: center
   
This dataset is the subvillage boundaries for Jakarta,
during the floods in January this year the Provincial disaster mangers
collected information about the flooding, one of which was the location of
the flooded area by sub-village boundary.

.. note:: The InaSAFE panel is currently showing a warning "Layer keywords missing:"
we will address this concern in later steps.

Lets examine this data by opening up its *attribute table*

17. Make sure the *flood_osm_bpbd18113_jakarta* is highlight (blue line in the 
**Layer List**). Select the :guilabel:`Open Attribute Table` tool. 

.. image:: /static/training/socialisation/048_attributetable.png
   :align: center
   
OBJECTID:  Feature ID

KAB_NAME:  District

KEC_NAME:  Sub-district

KEL_NAME:  Village

RW:        Sub-village

affected:  1= affected,
           NULL = not affected 
           
.. note:: This is the same information as the Identify Feature tool, but instead of just
viewing one object information, you can see all of the object at once.

18. :guilabel:`Close` the Attribute table

Symbolising Vector
..................

Now we are going to stylise the subvillage administration boundary to only see the 
affected = 1 areas. 

19. :guilabel:`Double click` on *flood_osm_BPBD18113_jakarta* layers - this
    will open up the properties table

20. Navigate to the style tab

.. image:: /static/training/socialisation/049_styletab.png
   :align: center

21. Follow the below steps to stylise the subvillage boundaries as illustrated in the 
picture and table below.

===========  	======================================================================
**Number**	 	**Step**								
-----------  	----------------------------------------------------------------------
1			 	Select "Catergorized" from the drop down menu
2				Select "affected" from the Column drop down menu
3				Click "Classify"
4				Highlight the row light blue "0 0"
5				Click "Delete"
6				Highlight the row dark blue "    "
7				Click "Delete" 
8				Confirm you only have 1 row left
9				Close the **Layer Properties** window
-----------  	----------------------------------------------------------------------

.. image:: /static/training/socialisation/050_layerproperties.png
   :align: center

Below are the results

.. image:: /static/training/socialisation/051_styleflood.png
   :align: center
   
You have now symbolised your first layer!  You can see only the subvillage
areas that were flooded on the 18th of January! Now, can we use this hazard
layer in |project_name|?

Adding Keywords
...............

22. As previously pointed out the |project_name| panel is showing a warning. It is 
explaining to us that the layer highlight *flood_osm_BPBD18113_jakarta* has no keywords.
Lets follow the instructions and select the :guilabel:`InaSAFE Keyword` tool.

.. image:: /static/training/socialisation/052_keyword.png
   :align: center


23. In the *Keywords Editor* window you have an option of changing the Title, Category and 
Subcategory. We are going to do just that by following the steps in the table below

==============  	======================================================================
**Quick edit**	 	**Variable**								
--------------  	----------------------------------------------------------------------
Title				:kbd:`Jakarta flooding on the 18th January 2013`
Category			Hazard
Subcategory			flood[wet/dry]
--------------  	----------------------------------------------------------------------

.. image:: /static/training/socialisation/053_keywordedited.png
   :align: center

24. Close the Keyword editor: :guilabel:`OK`

Lets run |project_name| again with this new flood hazard footprint

For more information about Keywords :doc:`../user-docs/function_docs/keywords`

Buildings within affected subvillages
.....................................

35. :guilabel:`Check` that |project_name| has the following in the drop-down
    boxes

.. image:: /static/socialisation/inasafe_floodpolygon.png

* Jakarta flooding on the 18th January 2013

* buildings

* Be Flooded

36. :guilabel:`Click Run`

.. note:: *This may take about a minute to run*

37. How many estimated buildings were flooded?

Answer  _____________________________________

38. Take some time to :guilabel:`examine` the results,
    read through the |project_name| window

39. :guilabel:`Click InaSAFE Print`, save accordingly

Now that you have run |project_name| to find out how many buildings might be
affected, lets find out how many people.

Evacuation as a percentage
..........................

.. note:: We were able to determine how many people needed to be evacuate in
   the last scenario by specifying how deep the water had to be for the
   location to be determined unsafe.  However when you don`t know how deep the
   water is and you only know the flooded area, it is hard to determine how
   many people will need evacuating. InaSAFE therefore needs your help!

Instead of determining how many people will be evacuated by  a spatial area,
this scenario used the affected population. |project_name| asks the user to
input a percentage of the affected population that could be evacuated.

40. :guilabel:`Un-check` buildings in the layer panel and recheck people

41. :guilabel:`Check` that |project_name| has the following in the drop-down
    boxes

* Jakarta flooding on the 18th January 2013

* people

* Need Evacuation

42. :guilabel:`Click` on the impact function editor (pencil)

.. image:: /static/socialisation/inasafe_pop.png

43. As you can see the default is 1, :guilabel:`Click OK`

.. image:: /static/socialisation/evacuation_per.png

44. :guilabel:`Run` |project_name|

.. note:: *This may take about a minute to run*

45. How many people were evacuated?

Answer  _______________________________________

46. How many people were affected?

Answer  _______________________________________

47. Take some time to examine the results, read through the |project_name|
    window

48. :guilabel:`Click` |project_name| Print, save accordingly

Comparing Results - Optional
----------------------------

You have now completed the following runs

=============  =============  =============  ============  =============  ===================  =============
**Hazard**     **Threshold**  **Data Type**  **Exposure**  **Data Type**  **Impact function**  **Data Type**
=============  =============  =============  ============  =============  ===================  =============
flood model    1.0m           Raster         People        Raster         Need Evacuation
flood model    0.8m           Raster         People        Raster         Need Evacuation
flood model    1.0m           Raster         Buildings     Vector         Be flooded
flood 180113                  Vector         Buildings     Vector         Be flooded
flood 180113   1%             Vector         People        Raster         Need Evacuation
=============  =============  =============  ============  =============  ===================  =============


49. Please :guilabel:`complete` the Data Type for each impact layer you have
    created through |project_name|

50. :guilabel:`Compare` between results, 1. How different are the results,
    2. Why are they different?

1. Answer _____________________________________________________

2. Answer _____________________________________________________

Basic Aggregation - Optional
----------------------------

23. :guilabel:`Click` Add vector button .. image:: /static/socialisation/

24. Navigate to the data folder and :guilabel:`Select` |project_name|
    projects/data/district_osm_jakarta.shp

.. image:: /static/socialisation/page_33.jpg
   :align: center

25. :guilabel:`Click` Open

26. :guilabel:`Click` once on the district of Jakarta Layer

.. image:: /static/socialisation/page_33_2.jpg
   :align: center

27. :guilabel:`Click` on the drop down menu for ´Aggregation results by´ and
    :guilabel:`Select` Subdistrict of Jakarta

.. image:: /static/socialisation/page_33_3.jpg
   :align: center

28. Change the threshold back to 1.0 (refer point 7)

29. Run |project_name| again

30. :guilabel:`Click` |project_name| Print, save accordingly

Keywords Editor
---------------

In the next chapter we will explore the keyword editor for the hazard and
exposure layers.

However the Keyword editor for postprocessing is slightly different. You are
able to :guilabel:`Select` an attribute to provide the percentage of females
per aggregation area. If there is no such layer |project_name| defaults at
50% or 0.5.

If you would like more detail please ask at the end of the session

.. image:: /static/socialisation/aggregation_keyword.png
   :align: center

31. Keywords Editor window will pop up, press OK

32. Scroll down the bottom of the results, you will see disaggregation of
the population data and demographics by district.

33. :guilabel:`Click` |project_name| Print, save accordingly

.. image:: /static/socialisation/page_34.jpg
   :align: center
