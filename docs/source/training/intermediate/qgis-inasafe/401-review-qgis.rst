.. image:: /static/training/intermediate/qgis-inasafe/image7.*

Module 1: Review QGIS
=====================

**Learning Objectives**

- Identify data types in QGIS
- Explain about data symbology
- Explain about map layout

Before we dive deeper into |project_name|, we will spend this Module in a
review of the QGIS techniques that we covered in Unit 2.
We will once more go over some of they key aspects of QGIS,
including adding vector and raster layers, symbolizing layers,
and using the Print Composer for layouting.
If you feel competent in all of these areas, feel free to jump ahead to the
next Module, but if you’d like a brief review, follow along!

**1. Data Types in QGIS**

As you may recall, there are two types of data that we often use in QGIS:
raster data and vector data.
Raster data is characterized as an array of data which consists of rows and
columns, like the pixels in an image.
Vector data, on the other hand, consists of discrete features made of points
and lines, and their position is defined by coordinates.

*1.1  Adding Vector Data*

Let’s add vector data to a new project.

- Open a new QGIS project. Your map and Layers list should be empty.

.. image:: /static/training/intermediate/qgis-inasafe/image8.*
   :align: center

- There are two ways to add a new vector layer to your project.
  You can navigate to :menuselection:`Layer > Add Vector Layer...` on the
  menu or you can click on the :guilabel:`Add Vector Layer` button on the
  toolbar:

.. image:: /static/training/intermediate/qgis-inasafe/image9.*
   :align: center

- If you can’t find the toolbar button, right-click the toolbars and make sure
  that the box is checked next to :guilabel:`File`
- The :guilabel:`Add vector layer` dialog looks like this:

.. image:: /static/training/intermediate/qgis-inasafe/image10.*
   :align: center

- Click on the :guilabel:`Browse` button and navigate to your exercise data.
  Go into the *qgis/Sleman/* directory and select *Jalan_Sleman_OSM, POI_Sleman*
  and *Kecamatan_Sleman*.
  You can select multiple files by holding the :kbd:`CTRL` key on your
  keyboard as you click each file.
  Click :guilabel:`Open` and then :guilabel:`Open` again.
- Your map canvas now will looks like this:

.. image:: /static/training/intermediate/qgis-inasafe/image11.*
   :align: center

Great! You’ve added some vector data to your map.
Don’t forget there are three kinds of vectors

- points,
- lines,
- and polygons.

We have just added one layer of each type.

*1.2  Adding Raster Data*

Raster data has different characteristics compared to vector data.
Raster data is composed by rows and columns which form small boxes (known as
pixels).
The ‘box’es contains information, which is usually expressed as grayscale or
color.
The information in each pixel could be the altitude of a point, the size of the
population, the area’s color, and so forth.

- There are two ways to add a new raster layer to your project.
  You can navigate to :menuselection:`Layer > Add Raster Layer...` on the
  menu or you can click on the :menuselection:`Add Vector Layer` button on
  the toolbar:

.. image:: /static/training/intermediate/qgis-inasafe/image12.*
   :align: center

- Navigate to qgis/Sleman/SRTM/ and select *SRTM_Sleman.tif*, which depicts the
  topography of the area.

.. image:: /static/training/intermediate/qgis-inasafe/image13.*
   :align: center

- Click :guilabel:`Open`.
  The raster will be added to our project as a grey-colored square.

.. image:: /static/training/intermediate/qgis-inasafe/image14.*
   :align: center

Next we will symbolize the data to make it easier to understand.

**2. Symbolizing Data**

Layer symbology is useful so that users can easily understand our maps.
It is also important to make our maps more attractive.
Your choice of a layer’s symbology is very important to deliver the right
information.

*2.1  Symbolize the Districts*

Let’s symbolize the district layer that we’ve added:

- Right click on the *Kecamatan_Sleman* layer,
  and choose :guilabel:`Properties`, or double click the layer name.
- Click on the :guilabel:`Style` tab.

.. image:: /static/training/intermediate/qgis-inasafe/image15.*
   :align: center

- Notice all the options that we have to change the appearance of this layer.
  We can change the layer’s transparency or its color, or make even more
  detailed variations by clicking on :guilabel:`Change`

.. image:: /static/training/intermediate/qgis-inasafe/image16.*
   :align: center

- We can also base the symbology on the data contained in the layer itself.
- Click on the box that says :guilabel:`Single Symbol`, and change it to
  :guilabel:`Categorized`.

.. image:: /static/training/intermediate/qgis-inasafe/image16.*
   :align: center

- Change the Color Ramp to a set of colors that you like, and then click
  :guilabel:`Classify`.
  It may look something like this (although your colors will be different):

.. image:: /static/training/intermediate/qgis-inasafe/image17.*
   :align: center

- Click :guilabel:`OK` to apply the style changes.

*2.2  Symbolize the Roads*

Next, let’s symbolize our roads layer.

- Double-click *Jalan_Sleman_OSM* in the Layers list to open the properties
  dialog.
- Click on the :guilabel:`Style` tab.
- Adjust the color as you like, or choose one of the style presets that are
  displayed at the bottom.
- Feel free to experiment, you can make changes, click :guilabel:`Apply` and
  view your changes on the map until you are satisfied.
- If you use multiple symbologies (as we covered in Unit 2), your roads may
  end up looking like this:

.. image:: /static/training/intermediate/qgis-inasafe/image18.*
   :align: center

- This isn’t ideal. To fix this, open the :guilabel:`Properties` dialog and on
  the :guilabel:`Style` tab click on the :guilabel:`Advanced` button and choose
  :guilabel:`Symbol Levels`.
  Check to box next to :guilabel:`Enable symbol levels`.

.. image:: /static/training/intermediate/qgis-inasafe/image19.*
   :align: center

- The roads will then look correct:

.. image:: /static/training/intermediate/qgis-inasafe/image20.*
   :align: center

Try editing the symbology of the *POI_Sleman_OSM* layer on your own.

*2.3  Editing Raster Symbology*

Lastly, let’s fix our raster layer so that it doesn’t look just like a grey
rectangle.

- Make sure that the raster toolbar is activated.
  It should look like this:

.. image:: /static/training/intermediate/qgis-inasafe/image21.*
   :align: center

- Select the *SRTM_Sleman* layer and click the :guilabel:`Stretch Histogram`
  button.

.. image:: /static/training/intermediate/qgis-inasafe/image22.*
   :align: center

- Your map should end up looking something like this:

.. image:: /static/training/intermediate/qgis-inasafe/image23.*
   :align: center

**3. Map Layout**

Your map is a medium to communicate information (as well as your ideas) to
your map’s reader.
You use layer symbology to convey the content of your data so that it can be
easily understood by the user.
By creating a map layout, you are going a step further in using your map as a
way to convey information.

For a full review of Map Composer, refer back to Unit 2.
For now, let’s create a basic layout with a legend.

- Start a new :guilabel:`Map Composer` window by going to
  :menuselection:`File > New Print Composer`
- Click the :guilabel:`Add new map` button and draw a box on the left side of
  the canvas.

.. image:: /static/training/intermediate/qgis-inasafe/image24.*
   :align: center

- Now click on the :guilabel:`Add new legend` button and draw a box on the
  right side of the canvas.

.. image:: /static/training/intermediate/qgis-inasafe/image25.*
   :align: center

- Your map will look similar to this:

.. image:: /static/training/intermediate/qgis-inasafe/image26.*
   :align: center

Play around a bit with the Print Composer if you like,
and refresh your memory!

We hope this was a useful refresher.
Now it’s time to get back to |project_name|!
