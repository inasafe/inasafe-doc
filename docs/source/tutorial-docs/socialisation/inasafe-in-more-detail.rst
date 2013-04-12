InaSAFE in more detail
======================

Interrogating the output data
-----------------------------

You will now have 3 layer that have been generated through InaSAFE

* 2 - “Population which need evacuating” - Raster Data

* 1 - “Estimated building affected” - Vector Data

We are now going to use the basic QGIS tools to examine the datasets. 


**About Estimate building affected**
....................................

1. Zoom into a section of buildings using the zoom in tool 

Here we have zoomed into 2 rivers going through the middle of Jakarta.


Note: that the red buildings are situated in water greater than 1 meter and the green building are determined not affected as they are in waters less than 1 meter deep.

2. Click once on “Estimate buildings affected”  to make sure layer is highlighted in blue

3. Click on the information tool

4. Click on an affected building (red)

Here I clicked on the building circled in the above picture to result is below.  This buildings has a lot of information recorded about it.

Note: As mentioned before, this information was gathered by the Provincial disaster managers, through an OpenStreetMap  data collection program.  They collect important structures and essential information about the building, such as name, address, type and building structural information.  Also included was if the building had roof access.

5. Zoom back to full extent using the Zoom Full tool 

**About Population which Needs evacuation**
...........................................

6. Uncheck the *“Estimated buildings affected”* and recheck one of  *“Population which Need evacuation”*

7. Again zoom into an area of your choice

8. Click once on *“Population which Need evacuation”* and use the selection tool to select a pixel (square)

Here I clicked on the light green area, to find that there is a value of 80.6411, which means there are approximately 80 people in one pixel (square). 

In this dataset a pixel is 100m by 100m

Click on other pixels to find out their value.

9. Click Close

10. Is each pixel really 100m by 100m, lets check. Use the measure line tool

*Note: it maybe easier to measure one pixel by zooming in further.*

The answer is yes, a pixel is 100 meter across, and if you measure from top to bottom it will also be 100 meter.

As you can see I got 102 meters but this is only because its very hard to click on one corner of the pixel and then the other, unless I zoom in real close!

11. Click Close

12. Zoom back to full extent using the Zoom Full tool

13. Uncheck all layers except

* buildings

* people
 
 
Flood footprint in InaSAFE
--------------------------

Adding a vector layer
.....................

14. Click on the Add vector tool

15. Click on browse and navigate to InaSAFE projects/data/ and select *flood_osm_bpbd18113_jakarta.shp* - click Open, then click Open again.

This dataset is the subvillage boundaries for Jakarta, during the floods in January this year the Provincial disaster mangers collected information about the flooding, one of which was the location of the flooded area by sub-village boundary.

Lets examine this data by opening up its attribute table

16. In the layer list Right click on the flood_osm_BPBD18113_jakarta layers  and select “Open Attribute Table”

OBJECTID: 	Feature ID

KAB_NAME:  District

KEC_NAME:  Sub-district

KEL_NAME:  Village

RW: 	   Sub-village

affected:    	1= affected,              	                            	     

                NULL = not affected

17. Close the Attribute table

Symbolising Vector
..................

Now we are going to colour only the area that were affected

18. Double click on *flood_osm_BPBD18113_jakarta* layers - this will open up the properties table

19. Make sure you are on the style tab

20. Select Categorised

21. Select attribute from the Column

22. Click on Classify (circle 1)

23. Click on ‘0’  (circle 2)

24. Click Delete (circle 3)

25. Click on  ‘_’ (circle 4)

26. Click Delete  (circle 3)

27. Confirm that you only have 1 left

28. Click OK (circle 6)

Below are the results

You have now symbolised your first layer!  You can see only the subvillage areas that were flooded on the 18th of January! Now, can we use this hazard layer in InaSAFE?

Adding Keywords
...............

29. Read through the error message (that occurs when you highlight *flood_osm_BPBD18113_jakarta* layer).  InaSAFE has identified that the layer does not have a keyword file.  As explained on page 10.

30. Click on the keyword editor

31. Fill out the title as **“Jakarta flooding on the 18th January 2013”**

32. For the Category check **Hazard**

33. For Subcategory select **flood[wet/dry]**

34. Click OK

Lets run InaSAFE again with this new flood hazard footprint


Buildings within affected subvillages
.....................................

35. Check that InaSAFE has the following in the drop-down boxes

* Jakarta flooding on the 18th January 2013

* buildings

* Be Flooded

36. Click Run

*Note: This may take about a minute to run*

37. How many estimated buildings were flooded?

Answer  __________________________
......

38. Take some time to examine the results, read through the InaSAFE window

39. Click InaSAFE Print, save accordingly

Now that you have run InaSAFE to find out “how many buildings might be affected”, lets find out how many people.

Evacuation as a percentage
..........................

*Note: We were able to determine how many people needed to be evacuate in the last scenario by specifying how deep the water had to be for the location to be determined unsafe.  However when you don’t know how deep the water is and you only know the flooded area, it is hard to determine how many people will need evacuating. InaSAFE therefore needs your help!*

Instead of determining how many people will be evacuated by  a spatial area, this scenario used the affected population. InaSAFE asks the user to input a percentage of the affected population that could be evacuated.

40. Un-check buildings in the layer panel and recheck people

41. Check that InaSAFE has the following in the drop-down boxes

* Jakarta flooding on the 18th January 2013

* people

* Need Evacuation

42. Click on the impact function editor (pencil)

43. As you can see the default is 1, Click OK

44. Run InaSAFE

*Note: This may take about a minute to run*

45. How many people were evacuated?

AnsweR  __________________________
......

46. How many people were affected?

AnsweR  __________________________
......

47. Take some time to examine the results, read through the InaSAFE window

48. Click InaSAFE Print, save accordingly

Comparing Results - Optional
----------------------------

You have now completed the following runs

+--------------+-------------+------------+------------+-------------+-------------------+-------------+ 
| Hazard	   |   Threshold |  Data Type |  Exposure  |  Data Type	 |  Impact function	 |  Data Type  |
+--------------+-------------+------------+------------+-------------+-------------------+-------------+ 
| flood model  |    1.0m     |   Raster	  |  People	   |   Raster	 |  Need Evacuation	 |             |
| flood model  |    0.8m     |   Raster	  |  People	   |   Raster	 |  Need Evacuation	 |             |
| flood model  |    1.0m     |   Raster	  | Buildings  |   Vector	 |   Be flooded	     |             |
| flood 180113 |             |   Vector	  | Buildings  |   Vector	 |   Be flooded	     |             |
| flood 180113 |     1%	     |   Vector	  |  People	   |   Raster	 |  Need Evacuation  |             |
+--------------+-------------+------------+------------+-------------+-------------------+-------------+

	
49. Please complete the Data Type for each impact layer you have created through InaSAFE

50. Compare between results, 1. How different are the results, 2 Why are they different?

1. AnsweR  _____________________________________________________________
.........

2. AnsweR  _____________________________________________________________
.........
