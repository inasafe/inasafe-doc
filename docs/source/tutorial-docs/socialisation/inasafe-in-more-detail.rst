InaSAFE in More Detail
======================

**Objectives:**

* To interrogate the results using simple GIS tools (Zoom in, Zoom full, Information and Measurement tools) 
* To add a new hazard layer, read its attribute table, and symbolize based on attribute
* To create a keyword for the new hazard layer
* To Run InaSAFE with the new hazard layer
* To Run InaSAFE and add the percentage of affected people who will need evacuation
* To explain the difference between the scenario run in last chapter with this chapter (optional)

**Expected Results:**

Participants are able to:

* use simple GIS tools like zoom in, zoom full, information and measurement tools and interogate its attribute table
* add a new vector layer and symbolised based on attribute
* create a keyword file for a hazard layer
* understand the difference between a model hazard and a footprint hazard
* input the percentage of people that will need evacuating for a flood footprint hazard
* rerun InaSAFE with new hazard layer and explain the difference between the flood model and new hazard layer. (optional) 


Interrogating the Output Data
-----------------------------

You will now have 3 layer that have been generated through InaSAFE

* 2 - :guilabel:`*Population which need evacuating*` - Raster Data

* 1 - :guilabel:`*Estimated building affected*` - Vector Data

We are now going to use the basic QGIS tools to examine the datasets. 


About Estimate Building Affected
................................

1. :guilabel:`Zoom into` a section of buildings using the zoom in tool  

.. image:: /static/socialisation/zoomin2.png

Here we have zoomed into 2 rivers going through the middle of Jakarta.

.. image:: /static/socialisation/buildings_zoom_2.png 

.. note:: *that the red buildings are situated in water greater than 1 meter and the green building are determined not affected as they are in waters less than 1 meter deep.*

2. :guilabel:`Click once` on :guilabel:`*Estimate buildings affected*`  to make sure layer is highlighted in blue

3. :guilabel:`Click` on the information tool 

.. image:: /static/socialisation/information_tool.png

4. :guilabel:`Click` on an affected building (red)

Here I clicked on the building circled in the above picture to result is below.  This buildings has a lot of information recorded about it.

.. image:: /static/socialisation/identy_results.png 

.. note:: *As mentioned before, this information was gathered by the Provincial disaster managers, through an OpenStreetMap  data collection program.  They collect important structures and essential information about the building, such as name, address, type and building structural information.  Also included was if the building had roof access.*

5. :guilabel:`Zoom back to full extent` using the Zoom Full tool

.. image:: /static/socialisation/zoom_extent.png 

About Population which Needs evacuation
.......................................

6. :guilabel:`Uncheck` the *Estimated buildings affected* and :guilabel:`recheck` one of  *Population which Need evacuation*

7. Again :guilabel:`zoom` into an area of your choice 

.. image:: /static/socialisation/zoomin2.png 

8. :guilabel:`Click` once on *Population which Need evacuation* and use the selection tool to select a pixel (square) 

.. image:: /static/socialisation/information_tool.png

Here I clicked on the :guilabel:`light green area` , to find that there is a value of 80.6411, which means there are approximately 80 people in one pixel (square). 

.. image:: /static/socialisation/raster_examine_2.png

In this dataset a pixel is 100m by 100m

:guilabel:`Click` on other pixels to find out their value.

9. :guilabel:`Click` Close

10. Is each pixel really 100m by 100m, lets check. Use the :guilabel:`measure line tool` 

.. image:: /static/socialisation/measure.png

.. note:: *it maybe easier to measure one pixel by zooming in further.*

The answer is yes, a pixel is 100 meter across, and if you measure from top to bottom it will also be 100 meter.

As you can see I got 102 meters but this is only because its very hard to click on one corner of the pixel and then the other, unless I zoom in real close!

.. image:: /static/socialisation/measure_test.png

11. :guilabel:`Click` Close

12. :guilabel:`Zoom back` to full extent using the Zoom Full tool  .. image:: /static/socialisation/zoom_extent.png

13. :guilabel:`Uncheck` all layers except

* buildings

* people
 
 
Flood Footprint in InaSAFE
--------------------------

Adding a Vector Layer  
.....................

14. :guilabel:`Click` on the Add vector tool  .. image:: /static/socialisation/add_vector.png

15. :guilabel:`Click` on browse and navigate to InaSAFE projects/data/ and select *flood_osm_bpbd18113_jakarta.shp* - click Open, then click Open again.

.. image:: /static/socialisation/jakarta18113_added.png

This dataset is the subvillage boundaries for Jakarta, during the floods in January this year the Provincial disaster mangers collected information about the flooding, one of which was the location of the flooded area by sub-village boundary.

Lets examine this data by opening up its :guilabel:`attribute table`

.. image:: /static/socialisation/openattributetable.png

16. In the layer list :guilabel:`Right click` on the *flood_osm_BPBD18113_jakarta* layers  and select *Open Attribute Table*

.. image:: /static/socialisation/attribute_table.png

OBJECTID: 	Feature ID

KAB_NAME:  District

KEC_NAME:  Sub-district

KEL_NAME:  Village

RW: 	   Sub-village

affected:    	1= affected,              	                            	     

                NULL = not affected

17. :guilabel:`Close` the Attribute table

Symbolising Vector
..................

Now we are going to colour only the area that were affected

18. :guilabel:`Double click` on *flood_osm_BPBD18113_jakarta* layers - this will open up the properties table

19. Make sure you are on the style tab

20. Select :guilabel:`Categorised`

.. image:: /static/socialisation/select_category_2.png

21. :guilabel:`Select` attribute from the Column

.. image:: /static/socialisation/select_attribute.png

22. Click on :guilabel:`Classify` (circle 1)

.. image:: /static/socialisation/classify_2.png

23. :guilabel:`Click` on 0  (circle 2)

24. :guilabel:`Click Delete` (circle 3)

25. :guilabel:`Click` on  _ (circle 4)

26. :guilabel:`Click Delete`  (circle 3)

27. Confirm that you only have 1 left

.. image:: /static/socialisation/1_left.png

28. :guilabel:`Click OK` (circle 6)

Below are the results

.. image:: /static/socialisation/result.png

You have now symbolised your first layer!  You can see only the subvillage areas that were flooded on the 18th of January! Now, can we use this hazard layer in InaSAFE?

Adding Keywords
...............

29. :guilabel:`Read` through the error message (that occurs when you highlight *flood_osm_BPBD18113_jakarta* layer).  InaSAFE has identified that the layer does not have a keyword file.  As explained on page 10.

.. image:: /static/error-display.png

30. :guilabel:`Click` on the keyword editor

.. image:: /static/socialisation/pencil.png

31. :guilabel:`Fill out` the title as **Jakarta flooding on the 18th January 2013**

.. image:: /static/socialisation/keyword_editor.png

32. For the Category :guilabel:`check` **Hazard**

33. For Subcategory :guilabel:`select` **flood[wet/dry]**

34. :guilabel:`Click OK`

Lets run InaSAFE again with this new flood hazard footprint


Buildings within affected subvillages
.....................................

35. :guilabel:`Check` that InaSAFE has the following in the drop-down boxes

.. image:: /static/socialisation/inasafe_floodpolygon.png

* Jakarta flooding on the 18th January 2013

* buildings

* Be Flooded

36. :guilabel:`Click Run`

.. note:: *This may take about a minute to run*

37. How many estimated buildings were flooded?

Answer  _______________________________________

38. Take some time to :guilabel:`examine` the results, read through the InaSAFE window

39. :guilabel:`Click InaSAFE Print`, save accordingly

Now that you have run InaSAFE to find out how many buildings might be affected, lets find out how many people.

Evacuation as a percentage
..........................

.. note:: *We were able to determine how many people needed to be evacuate in the last scenario by specifying how deep the water had to be for the location to be determined unsafe.  However when you dont know how deep the water is and you only know the flooded area, it is hard to determine how many people will need evacuating. InaSAFE therefore needs your help!*

Instead of determining how many people will be evacuated by  a spatial area, this scenario used the affected population. InaSAFE asks the user to input a percentage of the affected population that could be evacuated.

40. :guilabel:`Un-check` buildings in the layer panel and recheck people

41. :guilabel:`Check` that InaSAFE has the following in the drop-down boxes

* Jakarta flooding on the 18th January 2013

* people

* Need Evacuation

42. :guilabel:`Click` on the impact function editor (pencil)

.. image:: /static/socialisation/inasafe_pop.png

43. As you can see the default is 1, :guilabel:`Click OK`

.. image:: /static/socialisation/evacuation_per.png

44. :guilabel:`Run` InaSAFE

.. note:: *This may take about a minute to run*

45. How many people were evacuated?

Answer  _______________________________________

46. How many people were affected?

Answer  _______________________________________

47. Take some time to examine the results, read through the InaSAFE window

48. :guilabel:`Click` InaSAFE Print, save accordingly

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

	
49. Please :guilabel:`complete` the Data Type for each impact layer you have created through InaSAFE

50. :guilabel:`Compare` between results, 1. How different are the results, 2 Why are they different?

1. Answer  _______________________________________________________

2. Answer  _______________________________________________________
