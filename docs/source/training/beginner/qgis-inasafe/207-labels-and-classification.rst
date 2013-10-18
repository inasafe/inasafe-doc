.. image:: /static/training/beginner/qgis-inasafe/image6.*


Module 7: Labels and Classification
===================================

**Learning Objectives**

- Explore attribute data of an object and to understand the uses of different 
  types of data
- Add labels to vector layers
- Symbolize vector data using categories

Up to now, none of the changes we have made to the map have been influenced by
the objects that are being shown. In other words, every type of vegetation looks
alike, and all the roads look alike. When looking at the map, the viewers don’t
know anything about the roads they are seeing; only that there is a road of a
certain shape in a certain area.

But the whole strength of GIS is that all the objects that are visible on the
map also have attributes. Maps in a GIS aren’t just pictures. They represent not
only objects in locations, but also information about those objects.  In this
lesson we will explore the attribute data of an object and understand what the
various data can be useful for.

If you would like to start with the examples used in this chapter, begin by
opening the QGIS project :doc:`sleman_2_6.qgs`.


**1. Attribute Data**

- Open the attribute table for the **POI_Sleman_OSM** layer by selecting it in
  the layers list and clicking on the :guilabel:`Open Attribute Table` button
  (you can also right-click on the layer and select Open Attribute Table).

.. image:: /static/training/beginner/qgis-inasafe/image114.*
   :align: center 
 
- Which field would be the most useful to use as a label?

.. image:: /static/training/beginner/qgis-inasafe/image115.*
   :align: center
 
You now know how to use the attribute table to see what is actually in the data
you’re using. A dataset will only be useful to you if it has the attributes that
you care about. If you know which attributes you need, you can quickly decide if
you’re able to use a given dataset, or if you need to look for another one that
has the required attribute data.

Different attributes are useful for different purposes. Some of them can be
represented directly as text for the map user to see.  Next we’ll see how to use
attributes as labels, so that users can see the text on your map.


**2. The Label Tool**

Labels can be added to a map to show any information about an object. Any vector
layer can have labels associated with it.  Labels rely on the attribute data of
a layer for their content.

There are several ways to add labels in QGIS, but some are better than others.
You may notice that when you open the Layer Properties window for a layer, there
is a tab called “Labels.”  While this tab is designed to put labels on your map,
it is not nearly as good as the so-called “Label Tool,” which we will learn in
this section. Before being able to access the **Label tool**, you will need to
ensure that it has been activated.

- Go to the menu item :menuselection:`View ‣ Toolbars`.
- Ensure that the Label item has a checkmark next to it. If it doesn’t, click on
  the Label item, and it will be activated.  The Label toolbar looks like this:

.. image:: /static/training/beginner/qgis-inasafe/image116.*
   :align: center
 
- Click on the :guilabel:`POI_Sleman_OSM` layer in the Layers list, so that it 
  is highlighted.
- Click on the :guilabel:`Labelling` button:

.. image:: /static/training/beginner/qgis-inasafe/image117.*
   :align: center
 
This gives you the Layer labeling settings dialog.

- Check the box next to :guilabel:`Label this layer with...`

.. image:: /static/training/beginner/qgis-inasafe/image118.*
   :align: center
 
- We must indicate which of the attribute fields we want to use for the labels.
  The **NAME** field is the mostly likely candidate for a label, so let’s select
  NAME from the list:

.. image:: /static/training/beginner/qgis-inasafe/image119.*
   :align: center
 
- Click :guilabel:`OK`.  The map should now have labels like this:

.. image:: /static/training/beginner/qgis-inasafe/image120.*
   :align: center
 
What we have so far is good, but as you can see, the labels are overlapping the
points that they are associated with. That doesn’t look very nice. The text is
also a bit larger than it needs to be. Let’s fix these problems!

- Open the :guilabel:`Label tool` again by clicking on its button as before.
- Click on the :guilabel:`ellipsis (...)` button to change the text properties:

.. image:: /static/training/beginner/qgis-inasafe/image121.*
   :align: center
 
A standard text change dialog appears, similar to those in many other programs.
Change the font to *Arial size 9*. Your labels will now look like this:

.. image:: /static/training/beginner/qgis-inasafe/image122.*
   :align: center
 
That’s the font problem solved! Now let’s look at the problem of the labels
overlapping the points, but before we do that, let’s take a look at the Buffer
option.

- Open the :guilabel:`Label tool` dialog.
- Deactivate the label buffer by clicking on the checkbox next to the text that 
  says :guilabel:`Buffer`.

.. image:: /static/training/beginner/qgis-inasafe/image123.*
   :align: center 
 
- Click :guilabel:`Apply`.

Note the effects in the map:

.. image:: /static/training/beginner/qgis-inasafe/image124.*
   :align: center
 
Now you can see why we usually need label buffers!

- Reactivate the buffers by clicking in the same checkbox as before, and then clicking Apply.

Back to the problem of the labels that overlap points.

- In the Label tool dialog, go to the :guilabel:`Advanced` tab.

.. image:: /static/training/beginner/qgis-inasafe/image125.*
   :align: center
 
- Change the value of *Label distance to 2*.

.. image:: /static/training/beginner/qgis-inasafe/image126.*
   :align: center
 
- Click :guilabel:`Apply`.  The labels no longer hover over the icons, but are “buffered” a short distance away:

.. image:: /static/training/beginner/qgis-inasafe/image127.*
   :align: center 
 

**Labeling lines**

Now that you know how labeling works, there’s an additional problem. Points and
polygons are easy to label, but what about lines? If you label them the same way
as the points, your results would look like this:

.. image:: /static/training/beginner/qgis-inasafe/image128.*
   :align: center
 
This is not very useful! To make lines behave, we’ll need to edit some options.

- Hide the **POI_Sleman_OSM** layer so that it doesn’t distract you.
- Activate labels for the **Jalan_Sleman_OSM** layer as before. (Remember to use the Label tool on the toolbar, not the one in Label Properties!)
- Set the font *Size to 9* so that you can see more labels.
- Zoom in so that the scale is *around 1:10000*.
- In the Label tool dialog’s Advanced tab, choose the following settings:

.. image:: /static/training/beginner/qgis-inasafe/image129.*
   :align: center 

The map will look somewhat like this, depending on scale:

.. image:: /static/training/beginner/qgis-inasafe/image130.*
   :align: center
 
It’s better than before, but still not ideal. For starters, some of the names
appear more than once, and that’s not always necessary. To prevent that from
happening:

- Enable the option :guilabel:`Merge connected lines` to avoid duplicate labels
  (also under the Advanced tab you may need to scroll down to see it).

Another useful function is to prevent labels being drawn for features too short
to be of notice.

- Set the value of :guilabel:`Suppress labeling of features smaller than ...` to
  *5 mm* and note the results when you click :guilabel:`Apply`.
- Try out different :guilabel:`Placement settings` as well (also under the
  Advanced tab). As we’ve seen before, the horizontal option is not a good idea
  in this case, so let’s try the curved option instead!
- Select the *curved* option under the Advanced tab of the Layer labeling
  settings dialog.

Here’s the result:
 
.. image:: /static/training/beginner/qgis-inasafe/image131.*
   :align: center

As you can see, this hides a lot of the labels that were previously visible,
because of the difficulty of making some of them follow twisting street lines
and still be legible. You can decide which of these options to use, depending on
what you think seems more useful or what looks better.

Now that you know how attributes can make a visual difference for your map, how
about using them to change the symbology of objects themselves? That’s the topic
for the next section!


**3. Classification**

Labels are a good way to communicate information such as the names of individual
places, but they can’t be used for everything. For example, let’s say that we
want to show which district each feature in our vegetation layer is in.  Using
labels, it would look like this:

.. image:: /static/training/beginner/qgis-inasafe/image132.*
   :align: center
 
Obviously this is not ideal, so we need another solution. That’s what this
lesson is about!  In this section, we will learn how to classify vector data
effectively.

**Classifying nominal data**

- Open :guilabel:`Layer Properties` for the **vegetasi** layer.
- Go to the :guilabel:`Style` tab.
- Click on the dropdown that says :guilabel:`Single Symbol`:

.. image:: /static/training/beginner/qgis-inasafe/image133.*
   :align: center
 
- Change it to *Categorized* and the interface will change:

.. image:: /static/training/beginner/qgis-inasafe/image134.*
   :align: center
 
- Change the Column to **guna_lahan** and the Color ramp to *Spectral*:

.. image:: /static/training/beginner/qgis-inasafe/image135.*
   :align: center 
 
- Click the button labeled :guilabel:`Classify`:

.. image:: /static/training/beginner/qgis-inasafe/image136.*
   :align: center 
 
- Click :guilabel:`OK`.  You’ll see something like this:

.. image:: /static/training/beginner/qgis-inasafe/image137.*
   :align: center
 
- Click the :guilabel:`arrow` (or :guilabel:`plus` sign) next to rural in the
  Layer list, you’ll see the categories explained:

.. image:: /static/training/beginner/qgis-inasafe/image138.*
   :align: center
 
So, this is useful! But it hurts your eyes to look at it, so let’s see what we
can do about that.

- Open :guilabel:`Layer Properties` and go to the :guilabel:`Style` tab again.
- Click the :guilabel:`Change` button next to Symbol.

.. image:: /static/training/beginner/qgis-inasafe/image139.*
   :align: center
 
- Remove the outline as you did in the previous chapter.  (change the border 
  style to “No Pen”)
- Click the :guilabel:`Delete all` button:

.. image:: /static/training/beginner/qgis-inasafe/image140.*
   :align: center
 
- Now click :guilabel:`Classify` again, and the new symbols will appear.

You’ll notice they don’t have outlines. This is because because you just removed
the outlines!

- Change the color for each type of vegetation by double-clicking on the colored
  block next to its name.  You can change the color for each type of vegetation
  to something that you think is more applicable, as we’ve done here:

.. image:: /static/training/beginner/qgis-inasafe/image141.*
   :align: center
 
- Notice that the category on the bottom is empty.  Select it, and click the 
  :guilabel:`Delete` button.
- When we click :guilabel:`OK` our map looks like this:

.. image:: /static/training/beginner/qgis-inasafe/image142.*
   :align: center
 
If you feel confident in your new classification skills, try to classify the
residential layer yourself.  Use darker colors to distinguish it from
vegetation.

**Ratio classification**

In the previous example, we classified the **vegetasi** layer by what is known
as nominal classification.  This type of classification is when categories are
defined based on names.  Next we will classify the **pemukiman** layer based on
the size of each feature.  Classifiying with attributes that contain only
positive numbers, sych as land area, is known as ratio classification.

- Open the :guilabel:`attribute table` for the **pemukiman** layer.  Notice the
  final column, *luas_ha*.  This attribute contains the size of the land area
  contained within that feature polygon.

.. image:: /static/training/beginner/qgis-inasafe/image143.*
   :align: center
 
- Open the :guilabel:`layer properties` for **pemukiman**. 
- Change the :guilabel:`Style type` to *"Graduated"*, and use *luas_ha* as the 
  column.

.. image:: /static/training/beginner/qgis-inasafe/image144.*
   :align: center

- Because we are categorizing with numbers this time, a color gradient will be
  useful for representing our categories.  Click on :guilabel:`Oranges` in the  
  color ramp, and then click :guilabel:`Classify`.

.. image:: /static/training/beginner/qgis-inasafe/image145.*
   :align: center
 
- Now you’ll have something like this:

.. image:: /static/training/beginner/qgis-inasafe/image146.*
   :align: center