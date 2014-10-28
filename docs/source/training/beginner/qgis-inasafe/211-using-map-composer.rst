.. image:: /static/training/beginner/qgis-inasafe/image7.*

..  _using-map-composer:

Module 11: Using Map Composer
=============================

**Learning Objectives**

- Arrange map layout
- Add a new map
- Add title to a map
- Add graphic and numeric scales
- Add grid to a map
- Add an inset
- Customise the content of the legend
- Export a map to different formats (pdf, jpeg, svg)

A map is a means to communicate information (as well as new ideas) to 
the audience. We use symbology to convey the contents of our
data so it can be easily understood. When we create a map layout,
we go one step further - we present our map so that it becomes a means of
information.

No matter what media we plan to distribute our map by (whether it’s
printed or sent over the internet), we must pay attention to how we
compose the map elements in the layout. In this module we will discuss
the presentation of printed maps, and create our very own.

1. The Map Composer
-------------------

The QGIS Map Composer allows you to prepare your map for printing.
Apart from your map, you are able to add additional information such as
images, labels, legends and scalebars.

1. Let’s start with some data in the Sleman regency that has already been
   symbolised. Open the project named :file:`print_2_11.qgs` in the
   :file:`qgis/` directory.

.. image:: /static/training/beginner/qgis-inasafe/image246.*
   :align: center

This map shows some familiar layers from the previous module. We have
the roads and vegetation of Sleman, along with the three impact zones from a
Merapi eruption model.

Let’s see how we can use Map Composer to adjust the layout and prepare
this map for printing.

2. Go to :menuselection:`Project ‣ New Print Composer`. Then, give a unique
   title name for your layout, such as :kbd:`My Layout 1`. Click 
   :guilabel:`OK`. A new window will load that looks like this:

.. image:: /static/training/beginner/qgis-inasafe/image247.*
   :align: center

This is the window where you can compose the layout of a map that you want
to print. The blank white area is your “canvas.” It is
a model of the paper you are going to print out. You can put various
elements onto this canvas, such as your map (obviously), a title, scalebar
and legend. These are elements commonly used on printed maps.

Take a look at the right panel. In :guilabel:`Composition` tab, you can
change paper size, number of pages, and quality of output.

.. figure:: /static/training/beginner/qgis-inasafe/image248.*
   :align: center

Take a look at the icons across the top of the window.  We will use some
of these as we lay our map out, so here’s an overview of what they do:



+----------------------------------------------------------------+--------------------------------------------------------------------------+
| Display Icon                                                   | Function                                                                 |
+================================================================+==========================================================================+
| .. image:: /static/training/beginner/qgis-inasafe/image249.*   | **Add New Map** will add a map element.  This is what we will use to add |
|                                                                | the map from our project into our print layout.  It should be noted,     |
|                                                                | however, that if we change the map in our QGIS project,                  |
|                                                                | it will not update the same map that we have added to our print composer,|
|                                                                | as we shall see later.                                                   |
+----------------------------------------------------------------+--------------------------------------------------------------------------+
| .. image:: /static/training/beginner/qgis-inasafe/image250.*   | **Add Image** allows us to add a picture.  You can add a company or      |
|                                                                | organisational logo, or simply display images from a particular location.|
|                                                                | You can also add an image of a compass (to point North).                 |
+----------------------------------------------------------------+--------------------------------------------------------------------------+
| .. image:: /static/training/beginner/qgis-inasafe/image251.*   | **Add New Label** is used for adding text to the layout,                 |
|                                                                | such as titles or other information.                                     |
+----------------------------------------------------------------+--------------------------------------------------------------------------+
| .. image:: /static/training/beginner/qgis-inasafe/image252.*   | **Add New Legend** is for adding a legend, which will conform to the     |
|                                                                | active layer in the QGIS window.                                         |
+----------------------------------------------------------------+--------------------------------------------------------------------------+
| .. image:: /static/training/beginner/qgis-inasafe/image253.*   | **Add New Scalebar** is used to add a scale to the layout.               |
+----------------------------------------------------------------+--------------------------------------------------------------------------+
| .. image:: /static/training/beginner/qgis-inasafe/image254.*   | **Add Ellipse/Triangle/Rectangle** is used to add one of these geometric |
|                                                                | shapes.  For example, this might be used to indicate special areas or    |
|                                                                | highlight things on the map.                                             |
+----------------------------------------------------------------+--------------------------------------------------------------------------+
| .. image:: /static/training/beginner/qgis-inasafe/image255.*   | **Add Arrow** is used to draw an arrow on the map layout.                |
+----------------------------------------------------------------+--------------------------------------------------------------------------+
| .. image:: /static/training/beginner/qgis-inasafe/image256.*   | **Select / Move Item** allows us to move choose and move the elements    |
|                                                                | that you add to the map layout.  With this tool selected,                |
|                                                                | you can right -click on an element to lock its position.                 |
+----------------------------------------------------------------+--------------------------------------------------------------------------+


2. Adding a new map
-------------------

3. In the Print Composer window, click on the :guilabel:`Add new map` button.

.. image:: /static/training/beginner/qgis-inasafe/image249.*
   :align: center

4. Next, click and drag your mouse across the canvas, creating a box.
   Your map layout should look similar to this when you are done:

.. image:: /static/training/beginner/qgis-inasafe/image257.*
   :align: center

5. If you are not happy with the placement of your map,
   you can drag the corners to change the size, or drag the entire element
   around the canvas.

6. Once you are happy set the scale of your map by going to the 
   :guilabel:`Item Properties` tab in the right panel.

.. image:: /static/training/beginner/qgis-inasafe/image258.*
   :align: center

7. Edit the scale and press :kbd:`Enter`. You’ll see that the scale
   (zoom level) of the map element changes. A scale of about 200000 should
   be good for this project.

8. Add a frame by clicking the box next to :guilabel:`Frame`.
   Configure the frame color and border thickness.

.. image:: /static/training/beginner/qgis-inasafe/image259.*
   :align: center

.. note:: When you change the scale some parts of your map may become
   invisible. Click on the “Move item content” button and drag the map so that
   it is all visible.

   .. image:: /static/training/beginner/qgis-inasafe/image260.*
      :align: center

3. Adding a title
-----------------

Now we’ve got the most important thing added to our map layout - the map!
But let’s add some additional elements to make it more informative.

9. Let’s add a title to our map. Click on the :guilabel:`Add new label` button.

.. image:: /static/training/beginner/qgis-inasafe/image251.*
   :align: center

10. Adjust the size of the element. We will edit the text and the text
    properties in the panel on the right.

11. Click the :guilabel:`Font` button. Change the text size to 18 and make it
    bold. Change the alignment to center. Lastly, add the following text,
    or create your own:

.. image:: /static/training/beginner/qgis-inasafe/image261.*
   :align: center

.. image:: /static/training/beginner/qgis-inasafe/image262.*
   :align: center

Your map layout should now look similar to this:

.. image:: /static/training/beginner/qgis-inasafe/image263.*
   :align: center

4. Adding a scale bar
---------------------

Let’s add a scale bar, so that anyone who looks at our map will have an
idea what size area this map shows. 

12. Click on the :guilabel:`Add scale bar` button.

.. image:: /static/training/beginner/qgis-inasafe/image253.*
   :align: center

13. Draw the new scalebar element on your map. A good location for
    it is in the lower left corner of your map layout.

14. Next we need adjust the scalebar options. Since our project is in a PCS
    (Projected Coordinate System), our measurements are in metres.  Enter the
    following values in the scalebar options:

.. image:: /static/training/beginner/qgis-inasafe/image264.*
   :align: center

This should result in a scalebar that looks like this:

.. image:: /static/training/beginner/qgis-inasafe/image265.*
   :align: center

5. Creating a grid
------------------

Now let’s create a grid for our map.

15. Choose the :guilabel:`Select` tool and click on the map.

.. image:: /static/training/beginner/qgis-inasafe/image256.*
   :align: center

16. In the panel on the right you should see the word :guilabel:`Grid`.
    Click on it.

17. Check the box next to :guilabel:`Show grid` and enter the following values:

.. image:: /static/training/beginner/qgis-inasafe/image266.*
   :align: center

18. Check the box next to :guilabel:`Draw Coordinates` and enter the following
    values:

.. image:: /static/training/beginner/qgis-inasafe/image267.*
   :align: center

19. Your map should now have a grid appear over it, which will look something
    like this:

.. image:: /static/training/beginner/qgis-inasafe/image268.*
   :align: center

Tips
....

Play around a little bit with the coordinate format.
You can use decimal degrees as the coordinate format or change it
into Degree Minute format (DD MM) or Degree
Minute Second (DD MM SS).

You can also adjust the coordinate placement.
You can place the text inside or outside the frame, and make the
orientation either vertical or horizontal.

Change the font type and font size by clicking :guilabel:`Font` in the panel.


6. Overview inset
-----------------

Next, let’s add an inset that gives viewers of our map a little more
information about what they are looking at.

11. Minimise the Print Composer and go back into QGIS.

12. Add the layer :file:`Indonesia.shp`, which is located in
    :file:`qgis/peta_dunia`. Click :guilabel:`Zoom Full`.

.. image:: /static/training/beginner/qgis-inasafe/image269.*
   :align: center

The new layer will load.

.. image:: /static/training/beginner/qgis-inasafe/image270.*
   :align: center

13. Return to the Map Composer and create a new map with the
    :guilabel:`Add new map` button.

.. image:: /static/training/beginner/qgis-inasafe/image249.*
   :align: center

14. Draw a small box on the right side of your map layout.

15. The current view of your QGIS project will appear in the new map element
    (but notice that the old map element doesn’t change!) Add a frame
    for the inset, so that it looks like this:

.. image:: /static/training/beginner/qgis-inasafe/image271.*
   :align: center

7. Adding a legend
------------------

Now let’s add a legend so that viewers of our map will know what our
symbology represents.

16. Click on the :guilabel:`Add legend` button.

.. image:: /static/training/beginner/qgis-inasafe/image252.*
   :align: center

17. Draw a box in the remaining empty space on your map layout. You will see a
    legend with symbologies shown in a list.

18. In the panel on the right, click on :guilabel:`Legend items`.
    Use the edit button to change the names on the legend. Use the 
    :guilabel:`+` and :guilabel:`-` buttons to add or remove items from the 
    legend. Choose which elements are important to include.

.. image:: /static/training/beginner/qgis-inasafe/image272.*
   :align: center

19. Our legend looks like this:

.. image:: /static/training/beginner/qgis-inasafe/image273.*
   :align: center

20. When you are finished, your map layout should look similiar to this:

.. image:: /static/training/beginner/qgis-inasafe/image274.*
   :align: center

8. Printing the map
-------------------

21. Lastly, you can print your map. Simply click
    the :guilabel:`Print` button and follow the dialog.

.. image:: /static/training/beginner/qgis-inasafe/image275.*
   :align: center

22. You may also save the map as PNG image.

.. image:: /static/training/beginner/qgis-inasafe/image276.*
   :align: center

23. Additionally you can save the map as a PDF, which you can easily send over
    email or print later when you have a chance.

.. image:: /static/training/beginner/qgis-inasafe/image277.*
   :align: center


:ref:`Go to next module --> <understanding-inasafe>` 