.. image:: /static/training/beginner/qgis-inasafe/image6.*

Module 11: Using Map Composer
=============================

**Learning Objectives**

- Arrange map layout
- Add title to a map
- Add legend to a map
- Add graphic and numeric scales
- Add grid to a map
- Adding inset
- Customize the content of the legend
- Export a map to different formats (pdf, jpeg, svg)

Your map is a means to communicate information (as well as new ideas and
you) to the map reader.  You use symbology to convey the contents of your
data so it can be easily understood. When you create a map layout,
you go one step further - you present your map so that it becomes a means of
information.

No matter what media you plan to distribute your map by (whether it’s
printed or sent over the internet), you must pay attention to how you
compose your map elements in the layout.  In this chapter we will discuss
the presentation of printed maps, and create our very own.

**1. The Map Composer**

The QGIS Map Composer allows you layout your map and prepare it for printing
. Apart from your map, you are able to add additional information such as
images, labels, legends, and scalebars.

- Let’s start with some data in the Sleman regency that has already been
  symbolized.  Open the project named :file:`../qgis/print_2_11.qgs` in the
  qgis/ directory.

.. image:: /static/training/beginner/qgis-inasafe/image237.*
   :align: center

- This map shows some familiar layers from the previous chapter.  We have
  the roads and vegetation of Sleman, along with the three impact zones from a
  Merapi eruption model.
- Let’s see how we can use Map Composer to adjust the layout and prepare
  this map for printing.
- Go to :menuselection:`File ‣ New Print Composer`.  A new window will load that
  looks like this:

.. image:: /static/training/beginner/qgis-inasafe/image238.*
   :align: center

This is the window where you can compose the layout of a map that you want
to print.  The blank white area is your “canvas,” or in other words,
a model of the paper you are going to print out.  You can put various
elements onto this canvas, such as your map (obviously), a title, scalebar,
legend, and so on.  These are elements commonly used on printed maps.

Take a look at the icons across the top of the window.  We will use some of
these as we lay our map out, so here’s an overview of what they do:

.. figure:: /static/training/beginner/qgis-inasafe/image239.*
   :align: center

   **Add New Map** will add a map element.  This is what we will use to add
   the map from our project into our print layout.  It should be noted,
   however, that if we change the map in our QGIS project,
   it will not update the same map that we have added to our print composer,
   as we shall see later.

.. figure:: /static/training/beginner/qgis-inasafe/image240.*
   :align: center

   **Add Image** allows us to add a picture.  You can add a company or
   organizational logo, or simply display images from a particular location.
   You can also add an image of a compass (to point North).

.. figure:: /static/training/beginner/qgis-inasafe/image241.*
   :align: center

   **Add New Label** is used for adding text to the layout,
   such as titles or other information.

.. figure:: /static/training/beginner/qgis-inasafe/image242.*
   :align: center

   **Add New Legend** is for adding a legend, which will conform to the
   active layer in the QGIS window.

.. figure:: /static/training/beginner/qgis-inasafe/image243.*
   :align: center

   **Add New Scalebar** is used to add a scale to the layout.

.. figure:: /static/training/beginner/qgis-inasafe/image244.*
   :align: center

   **Add Ellipse/Triangle/Rectangle** is used to add one of these geometric
   shapes.  For example, this might be used to indicate special areas or
   highlight things on the map.

.. figure:: /static/training/beginner/qgis-inasafe/image245.*
   :align: center

   **Add Arrow** is used to draw an arrow on the map layout.

.. figure:: /static/training/beginner/qgis-inasafe/image246.*
   :align: center

   **Select / Move Item** allows us to move choose and move the elements
   that you add to the map layout.  With this tool selected,
   you can right -click on an element to lock its position.

**2. Add New Map**

- In the Print Composer window, click on the :guilabel:`Add new map` icon.

.. image:: /static/training/beginner/qgis-inasafe/image247.*
   :align: center

- Next, click and drag your mouse across the canvas, :guilabel:`creating a box`.
  Your map layout should look similar to this when you are done:

.. image:: /static/training/beginner/qgis-inasafe/image248.*
   :align: center

- If you are not happy with the placement of your map,
  you can drag the corners to change the size, or drag the entire element
  around the canvas.
- Once you are happy set the scale of your map by going to the “Item
  Properties” tab on the right panel.

.. image:: /static/training/beginner/qgis-inasafe/image249.*
   :align: center

- Edit the :guilabel:`Scale and press Enter`.  You’ll see that the scale
  (zoom level) of the map element changes.  A scale of about 200000 should
  be good for this project.

.. note:: that when you change the scale some parts of your map may become
   invisible.  Click on the “Move item content” button and drag the map so that
   it is all visible.

.. image:: /static/training/beginner/qgis-inasafe/image250.*
   :align: center

**3. Add a Title**

- Now we’ve got the most important thing added to our map layout - the map!
  But let’s add some additional elements to make it more informative.
- Let’s add a title to our map.  Click on the :guilabel:`Add new label` button.

.. image:: /static/training/beginner/qgis-inasafe/image251.*
   :align: center

- Adjust the size of the element.  We will edit the text and the text
  properties in the panel on the right.

.. image:: /static/training/beginner/qgis-inasafe/image252.*
   :align: center

- Click the :guilabel:`Font` button and change the text size to 18 and make it
  bold. Change the alignment to center.  Lastly, add the following text,
  or create your own:

.. image:: /static/training/beginner/qgis-inasafe/image253.*
   :align: center

- Your map layout should now look similar to this:

.. image:: /static/training/beginner/qgis-inasafe/image254.*
   :align: center

**4. Add a Scale Bar**

- Let’s add a scale bar, so that anyone who looks at our map will have an
  idea what size area this map shows.  Click on the :guilabel:`Add scale bar`
  button.

.. image:: /static/training/beginner/qgis-inasafe/image255.*
   :align: center

- :guilabel:`Draw the new scalebar` element on your map.  A good location for
  it is in the lower left corner of your map layout.
- Next we need adjust the scalebar options.  Since our project is in a PCS
  (Projected Coordinate System), our measurements are in meters.  Enter the
  following values in the scalebar options:

.. image:: /static/training/beginner/qgis-inasafe/image256.*
   :align: center

- This should result in a scalebar that looks like this:

.. image:: /static/training/beginner/qgis-inasafe/image257.*
   :align: center

**5. Create a Grid**

- Now let’s create a grid for our map.
- Choose the :guilabel:`Select` tool and click on the map.

.. image:: /static/training/beginner/qgis-inasafe/image258.*
   :align: center

- In the panel on the right you should see the word :guilabel:`Grid`.
  Click on it.
- Check the box next to :guilabel:`Show grid?` and enter the following values:

.. image:: /static/training/beginner/qgis-inasafe/image259.*
   :align: center

- Check the box next to :guilabel:`Draw annotation` and enter the following
  values:

.. image:: /static/training/beginner/qgis-inasafe/image260.*
   :align: center

- Your map should now have a grid appear over it, which will look something
  like this:

.. image:: /static/training/beginner/qgis-inasafe/image261.*
   :align: center

**6. Overview Inset**

- Next, let’s add an inset that gives views of our map a little more
  information about what they are looking at.  Minimize the Print Composer and
  go back into QGIS.
- Add the layer **Indonesia.shp**, which is located in
  :file:`../qgis/peta_dunia`. Click :guilabel:`Zoom Full`.

.. image:: /static/training/beginner/qgis-inasafe/image262.*
   :align: center

- You will see the new layer load.

.. image:: /static/training/beginner/qgis-inasafe/image263.*
   :align: center

- Return to the Map Composer and create a new map with the
  :guilabel:`Add new map` button.

.. image:: /static/training/beginner/qgis-inasafe/image247.*
   :align: center

- :guilabel:`Draw a small box` on the right side of your map layout.
- The current view of your QGIS project will appear in the new map element
  (but notice that the old map element doesn’t change!)

.. image:: /static/training/beginner/qgis-inasafe/image264.*
   :align: center

**7. Add a Legend**

Now let’s add a legend so that viewers of our map will know what our
symbology represents.

- Click on the :guilabel:`Add legend` button.

.. image:: /static/training/beginner/qgis-inasafe/image265.*
   :align: center

- Draw a box in the remaining empty space on our map layout. You will see a
  legend with all of our symbologies shown in a list.
- In the panel on the right, click on :guilabel:`Legend items`.
  Use the edit button to change the names on the legend.  Use the + an -
  buttons to add or remove items from the legend.  You may choose which elements
  are important to include.  Our legend has been made to look like this:

.. image:: /static/training/beginner/qgis-inasafe/image266.*
   :align: center


When you are finished, your map layout should look similiar to this:

.. image:: /static/training/beginner/qgis-inasafe/image267.*
   :align: center

**8. Printing the Map**

- Lastly, you can print your map.  This part is easy,
  you can simply click the :guilabel:`Print` button and follow the dialog.

.. image:: /static/training/beginner/qgis-inasafe/image268.*
   :align: center

- Additionally you can save the map as a PDF, which you can easily send over
  email or print later when you have a chance.

.. image:: /static/training/beginner/qgis-inasafe/image269.*
   :align: center
