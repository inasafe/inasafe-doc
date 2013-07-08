Working with Raster Data
========================

Learning Objectives
-------------------

- Loading Raster Data (shakemap, tsunami models)
- Transform raster symbology
- Explore a raster layer


Introduction
------------

Thus far we've worked mostly with vector data, which consists of features, and these features are themselves made up of points and lines.  In this chapter we will learn about raster data.  Remember when you were editing OpenStreetMap in JOSM?  The points, lines and shapes that you drew were vector data.  But when you loaded Bing aerial imagery in the background, that was raster data.  So what's the difference?

Raster data essentially comes in the form of an image.  It is made up of pixels, like a photograph, and a raster image will always be some number of pixels wide and some number of pixels high.  If you zoom in far enough on a raster image, it will start to become blurry, just as if you opened a photo on your computer and zoomed in very close.  As we'll see in this chapter, however, a raster image can mean more than just a photograph from the sky.  Follow along and we'll learn all about rasters!

<br>
###1. Loading Raster Data

* Open the project named _**sleman___2___7.qgs**_ in the directory **_qgis/_**.  We've simplified the project since our last chapter, to make it easier to follow along, and so that our layers load a bit faster.  However, if you are comfortable you can easily carry on with your project from the previous chapter.
* Click on the Load Raster Layer button:

.. image:: /static/tutorial/intro-analysis/7_loadraster.png

* The Load Raster Layer dialog will open.  Find the file in the directory **_Sleman/_** named **_Sleman.tif_**.  Open it.
* QGIS will open a dialog which explains that the new layers does not have a CRS assigned.  In the box at the bottom, scroll down until you find **WGS 84 / UTM zone 49S**.  Select it and click OK.

.. image:: /static/tutorial/intro-analysis/7_coordinatereference.png

* When the raster layer loads, be sure to drag it to the bottom of your layers list.
* If you can't see the raster layer, you may need to enable "on the fly" transformations.  To do so:

	- Go to Settings -> Project Properties...
	- Enable "on the fly" reprojection.
	
		.. image:: /static/tutorial/intro-analysis/7_onthefly.png
	
	- Click OK.

* The raster should display nicely underneath your vector data layers.

	.. image:: /static/tutorial/intro-analysis/7_map1.png

<br>
###2. Changing Raster Symbology

Not all raster data consists of aerial photographs. There are many other forms of raster data, and in many of those cases, it's essential to symbolize the data properly so that it becomes properly visible and useful.  In this section we'll add a new kind of raster and see how to change it's symbology.

- First let's remove our previous raster image so that our project will load faster.  Right-click on the **_Sleman_** layer and click "Remove".
- Click on the Load Raster Layer button:

.. image:: /static/tutorial/intro-analysis/7_loadraster.png

- Open the file named _**SRTM___Sleman.tif**_, which is located in **_Sleman/SRTM_**.
- When it appears in the Layers list, right-click on it and click "Rename".  Give it the name **_DEM_**.


.. note:: This dataset is a Digital Elevation Model (DEM). It's a map of the elevation (altitude) of the terrain, showing us where the mountains and valleys are. In an aerial photograph, each pixel in the image is a color. When we view all of these different colored pixels together, they show us something we can understand - the Earth as viewed from above. In a DEM, each pixel has a different value instead of color. The value of each pixel represents elevation.


- When it loads, you'll notice that the new raster image appears as a gray rectangle. It's seen here with the roads layers on top:

.. image:: /static/tutorial/intro-analysis/7_map2.png

The layer appears gray (and doesn't give us any information) because its symbology hasn't been customized yet.  In the color aerial photograph we loaded previously, everything is already defined.  But if you load a raster image and it's just a gray rectangle, then you know there's no symbology for it yet. It still needs to be defined. So that's what we will do now.

- Open the Layer Properties dialog for the SRTM layer, which is now named **_DEM_**.
- Switch to the Style tab.  This shows the current symbology settings, and as we've seen, they don't give us much information on the layer.  Let's make sure the layer has data in it.
- Change the Color map to Pseudocolor:

.. image:: /static/tutorial/intro-analysis/7_pseudocolor.png

- Click OK.  The raster should look like this:

.. image:: /static/tutorial/intro-analysis/7_map3.png

- Good!  This tells us that there is data in this layer.  And by looking at it we can get an idea of where the elevation gets higher.  In the north we can see the location of Mount Merapi.

Let's stop for a minute and understand what is happening here.  Remember that an image is made up of pixels, individual cells that contain a value, which is usually a color value.  For example, if you zoom in very closely on a photograph you can see those individual pixels, like this:

.. image:: /static/tutorial/intro-analysis/7_orange.png

The value of each cell is saved in the file.  Imagine the file being saved something like this, where each square is a pixel::

.. image:: /static/tutorial/intro-analysis/7_squarepixel.png

Of course the computer doesn't understand words for colors.  In fact the value of each cell would be a number, which the computer then associates with a certain color.  For our aerial image, this is already defined.  Since it is a normal image, it knows to associate the numbers for each pixel in the file with the common colors that we see every day.  But this new raster image is different, because the values of each pixel don't represent colors, but rather altitude, and QGIS doesn't know automatically how to display it.  Hence it shows every pixel in the image as gray, even if the values in each pixel are different.  When we change the symbology to Psuedocolor, we can see all the different pixel values shown with various colors.

It would be nice to represent our DEM layer as a grayscale spectrum, rather than a variety of bright colors..  Next we will tell QGIS to symbolize the layer with colors in a spectrum, beginning at the lowest pixel value in the file and ending at the highest pixel value.  In other words, if the pixel values looked like this:

.. image:: /static/tutorial/intro-analysis/7_squarepixel1.png

QGIS would create a spectrum equating numbers to colors like this:

.. image:: /static/tutorial/intro-analysis/7_squarepixel2.png

And render the image like this:

.. image:: /static/tutorial/intro-analysis/7_squarepixel3.png

- Open Layer Properties again.
- Switch the Color map back to Grayscale.
- Tell it to use Custom min / max values:

.. image:: /static/tutorial/intro-analysis/7_customvalue.png

- Under Contrast enhancement, set the value of Current to "Stretch To MinMax":

.. image:: /static/tutorial/intro-analysis/7_stretchtominmax.png

But what are the minimum and maximum values that should be used?  The ones that are currently under Custom min / max values are the same values that just gave us a gray rectangle before. Instead, we should be using the minimum and maximum pixel values that are actually in the image.  You can determine those values easily by loading the minimum and maximum values of the raster.

- Under Load min / max values from band, select Estimate (faster).
- Click the Load button:

.. image:: /static/tutorial/intro-analysis/7_loadminmax.png

Notice how the Custom min / max values have changed.  The lowest pixel value in this image file is 0 and the highest is about 195.

.. image:: /static/tutorial/intro-analysis/7_customvalue1.png

- Click OK.  You should see the values of the raster properly displayed, with the darker colors representing valleys and the lighter ones, mountains:

.. image:: /static/tutorial/intro-analysis/7_map4.png

We've learned to do this the tricky way, but can we do it faster?  Of course!  Now that you understand what needs to be done, you'll be glad to know that there's a tool for doing all of this easily.

- Remove the current DEM from the Layers list, by right-clicking and clicking "Remove".
- Load the raster image again, renaming it to DEM as before. It's will be a gray rectangle again.
- Enable the tool you'll need by enabling View ? Toolbars ? Raster. These icons will appear in the interface:

.. image:: /static/tutorial/intro-analysis/7_rasterbutton.png

The button on the right will stretch the minimum and maximum values to give you the best contrast in the local area that you're zoomed into. It's useful for large datasets. The button on the left will stretch the minimum and maximum values to constant values across the whole image.

- Click the button on the left (Stretch Histogram to Full Dataset). You'll see the data is now correctly represented as before!  Easy!

<br>
###3. Terrain Analysis
Certain types of rasters allow you to gain more insight into the terrain that they represent. Digital Elevation Models (DEMs) are particularly useful in this regard.  In this section we'll do a little bit more with our DEM raster, in order to try to extract even more information from it.


**_3.1 Calculating a Hillshade_**

The DEM you have on your map right now does show you the elevation of the terrain, but it can sometimes seem a little abstract. It contains all the 3D elevation information about the terrain that you need, but it doesn't really _look_ 3-Dimensional. To get a better look at the terrain, it is possible to calculate a hillshade, which is a raster that maps the terrain using light and shadow to create a 3D-looking image.

To work with DEMs, you should use QGIS' all-in-one DEM (Terrain models) analysis tool.

- Click on the menu item Raster -> Analysis -> DEM (Terrain models).
- In the dialog that appears, ensure that the Input file is the DEM layer.
- Set the Output file to **_hillshade.tif_** in the directory **_qgis/Sleman/_**.

.. image:: /static/tutorial/intro-analysis/7_inputdem.png

- Check the box next to Load into canvas when finished.

.. image:: /static/tutorial/intro-analysis/7_loadintocanvas.png

- You may leave all the other options unchanged.
- Click OK to generate the hillshade.
- When it tells you that processing is completed, click OK on the message to get rid of it.
- Click Close on the main DEM (Terrain models) dialog.

You will now have a new layer called hillshade that looks like this:

.. image:: /static/tutorial/intro-analysis/7_map5.png

This looks more 3-Dimensional, but can we improve on this?  On its own, the hillshade looks like a plaster cast.  It will look better if we can combine it with our more colorful DEM.  We can do this by making the **_hillshade_** layer an overlay.


**_3.2  Using a Hillshade as an Overlay_**

A hillshade can provide very useful information about the sunlight at a given time of day. But it can also be used for aesthetic purposes, to make the map look better. The key to this is setting the hillshade to being mostly transparent.

- Change the symbology of the original **_DEM_** layer to use the Pseudocolor scheme.
- Hide all the layers except the DEM and hillshade layers.
- Click and drag the DEM to be beneath the hillshade layer in the Layers list.

.. image:: /static/tutorial/intro-analysis/7_layers.png

- Control rendering order(beneath the list) should be checked as well.

.. image:: /static/tutorial/intro-analysis/7_controlrendering.png

- Now we will make the **_hillshade_** layer somewhat transparent.  Open its Layer Properties and go to the Transparency tab.
- Set the Global transparency to 50%:

.. image:: /static/tutorial/intro-analysis/7_globaltransparency.png

- Click OK on the Layer Properties dialog. You'll get a result like this:

.. image:: /static/tutorial/intro-analysis/7_map6.png

- Switch the hillshade layer off and back on in the Layers list to see the difference it makes.


Using a hillshade in this way, it's possible to enhance the topography of the landscape. If the effect doesn't seem strong enough to you, you can change the transparency of the hillshade layer; but of course, the brighter the hillshade becomes, the dimmer the colors behind it will be. You will need to find a balance that works for you.

<br>
Summary
-------

Now you've seen how to work with raster images, and how to derive information from a Digital Elevation Model (DEM).  Congratulations, you've come a long way!