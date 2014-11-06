.. image:: /static/training/beginner/qgis-inasafe/image7.*

..  _labels-and-classifications:

Module 7: Labels and Classification
===================================

**Learning Objectives**

- Explore attribute data of an object and understand the uses of different
  types of data
- Add labels to vector layers
- Symbolise vector data using categories

Up to now, none of the changes we have made to the map have been influenced by
the objects that are being shown. In other words, every type of vegetation looks
alike, and all the roads look alike. When looking at the map, the viewers don’t
know anything about the roads they are seeing; only that there is a road of a
certain shape in a certain area.

But the whole strength of GIS is that all the objects that are visible on the
map also have attributes. Maps in a GIS aren’t just pictures. They represent not
only objects in locations, but also information about those objects. In this
lesson we will explore the attribute data of an object and understand what the
various data can be useful for.

If you would like to start with the examples used in this module, begin by
opening the QGIS project :file:`sleman_2_6.qgs`.

1. Attribute data
-----------------

1. Open the attribute table for the :guilabel:`POI_Sleman_OSM` layer by
   selecting it in the layers list and clicking the 
   :guilabel:`Open Attribute Table` button
   (or right-click on the layer and select 
   :menuselection:`Open Attribute Table`).

.. image:: /static/training/beginner/qgis-inasafe/image40.*
   :align: center

2. Which field would be the most useful to use as a label?

.. image:: /static/training/beginner/qgis-inasafe/image117.*
   :align: center

You now know how to use the attribute table to see what is actually in the data
you’re using. A dataset will only be useful to you if it has the attributes that
you care about. If you know which attributes you need, you can quickly decide if
you’re able to use a given dataset, or if you need to look for another one that
has the required attribute data.

Different attributes are useful for different purposes. Some of them can be
represented directly as text for the map user to see. Next we’ll see how to use
attributes as labels, so that users can see the text on your map.

2. Label tool
-------------

Labels can be added to a map to show any information about an object. Any 
vector layer can have labels associated with it. Labels rely on the attribute 
data of a layer for their content.

There are several ways to add labels in QGIS, but some are better than others.
You may notice that when you open the Layer Properties window for a layer, there
is a tab called “Labels.”  While this tab is designed to put labels on your map,
it is not nearly as good as the so-called “Label Tool,” which we will learn in
this section. Before being able to access the Label tool, you will need to
ensure that it has been activated.

3. Go to the menu item :menuselection:`View ‣ Toolbars`.
4. Ensure that the Label item has a checkmark next to it. If it doesn’t, click on
   the Label item, and it will be activated. The Label toolbar looks like this:

.. image:: /static/training/beginner/qgis-inasafe/image118.*
   :align: center

5. Click on the :guilabel:`POI_Sleman_OSM` layer in the Layers list, so that it
   is highlighted.

6. Click on the :guilabel:`Layer Labeling Options` button:

.. image:: /static/training/beginner/qgis-inasafe/image119.*
   :align: center

This gives you the Layer labeling settings dialog.

7. Check the box next to :guilabel:`Label this layer with...`

.. image:: /static/training/beginner/qgis-inasafe/image120.*
   :align: center

8. We must indicate which of the attribute fields we want to use for the labels.
   The **NAME** field is the mostly likely candidate for a label, so select
   NAME from the dropdown box:

.. image:: /static/training/beginner/qgis-inasafe/image121.*
   :align: center

9. Click :guilabel:`OK`. The map should now have labels like this:

.. image:: /static/training/beginner/qgis-inasafe/image122.*
   :align: center

This is good, but as you can see, the labels are overlapping the
points that they are associated with. That doesn’t look very nice. The text is
also a bit larger than it needs to be. Let’s fix these problems!

10. Open the :guilabel:`Layer Labeling Options` again by clicking on its button.

11. Click on the :guilabel:`Text` tab to change the text properties:

.. image:: /static/training/beginner/qgis-inasafe/image123.*
   :align: center

12. A standard text change dialog appears, similar to those in many other
    programs. Change the font to :kbd:`Arial` and size to :kbd:`9`. 

13. Now click on the :guilabel:`Buffer` tab to add a buffer space around the 
    text. Check the box labelled :guilabel:`Draw text buffer`.

.. image:: /static/training/beginner/qgis-inasafe/image124.*
   :align: center

Your labels will look like this:

.. image:: /static/training/beginner/qgis-inasafe/image125.*
   :align: center

That’s the font problem solved! Now let’s look at the problem of the labels
overlapping the points.

14. In the Label window dialog, go to the :guilabel:`Placement` tab.

15. Change the value of :guilabel:`Distance` to :kbd:`2`.

.. image:: /static/training/beginner/qgis-inasafe/image126.*
   :align: center

16. Click :guilabel:`OK`. The labels no longer hover over the icons,
    but are “buffered” a short distance away:

.. image:: /static/training/beginner/qgis-inasafe/image127.*
   :align: center

Labeling lines
..............

Now that you know how labeling works, there’s an additional problem. Points and
polygons are easy to label, but what about lines? If you label them the same way
as the points, your results would look like this:

.. image:: /static/training/beginner/qgis-inasafe/image128.*
   :align: center

This is not very useful! To make lines behave, we’ll need to edit some options.

17. Hide the :guilabel:`POI_Sleman_OSM` layer so that it doesn’t distract you.

18. Activate labels for the :guilabel:`Jalan_Sleman_OSM` layer as before. 
    (Remember to use the Label tool on the toolbar, not the one in Label 
    Properties!)

19. Set the font size to :kbd:`9` so that you can see more labels.

20. Zoom in so that the scale is near 1:10000.

21. On the Label window’s :guilabel:`Placement` tab, choose the following 
    settings:

.. image:: /static/training/beginner/qgis-inasafe/image129.*
   :align: center

The map will look somewhat like this, depending on scale:

.. image:: /static/training/beginner/qgis-inasafe/image130.*
   :align: center

It’s better than before, but still not ideal. For starters, some of the names
appear more than once, and that’s not always necessary. To prevent that from
happening:

22. Enable the option :guilabel:`Merge connected lines to avoid duplicate labels`
    which is located on the :guilabel:`Rendering` tab.

Another useful function is to prevent labels being drawn for features too short
to be of notice.

23. Also on the :guilabel:`Rendering` tab, set the value of 
    :guilabel:`Suppress labeling of features smaller than ...` to
    :kbd:`5.0 mm`. Observe the results after you click :guilabel:`Apply`.

24. Try out different settings on the :guilabel:`Placement` tab as well.
    As we’ve seen before, the horizontal option is not a good idea for roads
    in this case, so let’s try the curved option instead!

25. Select :guilabel:`Curved` under :guilabel:`Placement`. Here’s the result:

.. image:: /static/training/beginner/qgis-inasafe/image131.*
   :align: center

As you can see, this hides a lot of the labels that were previously visible,
because of the difficulty of making some of them follow twisting street lines
and still be legible. You can decide which of these options to use, depending on
what you think seems more useful or what looks better.

Now that you know how attributes can make a visual difference for your map, how
about using them to change the symbology of objects themselves? That’s the topic
for the next section!

3. Classification
-----------------

Labels are a good way to communicate information such as the names of individual
places, but they can’t be used for everything. For example, let’s say that we
want to show which district each feature in our vegetation layer is in. Using
labels, it would look like this:

.. image:: /static/training/beginner/qgis-inasafe/image132.*
   :align: center

Obviously this is not ideal, so we need another solution. That’s what this
lesson is about! In this section, we will learn how to classify vector data
effectively.

3.1 Classifying nominal data
............................

26. Open Layer Properties for the :guilabel:`vegetasi` layer.

27. Go to the :guilabel:`Style` tab.

28. Click on the dropdown that says :guilabel:`Single Symbol`.

.. image:: /static/training/beginner/qgis-inasafe/image133.*
   :align: center

29. Change it to :guilabel:`Categorized`. The interface will change:

.. image:: /static/training/beginner/qgis-inasafe/image134.*
   :align: center

30. Change the :guilabel:`Column` field to :guilabel:`guna_lahan` and the 
    :guilabel:`Color ramp` to :guilabel:`Spectral`:

.. image:: /static/training/beginner/qgis-inasafe/image135.*
   :align: center

31. Click the button labelled :guilabel:`Classify`:

.. image:: /static/training/beginner/qgis-inasafe/image136.*
   :align: center

32. Click :guilabel:`OK`. You’ll see something like this:

.. image:: /static/training/beginner/qgis-inasafe/image137.*
   :align: center

33. In the Layers panel, click the plus sign next to the :guilabel:`vegetasi`
    layer. This will show more information about the layer classification
    and styles.

.. image:: /static/training/beginner/qgis-inasafe/image138.*
   :align: center

So, this is useful! But it hurts your eyes to look at it, so let’s see what we
can do about that.

34. Open :guilabel:`Layer Properties` and go to the :guilabel:`Style` tab again.

35. Click the :guilabel:`Change` button next to :guilabel:`Symbol`.

.. image:: /static/training/beginner/qgis-inasafe/image139.*
   :align: center

36. Remove the outline as you did in the previous module (change the border
    style to “No Pen”).

37. Click the :guilabel:`Delete all` button.

.. image:: /static/training/beginner/qgis-inasafe/image140.*
   :align: center

38. Now click :guilabel:`Classify` again, and new symbols will appear.

39. Change the colour for each type of vegetation by double-clicking on the 
    coloured block next to its name. You can change the colour for each type 
    of vegetation to something that you think is more applicable, as we’ve 
    done here:

.. image:: /static/training/beginner/qgis-inasafe/image141.*
   :align: center

40. Notice that the category on the bottom is empty. Select it, and click the
    :guilabel:`Delete` button.

41. When we click :guilabel:`OK` our map looks like this:

.. image:: /static/training/beginner/qgis-inasafe/image142.*
   :align: center

If you feel confident in your new classification skills, try to classify the
residential layer yourself. Use darker colours to distinguish it from
vegetation.

3.2 Ratio classification
........................

In the previous example, we classified the :guilabel:`vegetasi` layer by what 
is known as nominal classification. This type of classification is when 
categories are defined based on names. Next we will classify the 
:guilabel:`pemukiman` layer based on the size of each feature. Classifiying 
with attributes that contain only positive numbers, such as land area, is 
known as ratio classification.

42. Open the Attribute Table for the :guilabel:`pemukiman` layer. Notice the
    final column, :guilabel:`luas_ha`. This attribute contains the size of the 
    land area contained within that feature polygon.

.. image:: /static/training/beginner/qgis-inasafe/image143.*
   :align: center

43. Open the Layer Properties for :guilabel:`pemukiman`.

44. Change the style type to :guilabel:`Graduated` and use :guilabel:`luas_ha` 
    as the :guilabel:`Column`.

.. image:: /static/training/beginner/qgis-inasafe/image144.*
   :align: center

45. Because we are categorising with numbers this time, a colour gradient will be
    useful for representing our categories. Click on :guilabel:`Oranges` next
    to :guilabel:`Color ramp` and then click :guilabel:`Classify`.

.. image:: /static/training/beginner/qgis-inasafe/image145.*
   :align: center

Now you’ll have something like this:

.. image:: /static/training/beginner/qgis-inasafe/image146.*
   :align: center


:ref:`Go to next module --> <working-with-raster-data>`