Other Hazards in InaSAFE
========================

Objectives
----------

* To run InaSAFE with other hazards, specifically Volcano and Earthquake
* To save a subset of an existing layer
* To acknowledge the memory limitation of your computer
* To understand the difference in scale between hazards
* To run InaSAFE using a Tsunami model (optional)

Expected Results
----------------

Participants are able to:

* save a selected feature
* run a Volcano scenario in InaSAFE using a volcano vent location
* determine the best course of action to fix a memory error
* run an Earthquake scenario in InaSAFE using a shakemap
* run a Tsunami scenario in InaSAFE (optional)

Volcanoes in Indonesia
----------------------

There are 129 active volcanoes in Indonesia, and its always valuable to know how many people, or how much infrastructure is in a certain perimeter of the vent.Hence InaSAFE is able to use a vent location (point) as a hazard layer, the dataset that we are going to use came from downloading locations from Smithsonian website.  You may ask “How can we use a point to figure out impact? InaSAFE needs your help!.

1. :guilabel:`Open a QGIS project` called Volcano_Indonesia.qgs - **File/Open Project...** , :guilabel:`navigate` to InaSAFE projects and select Volcano_Indonesia

.. image:: ../_static/socialisation/volcanoes.png
   :align: center

Select Feature and Save
-----------------------

2. As you can see there are many Volcanoes in Indonesia, lets zoom into one volcano to analysis. Right click on the Volcanoes layer and select “Open Attribute Table”
3. Type “Merapi” in “Look for” section - circle 1,
4. select NAME from dropdown menu- circle 2 
5. Click search - circle 3 -This will select only the Volcano that have Merapi in the name column
6. Check “Show selected only - circle 4 -This will identify only the selected layers
7. Click on “Pan map to the selected row” - circle 5 -Selected layer is centre  on the map canvas
8. Close Attribute Table - circle 6


**image**


9. Click on the zoom to selected tool to zoom in further. Keep clicking the tool until you get to an extent similar to the one below. (The yellow triangle is Merapi)

**image**

Now that we know where Merapi is, and have check that it is in fact in the right location, we are going to make a hazard layer with just this point.

10. Right click on Volcano and ‘Save selection as’
11. Click Browse and navigate to your data area, save as “Merapi” (circle 1)
12. Check “Add saved file to map” (circle 2)
13. Click OK (circle 3)


**image**


14. Uncheck Volcanoes in the layer window. 
You should now have a point that shows the location of Merapi. Lets take some time to examine the ‘dot’
15. Use the Information tool to find more out about the Volcano
16. Use the measurement tool to find out how far away is the closest population hub (brown areas on the map)

*Note: For the Information and Measurement tool to work you need to have the Merapi layer highlighted in the layer window.*

Keywords
--------

We are reminded by InaSAFE that we do not have a keyword for this new layer, so lets make one!

17. Click on the keyword editor
18. Fill out the title as **“Merapi erupting”**
19. For the Category check Hazard
20. For Subcategory select volcano
21. Click OK



Configure and Run InaSAFE
-------------------------

22. Check that InaSAFE has the following in the drop-down boxes

 #. Merapi erupting
 #. people
 #. Need evacuation

23. Before we run InaSAFE again, we have to tell InaSAFE what the hazard zone is!
Click on the impact function editor
As a default InaSAFE has made 3 hazard areas:

#. Vent -3 km
#. 3-5 km
#. 5-10 km

*Note: that its written 3,5,10 so if you wanted Vent-2, 2-6 and then 6-10 it would be 2,6,10*

24. Click OK
25. Run InaSAFE
26. Click InaSAFE Print, save accordingly
27. Analysis Results

*Note: Needs per week are based on the cumulative of all 3 zone hence vent - 10km*

Free time
---------

Its time for you to run through InaSAFE yourself, with no instructions, make sure to print each result!
Take 10 mins to run:
In the event of **Merapi erupting** how many **buildings** will **be affected** within 3,5,10 km of the vent
In the event of **Merapi erupting** how many **people** will **be affected** within 5,10,25 km of the vent
In the event of **Merapi erupting** how many **buildings** will **be affected** within 5,10,25 km of the vent

**ANSWER** _________________________ **ANSWER** ________________________ **ANSWER** __________________________

*Note: You can see in this example, and in the previous flooding examples that we do not have every single building. In Jakarta we are confident that we have the majority of schools, hospitals etc. But around Merapi we only have a selection, most of which have no attributes, to make a scenario more useful a organised data collection is necessary!.*

Earthquake
----------

Indonesia’s location on the edges of the Pacific, Eurasian, and Australian tectonic plates makes it not only a site of numerous volcanoes but also frequent earthquakes. The hazard layer we are going to use for this example has been provided by Badan Geologi & AIFDR and describes the shaking or Modified Mercalli Intensity (MMI) Scale.

This particular scenario is a modelled version of the 2009 Padang earthquake.

28. Open a QGIS project called Padang_earthquake.qgs - **File/Open Project...** , navigate to InaSAFE projects and select Padang_earthquake
29. You will see that there is 4 layers in the layer panel, click on each of them to read the keywords in the InaSAFE window

**image**

30. Notice the difference between the first **people** layer and the second, the second one has a source of AsiaPop rescale, keep this in mind for the next step.
31. In the **How many** drop box pick the top **people**.
32. Use the Pan Map tool to move the map slightly.
(click hold and slightly move the mouse - this is just to reset the extent)

Memory usage warning
--------------------

You can see there is a problem with memory usage, its tells you that you may not be able to run this InaSAFE project because your computer has not enough memory. 
You will recall that there is another **people** layer, the difference is the size of the pixel, the one we are trying to run is 100 m by 100 m and the one we will run is 1km by 1km.

**Basically less pixels less memory need**

33. Select the second “people” in the drop down menu
34. Click on the drop down menu for the “Might”, this is the first InaSAFE run where there are actually 2 impact functions that we can choose from!
35. Select the “Die or be displaced according to the pager model”
*Note: This particular impact function was developed in Italy last November during a code sprint.*

36. Run InaSAFE

37. Click InaSAFE Print, save accordingly

38. How many people are estimated to die?

**ANSWER**
_____________________________________________________________

39. How many people are estimated to be displaced?

**ANSWER**
_____________________________________________________________


40. Analysis the Action list, how is this different to the action list for floods or volcanoes?

**ANSWER**
_____________________________________________________________________________________
_____________________________________________________

Will a building fall down in an earthquake?
-------------------------------------------

As we are all aware, its generally not the earthquake that kills its the collapsing buildings that kill the majority of the people. Hence understanding the structure of the building and how they may act under certain shaking is crucial in understanding the impact of an earthquake.  Unfortunately  earthquakes cover a large area, so mapping every structure in that area is extensive.  In Padang the international OpenStreetMap community assisted mapping, totalling roughly 95,000 structures. 

Lets find out how they are affected by the modelled Padang 2009 earthquake.

41. Select “buildings” in the How many drop box
42. Run InaSAFE

*Note: InaSAFE is design to zoom into the extent of impact zone, hence in a minute or so, it will automatically zoom into Padang.*

43. Investigate the results, both by looking at the InaSAFE results, and using the information tool to select a building.
44. Click InaSAFE Print, save accordingly

Tsunami (Optional)
------------------

The 1992 Flores earthquake occurred on December 12, 1992 on the island of 
Flores in Indonesia. With a magnitude of 7.8, it was the largest and also the deadliest earthquake in 1992. 
This particular scenario is a modelled version of a Magnitude 8.1 earthquake generating a Tsunami that impact Maumere.

45. Open a QGIS project called Maumere_tsunami.qgs - File/Open Project... , navigate to InaSAFE projects and select Maumere_tsunami

You will see that there is 3 layers in the layer panel, click on each of them to read the keywords in the InaSAFE window

**image**

*Note: The InaSAFE functionality for Tsunami and floods are very similar, however due to the force of the tsunami waves, the maximum depth of the water that would affect people and infrastructure is shallower.*

46. Check that InaSAFE has the following in the drop-down boxes
#. A tsunami in Maumere (Mw 8.1)
#. building
#. be flooded

47. Change the Impact function parameter to 0.3m
48. How many buildings are estimated to be flooded

*ANSWER* _____________________________________________________________

49. Click InaSAFE Print, save accordingly
50. Run InaSAFE again with the following in the drop-down boxes:
#. A tsunami in maumere (Mw 8.1)
#. people
#. need evacuation

51. Change the Impact function parameter to 0.5m
52. How many people are estimated to need evacuation
*ANSWER*
_____________________________________________________________

53. Click InaSAFE Print, save accordingly

Map Canvas Extent
-----------------

**IMAGE**

54. Try zooming into one section of the tsunami
55. Run steps 45-53 again place your 2 results below
56. How many buildings are estimated to be flooded

ANSWER  _____________________________________________________________

57.How many people are estimated to need evacuation

ANSWER  _____________________________________________________________

*Note: You will now see that your results are different than the original InaSAFE runs,  this is because your extent window determines the area in which you are analysing the data. The next chapter will show you how to change this if needed.*

You have now gone through InaSAFE using 4 different natural hazards, changing a variety of paramaters and analysing the results.  This chapter has been designed to help you understand a little more about InaSAFE as well as where you can go for help.


