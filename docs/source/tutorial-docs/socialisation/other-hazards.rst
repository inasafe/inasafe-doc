===============================
Other Hazards in |project_name|
===============================

**Objectives:**

* To run |project_name| with other hazards, specifically Volcano and Earthquake
* To save a subset of an existing layer
* To acknowledge the memory limitation of your computer
* To understand the difference in scale between hazards
* To run |project_name| using a Tsunami model (optional)

**Expected Results**

Participants are able to:

* save a selected feature
* run a Volcano scenario in |project_name| using a volcano vent location
* determine the best course of action to fix a memory error
* run an Earthquake scenario in |project_name| using a shakemap
* run a Tsunami scenario in |project_name| (optional)

Volcanoes in Indonesia
----------------------

There are 129 active volcanoes in Indonesia, and its always valuable to know
how many people, or how much infrastructure is in a certain perimeter of the
vent. Hence |project_name| is able to use a vent location (point) as a hazard
layer, the dataset that we are going to use came from downloading locations
from Smithsonian website.  You may ask “How can we use a point to figure out
impact? |project_name| needs your help!.

1. :guilabel:`Open a QGIS project` called Volcano_Indonesia.qgs -
   **File/Open Project...** , :guilabel:`navigate` to |project_name| projects
   and select Volcano_Indonesia

.. image:: /static/socialisation/volcanoes.png

Select Feature and Save
-----------------------

2. As you can see there are many Volcanoes in Indonesia,
   lets :guilabel:`zoom` into one volcano to analysis. :guilabel:`Right click`
   on the Volcanoes layer and :guilabel:`select` “Open Attribute Table”
3. :guilabel:`Type` “Merapi” in “Look for” section (circle 1),
4. :guilabel:`select` NAME from dropdown menu (circle 2)
5. :guilabel:`Click search` (circle 3). This will select only the Volcano that
   have Merapi in the name column
6. :guilabel:`Check` “Show selected only" (circle 4) This will identify only
   the selected layers.
7. :guilabel:`Click` on “Pan map to the selected row” (circle 5). Selected
   layer is centre  on the map canvas
8. Close Attribute Table (circle 6)

.. image:: /static/socialisation/merapi_attribute2.png
   :align: center

9. :guilabel:`Click` on the zoom to selected tool to zoom in further.
   :guilabel:`Keep clicking` the tool until you get to an extent similar to the
   one below. (The yellow triangle is Merapi)

.. image:: /static/socialisation/merapi2.png
   :align: center

Now that we know where Merapi is, and have check that it is in fact in the
right location, we are going to make a hazard layer with just this point.

10. :guilabel:`Right click` on Volcano and :guilabel:`Save selection as`
11. :guilabel:`Click Browse` and :guilabel:`navigate` to your data area,
    :guilabel:`save as` “Merapi” (circle 1).
12. Check “Add saved file to map” (circle 2)
13. Click OK (circle 3)

.. image:: /static/socialisation/save_selection.png
   :align: center

14. :guilabel:`Uncheck` Volcanoes in the layer window.

You should now have a point that shows the location of Merapi. Lets take some
time to examine the ‘dot’.

15. Use the Information tool to find more out about the Volcano
16. Use the measurement tool to find out how far away is the closest
    population hub (brown areas on the map)

.. Note:: For the Information and Measurement tool to work you need to have
   the Merapi layer highlighted in the layer window.

.. image:: /static/socialisation/save_selection.png
   :align: center

Keywords
--------

We are reminded by |project_name| that we do not have a keyword for this new
layer, so lets make one!

17. :guilabel:`Click` on the keyword editor
18. :guilabel:`Fill` out the title as :kbd:`Merapi erupting`
19. For the Category check :guilabel:`Hazard`
20. For Subcategory select :guilabel:`volcano`
21. :guilabel:`Click OK`

.. image:: /static/socialisation/merapi_keyword.png
   :align: center

Configure and Run |project_name|
--------------------------------

22. :guilabel:`Check` that |project_name| has the following in the drop-down
    boxes

 * Merapi erupting
 * people
 * Need evacuation

23. Before we run |project_name| again, we have to tell |project_name| what
    the hazard zone is!

:guilabel:`Click` on the impact function editor
As a default |project_name| has made 3 hazard areas:

* Vent -3 km
* 3-5 km
* 5-10 km

.. image:: /static/socialisation/impact_function_config.png
   :align: center

.. Note:: that its written 3,5,10 so if you wanted Vent-2,
   2-6 and then 6-10 it would be 2,6,10*

24. :guilabel:`Click OK`
25. :guilabel:`Run` |project_name|
26. :guilabel:`Click` |project_name| Print, save accordingly
27. Analysis Results

.. Note:: Needs per week are based on the cumulative of all 3 zone hence vent
   - 10km

Free time
---------

It is time for you to run through |project_name| yourself,
with no instructions, make sure to print each result!
Take 10 mins to run:

In the event of **Merapi erupting** how many **buildings** will
**be affected** within 3,5,10 km of the vent.

In the event of **Merapi erupting** how many **people** will
**be affected** within 5,10,25 km of the vent.

In the event of **Merapi erupting** how many **buildings** will
**be affected** within 5,10,25 km of the vent.

**ANSWER** __________________________
**ANSWER** __________________________
**ANSWER** __________________________

.. Note:: You can see in this example, and in the previous flooding examples
   that we do not have every single building. In Jakarta we are confident that
   we have the majority of schools, hospitals etc. But around Merapi we only
   have a selection, most of which have no attributes,
   to make a scenario more useful a organised data collection is necessary!.

Earthquake
----------

Indonesia’s location on the edges of the Pacific, Eurasian,
and Australian tectonic plates makes it not only a site of numerous volcanoes
but also frequent earthquakes. The hazard layer we are going to use for this
example has been provided by Badan Geologi and |AIFDR|, |AusAID| and describes the
shaking or Modified Mercalli Intensity (MMI) Scale.

This particular scenario is a modelled version of the 2009 Padang earthquake.

28. :guilabel:`Open` a QGIS project called Padang_earthquake.qgs -
    **File/Open Project...** , :guilabel:`navigate` to |project_name|
    projects and :guilabel:`select` Padang_earthquake
29. You will see that there is 4 layers in the layer panel,
    :guilabel:`click` on each of them to read the keywords in the
    |project_name| window

.. image:: /static/socialisation/padang_earthquake2.png
   :align: center

30. Notice the difference between the first **people** layer and the second,
    the second one has a source of AsiaPop rescale, keep this in mind for the
    next step.
31. In the **How many** drop box pick the top **people**.
32. :guilabel:`Use` the Pan Map tool to move the map slightly.

(:guilabel:`click hold and slightly move the mouse` - this is just to reset
the extent)

Memory usage warning
--------------------

You can see there is a problem with memory usage, its tells you that you may
not be able to run this |project_name| project because your computer has not
enough memory. You will recall that there is another **people** layer,
the difference is the size of the pixel, the one we are trying to run is 100
m by 100 m and the one we will run is 1km by 1km.

.. image:: /static/socialisation/memory_error.png
   :align: center

**Basically less pixels less memory need**

.. image:: /static/socialisation/cell_size.png
   :align: center

33. :guilabel:`Select` the second “people” in the drop down menu
34. :guilabel:`Click` on the drop down menu for the “Might”,
    this is the first |project_name| run where there are actually 2 impact
    functions that we can choose from!
35. :guilabel:`Select` the “Die or be displaced according to the pager model”

.. Note:: This particular impact function was developed in Italy last
   November during a code sprint.

36. :guilabel:`Run` |project_name|

37. :guilabel:`Click` |project_name| Print, :guilabel:`save` accordingly

38. How many people are estimated to die?

**ANSWER** __________________________

39. How many people are estimated to be displaced?

**ANSWER** __________________________


40. Analysis the Action list, how is this different to the action list for
    floods or volcanoes?

**ANSWER** __________________________

Will a building fall down in an earthquake?
-------------------------------------------

As we are all aware, its generally not the earthquake that kills its the
collapsing buildings that kill the majority of the people. Hence
understanding the structure of the building and how they may act under
certain shaking is crucial in understanding the impact of an earthquake.
Unfortunately  earthquakes cover a large area, so mapping every structure in
that area is extensive.  In Padang the international OpenStreetMap community
assisted mapping, totalling roughly 95,000 structures.

Lets find out how they are affected by the modelled Padang 2009 earthquake.

41. :guilabel:`Select` “buildings” in the How many drop box
42. :guilabel:`Run` |project_name|

.. Note:: InaSAFE is design to zoom into the extent of impact zone,
   hence in a minute or so, it will automatically zoom into Padang.*

43. :guilabel:`Investigate` the results, both by looking at the
    |project_name| results, and using the information tool to select a building.
44. :guilabel:`Click` |project_name| Print, :guilabel:`save` accordingly

Tsunami (Optional)
------------------

The 1992 Flores earthquake occurred on December 12, 1992 on the island of
Flores in Indonesia. With a magnitude of 7.8, it was the largest and also the
deadliest earthquake in 1992. This particular scenario is a modelled version
of a Magnitude 8.1 earthquake generating a Tsunami that impact Maumere.

45. :guilabel:`Open` a QGIS project called Maumere_tsunami.qgs - File/Open
    Project... , :guilabel:`navigate` to |project_name| projects and
    :guilabel:`select` Maumere_tsunami.

You will see that there is 3 layers in the layer panel,
click on each of them to read the keywords in the |project_name| window.

.. image:: /static/socialisation/maumere_tsunami2.png
   :align: center

.. Note:: The InaSAFE functionality for Tsunami and floods are very similar,
   however due to the force of the tsunami waves, the maximum depth of the
   water that would affect people and infrastructure is shallower.

46. :guilabel:`Check` that |project_name| has the following in the drop-down
    boxes.

* A tsunami in Maumere (Mw 8.1)
* building
* be flooded

47. :guilabel:`Change` the Impact function parameter to 0.3m.

48. How many buildings are estimated to be flooded?

**ANSWER** __________________________

49. :guilabel:`Click` |project_name| Print, save accordingly.
50. :guilabel:`Run` |project_name| again with the following in the drop-down
    boxes:

#. A tsunami in maumere (Mw 8.1)
#. people
#. need evacuation

51. :guilabel:`Change` the Impact function parameter to 0.5m
52. How many people are estimated to need evacuation

**ANSWER** __________________________

53. :guilabel:`Click` |project_name| Print, save accordingly

Map Canvas Extent
-----------------

.. image:: /static/socialisation/maumere_zoomin2.png
   :align: center

54. Try :guilabel:`zooming` into one section of the tsunami
55. :guilabel:`Run` steps 45-53 again place your 2 results below
56. How many buildings are estimated to be flooded

**ANSWER** __________________________

57.How many people are estimated to need evacuation

**ANSWER** __________________________

.. Note:: You will now see that your results are different than the original
   InaSAFE runs,  this is because your extent window determines the area
   in which you are analysing the data. The next chapter will show you how to
   change this if needed.

You have now gone through |project_name| using 4 different natural hazards,
changing a variety of paramaters and analysing the results.  This chapter has
been designed to help you understand a little more about |project_name| as
well as where you can go for help.


