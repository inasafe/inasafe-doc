.. image:: /static/training/beginner/qgis-inasafe/image7.*

..  _working-with-vector-data:

Module 6: Working with Vector Data ==================================

**Learning Objectives

- Understand vector data Identify attributes of vector data Add vector layers
- Symbolise vector layers

In this module, we will learn what is meant by vector data. We will practise
adding it to our QGIS projects, and we will learn how to style the data in
different ways.


1. Vector data --------------

Vector data is the most common type of data found in GIS. A vector is
essentially something made up of single points, or lines connecting those
points. In other words, points, lines and polygons are all vectors (curved lines
are vectors too, but we won’t worry about that for now). We are already quite
familiar with vector data because in the previous unit, we used JOSM to create
it!

Each object in a vector dataset is referred to as a feature. In JOSM we often
refer to them as objects, but in traditional GIS terminology they are features.
A polygon that represents a building is a feature, as is a line that represents
a river. Each feature has a geographic location and is attached to other data
that describe the feature.

One important thing to note is that QGIS layers can only contain one type of
feature. That is, one layer can’t contain both point features and line features,
because they are different types of data. Hence if you have a file that contains
school polygons and another file that contains school points, you would add them
as two separate layers.

Almost always, polygon layers will be at the bottom of your layers list, line
layers in the middle and point layers at the top. You don’t generally want your
polygons overlapping your lines and points.

2. Attribute data -----------------

It’s important to know that the data you will be working with does not only
represent where objects are in space, but also tells you what those objects are.

1. Open the project :file:`sleman_2_5.qgs`. This is the same project that you
worked with previously.

In the project we see the position of Sleman districts, the railway, and some
roads, but we can’t see all of the data contained in those layers.

2. Select :guilabel:`Jalan_Sleman_OSM` in the Layers panel.

.. image:: /static/training/beginner/qgis-inasafe/image72.*    :align: center

3. Click the :guilabel:`Open Attribute Table` button:

.. image:: /static/training/beginner/qgis-inasafe/image40.*    :align: center

You will see a table with more data about the streets layer. This extra data is
called **attribute data**. The lines that you can see on your map which
represent the location of the  streets is called **spatial data**. Remember in
JOSM there was the same division. The points, lines and shapes we draw tell us
**where**, but the tags, or attributes, tell us **what**. These definitions are
commonly used in GIS, so it’s essential to remember them!

.. image:: /static/training/beginner/qgis-inasafe/image73.*    :align: center

4. Take a look at the attribute table.    Each row in the table is associated
with one feature in the streets layer.    Each column contains one of the
attributes.    If you select other layers and click on the :guilabel:`Open
Attribute    Table` button, you’ll see different tables.

5. Close the attribute table.

3. Adding vector data ---------------------

3.1 Shapefiles ..............

You’ve already added vector data to a project in the form of a shapefile. As we
mentioned previously, a shapefile is a commonly used geographic file format. It
can easily be converted into other formats, and most GIS software can read this
type of file. You may notice when adding a shapefile that there are numerous
files in your shapefile directory with the same name. This is because a
shapefile actually relies on a collection of several other files to store the
data and keep various settings. When you add a shapefile to your project, you
should always add the one that ends in :file:`.shp`, but the rest of the files
are important too!

6. Do you remember how to add a shapefile to a project?    Try adding the layer
:file:`POI_Sleman_OSM`, from the shapefile located in    the tutorial directory.
If you don’t remember how to add a new vector layer,    refer to the
instructions :ref:`module 3 <adding-vector-layer>`.

Your project should look like this after the new layer has been added:

.. image:: /static/training/beginner/qgis-inasafe/image74.*    :align: center

3.2 Databases .............

Shapefiles (and other types of files) are one way to store geographic data. You
can also load a vector layer into QGIS from a database. You may already be
familiar with Database Management Systems (DBMS) such as Microsoft Access. GIS
applications also make use of databases to store geographic data. Databases can
be hosted and used locally on your computer, or could be shared between users
over a network or the internet.

7. Let’s try adding a layer from a database.    Click the :guilabel:`Add
SpatiaLite Layer` button.    If you can’t find it, right-click on the toolbar
and make sure that the    :guilabel:`Manage Layers` toolbar is enabled.

.. image:: /static/training/beginner/qgis-inasafe/image75.*    :align: center

8. You will see a dialog box.    Click :guilabel:`New`.

.. image:: /static/training/beginner/qgis-inasafe/image76.*    :align: center

9. Navigate to the :file:`qgis_data/Sleman/` folder and find
:file:`guna_lahan.db`.    Select the file and click :guilabel:`Open`.

10. Now in the original dialog box, notice that the drop-down button
contains *“guna_lahan.db @ ...”*, followed by the path of the database file
on your computer.

11. Click :guilabel:`Connect`.     You will see the following in the box:

.. image:: /static/training/beginner/qgis-inasafe/image77.*    :align: center

12. This database actually has three different layers available, all saved
in the database.     Click on the first layer to select it, then hold
:kbd:`SHIFT` and click the     last layer to select them all.

13. Click :guilabel:`Add`.     This will add all three layers to our project.

.. note:: Remember frequently to save your map!    Your QGIS project file does
not save the data (data is saved in a    shapefile or a database), but it does
remember the layers that you have    added to the project, their order and any
settings that you adjust.

14. The layers you have just added are all polygon layers, so you will want
to drag them down below the line and point layers.     If you have a checkbox
beneath your layers list that reads     :guilabel:`Control rendering order`, go
ahead and check it.

15. Let’s remove a couple of layers to make it easier to deal with our data.
Right-click on the :guilabel:`railway` and :guilabel:`district` layers and
click :guilabel:`Remove`.     Then order your layers like this:

.. image:: /static/training/beginner/qgis-inasafe/image78.*    :align: center

4. Symbology ------------

The symbology of a layer is its visual appearance on the map. One of the basic
strengths of GIS is that you have a dynamic visual representation of the data
you are working with. Therefore, the visual appearance of the map (which depends
on the symbology of the individual layers) is very important. The end user of
the maps you produce will need to be able to easily see what the map represents.
Equally as important, you need to be able to explore the data as you’re working
with it, and good symbology helps a lot.

In other words, having proper symbology is not a luxury or just nice to have. In
fact, it’s essential for you to use a GIS properly and produce maps and
information that people will understand and be able to use.

4.1 Changing colours ....................

To change a layer’s symbology, we will open its properties. Let’s begin by
changing the colour of the :guilabel:`pemukiman` layer.

16. Right-click on the :guilabel:`pemukiman` layer in the Layers panel.

17. Select :guilabel:`Properties` in the menu that appears.

.. note:: By default you can also access the Properties menu by double-clicking
on the name of the layer.

18. In the Properties window select the :guilabel:`Style` tab.

.. image:: /static/training/beginner/qgis-inasafe/image79.*    :align: center

19. Click the :guilabel:`Color` button to change the colour.

.. image:: /static/training/beginner/qgis-inasafe/image80.*    :align: center

20. A standard colour dialog will appear.     Choose a pink colour and click
:guilabel:`OK`.

.. image:: /static/training/beginner/qgis-inasafe/image81.*    :align: center
   
21. If you success to change the colour of :guilabel:`pemukiman`layer then you
can try to   change colour of :guilabel:`vegetasi` layer and
:guilabel:`tubuh_air` layer too.   You can use green colour for
:guilabel:`vegetasi` layer and blue colour for :guilabel:`tubuh_air` layer

22. Click :guilabel:`OK` again in the Layer Properties window, and you will
see the colour change being applied to the layer.

.. image:: /static/training/beginner/qgis-inasafe/image82.*    :align: center

4.2 Changing symbol structure .............................

There’s more to a layer’s symbology than just its colour. Next we also want to
eliminate the lines between the different types of vegetation so as to make the
map less visually cluttered.

22. Open the :guilabel:`Layer Properties` window for the :guilabel:`vegetasi`
layer. Under the :guilabel:`Style` tab, you will see the same kind of
dialog as before.     This time, however, we will do more than just change the
colour.

23. Click on :guilabel:`Simple Fill` under :guilabel:`Symbol layers`.     The
Symbol layer dialog will appear on the right side of the panel.

.. image:: /static/training/beginner/qgis-inasafe/image83.*    :align: center

24. You can change the colour inside the polygons in the layer by clicking the
button      next to the :guilabel:`Fill` label:

.. image:: /static/training/beginner/qgis-inasafe/image84.*    :align: center

25. In the dialog that appears, choose a new colour (one that suits
vegetation).

26. Click :guilabel:`OK`.

Next, we want to get rid of the lines between all the farms.

27. Click on the :guilabel:`Border style` drop-down box.     At the moment, it
should be showing a short line and the words     :guilabel:`Solid Line`.

28. Change this to :guilabel:`No Pen`.

.. image:: /static/training/beginner/qgis-inasafe/image85.*    :align: center

29. Click :guilabel:`OK`, and then :guilabel:`OK` again.
    
30. Try changing the symbology of the :guilabel:`pemukiman` layer so that it
also does not have outlines. Now when we look at our map, the
:guilabel:`vegetasi` and :guilabel:`pemukiman` layer   will have new colours and
no lines between polygons.
	
.. image:: /static/training/beginner/qgis-inasafe/image86.*    :align: center

4.3 Scale-based visibility ..........................

Sometimes you will find that one of your layers is not suitable for a given
scale. For example, if you have a layer which shows the earth’s continents but
not with very much detail, the continent lines may not be very accurate when you
are zoomed in very far.

.. note::  Scale is a reference to how your map references what is actually on
the ground in terms of size.    Scale is usually given in terms like 1:10000,
which means that one    centimetre of length on your map is equal to 10000
centimetres in the real    world.    When you zoom in or out on a map, the scale
changes,    as you can see in the status bar at the bottom of QGIS.

In our case, we may decide to hide our streets layer when we are zoomed out very
far (a small scale). For example, the streets layer is not very useful when we
are zoomed out far and it looks like a blob.

Let’s enable scale-based rendering:

31. Open the :guilabel:`Layer Properties` dialog for the
:guilabel:`Jalan_Sleman_OSM` layer.

32. Click the :guilabel:`General` tab.

.. image:: /static/training/beginner/qgis-inasafe/image87.*    :align: center

33. Enable scale-based rendering by clicking on the checkbox
:guilabel:`Scale dependent visibility` then change the value in
:guilabel:`Maximum` to 1:10 and :guilabel:`Minimum` to 1:100000.

.. image:: /static/training/beginner/qgis-inasafe/image88.*    :align: center

34. Click :guilabel:`OK`.

35. Look at your map and see what happens when you zoom in and out.     The
streets layer should appear when you are at a large scale and      disappear at
small scales.

.. note::  You can use your mouse wheel to zoom in increments.    Alternatively,
use the zoom tools to draw a box and zoom to it:

.. image:: /static/training/beginner/qgis-inasafe/image89.*    :align: center

4.4 Adding symbol layers ........................

Now that we know how to change simple symbology for layers, the next step is to
create more complex symbology. QGIS allows us to do this using symbol layers.

36. Open the :guilabel:`vegetasi` layer’s Symbol properties dialog as before.

37. In this example, the current symbology has no outline (i.e., it uses the
:guilabel:`No Pen` border style).

.. image:: /static/training/beginner/qgis-inasafe/image90.*    :align: center

38. Select :guilabel:`Fill` and Click the :guilabel:`+` button on the left.

.. image:: /static/training/beginner/qgis-inasafe/image91.*    :align: center

39. Another symbol layer will be added to the list:

.. image:: /static/training/beginner/qgis-inasafe/image92.*    :align: center

.. note:: The symbol layers may appear different in colour, but don't worry,
we’re going to customise it anyway.

Now this layer has two different symbologies. In other words, both the blue
colour AND the green colour will be drawn. However, the blue colour will be
drawn above the green, and since it is a solid colour, it will completely hide
the green colour. So let’s change it.

.. note:: It’s important not to get confused between a map layer and a symbol
layer. A map layer is a vector (or raster) that has been loaded into the
map. A symbol layer is only the symbology used to represent a map layer.    This
course will usually refer to a map layer as just a layer, but a symbol     layer
will always be called a symbol layer, to prevent confusion.

40. Set the :guilabel:`Border style` to :guilabel:`No Pen` as before.

41. Change the :guilabel:`Fill style` to something other than :guilabel:`Solid`
or      :guilabel:`No brush`. For example, :guilabel:`Dense 7`:

.. image:: /static/training/beginner/qgis-inasafe/image93.*    :align: center

42. Click :guilabel:`OK` and then :guilabel:`OK` and take a look at your
layer's new symbology.

.. image:: /static/training/beginner/qgis-inasafe/image94.*    :align: center

43. Now try it yourself. Add an additional symbology layer to      the
:guilabel:`Jalan_Sleman_OSM` layer.

    - Give the thickness of the original layer a value of 2.0 Give the thickness
    - of the new symbology layer a value of 1.0

    This will result in your roads looking something like this:

.. image:: /static/training/beginner/qgis-inasafe/image95.*    :align: center

44. Our streets now appear to have an outline, but they seem disjointed, as if
they don’t connect with each other.     To prevent this from happening, we can
enable symbol levels,     which will control the order in which the different
symbol layers are     rendered.

45. In the Layer Properties dialog, go to     :menuselection:`Advanced ‣ Symbol
levels...`:

.. image:: /static/training/beginner/qgis-inasafe/image96.*    :align: center

46. The Symbol Levels dialog will appear.     Check the box next to
:guilabel:`Enable symbol levels`.

.. image:: /static/training/beginner/qgis-inasafe/image97.*    :align: center

Your map will now look like this:

.. image:: /static/training/beginner/qgis-inasafe/image98.*    :align: center

47. When you’re done, you can save the symbol itself in QGIS so that you won’t
have to do all this work again if you want to use the symbol in the     future.
Save your current symbol style by clicking the      :guilabel:`Save Style`
button under the :guilabel:`Style` tab of the Layer      Properties dialog and
choose :guilabel:`QGIS Layer Style File`

48. Give your style file a name and save.     You can load a previously saved
style at any time by clicking the     :guilabel:`Load Style ...` button.
Before you change a style, keep in mind that any unsaved style you are
replacing will be lost.

.. image:: /static/training/beginner/qgis-inasafe/image99.*    :align: center
   
49. Try to change the appearance of the streets layer again, so that the roads
are dark grey or black, with a thin yellow outline and a dashed white line
running in the middle.

.. image:: /static/training/beginner/qgis-inasafe/image100.*    :align: center

4.5 Classified symbology ........................

Symbol levels also work for classified layers (i.e., layers having multiple
symbols). We will cover classification in the next module, but you can see how
it works here with roads. By classifying various streets according to their
type, we can give them different symbologies and they will still appear to flow
into each other.

.. image:: /static/training/beginner/qgis-inasafe/image101.*    :align: center

4.6 Symbol layer types ......................

In addition to setting fill colours and using predefined patterns, you can use
different symbol layer types entirely. The only type we’ve been using up to now
was the Simple Fill type. The more advanced symbol layer types allow you to
customise your symbols even further.

Each type of vector (point, line and polygon) has its own set of symbol layer
types.

4.6.1 Vector points ^^^^^^^^^^^^^^^^^^^

50. Open the symbol properties for the :guilabel:`POI_Sleman_OSM` layer:

.. image:: /static/training/beginner/qgis-inasafe/image102.*    :align: center

51. Access the various symbol layer types by clicking a symbol layer (1)
then clicking the drop-down box in the upper right corner (2)

.. image:: /static/training/beginner/qgis-inasafe/image103.*    :align: center

52. Investigate the various options available to you, and choose a symbol layer
type other than the default Simple Marker.

53. If in doubt, use an :guilabel:`Ellipse Marker`.

54. Choose a white outline and dark fill, with a symbol width of 2.00 and
symbol height of 4.00.

.. image:: /static/training/beginner/qgis-inasafe/image104.*    :align: center

.. image:: /static/training/beginner/qgis-inasafe/image104a.*    :align: center
   
4.6.2 Vector lines ^^^^^^^^^^^^^^^^^^

55. To see the various symbology options for vector lines, open the Layer
Properties for the :guilabel:`Jalan_Sleman_OSM` layer, and click on the drop-
down box of :guilabel:`Symbol Layer Type` :

.. image:: /static/training/beginner/qgis-inasafe/image106.*    :align: center

56. Click :guilabel:`Marker line`.

.. image:: /static/training/beginner/qgis-inasafe/image107.*    :align: center

57. Click :guilabel:`Simple Marker` in the Symbol layers panel (1).

.. image:: /static/training/beginner/qgis-inasafe/image108.*    :align: center

58. Change the symbol properties to match this dialog:

.. image:: /static/training/beginner/qgis-inasafe/image109.*    :align: center

59. Click on :guilabel:`Marker line` in the Symbol layers panel,     and change
the interval to 2.00:

.. image:: /static/training/beginner/qgis-inasafe/image110.*    :align: center

Once you have applied the style, take a look at its results on the map. As you
can see, these symbols change direction along with the road but don’t always
bend along with it. This is useful for some purposes, but not for others. If you
prefer, you can change the symbol layer in question back to the way it was
before.

.. image:: /static/training/beginner/qgis-inasafe/image110a.*    :align: center

4.6.3 Vector polygons ^^^^^^^^^^^^^^^^^^^^^

60. Now let’s change the symbol layer type for the :guilabel:`pemukiman` layer.
Take a look at the drop-down menu as you’ve done for the point and line
layers, and see what the various options can do.

.. image:: /static/training/beginner/qgis-inasafe/image113.*    :align: center

61. Feel free to play around with the various options.     We will use the
:guilabel:`Point pattern fill` with the following settings:

.. image:: /static/training/beginner/qgis-inasafe/image114.*    :align: center

62. Add a new symbol layer with a normal Simple fill.

63. Make it grey with no outlines.

64. Move it underneath the point pattern symbol layer with the
:guilabel:`Move down` button:

.. image:: /static/training/beginner/qgis-inasafe/image115.*    :align: center

The symbol properties should look like this:

.. image:: /static/training/beginner/qgis-inasafe/image116.*    :align: center

As a result, you have a textured symbol for the urban layer, with the added
benefit that you can change the size, shape and distance of the individual dots
that make up the texture.


:ref`Go to next module --> <labels-and-classifications>`
