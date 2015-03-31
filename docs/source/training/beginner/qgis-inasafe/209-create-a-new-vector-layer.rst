.. image:: /static/training/beginner/qgis-inasafe/image7.*

..  _create-a-new-vector-layer:

Module 9: Creating Vector Layers
================================

**Learning Objectives**

- Add a raster layer for digitising
- Create new vector features (polygons, lines and points)
- Digitise new vectors  by tracing a raster layer, considering topology
- Georeference an image

Creating a map using data that already exists is only the beginning.
We have already learned how to edit and add features to OpenStreetMap using
JOSM.
In this module, we will discuss how to edit existing vector layers in QGIS,
and how to create an entirely new dataset.

1. The layer creation dialog
----------------------------

Before you can add new vector data, you need a vector dataset (a layer) to
add it to.
In our case, we’ll begin by creating a new data layer,
and then we’ll add features to it.
First, we must define our dataset.

1. Create a new project in QGIS by clicking on the
   :guilabel:`New Project` icon.

.. image:: /static/training/beginner/qgis-inasafe/image172.*
   :align: center

2. Go to :menuselection:`Layer ‣ Create Layer ‣ New Shapefile Layer`.
   You’ll be presented with the following dialog:

.. image:: /static/training/beginner/qgis-inasafe/image173.*
   :align: center

At this point we must decide what kind of dataset we want to create.
Remember that a data layer can only contain features of points, lines
or polygons - never a mix.
When we create the layer, we must define
what type of data it will contain.

Since polygons are made up of points and lines, let’s jump into polygons.
Once you’ve mastered this, creating a point or a line layer should be easy!

3. Check the box next to :guilabel:`Polygon`.

.. image:: /static/training/beginner/qgis-inasafe/image174.*
   :align: center

4. We’ll specify the Coordinate Reference System (CRS) in the next box.
   By default the box will contain the CRS of the project, which for us will
   be WGS84.
   This is a widely used and very useful CRS, so let’s stick with it!

.. image:: /static/training/beginner/qgis-inasafe/image175.*
   :align: center

5. When we create our new layer, the attribute table will only have one
   column by default - **id**.
   This attribute contains a unique id number for every feature.
   We can add additional fields to the attribute table now,
   when we create the layer.
   Let’s add a name field.

6. Type :kbd:`nama` into the box next to Name.
   The settings should match those shown here:

.. image:: /static/training/beginner/qgis-inasafe/image176.*
   :align: center

7. Click the :guilabel:`Add to attributes list` button.

Your attributes list should now look like this.

.. image:: /static/training/beginner/qgis-inasafe/image177.*
   :align: center

8. Click :guilabel:`OK`.
   A save dialog will appear.

9. Navigate to a directory of your choosing.

10. Save the new layer as :kbd:`gedung_kampus.shp`.

The new layer should appear in your Layers panel.

2. Data sources
---------------

When you create new data, it should represent objects that really
exist on the ground.
We have already learned of numerous ways to collect data using OSM
tools.
We learned about GPS to record locations, Field Papers and of course,
aerial imagery.
These are all tools that we can use to identify real-life locations and
record them in a digital data layer.

In QGIS, we can use the same types of sources to get information about the
ground.
In this example, we will once again turn to aerial imagery,
but instead of using Bing, we will use a raster image provided in the
tutorial directory.

11. Click on the :guilabel:`Add Raster Layer` button:

.. image:: /static/training/beginner/qgis-inasafe/image147.*
   :align: center

12. Navigate to :file:`/qgis/Sleman/`.

13. Select the file :file:`UGM.tif`.

14. Click :guilabel:`Open`.
    An image will load into your map.

15. Find the new entry in the Layers panel.

16. Drag it to the bottom of the list so that it is below
    the vector layer you created in the previous section.

.. image:: /static/training/beginner/qgis-inasafe/image178.*
   :align: center

17. Go to :menuselection:`Project ‣ Project Properties` and enable
    'on the fly' transformation.

18. Make sure that “WGS 84” is selected as the CRS, and click :guilabel:`OK`.

.. image:: /static/training/beginner/qgis-inasafe/image179.*
   :align: center

19. Right-click on the :guilabel:`UGM` layer and click
    :guilabel:`Zoom to Layer`.

20. Zoom in to the centre of the raster image.
    We will be digitising three areas:

.. image:: /static/training/beginner/qgis-inasafe/image180.*
   :align: center

3. Digitising
-------------

Digitising, as you might have guessed, is the art (or science) of creating
digital vector data from another source, such as a raster image.
In order to begin digitising, we must first enter edit mode.
GIS software commonly requires a separate mode for editing,
to prevent users from accidentally editing or deleting important data.
Edit mode is switched on or off individually for each layer.

Let’s enter edit mode for the :guilabel:`gedung_kampus` layer:

21. Select :guilabel:`gedung_kampus` in the Layers panel.

22. Click on the :guilabel:`Toggle Editing` button:

.. image:: /static/training/beginner/qgis-inasafe/image35.*
   :align: center

23. If you can’t find this button, ensure that the Digitising toolbar is
    enabled.
    There should be a check mark next to the
    :menuselection:`View ‣ Toolbars ‣ Digitizing` menu entry.

24. Once you are in edit mode, the digitising tools will become active:

.. image:: /static/training/beginner/qgis-inasafe/image181.*
   :align: center

From left to right on the image above, they are:

- **Toggle Editing**: activates / deactivates edit mode.
- **Save Layer Edits**: saves changes made to the layer.
- **Add Feature**: start digitising a new feature.
- **Move Feature(s)**: move an entire feature around.
- **Node Tool**: move only one part of a feature.
- **Delete Selected**: delete the selected feature (only active if a feature is
  selected).
- **Cut Features**: cut the selected feature (only active if a feature is
  selected).
- **Copy Features**: copy the selected feature (only active if a feature is
  selected).
- **Paste Features**: paste a cut or copied feature back into the map (only
  active if a feature has been cut or copied).

We want to add a new feature.

25. Click on the :guilabel:`Add Feature` button to start digitising:

.. image:: /static/training/beginner/qgis-inasafe/image182.*
   :align: center

You’ll notice that your mouse cursor becomes a crosshair.
This allows you to more accurately place the points you’ll be digitising.
Remember that even as you’re using the digitising tool,
you can zoom in and out on your map by rolling the mouse wheel,
and you can pan around by holding down the mouse wheel and dragging around
in the map.

The first feature you’ll digitise is a field (called "GSP Field"):

.. image:: /static/training/beginner/qgis-inasafe/image183.*
   :align: center

26. Start by clicking on a point somewhere along the edge of the field.

27. Place more points by clicking further along the edge,
    until the shape you’re drawing completely covers the field.
    This is very similar to drawing a polygon in JOSM.

28. To place the last point, right-click where you want it to be.
    This will finalise the feature and bring up the Attributes dialog.

29. Fill in the values as shown here:

.. image:: /static/training/beginner/qgis-inasafe/image184.*
   :align: center

30. Click :guilabel:`OK`. You’ve created a new feature!

If you make a mistake while digitising a feature,
you can always edit it later.
Simply finish digitising the feature and then follow these steps:

- Select the feature with the :guilabel:`Select Feature` tool:

.. image:: /static/training/beginner/qgis-inasafe/image185.*
   :align: center

- Then use one of these tools to edit the feature:

+----------------------------------------------------------------+--------------------------------------+-------------------------------------------------------+
|.. image:: /static/training/beginner/qgis-inasafe/image186.*    | Move feature(s) tools                | Move the entire feature(s)                            |
+----------------------------------------------------------------+--------------------------------------+-------------------------------------------------------+
|.. image:: /static/training/beginner/qgis-inasafe/image187.*    | Node tools                           | move only one point where you may have misclicked     |
+----------------------------------------------------------------+--------------------------------------+-------------------------------------------------------+
|.. image:: /static/training/beginner/qgis-inasafe/image188.*    | Delete selected                      | get rid of the feature entirely so you can try again  |
+----------------------------------------------------------------+--------------------------------------+-------------------------------------------------------+
| Go to Edit ‣ Undo or press :kbd:`Ctrl+Z` on keyboard           | Undo mistakes                        |                                                       |
+----------------------------------------------------------------+--------------------------------------+-------------------------------------------------------+

Now try it on your own:

31. Digitise the school itself and the upper field.
    Use this image to assist you:

.. image:: /static/training/beginner/qgis-inasafe/image189.*
   :align: center

32. Remember that each new feature needs to have a unique id value!

When you are finished adding features to a layer, you must save the changes
to that layer.

33. Click on the :guilabel:`Toggle Editing` button.

.. image:: /static/training/beginner/qgis-inasafe/image35.*
   :align: center

34. You will be asked to save your edits.
    Click :guilabel:`Save`.

.. image:: /static/training/beginner/qgis-inasafe/image190.*
   :align: center

Now you know how to create polygon features!
Creating points and line layers is just as easy - you simply need to
define the type of layer when you create it, and of course you can only
create points in point layers and lines in line layers.

4. Georeferencing
-----------------

In the previous section we digitised a raster image, thus creating vector
data.
This is essentially the same process as when we use Bing imagery in JOSM to
add to OSM.
In both of these cases, the imagery that we use is already
**georeferenced** - that is, it is correctly placed in its proper location.

When an image is georeferenced, it is stretched in different ways so that
each pixel in the image corresponds as closely as possible to the area it
represents on the spherical Earth.
Because it is difficult to perfectly align a flat image on a round object,
there are often small georeferencing errors, as we learned previously with
imagery offset.

What if you have a map that is not georeferenced?
What if you have a paper map given to you by a government agency?
How can you digitise it?

The first step is to turn your paper map into a digital image that you can
manipulate with your computer.
You can do this with a scanner (or possibly a digital camera),
although doing so is beyond the scope of this module.

4.1 Georeferencing an image
...........................

Now we will learn how to georeference an image in QGIS so that is correctly
located on Earth.
We will be using a map provided in the tutorial files, which looks like this:

.. image:: /static/training/beginner/qgis-inasafe/image191.*
   :align: center

35. Start a new QGIS project.
    Save your previous work if you like.

36. Go to :menuselection:`Raster ‣ Georeferencer ‣ Georeferencer`.

.. image:: /static/training/beginner/qgis-inasafe/image192.*
   :align: center

37. Click the :guilabel:`Open raster` button.

.. image:: /static/training/beginner/qgis-inasafe/image193.*
   :align: center

38. Find the file :file:`peta_krb_merapi_2002.jpg`, which is located in the the 
    :file:`qgis/Sleman/Merapi/` folder. Click :guilabel:`Open`.

39. Select :guilabel:`WGS 84` when prompted and click :guilabel:`OK`.

.. image:: /static/training/beginner/qgis-inasafe/image194.*
   :align: center

In order to georeference this image, we need to associate points on the
image, to known points on the Earth.
Such points are called ground control points (GCPs).
Luckily, this map image has latitude and longitude coordinates written on it
at every corner.
So, to georeference this image, we will create four GCPs,
one at each corner of the map, and we will turn our jpeg file into a geotiff,
a georeferenced image.

40. Zoom in to the upper left corner of the map.

.. image:: /static/training/beginner/qgis-inasafe/image195.*
   :align: center

41. Click the :guilabel:`Add point` button.

.. image:: /static/training/beginner/qgis-inasafe/image196.*
   :align: center

42. Click on the very top left point of the map, right where the
    top border of the map meets the left border.

43. A box will pop up requesting the x and y coordinates of the point you just
    clicked.
    The coordinates are written in blue on the map.
    The longitude (x coordinate) is 110° 15’ 00” E and the latitude (y
    coordinate) is 7° 29’ 47” S.
    We can enter the coordinates in the box as follows.
    Remember that south and west coordinates will be negative numbers.

.. image:: /static/training/beginner/qgis-inasafe/image197.*
   :align: center

44. Click :guilabel:`OK`.

45. You will see a red point appear showing the location of your control
    point, and an entry in the table at the bottom.

46. Repeat this process, creating ground control points at each of the four
    corners of the map.
    Remember to enter the longitude and latitude that is written at each corner.
    When you are finished, you should have four GCPs and your table will look
    like this:

.. image:: /static/training/beginner/qgis-inasafe/image198.*
   :align: center

Lastly we will adjust the settings and then create our output file.

47. Click on the :guilabel:`Transformation settings` button.

.. image:: /static/training/beginner/qgis-inasafe/image199.*
   :align: center

48. Next to :guilabel:`Transformation type` select :guilabel:`Linear`.

49. Provide a filename for the output raster.
    The file type will be :file:`.tif`.

50. Check the box next to :guilabel:`Load in QGIS when done`.
    It should look like this:

.. image:: /static/training/beginner/qgis-inasafe/image200.*
   :align: center

51. Click :guilabel:`OK` and look at the table.

.. image:: /static/training/beginner/qgis-inasafe/image201.*
   :align: center

52. Make sure the residual value is near zero to improve accuracy.

53. Now we are ready to produce the georeferenced image file.
    Click on the :guilabel:`Start georeferencing` button.

.. image:: /static/training/beginner/qgis-inasafe/image202.*
   :align: center

54. If you are asked to select the layer’s coordinate system,
    choose :guilabel:`WGS 84`.

55. Go to :menuselection:`Project ‣ Project Properties` and make sure
    that on the fly transformation is enabled.

.. image:: /static/training/beginner/qgis-inasafe/image203.*
   :align: center

56. The output file will be created and automatically added to 
    your project.
    If you hover over the image, you should see coordinates at the bottom of
    QGIS, which are close to the coordinates you entered when placing the GCPs.

.. image:: /static/training/beginner/qgis-inasafe/image204.*
   :align: center

Another way to see that the image is correctly placed, is by adding a layer
with the OpenLayers plugin.
Here we have added Bing satellite imagery, and made our new geotiff
transparent to see Merapi in the background.

.. image:: /static/training/beginner/qgis-inasafe/image205.*
   :align: center

Knowing how to georeference is important when you want to digitise from a
paper map or an image that is not already georeferenced.
Once you have georeferenced an image like this, you can apply the same
digitisation techniques that we learned previously in this module to create
vector shapefiles that can be used in QGIS and |project_name|.

:ref:`Go to next module --> <vector-analysis-for-problem-solving>`
