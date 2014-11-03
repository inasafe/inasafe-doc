.. image:: /static/training/intermediate/qgis-inasafe/image7.*

..  _review-qgis:

Module 1: Review QGIS
=====================

**Learning Objectives**

- Identify data types in QGIS
- Understand symbology
- Understand map layout

Before we dive deeper into |project_name|, we will review
review the QGIS techniques that we covered in Unit 2.
We will once more go over some of they key aspects of QGIS,
including adding vector and raster layers, symbolising layers,
and using the Print Composer.
If you feel competent in all of these areas, feel free to jump ahead to the
:ref:`next module <preparing-data-and-keywords-for-inasafe>`, 
but otherwise follow along for a brief review!

1. Data types in QGIS
---------------------

As you may recall, there are two types of data that we often use in QGIS:
raster and vector data.
Raster data is characterised as an array of data which consists of rows and
columns, like the pixels in an image.
Vector data, on the other hand, consists of discrete features made of points
and lines, and their position is defined by coordinates.

1.1 Adding vector data
......................

Let’s add vector data to a new project.

1. Open a new QGIS project. Your map and Layers panel should be empty.

.. image:: /static/training/intermediate/qgis-inasafe/image8.*
   :align: center

2. There are two ways to add a new vector layer to your project.
   Navigate to :menuselection:`Layer ‣ Add Vector Layer...` on the
   menu or click on the :guilabel:`Add Vector Layer` button on the
   toolbar:

.. image:: /static/training/intermediate/qgis-inasafe/image9.*
   :align: center

3. If you can’t find the toolbar button, right-click the toolbars and make sure
   that the box is checked next to :guilabel:`File`.

The :guilabel:`Add vector layer` dialog looks like this:

.. image:: /static/training/intermediate/qgis-inasafe/image10.*
   :align: center

4. Click on the :guilabel:`Browse` button and navigate to your exercise data.
   Go into the :file:`qgis/Sleman/` directory and select 
   :file:`Jalan_Sleman_OSM`, :file:`POI_Sleman` and
   :file:`Kecamatan_Sleman`.
   Select multiple files by holding the :kbd:`CTRL` key on your
   keyboard as you click each file.
   Click :guilabel:`Open` and then :guilabel:`Open` again.

Your map canvas will now look like this:

.. image:: /static/training/intermediate/qgis-inasafe/image11.*
   :align: center

Great! You’ve added some vector data to your map.

.. note:: Remember that there are three kinds of vectors:
     
     - points,
     - lines,
     - and polygons

   We have just added one layer of each type.


1.2  Adding Raster Data
.......................

Raster data has different characteristics than vector data.
Raster data is composed by rows and columns which form small boxes (known as
pixels).
The pixels contain information, which is usually expressed as greyscale or
colour.
The information in each pixel could be the altitude of a point, the size of the
population, the area’s colour or another value.

5. There are two ways to add a new raster layer to your project.
   Navigate to :menuselection:`Layer ‣ Add Raster Layer...` on the
   menu or click on the :guilabel:`Add Raster Layer` button on the
   toolbar:

.. image:: /static/training/intermediate/qgis-inasafe/image12.*
   :align: center

6. Navigate to :file:`qgis/Sleman/SRTM/` and select :file:`SRTM_Sleman.tif`, 
   which depicts the topography of the area.

.. image:: /static/training/intermediate/qgis-inasafe/image13.*
   :align: center

7. Click :guilabel:`Open`.
   The raster will be added to our project.

.. image:: /static/training/intermediate/qgis-inasafe/image14.*
   :align: center

Next we will symbolise the data to make it easier to understand.

2. Symbolising data
-------------------

Layer symbology is useful so that users can easily understand our maps.
It is also important to make our maps more attractive.
Your choice of a layer’s symbology is very important to deliver the right
information.

2.1  Symbolise the districts
............................

Let’s symbolise the district layer that we’ve added:

8. Right-click on the :guilabel:`Kecamatan_Sleman` layer,
   and click :guilabel:`Properties`, or double click the layer name.

9. Click on the :guilabel:`Style` tab.

.. image:: /static/training/intermediate/qgis-inasafe/image15.*
   :align: center

Notice all the options that we have to change the appearance of this layer.
We can change the layer’s transparency or its colour, or make even more
detailed variations by clicking on :guilabel:`Change`.

.. image:: /static/training/intermediate/qgis-inasafe/image16.*
   :align: center

We can also base the symbology on the data contained in the layer itself.

10. Click on the box that says :guilabel:`Single Symbol`, and change it to
    :guilabel:`Categorized`.

.. image:: /static/training/intermediate/qgis-inasafe/image16.*
   :align: center

11. Change the Color Ramp to a set of colours that you like, and then click
    :guilabel:`Classify`.
    It may look something like this (although your colours will be different):

.. image:: /static/training/intermediate/qgis-inasafe/image17.*
   :align: center

12. Click :guilabel:`OK` to apply the style changes.

2.2  Symbolise the roads
........................

Next, let’s symbolise our roads layer.

13. Double-click :guilabel:`Jalan_Sleman_OSM` in the Layers panel to open the 
    Poperties window.

14. Click on the :guilabel:`Style` tab.

15. Adjust the colour as you like, or choose one of the style presets that are
    displayed at the bottom.

16. Feel free to experiment. As you make changes, click :guilabel:`Apply` to
    view your changes on the map.

If you use multiple symbologies (as we covered in Unit 2), your roads may
end up looking like this:

.. image:: /static/training/intermediate/qgis-inasafe/image18.*
   :align: center

18. This isn’t ideal. To fix this, open the Properties window and on
    the :guilabel:`Style` tab click on the :guilabel:`Advanced` button and choose
    :guilabel:`Symbol Levels`.
    Check to box next to :guilabel:`Enable symbol levels`.

.. image:: /static/training/intermediate/qgis-inasafe/image19.*
   :align: center

The roads will then look correct:

.. image:: /static/training/intermediate/qgis-inasafe/image20.*
   :align: center

Try editing the symbology of the :guilabel:`POI_Sleman_OSM` layer on your own.

Your map should end up looking something like this:

.. image:: /static/training/intermediate/qgis-inasafe/image23.*
   :align: center

3. Map layout
-------------

Your map is a medium to communicate information (as well as your ideas).
Layer symbology is used to convey the content of your data so that it can be
easily understood by the user.
By creating a map layout, you are going a step further in using your map as a
way to convey information.

For a full review of Map Composer, refer back to 
:ref:`Unit 2 <using-map-composer>`.
For now, let’s create a basic layout with a legend.

21. Start a new :guilabel:`Map Composer` window by going to
    :menuselection:`File ‣ New Print Composer`.

22. Click the :guilabel:`Add new map` button and draw a box on the left side of
    the canvas.

.. image:: /static/training/intermediate/qgis-inasafe/image24.*
   :align: center

23. Now click on the :guilabel:`Add new legend` button and draw a box on the
    right side of the canvas.

.. image:: /static/training/intermediate/qgis-inasafe/image25.*
   :align: center

Your map will look similar to this:

.. image:: /static/training/intermediate/qgis-inasafe/image26.*
   :align: center

Play around a bit with the Print Composer if you like,
and refresh your memory!

Now it’s time to get back to |project_name|!


:ref:`Go to next module --> <preparing-data-and-keywords-for-inasafe>`
