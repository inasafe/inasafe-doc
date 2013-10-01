.. image:: /static/beginner/qgis-inasafe/image6.png

*********
Module 11
*********
Using Map Composer
==================

**Learning Objectives**

- Arrange map layout
- Add title to a map
- Add legend to a map
- Add graphic and numeric scales
- Add grid to a map
- Adding inset
- Customize the content of the legend
- Export a map to different formats (pdf, jpeg, svg)

Your map is a means to communicate information (as well as new ideas and you) to the map reader.  You use symbology to convey the contents of your data so it can be easily understood. When you create a map layout, you go one step further - you present your map so that it becomes a means of information.

No matter what media you plan to distribute your map by (whether it’s printed or sent over the internet), you must pay attention to how you compose your map elements in the layout.  In this chapter we will discuss the presentation of printed maps, and create our very own.

**1. The Map Composer**

The QGIS Map Composer allows you layout your map and prepare it for printing.  Apart from your map, you are able to add additional information such as images, labels, legends, and scalebars.

- Let’s start with some data in the Sleman regency that has already been symbolized.  Open the project named print_2_11.qgs in the qgis/ directory.

.. image:: /static/beginner/qgis-inasafe/image237.png

- This map shows some familiar layers from the previous chapter.  We have the roads and vegetation of Sleman, along with the three impact zones from a Merapi eruption model.
- Let’s see how we can use Map Composer to adjust the layout and prepare this map for printing.
- Go to File ‣ New Print Composer.  A new window will load that looks like this:

.. image:: /static/beginner/qgis-inasafe/image238.png
 
This is the window where you can compose the layout of a map that you want to print.  The blank white area is your “canvas,” or in other words, a model of the paper you are going to print out.  You can put various elements onto this canvas, such as your map (obviously), a title, scalebar, legend, and so on.  These are elements commonly used on printed maps.

Take a look at the icons across the top of the window.  We will use some of these as we lay our map out, so here’s an overview of what they do:

.. image:: /static/beginner/qgis-inasafe/image239.png

   **Add New Map** will add a map element.  This is what we will use to add the map from our project into our print layout.  It should be noted, however, that if we change the map in our QGIS project, it will not update the same map that we have added to our print composer, as we shall see later.

.. image:: /static/beginner/qgis-inasafe/image240.png

   **Add Image** allows us to add a picture.  You can add a company or organizational logo, or simply display images from a particular location. You can also add an image of a compass (to point North).

.. image:: /static/beginner/qgis-inasafe/image241.png

   **Add New Label** is used for adding text to the layout, such as titles or other information.

.. image:: /static/beginner/qgis-inasafe/image242.png

   **Add New Legend** is for adding a legend, which will conform to the active layer in the QGIS window.

.. image:: /static/beginner/qgis-inasafe/image243.png

   **Add New Scalebar** is used to add a scale to the layout.

.. image:: /static/beginner/qgis-inasafe/image244.png

   **Add Ellipse/Triangle/Rectangle** is used to add one of these geometric shapes.  For example, this might be used to indicate special areas or highlight things on the map.

.. image:: /static/beginner/qgis-inasafe/image245.png

  ** Add Arrow** is used to draw an arrow on the map layout.

.. image:: /static/beginner/qgis-inasafe/image246.png

   **Select / Move Item** allows us to move choose and move the elements that you add to the map layout.  With this tool selected, you can right-click on an element to lock its position.

**2. Add New Map**

- In the Print Composer window, click on the “Add new map” icon.

.. image:: /static/beginner/qgis-inasafe/image247.png
 
- Next, click and drag your mouse across the canvas, creating a box.  Your map layout should look similar to this when you are done:

.. image:: /static/beginner/qgis-inasafe/image248.png
 
- If you are not happy with the placement of your map, you can drag the corners to change the size, or drag the entire element around the canvas.
- Once you are happy set the scale of your map by going to the “Item Properties” tab on the right panel.

.. image:: /static/beginner/qgis-inasafe/image249.png
 
- Edit the Scale and press Enter.  You’ll see that the scale (zoom level) of the map element changes.  A scale of about 200000 should be good for this project.
- Note that when you change the scale some parts of your map may become invisible.  Click on the “Move item content” button and drag the map so that it is all visible.

.. image:: /static/beginner/qgis-inasafe/image250.png
 

**3. Add a Title**

- Now we’ve got the most important thing added to our map layout - the map!  But let’s add some additional elements to make it more informative.
- Let’s add a title to our map.  Click on the “Add new label” button.

.. image:: /static/beginner/qgis-inasafe/image251.png
 
- Adjust the size of the element.  We will edit the text and the text properties in the panel on the right.

.. image:: /static/beginner/qgis-inasafe/image252.png

- Click the “Font” button and change the text size to 18 and make it bold.  Change the aligment to center.  Lastly, add the following text, or create your own:

.. image:: /static/beginner/qgis-inasafe/image253.png
 
- Your map layout should now look similar to this:

.. image:: /static/beginner/qgis-inasafe/image254.png
 
**4. Add a Scale Bar**

- Let’s add a scale bar, so that anyone who looks at our map will have an idea what size area this map shows.  Click on the “Add scale bar” button.

.. image:: /static/beginner/qgis-inasafe/image255.png
 
- Draw the new scalebar element on your map.  A good location for it is in the lower left corner of your map layout.
- Next we need adjust the scalebar options.  Since our project is in a PCS (Projected Coordinate System), our measurements are in meters.  Enter the following values in the scalebar options:

.. image:: /static/beginner/qgis-inasafe/image256.png 

- This should result in a scalebar that looks like this:

.. image:: /static/beginner/qgis-inasafe/image257.png
 

**5. Create a Grid**

- Now let’s create a grid for our map.
- Choose the “Select” tool and click on the map.

.. image:: /static/beginner/qgis-inasafe/image258.png
 
- In the panel on the right you should see the word “Grid.”  Click on it.
- Check the box next to “Show grid?” and enter the following values:

.. image:: /static/beginner/qgis-inasafe/image259.png
 
- Check the box next to “Draw annotation” and enter the following values:

.. image:: /static/beginner/qgis-inasafe/image260.png
 
- Your map should now have a grid appear over it, which will look something like this:

.. image:: /static/beginner/qgis-inasafe/image261.png
 
**6. Overview Inset**

- Next, let’s add an inset that gives views of our map a little more information about what they are looking at.  Minimize the Print Composer and go back into QGIS.
- Add the layer Indonesia.shp, which is located in qgis/peta_dunia.  Cllick “Zoom Full.”

.. image:: /static/beginner/qgis-inasafe/image262.png
 
- You will see the new layer load.

.. image:: /static/beginner/qgis-inasafe/image263.png
 
- Return to the Map Composer and create a new map with the “Add new map” button.

.. image:: /static/beginner/qgis-inasafe/image247.png
 
- Draw a small box on the right side of your map layout.
- The current view of your QGIS project will appear in the new map element (but notice that the old map element doesn’t change!)

.. image:: /static/beginner/qgis-inasafe/image264.png

**7. Add a Legend**

Now let’s add a legend so that viewers of our map will know what our symbology represents.

- Click on the “Add legend” button.

.. image:: /static/beginner/qgis-inasafe/image265.png
 
- Draw a box in the remaining empty space on our map layout.  You will see a legend with all of our symbologies shown in a list.
- In the panel on the right, click on “Legend items.”  Use the edit button to change the names on the legend.  Use the + an - buttons to add or remove items from the legend.  You may choose which elements are important to include.  Our legend has been made to look like this:

.. image:: /static/beginner/qgis-inasafe/image266.png
 

When you are finished, your map layout should look similiar to this:

.. image:: /static/beginner/qgis-inasafe/image267.png
 
**8. Printing the Map**

- Lastly, you can print your map.  This part is easy, you can simply click the “Print” button and follow the dialog.

.. image:: /static/beginner/qgis-inasafe/image268.png
 
- Additionally you can save the map as a PDF, which you can easily send over email or print later when you have a chance.

.. image:: /static/beginner/qgis-inasafe/image269.png
  