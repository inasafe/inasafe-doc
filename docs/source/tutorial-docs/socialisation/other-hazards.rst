Other Hazards in InaSAFE
========================

*Objectives:*
-------------

* To run InaSAFE with other hazards, specifically Volcano and Earthquake
* To save a subset of an existing layer
* To acknowledge the memory limitation of your computer
* To understand the difference in scale between hazards
* To run InaSAFE using a Tsunami model (optional)

*Expected Results:*
-------------------

Participants are able to:

* save a selected feature
* run a Volcano scenario in InaSAFE using a volcano vent location
* determine the best course of action to fix a memory error
* run an Earthquake scenario in InaSAFE using a shakemap
* run a Tsunami scenario in InaSAFE (optional)

Volcanoes in Indonesia
----------------------

There are 129 active volcanoes in Indonesia, and its always valuable to know how many people, or how much infrastructure is in a certain perimeter of the vent.Hence InaSAFE is able to use a vent location (point) as a hazard layer, the dataset that we are going to use came from downloading locations from Smithsonian website.  You may ask “How can we use a point to figure out impact? InaSAFE needs your help!.

1. Open a QGIS project called Volcano_Indonesia.qgs - **File/Open Project...** , navigate to InaSAFE projects and select Volcano_Indonesia

.. image:: ..../_static/volcanoes.png
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


