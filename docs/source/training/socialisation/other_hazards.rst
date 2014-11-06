.. _other-hazards:

Other Hazards in |project_name|
===============================

**Learning Objectives:**

* Run |project_name| with other hazards, specifically volcanoes, earthquakes,
  and tsunamis
* Run a volcano scenario in |project_name| using a vent location
* Run an earthquake scenario in |project_name| using a shakemap
* Run a tsunami scenario in |project_name|
* Save subsets of existing layers
* Determine the best course of action to fix a memory error
* Download building data with the OpenStreetMap Downloader


Volcanoes in Indonesia
----------------------

There are 129 active volcanoes in Indonesia, and it is valuable to know
how many people and how much infrastructure is within a certain perimeter of 
the vent. To this end |project_name| can use a vent location (point) 
as a hazard layer. The data that we will use in this section of the 
training was downloaded from the Smithsonian website.
But how can we use a point to figure out impact?
|project_name| needs your help!.

1. Go to :menuselection:`Project --> Open`. Navigate to the |project_name|
   tutorial folder and select :file:`Indonesia_volcano.qgs`. 
   Click :guilabel:`Open`.

.. image:: /static/training/socialisation/061_volcano.*
   :align: center

Select Feature and Save
.......................

2. We see that there are many volcanoes in Indonesia. Let's zoom in to one 
   volcano to analyse. Right-click on the volcanoes layer in the Layers panel and
   click :guilabel:`Open Attribute Table`.
3. Click :guilabel:`Show All Features` (circle 1), then hover your pointer to
   :guilabel:`Column Filter` (circle 2), and then select :guilabel:`NAME` 
   (circle 3).

.. image:: /static/training/socialisation/062_merapi_attribute.*
   :align: center

4. We will try to find Mount Merapi.
   Type :kbd:`merapi` in the box (1). You should uncheck :guilabel:`Case
   Sensitive` (2) to ignore whether the search is upper or lower case.
   Then click :guilabel:`Apply` (3).

.. image:: /static/training/socialisation/062_merapi_attribute2.*
   :align: center

5. A single result will remain from the search. Select it by clicking
   the number "163" on the left side of the row. The row will be highlighted
   in blue. Move or close the attribute table so you can see the map. You should 
   see that the selected point, Mount Merapi, is highlighted in yellow.

   .. note:: Make sure that the volcanoes layer is not covered by one of the
      polygon layers. It should be the uppermost item in the Layers panel.

.. image:: /static/training/socialisation/063_merapi.*
   :align: center

6. Zoom in to the highlighted point. This can be done with the Zoom In tool, by 
   dragging a small box around the point.

.. image:: /static/training/socialisation/063a_merapi2.*
   :align: center

Now that we know where Merapi is, and have checked that it is in fact in the
correct location, we are going to make a hazard layer using just this point.

7. Right-click on :guilabel:`Volcanoes` in the Layers panel and 
   click :guilabel:`Save As...`
8. Click :guilabel:`Browse` and navigate to a folder of your choice. Save
   the file as :file:`Merapi`.
9. Check the boxes next to :guilabel:`Save only selected features`
   and :guilabel:`Add saved file to map`.
10. Click :guilabel:`OK`.

.. image:: /static/training/socialisation/064_save_volcano.*
   :align: center

11. Uncheck :guilabel:`Volcanoes` in the Layers panel.

We have now hidden the original volcanoes layer, and created a new layer which
contains only Merapi. Let's examine the point.

12. Use the :guilabel:`Identify feature` tool to find more out about the
    data point.
13. Use the :guilabel:`Measure line` tool to find out how far away is the
    closest population hub (brown areas in the people layer).

.. note:: For the tools to work you must have the Merapi layer selected
   in the Layers panel.

.. image:: /static/training/socialisation/065_merapi_nokeyword.*
   :align: center

Keywords
........

With the Merapi layer selected we are reminded in the |project_name| panel
that we have not set any keywords for this new layer, so let's make some!

14. Open the :guilabel:`InaSAFE Keyword Editor`.
15. Type :kbd:`Merapi eruption` as the title.
16. As the source, enter where the data came from (in our case
    this should be :kbd:`Smithsonian Institute`).
17. Next to :guilabel:`Category`, check :guilabel:`Hazard`.
18. Next to :guilabel:`Subcategory` select :guilabel:`volcano`.
19. Click :guilabel:`OK`.

.. image:: /static/training/socialisation/066_merapi_keyword.*
   :align: center

.. note:: When you add |project_name| keywords to a layer, |project_name|
   creates a new file on your system which contains the keyword values.
   Some previous examples have not required that we add our own keywords,
   because the keyword files are included in the tutorial data.

Configure and Run |project_name|
................................

20. Confirm that |project_name| has the following in the drop-down menus:

* Merapi eruption
* people
* Need evacuation

Before we run |project_name|, we must define what the hazard zone is. Since
our hazard layer is simply a point, we will define a series of impact zones
around the volcano.

21. Click on :guilabel:`Options...` to open the impact function editor.

By default |project_name| has set three hazard areas - the first is within
a three kilometre radius around the volcano, then between three and five km,
and lastly between five and 10 km.

These hazard zones can be altered by editing the comma separated values in
the :guilabel:`Distance [km]` field. For example, if you wanted three zones
of five, five to 10, and 10 to 25, you would enter :kbd:`5,10,25`.

.. image:: /static/training/socialisation/067_volcano_config.*
   :align: center

22. Set the values as you like and click :guilabel:`OK`.

23. Click :guilabel:`Run` to process the scenario.

24. Click :guilabel:`Print...` and save accordingly.

25. Look at the results to see the number of people and material needs
    required, divided into the three (or more) hazard zones.

.. image:: /static/training/socialisation/068_merapi_results.*
   :align: center

.. note:: The needs per week are calculated cumulatively over all hazard zones.

Try it yourself
...............

It is time for you to run an |project_name| scenario yourself,
with no instructions. Make sure to print each result!

Take 10 minutes to run the following scenarios:
::

 In the event of Merapi erupting how many buildings will
 be affected within 3,5,10 km of the vent?

 ANSWER __________________________

 In the event of Merapi erupting how many people will
 be affected within 5,10,25 km of the vent?

 ANSWER __________________________

 In the event of Merapi erupting how many buildings will
 be affected within 5,10,25 km of the vent?

 ANSWER __________________________

.. note:: You can see in this example and in the previous flooding examples
   that the building layers do not contain every single building that exists.
   In Jakarta we are confident that we have the majority of schools,
   hospitals and other important structures, but around Merapi we only have a 
   selection, most of which have no attributes. To make this scenario more 
   useful, additional well-organised data collection is necessary!

Earthquake
----------

Indonesia’s location on the edges of the Pacific, Eurasian,
and Australian tectonic plates makes it not only a site of numerous volcanoes
but also frequent earthquakes.
The hazard layer we are going to use for this example has been provided by
Badan Geologi and |AIFDR|, |GoA| and describes the shaking or Modified
Mercalli Intensity (MMI) Scale.

This particular scenario is a modelled version of the 2009 Padang earthquake.

26. Go to :menuselection:`Project --> Open`. Open :file:`Padang_earthquake.qgs`.

.. image:: /static/training/socialisation/069_earthquake.*
   :align: center

27. You will see that there are five layers in the Layers panel,
    Click on each of them to read the keywords in the
    |project_name| window.

.. image:: /static/training/socialisation/070_people_scale.*
   :align: center

.. note:: Notice the difference between the first people layer and the
   other two people layers, the second one has a source of
   **AsiaPop rescaled 1km2**, the third **AsiaPop rescaled 5km2**.

28. Make sure the only **people** checked is the one where Source = AsiaPop
    (it should be checked by default).

29. In the :guilabel:`How many` drop-down menu select :guilabel:`people`.

30. Run |project_name|.

Memory usage warning
....................

At this point a warning message appears informing us that we might not have
enough system memory for this analysis.

.. image:: /static/training/socialisation/071_memory.*
   :align: center

31. Click :guilabel:`No` to cancel the operation.

In the |project_name| panel there is a suggestion on how to proceed:

"Try zooming in to a smaller area or using a raster layer with a coarser
resolution to speed up execution and reduce memory requirements.
You could also try adding more RAM to your computer."

Recall that there are another two **people** layers (raster layers) - 
the difference is the size of the pixel. We are attempting to use a layer
with 100m x 100m pixels, and most personal computers will not have enough
memory to process this. Instead, let's try to use the layer where the pixels
are 1km x 1km. If this still fails, we can still try the third **people**
layer, in which pixels are 5km x 5km! The key point to notice is that fewer
pixels require less memory.

.. image:: /static/training/socialisation/072_cellsize.*
   :align: center

32. Uncheck the current people layer, and instead check the second layer which
    is scaled to 1km.

33. Once again select :guilabel:`people` in the :guilabel:`How many` drop-down 
    menu.

34. Click on the drop-down menu under :guilabel:`Might`. This is the first
    |project_name| project where there are two impact functions that we can 
    choose from!

35. Select :guilabel:`Die or be displaced according Pager model`.

.. note:: This particular impact function was developed in Italy in
   November 2013 during a code sprint.

36. Run |project_name|.

37. Click :guilabel:`Print...` and save accordingly.

::

 How many people are estimated to die?

 ANSWER __________________________

 How many people are estimated to be displaced?

 ANSWER __________________________


38. Analyse the Action list. How is this different to the action list for
    floods or volcanoes?

::

 ANSWER __________________________


Will a building fall down in an earthquake?
...........................................

Generally it is not the earthquake that kills, but collapsing buildings that 
kill the majority of people. Hence understanding the structure of buildings
and how they may behave under certain shaking is crucial in understanding 
the impact of an earthquake. Earthquakes cover a large area, so mapping every 
structure in that area is extensive work.

In Padang the international OSM community assisted mapping,
totalling roughly 95,000 structures.

Lets find out how they are affected by the modelled Padang 2009 earthquake.

39. Uncheck :guilabel:`people` in the Layers panel and instead check
    :guilabel:`Buildings`.

40. Confirm that |project_name| has the following in the drop-down menus:

* an earthquake in Padang like in 2009
* Buildings
* Be affected

41. Run |project_name|.

.. note::
    |project_name| is designed to zoom into the extent of the impact zone,
    so when the processing completes it will automatically zoom to Padang.

42. Investigate the results, both by looking at the |project_name| results,
    and using the information tool to select a building.

43. Click :guilabel:`Print...` and save accordingly.

Tsunami
-------

The 1992 Flores earthquake occurred on December 12, 1992 on the island of
Flores in Indonesia. With a magnitude of 7.8, it was the largest and also 
the deadliest earthquake in 1992.

The next scenario is a modelled version of a Magnitude 8.1 earthquake
generating a tsunami which impacts Maumere.

44. Go to :menuselection:`Project --> Open`. Open :file:`Maumere_tsunami.qgs`.

You will see that there are two layers in the Layers panel.
Click on each of them to see the keywords in the |project_name| panel.

.. image:: /static/training/socialisation/073_tsunami.*
   :align: center

.. note::
    The |project_name| functionality for tsunamis and floods is very similar,
    but due to the force of tsunami waves, the maximum depth of 
    water that would affect people and infrastructure is shallower.

45. Confirm that |project_name| has the following in the drop-down menus:

* A tsunami in Maumere (Mw 8.1)
* people
* Need evacuation

46. Click :guilabel:`Options...` to change the water level for evacuation.
    Instead of one metre, type :kbd:`0.5` as the threshold.

47. Run |project_name|.

48. Click :guilabel:`Print...` and save accordingly.

Map Canvas Extent
.................

Let's run the same scenario again, but only on a quarter of the total
map extent. The extent of our window (the area in which we are zoomed in)
determines the area which |project_name| analyses.

49. Try it out by zooming in to a smaller area.

50. Click :guilabel:`Run` again.

.. image:: /static/training/socialisation/074_tsunami_zoom.*
   :align: center

You can see that the results are confined to the extent in which you
have zoomed the map.

.. note:: You may notice that in this example, the two layers are not perfectly
   aligned, which results in potentially inaccurate results. It can be a 
   significant problem when your population dataset does not reflect reality.
   Remember that your results are only as good as the data you use to get
   them. It is important to always quality assure your data, and avoid 
   accepting |project_name| results without analysing them critically.


OpenStreetMap Downloader
........................

Notice that there is no building layer in this project file. Let's see
how we can download OSM buildings directly from the OSM server.

51. Select the tsunami layer in the Layers panel and 
    click :guilabel:`Zoom to Layer`.

52. Click the :guilabel:`InaSAFE OpenStreetMap Downloader` button.

.. image:: /static/training/socialisation/075_osmdownloader.*
   :align: center

.. note:: The current extent of the map canvas is automatically applied
   in the Bounding box part of this window.

53. Click :guilabel:`...` to set the output directory. Navigate to a location
    to save the data on your computer. Then click :guilabel:`OK`.

54. Building and road data is downloaded from OSM, saved and opened in 
    the project.

.. image:: /static/training/socialisation/076_building_loaded.*
   :align: center

.. note:: On inspection of the buildings, we see that they don't have many
   attributes at all. This area was digitised to test this analysis, and
   field surveys still need to be conducted.

55. Confirm that |project_name| has the following in the drop-down menus:

  * A tsunami in Maumere (Mw 8.1)
  * Buildings
  * Be flooded

56. Run |project_name|.

57. Click :guilabel:`Print...` and save accordingly.

.. note:: For more information on this tool please
   visit :ref:`openstreetmap_downloader`.


:ref:`Go to next module --> <helpful-hints-and-tips>`