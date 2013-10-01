.. image:: /static/training/intermediate/qgis-inasafe/image6.png

********
Module 1
********
Review QGIS
============

**Learning Objectives**

- Identify data types in QGIS
- Explain about data symbology
- Explain about map layout

Before we dive deeper into InaSAFE,  we will spend this Module in a review of the QGIS techniques that we covered in Unit 2.  We will once more go over some of they key aspects of QGIS, including adding vector and raster layers, symbolizing layers, and using the Print Composer for layouting.  If you feel competent in all of these areas, feel free to jump ahead to the next Module, but if you’d like a brief review, follow along!

**1. Data Types in Quantum GIS**

As you may recall, there are two types of data that we often use in QGIS: raster data and vector data.  Raster data is characterized as an array of data which consists of rows and columns, like the pixels in an image.  Vector data, on the other hand, consists of discrete features made of points and lines, and their position is defined by coordinates.

*1.1  Adding Vector Data*

Let’s add vector data to a new project.

- Open a new QGIS project.  Your map and Layers list should be empty.

.. image:: /static/training/intermediate/qgis-inasafe/image7.png
 
- There are two ways to add a new vector layer to your project.  You can navigate to Layer > Add Vector Layer... on the menu or you can click on the “Add Vector Layer” button on the toolbar:

.. image:: /static/training/intermediate/qgis-inasafe/image8.png
 
- If you can’t find the toolbar button, right-click the toolbars and make sure that the box is checked next to “File.”
- The “Add vector layer” dialog looks like this:

.. image:: /static/training/intermediate/qgis-inasafe/image9.png
 
- Click on the Browse button and navigate to your exercise data.  Go into the qgis/Sleman/ directory and select Jalan_Sleman_OSM, POI_Sleman and Kecamatan_Sleman.  You can select multiple files by holding the CTRL key on your keyboard as you click each file.
- Click “Open” and then “Open” again.
- Your map canvas now will looks like this:

.. image:: /static/training/intermediate/qgis-inasafe/image10.png
 
Great!  You’ve added some vector data to your map.  Don’t forget there are three kinds of vectors - points, lines, and polygons.  We have just added one layer of each type.

*1.2  Adding Raster Data*

Raster data has different characteristics compared to vector data. Raster data is composed by rows and columns which form small boxes (known as pixels). The ‘box’es contains information, which is usually expressed as grayscale or color. The information in each pixel could be the altitude of a point, the size of the population, the area’s color, and so forth.

- There are two ways to add a new raster layer to your project.  You can navigate to Layer > Add Raster Layer... on the menu or you can click on the “Add Vector Layer” button on the toolbar:

.. image:: /static/training/intermediate/qgis-inasafe/image11.png
 
- Navigate to qgis/Sleman/SRTM/ and select SRTM_Sleman.tif, which depicts the topography of the area.

.. image:: /static/training/intermediate/qgis-inasafe/image12.png
 
- Click Open.  The raster will be added to our project as a grey-colored square.

.. image:: /static/training/intermediate/qgis-inasafe/image13.png
 
Next we will symbolize the data to make it easier to understand.

**2. Symbolizing Data**

Layer symbology is useful so that users can easily understand our maps.  It is also important to make our maps more attractive.  Your choice of a layer’s symbology is very important to deliver the right information.

*2.1  Symbolize the Districts*

Let’s symbolize the district layer that we’ve added:

- Right click on the Kecamatan_Sleman layer, and choose Properties, or double click the layer name.
- Click on the Style tab.

.. image:: /static/training/intermediate/qgis-inasafe/image14.png
 
- Notice all the options that we have to change the appearance of this layer.  We can change the layer’s transparency or its color, or make even more detailed variations by clicking on “Change.”

.. image:: /static/training/intermediate/qgis-inasafe/image15.png
  
- We can also base the symbology on the data contained in the layer itself.
- Click on the box that says “Single Symbol,” and change it to “Categorized.”

.. image:: /static/training/intermediate/qgis-inasafe/image16.png
 
- Change the Color Ramp to a set of colors that you like, and then click “Classify.”  It may look something like this (although your colors will be different):

.. image:: /static/training/intermediate/qgis-inasafe/image17.png
 
- Click OK to apply the style changes.

*2.2  Symbolize the Roads*

Next, let’s symbolize our roads layer.

- Double-click Jalan_Sleman_OSM in the Layers list to open the properties dialog.
- Click on the “Style” tab.
- Adjust the color as you like, or choose one of the style presets that are displayed at the bottom.
- Feel free to experiment, you can make changes, click “Apply,” and view your changes on the map until you are satisfied.
- If you use multiple symbologies (as we covered in Unit 2), your roads may end up looking like this:

.. image:: /static/training/intermediate/qgis-inasafe/image18.png

- This isn’t ideal.  To fix this, open the Properties dialog and on the Style tab click on the “Advanced” button and choose Symbol Levels.  Check to box next to “Enable symbol levels.”

.. image:: /static/training/intermediate/qgis-inasafe/image19.png
 
- The roads will then look correct:

.. image:: /static/training/intermediate/qgis-inasafe/image20.png
 
Try editing the symbology of the POI_Sleman_OSM layer on your own.

*2.3  Editing Raster Symbology*

Lastly, let’s fix our raster layer so that it doesn’t look just like a grey rectangle.

- Make sure that the raster toolbar is activated.  It should look like this:

.. image:: /static/training/intermediate/qgis-inasafe/image21.png

- Select the SRTM_Sleman layer and click the “Stretch Histogram” button.

.. image:: /static/training/intermediate/qgis-inasafe/image22.png
 
- Your map should end up looking something like this:

.. image:: /static/training/intermediate/qgis-inasafe/image23.png
 
**3. Map Layout**

Your map is a medium to communicate information (as well as your ideas) to your map’s reader.  You use layer symbology to convey the content of your data so that it can be easily understood by the user.  By creating a map layout, you are going a step further in using your map as a way to convey information.

For a full review of Map Composer, refer back to Unit 2.  For now, let’s create a basic layout with a legend.

- Start a new Map Composer window by going to File > New Print Composer
- Click the “Add new map” button and draw a box on the left side of the canvas.

.. image:: /static/training/intermediate/qgis-inasafe/image24.png
 
- Now click on the “Add new legend” button and draw a box on the right side of the canvas.

.. image:: /static/training/intermediate/qgis-inasafe/image25.png
 
- Your map will look similar to this:

.. image:: /static/training/intermediate/qgis-inasafe/image26.png
 
Play around a bit with the Print Composer if you like, and refresh your memory!

We hope this was a useful refresher.  Now it’s time to get back to InaSAFE!



 