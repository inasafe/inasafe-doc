.. _other-hazards:

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
layer, the dataset that we are going to use in section of the training was
downloaded from the Smithsonian website.  You may ask “How can we use a point
to figure out impact? |project_name| needs your help!.

1. :menuselection:`File --> Open Projects`, browse to *Volcano_Indonesia.qgs*

.. image:: /static/training/socialisation/061_volcano.*
   :align: center

Select Feature and Save
-----------------------

2. As you can see there are many Volcanoes in Indonesia,
   lets zoom into one volcano to analysis. :guilabel:`Right Click`
   on the Volcanoes layer in the **Layer List** and :guilabel:`Select`
   *Open Attribute Table*
3. In the *Look for* section type :kbd:`Merapi` (circle 1),
4. :guilabel:`Select` **NAME** from dropdown menu (circle 2)
5. :guilabel:`Search` (circle 3). This will select only the Volcano that
   have Merapi in the name column
6. :guilabel:`Check` *Show selected only* (circle 4) This will identify only
   the selected layers.
7. :guilabel:`Click` on *Pan map to the selected row* (circle 5). Selected
   layer should be in the centre  on the map canvas
8. :guilabel:`Close` Attribute Table Window (circle 6)

.. image:: /static/training/socialisation/062_merapi_attribute.*
   :align: center

9. :guilabel:`Zoom to Selection` to zoom in further, continue until you get to an extent
	similar to the one below. (The yellow triangle is Merapi)

.. image:: /static/training/socialisation/063_merapi.*
   :align: center

Now that we know where Merapi is, and have check that it is in fact in the
right location, we are going to make a hazard layer with just this point.

10. :guilabel:`Right Click` on Volcano in the **Layer List**
	and :guilabel:`Save selection as`
11. :guilabel:`Browse` and navigate to your data area,
    :guilabel:`save as` “Merapi” (circle 1).
12. :guilabel:`Check` *Add saved file to map* (circle 2)
13. :guilabel:`OK` (circle 3)

.. image:: /static/training/socialisation/064_save_volcano.*
   :align: center

14. :guilabel:`Uncheck` Volcanoes in the layer window.

You should now have a point that shows the location of Merapi. Lets take some
time to examine the ‘dot’.

15. Use the :guilabel:`Identify feature` tool to find more out about the Volcano
16. Use the :guilabel:`Measure line` tool to find out how far away is the closest
    population hub (brown areas on the map)

.. note:: For the Identify feature and Measure line tool to work you need to
   have the Merapi layer highlighted in the layer window. Which can be
   accomplished by clicking once on the layer in the Layer List.

.. image:: /static/training/socialisation/065_merapi_nokeyword.*
   :align: center

Keywords
--------

We are reminded by |project_name| result window that we do not have a keyword for this new
layer, so lets make one!

17. Go to :guilabel:`InaSAFE Keyword Editor`
18. Type :kbd:`Merapi erupting` as the title
19. For the Category :guilabel:`Check` **Hazard**
20. For Subcategory :guilabel:`Select` **Volcano**
21. :guilabel:`OK`

.. image:: /static/training/socialisation/066_merapi_keyword.*
   :align: center

Configure and Run |project_name|
--------------------------------

22. Confirm that |project_name| has the following in the drop-down
    boxes

* Merapi erupting
* people
* Need evacuation

Before we run |project_name| again, we have to tell |project_name| what the hazard
zone is!

23. Click on :guilabel:`...` (impact function editor) next to *Need evacuation*
    As a default |project_name| has made 3 hazard areas:

* Vent -3 km
* 3-5 km
* 5-10 km

.. image:: /static/training/socialisation/067_volcano_config.*
   :align: center

.. note:: that its written 3,5,10 so if you wanted the categories to be Vent-5,
   5-10 and then 10-25 then you would type  5,10,25

24. :guilabel:`OK`

25. :guilabel:`Run` |project_name|

26. :guilabel:`Click` |project_name| Print, save accordingly

27. Analysis Results

.. image:: /static/training/socialisation/068_merapi_results.*
   :align: center

.. note:: Needs per week are based on the cumulative of all 3 zone hence vent
   - 10km

Free time
---------

It is time for you to run through |project_name| yourself,
with no instructions, make sure to print each result!
Take 10 mins to run:
::

 In the event of Merapi erupting how many buildings will
 be affected within 3,5,10 km of the vent?

 ANSWER __________________________

 In the event of Merapi erupting how many people will
 be affected within 5,10,25 km of the vent?

 ANSWER __________________________

 In the event of Merapi erupting how many buildings will
 be affected within **5,10,25** km of the vent?

 ANSWER __________________________

.. note:: You can see in this example, and in the previous flooding examples
   that we do not have every single building. In Jakarta we are confident that
   we have the majority of schools, hospitals etc. But around Merapi we only
   have a selection, most of which have no attributes,
   to make a scenario more useful a organised data collection is necessary!.

Earthquake
----------

Indonesia’s location on the edges of the Pacific, Eurasian,
and Australian tectonic plates makes it not only a site of numerous volcanoes
but also frequent earthquakes. The hazard layer we are going to use for this
example has been provided by Badan Geologi and |AIFDR|, |DFATAusAid| and describes the
shaking or Modified Mercalli Intensity (MMI) Scale.

This particular scenario is a modelled version of the 2009 Padang earthquake.

28. :menuselection:`File --> Open Projects`, browse to *Padang_earthquake.qgs*

.. image:: /static/training/socialisation/069_earthquake.*
   :align: center


29. You will see that there is 4 layers in the layer panel,
    :guilabel:`Click` on each of them to read the keywords in the
    |project_name| window

.. image:: /static/training/socialisation/070_people_scale.*
   :align: center

.. note:: Notice the difference between the first **people** layer and the
   other 2 people, the second one has a source of *AsiaPop rescaled 1km2*,
   the third *AsiaPop rescaled 5km2*

30. Make sure the only **people** checked is Source= AsiaPop

31. In the **How many** drop box pick the top **people**.

32. :guilabel:`Run` |project_name|

Memory usage warning
--------------------

.. image:: /static/training/socialisation/071_memory.*
   :align: center

A warning message appears "You may not have sufficient free system memory to
carry out the analysis.
See the dock panel message for more information.
Would you like to continue regardless?"

33. :guilabel:`No`

You will see in the |project_name| panel that there is a suggestion on how
to continue:

"Try zooming in to a smaller area or using a raster layer with a coarser
resolution to speed up execution and reduce memory requirements. You could
also try adding more RAM to your computer"

You will recall that there is another 2 **people** layer,
the difference is the size of the pixel, the one we are trying to run is 100
m by 100 m and the one we will run now is 1km by 1km.
If the 1km population fails, the third **people** layer is our backup!

**Basically less pixels less memory need.**

.. image:: /static/training/socialisation/072_cellsize.*
   :align: center

34. :guilabel:`Check` the second “people” in the drop down menu - check the
    keywords to confirm its the source is *AsiaPop 1km2*

35. :guilabel:`Click` on the drop down menu for the “Might”,
    this is the first |project_name| run where there are actually 2 impact
    functions that we can choose from!

36. :guilabel:`Select` the “Die or be displaced according to the pager model”

.. note:: This particular impact function was developed in Italy last
   November during a code sprint.

37. :guilabel:`Run` |project_name|

38. :guilabel:`Print` |project_name|, :guilabel:`Save` accordingly

::

 How many people are estimated to die?

 ANSWER __________________________

 How many people are estimated to be displaced?

 ANSWER __________________________


39. Analysis the Action list, how is this different to the action list for
    floods or volcanoes?

::

 ANSWER __________________________


Will a building fall down in an earthquake?
-------------------------------------------

As we are all aware, its generally not the earthquake that kills,
its the collapsing buildings that kill the majority of the people.
Hence understanding the structure of the building and how they may act under
certain shaking is crucial in understanding the impact of an earthquake.
Unfortunately  earthquakes cover a large area, so mapping every structure in
that area is extensive.
In Padang the international |OSM| community assisted mapping,
totalling roughly 95,000 structures.

Lets find out how they are affected by the modelled Padang 2009 earthquake.

40. :guilabel:`Uncheck` *people* in the **Layer List** and :guilabel:`Check` *building*

41. Confirm that |project_name| window has the following:

* an earthquake in Padang like in 2009
* buildings
* be affected

42. :guilabel:`Run` |project_name|

.. note:: InaSAFE is design to zoom into the extent of impact zone,
   hence in a minute or so, it will automatically zoom into Padang.

43. Investigate the results, both by looking at the
    |project_name| results, and using the information tool to select a building.

44. :guilabel:`Print` |project_name|, :guilabel:`Save` accordingly

Tsunami
------------------

The 1992 Flores earthquake occurred on December 12, 1992 on the island of
Flores in Indonesia.
With a magnitude of 7.8, it was the largest and also the deadliest earthquake
in 1992.
This particular scenario is a modelled version of a Magnitude 8.1 earthquake
generating a Tsunami that impact Maumere.

45. :menuselection:`File --> Open Projects`, browse to *Maumere_tsunami.qgs*

You will see that there is 2 layers in the layer panel,
click on each of them to read the keywords in the |project_name| window.

.. image:: /static/training/socialisation/073_tsunami.*
   :align: center

.. note:: The InaSAFE functionality for Tsunami and floods are very similar,
   however due to the force of the tsunami waves, the maximum depth of the
   water that would affect people and infrastructure is shallower.

46. Confirm that |project_name| window has the following boxes.

* A tsunami in Maumere (Mw 8.1)
* people
* be flooded

47. :guilabel:`...` to change the water level for evacuation from 1m to :kbd:`0.5m`

48. :guilabel:`Run` |project_name|

49. :guilabel:`Print` |project_name|, :guilabel:`Save` accordingly

Map Canvas Extent
-----------------

50. We are going to run again, but only on a 1/4 of the extent,
    :guilabel:`Zoom In`

51. :guilabel:`Run` |project_name|

.. image:: /static/training/socialisation/074_tsunami_zoom.*
   :align: center

You will now see that your results are different than the original InaSAFE
runs, this is because your extent window determines the area in which you are
analysing the data.
The next chapter will show you how to change this if needed.

.. note:: The population coverage coastline in this zoomed in area is
   different to the hazard coastline, this can be a significant problem when
   your population dataset does not reflect the same extents as reality.
   Through OpenLayers select Bing imagery and examine the two layers (people
   and tsunami). Always quality assure your input layers.

OpenStreetMap Downloader
------------------------

Notice that there are no building footprints in this project file,
that is because we are going to download them straight from |OSM| server.

52. Highlight the tsunami layer and :guilabel:`Zoom to Layer`

53. :guilabel:`InaSAFE OpenStreetMap Downloader`

.. image:: /static/training/socialisation/075_osmdownloader.*
   :align: center

.. note:: The extent of the **Map Canvas** will automatically be added to the
   Bounding box.

54. Confirm the location of the output directory, :guilabel:`OK`

.. image:: /static/training/socialisation/076_building_loaded.*
   :align: center

.. note:: On inspection of the buildings, they don't really have many
   attributes at all, this area was digitised for this analysis,
   field surveys are still to be conducted.

55. Confirm that  window has the following boxes.

  * A tsunami in Maumere (Mw 8.1)
  * buildings
  * be flooded

56. :guilabel:`Run` |project_name|

57. :guilabel:`Print` |project_name|, :guilabel:`Save` accordingly

.. note:: For more information on the OSM loader please go to
   :ref:`openstreetmap_downloader`
