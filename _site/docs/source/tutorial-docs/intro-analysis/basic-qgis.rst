The Basics of QGIS
==================

Learning Objectives
-------------------

* Install QGIS
* Open a previously created QGIS project
* See the list of all layers available at layer list.
* Access basic tools through 'toolbar'
* Clean up the toolbar
* Show a map through map window
* Get information on an active map through status bar


Introduction
------------

In this chapter, we will get started using Quantum GIS (QGIS).  You'll see how to install the software (if you haven't already), understand the layout and interface, and other core functions of the software.  By the end of this chapter, you'll be on your way to becoming a competent GIS user!

Note that if you followed along with the instructions in the introduction to this guide, you may have already installed QGIS and InaSAFE. If so, feel free to skip ahead to section three in this chapter.  Otherwise, let's start here and get QGIS installed.


1. Get Quantum GIS
..................
* The Quantum GIS installer is contained in the file package that comes with this guide, in **software/QGIS-OSGeo4W-1.8.0-2-Setup.exe.** If you have this file, skip to section 2.  Otherwise you can download it from the QGIS website.
* Open your web browser and in the address bar at the top of the window, type <https://qgis.org>`_. Press enter.

.. image:: /static/tutorial/intro-analysis/2_1.png
   :align: center

* The QGIS website will look something like this:

.. image:: /static/tutorial/intro-analysis/2_2.png
   :align: center

* Click 'Download Now Free!"

.. image:: /static/tutorial/intro-analysis/2_3.png
   :align: center

* If you are using Windows click on **1.1 Standalone Installer (recommended for new users)**.

.. image:: /static/tutorial/intro-analysis/2_4.png
   :align: center

* If you are not using Windows, select your Operating System from the menu.
* Click on "Download QGIS"
.. image:: /static/tutorial/intro-analysis/2_5.png

* When the file is downloaded, run it and follow the instructions to install Quantum GIS.

2. Install Quantum GIS
......................
* Open the folder where you have the QGIS installation file.

.. image:: /static/tutorial/intro-analysis/2_6.png
   :align: center

* Run the installation file. If you are installing QGIS version 1.8.0, it should look like this:

.. image:: /static/tutorial/intro-analysis/2_7.png
   :align: center

* Click Next.
* Click "I Agree" to agree with the conditions in the license agreement.

.. image:: /static/tutorial/intro-analysis/2_8.png
   :align: center

* The next window asks where you would like to install QGIS.  In most cases, the default should be fine.  Click Next.

.. image:: /static/tutorial/intro-analysis/2_9.png
   :align: center

* In the next window, Click "Install" without checking any of the boxes.

.. image:: /static/tutorial/intro-analysis/2_10.png
   :align: center

* QGIS will begin to install.  It may take a few minutes to complete.

.. image:: /static/tutorial/intro-analysis/2_11.png
   :align: center

* Click "Finish" to complete the installation.
* You can now open QGIS from your Start Menu.

.. image:: /static/tutorial/intro-analysis/2_12.png
   :align: center

* Quantum GIS will look something like this:

.. image:: /static/tutorial/intro-analysis/2_13.png
   :align: center

3. The QGIS Layout
..................
In this section we will open up a QGIS project, and take a look at the different pieces of the QGIS interface.  If you installed InaSAFE previously, make sure it is closed by clicking on the X in the upper right corner of the InaSAFE panel.  If  it isn't open or you haven't installed it yet, carry on.  We will come back to this later.

.. image:: /static/tutorial/intro-analysis/2_14.png
   :align: center

* Click on the folder icon on the upper toolbar or go to File ? Open Project...

* Navigate to the tutorial files and go into the ***qgis***/ directory.  Open the file named **sleman_2_2.qgs**.
* QGIS should now look something like the following image.  Let's pause for a moment and go over the various components of the QGIS interface.

.. image:: /static/tutorial/intro-analysis/2_15.png
   :align: center

_**Map Canvas**_
This is the window where the map is shown.  Our project has two different files open, one which shows districts of the Sleman regency, and another that shows the railway line running through the area.  You can see both of these files are drawn together in the map canvas.


_**Layers List**_
On the left side of QGIS is the layers list.  This lists the layers, or files, that are loaded into our QGIS project.  In this project, we have two layers, **Kecamatan_Sleman** and **railway_Sleman_OSM**.  The layers panel not only shows all the files that are currently open, it also determines the order that they will be drawn on the map canvas.  A layer that is at the bottom of the list will be drawn first, and any layers above it will be drawn on top.
* Click on the layer **railway_Sleman_OSM** and drag it below the layer named **Kecamatan_Sleman**.

.. image:: /static/tutorial/intro-analysis/2_16.png
   :align: center

* Notice how the map canvas changes.  The railway layer is now shown below the district layer, and part of the railway is now obscured.  A map will never show railway hidden beneath district areas, so go ahead and move the layers back.
* Uncheck the box next to a layer's name.  It will be hidden from the map canvas.
* You can expand collapsed items by clicking the arrow or plus symbol beside them.  This will provide you with more information on the layer's current appearance.

.. image:: /static/tutorial/intro-analysis/2_17.png
   :align: center

* Right-click on a layer to view a menu with menu extra options.  You'll be using some of them before long, so take a look around!


_**Toolbars**_
At the top of QGIS are a large number of tools, which are contained within various "toolbars."  For example, the File toolbar allows you to save, load, print, and start a new project.  We already used one of these tools when we opened this project.

.. image:: /static/tutorial/intro-analysis/2_18.png
   :align: center

* By hovering your mouse over an icon, the name of the tool will appear to help you identify each tool.
* The number of tools (buttons) can seem a bit overwhelming at first, but you will gradually get to know them.  The tools are grouped into related functions on toolbars.  If you look closed you can see a vertical array of ten dots to the left of each toolbar.  If you grab these with your mouse, you can move the toolbar to a more convenient location, or separate it so that it sits on its own.

.. image:: /static/tutorial/intro-analysis/2_19.png
   :align: center

* If you feel overwhelmed by the number of toolbars, you can customize the interface to see only the tools you use most often, adding or removing toolbars as necessary.  To add or remove a toolbar, right-click on any of the toolbars, or go to View ? Toolbars.

.. image:: /static/tutorial/intro-analysis/2_20.png
   :align: center

* Let's remove some of the toolbars that we will not be using in this training, to make the interface a bit cleaner.  Right-click on the toolbar, and uncheck the boxes next to the following toolbars:
	* Advanced Digitizing
	* Database
	* GRASS
	* Label
	* Raster
	* Vector
* After removing these toolbars and moving them around, your tools should look like this:

.. image:: /static/tutorial/intro-analysis/2_21.png
   :align: center
 
Even if they are not visible in a toolbar, all of your tools will remain accessible via the menus. For example, if you remove the File toolbar (which contains the Save button), you can still save your map by clicking on the File menu and then clicking on Save.


_**Status Bar**_
This shows information about the current map.  It allows you to adjust the map scale and see the mouse cursor's coordinates on the map.

.. image:: /static/tutorial/intro-analysis/2_22.png
   :align: center

The coordinates of this map are the same type of coordinates that you learned about when learning about GPS devices.  The status bar show shows the longitude and latitude of your mouse cursor.


This may not all be clear right now, but as you progress in your knowledge of GIS is will make more and more sense.


4.  Add Vector Layer
....................
Now we will add an additional layer containing roads to our project.
* Click on the "Add Vector Layer" button on the toolbar.

.. image:: /static/tutorial/intro-analysis/2_23.png
   :align: center

* A dialog box will open.  Click the "Browse" button.

.. image:: /static/tutorial/intro-analysis/2_24.png
   :align: center
   
* Navigate to the file **qgis/Sleman/Jalan_Sleman_OSM.shp** (in the training directory). Select the file and click Open.


.. note::  One of the most common file formats are **shapefiles**, which end with the extension **.shp**.  Shapefiles are often used to save geodata, and are commonly used with GIS applications like Quantum GIS.


* You should now see your new layer appear both in the map canvas and in the layers list.  It should be drawn above both the district and railway layers.

.. image:: /static/tutorial/intro-analysis/2_25.png
   :align: center

5.  Basic QGIS Tools
....................
We've already taken a look at the QGIS toolbar and seen the tools for opening a project and adding a new layer.  Here's a list of some other commonly used tools.  Feel free to play around with them if you like.  The important thing for now is to start getting familiar with QGIS.

+----------------------------------------------------+-----------------------------+-----------------------------------------------+
| image:: /static/tutorial/intro-analysis/2_26.png   | Toggle Editing              | Edit features in a layer                      |
+----------------------------------------------------+-----------------------------+-----------------------------------------------+ 
| image:: /static/tutorial/intro-analysis/2_27.png   | Pan Map                     | Drag the map to a new location                | 
+----------------------------------------------------+-----------------------------+-----------------------------------------------+
| image:: /static/tutorial/intro-analysis/2_28.png   | Zoom In                     | Zoom in on the map                            | 
+----------------------------------------------------+-----------------------------+-----------------------------------------------+
| image:: /static/tutorial/intro-analysis/2_29.png   | Zoom Out                    | Zoom out on the map                           |
+----------------------------------------------------+-----------------------------+-----------------------------------------------+
| image:: /static/tutorial/intro-analysis/2_30.png   | Zoom Full                   | Zoom so that all layers fit in the map window |
+----------------------------------------------------+-----------------------------+-----------------------------------------------+
| image:: /static/tutorial/intro-analysis/2_31.png   | Open Attribute Table        | Open a layer's attribute table                |
+----------------------------------------------------+-----------------------------+-----------------------------------------------+
| image:: /static/tutorial/intro-analysis/2_32.png   | Select Single Feature       | Select a feature in the selected layer        |
+----------------------------------------------------+-----------------------------+-----------------------------------------------+

6. Navigate the Map
....................
- Before we examine the attributes of individual features, let's take a quick look at how to navigate the map.  The main controls for moving the map around and zooming in and out are by default on the panels at the top of QGIS.

.. image:: /static/tutorial/intro-analysis/2_33.png
   :align: center

- When you click on one of these buttons, it changes what you can do with your mouse in the main map window.
- Select the first button that looks like a hand.  Now hold your left mouse button down and drag your mouse in the map window.  This allows you to pan the map, or move it around.
- The button which has a plus sign below a magnifying glass, allows you to zoom in on the map.  Select this button.  Using your mouse, draw a box around an area that you want to zoom in on, and release your mouse.
- The button which has a minus sign below a magnifying glass, allows you to zoom out on the map.  Select this button and click on the map.  This allows you to zoom out.
- The button that looks like a magnifying glass with red arrows pointing away from it lets you zoom to the full extent of your map.  When you click this button, you will be able to see all of the data that you have loaded in your project fit into the map canvas.


Summary
-------

That's it for this chapter.  We've covered a lot!  By now you should have your first taste of QGIS and know some of the basics.  Go ahead and save your project by clicking on the "Save" button on the top toolbar.

.. image:: /static/tutorial/intro-analysis/2_34.png
   :align: center