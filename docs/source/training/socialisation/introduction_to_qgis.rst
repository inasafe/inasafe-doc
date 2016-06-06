.. image:: /static/training/socialisation/inasafe_logo.*

.. _introduction_to_qgis:

Introduction to QGIS
====================

Introduction
------------

QGIS is a user-friendly open source Geographic Information System (GIS).
It runs on Linux, OS X, Windows and Android. QGIS supports numerous vector, raster,
database formats and provide extendable functionality. Learn more about the project at:
`http://www.qgis.org <http://www.qgis.org>`__

QGIS is great because:

-  It is completely free. It doesn’t cost anything.

-  It’s free, as in liberty. If you think a feature is missing,
   you can sponsor the development of a feature,
   or add it yourself if you are familiar with programming.

-  It’s constantly developing and improving. Because many people continue adding features,
   it keeps getting better.

-  Extensive help and documentation is available.
   If you have problems you can always turn to the software documentation,
   other QGIS users, or even the developers.

QGIS provides a continuously growing number of capabilities provided by core functions and plugins.
You can visualise, manage, edit, analyse data and compose printable maps.
QGIS is also the platform which InaSAFE is built on,
and so this document focuses on building foundational skills using QGIS.

Learning objectives:
--------------------

- Understand how to get QGIS

- Understand how to install QGIS

- Understand QGIS and its layout

- Understand QGIS toolbars and how to manage them

- Learn basic operation in QGIS

- How to install InaSAFE from QGIS

- Introduction to the InaSAFE toolbar and functionality

Data for this exercise:
-----------------------

The data for this exercise is available in Introduction to QGIS.zip which can be downloaded
in `InaSAFE Training Data Packages <http://data.inasafe.org/TrainingDataPackages/>`__.
To download QGIS, go to the `QGIS Website <http://qgis.org/en/site/>`__
(we will explain how to download and install QGIS later in this exercise).
We will use the following QGIS project and data:

1. DKI_Jakarta_Introduction.qgs

2. Jakarta_roads_WGS84.shp

3. Jakarta_Flood_18113_WGS84.shp

4. Jakarta_Flood_HKV_WGS84.tif

Exercises
---------

1. Getting QGIS
...............

You can download QGIS software by accessing the main QGIS website:

-  Open your web browser and in the address bar at the top of the window
   type :kbd:`qgis.org`. Press :kbd:`Enter`.

-  The QGIS website will look something like this:

.. image:: /static/training/socialisation/Intro_QGIS_01.*
   :align: center

-  Click :guilabel:`Download Now`.

-  If you are using Windows, there are 2 versions of QGIS (version 2.14 and version 2.8).
   Choose :kbd:`Latest release (eg. for new users)` and click 
   :guilabel:`QGIS Standalone Installer Version 2.14 (32 bit or 64 bit depend your computer operating system)`.
   Your exact version number may be different.

.. image:: /static/training/socialisation/Intro_QGIS_02.*
   :align: center

-  If you are not using Windows, select your operating system from the menu.
   Follow the installation instructions.

2. Installing QGIS
..................

After you download the QGIS software installer, the next step is to install QGIS to your computer.

* Open the folder where you have the QGIS installation file.

.. image:: /static/training/socialisation/Intro_QGIS_03.*
   :align: center

* Run the installation file. If you are installing QGIS version 2.x, it should look something like this:

.. image:: /static/training/socialisation/Intro_QGIS_04.*
   :align: center

* Click :guilabel:`Next` and follow the instructions.

* Once the installation is finished, you can open your QGIS in Start Menu.

.. image:: /static/training/socialisation/Intro_QGIS_05.*
   :align: center

* QGIS will look something like this:

.. image:: /static/training/socialisation/Intro_QGIS_06.*
   :align: center

3. Understanding QGIS interface
...............................

Next, we will introduce the main QGIS interface. In general, there are
four elements in QGIS:

.. image:: /static/training/socialisation/Intro_QGIS_07.*
   :align: center

1. **Layers Panel**: On the left side of QGIS is the layers panel.
   This panel lists the layers, or files, that are loaded into our QGIS project.
   The Layers Panel not only shows all the files that are currently open,
   it also determines the order that they will be drawn on the map canvas.
   A layer that is at the bottom of the list will be drawn first,
   and any layers above it will be drawn on top.

2. **Toolbar**: At the top of QGIS are a large number of tools,
   which are contained within various *toolbars*.
   For example, the :guilabel:`File` toolbar allows you to save, load,
   print and start a new project.
   We already used one of these tools when we opened this project.

.. image:: /static/training/socialisation/Intro_QGIS_08.*
   :align: center

By hovering your mouse over an icon, the name of the tool will
appear to help you identify each tool. The number of tools (buttons)
can seem a bit overwhelming at first, but you will gradually get to
know them. The tools are grouped into related functions on toolbars.
If you look closely you can see a vertical array of ten dots to the
left of each toolbar. By grabbing these with your mouse, you can
move the toolbar to a more convenient location, or separate it so
that it sits on its own.

.. image:: /static/training/socialisation/Intro_QGIS_09.*
   :align: center

3. **Map Canvas**: All of the map data that we load into QGIS
   will be displayed here, both vector data and raster data.

4. **Status bar**: The status bar shows information about the current map.
   It allows you to adjust the map scale and see the mouse cursor’s coordinates
   on the map.

.. image:: /static/training/socialisation/Intro_QGIS_10.*
   :align: center

The coordinates of this map are the same type of coordinates that are recorded by GPS devices.
The status bar shows the longitude and latitude of your mouse cursor.

4. Manage toolbars
..................

At the top of QGIS are a large number of tools, which are contained within various 'toolbars.'
For example, the File toolbar allows you to save, load, print, and start a new project.
We already used one of these tools when we opened this project.

.. image:: /static/training/socialisation/Intro_QGIS_11.*
   :align: center

By hovering your mouse over an icon, the name of the tool will appear to
help you identify each tool.

The number of tools (buttons) can seem a bit overwhelming at first, but
you will gradually get to know them. The tools are grouped into related
functions on toolbars. If you look closly you can see a vertical array
of ten dots to the left of each toolbar. By grabbing these with your
mouse, you can move the toolbar to a more convenient location, or
separate it so that it sits on its own.

.. image:: /static/training/socialisation/Intro_QGIS_12.*
   :align: center

If you feel overwhelmed by the number of toolbars, you can customize the
interface to see only the tools you use most often, adding or removing
toolbars as necessary.

To add or remove a toolbar, **right-click** on empty space in toolbars,
or go to :menuselection:`View ‣ Toolbars`.

Rearrange the toolbar so that it’s on one line. Left-click and hold the
vertical dots on the left hand side of the tool. Drag to the first line
of the toolbar.

.. image:: /static/training/socialisation/Intro_QGIS_13.*
   :align: center

5. QGIS basic tools
...................

We’ve already taken a look at the QGIS toolbar and have seen the tools
for opening QGIS. Here’s a list of some of the most commonly used tools.
Feel free to play around with them if you like. The important thing for
now is to start getting familiar with QGIS.

+-------------------------------------------------------------+-------------------------+---------------------------------------------------------------+
| .. image:: /static/training/socialisation/Intro_QGIS_14.*   | Add Vector Layer        | Add vector data to Layer List                                 |
+-------------------------------------------------------------+-------------------------+---------------------------------------------------------------+
| .. image:: /static/training/socialisation/Intro_QGIS_15.*   | Add Raster Layer        | Add raster data to Layer List                                 |
+-------------------------------------------------------------+-------------------------+---------------------------------------------------------------+
| .. image:: /static/training/socialisation/Intro_QGIS_16.*   | New                     | Create new QGIS project                                       |
+-------------------------------------------------------------+-------------------------+---------------------------------------------------------------+
| .. image:: /static/training/socialisation/Intro_QGIS_17.*   | Open                    | Open QGIS project                                             |
+-------------------------------------------------------------+-------------------------+---------------------------------------------------------------+
| .. image:: /static/training/socialisation/Intro_QGIS_18.*   | Toggle Editing          | Edit features in a layer                                      |
+-------------------------------------------------------------+-------------------------+---------------------------------------------------------------+
| .. image:: /static/training/socialisation/Intro_QGIS_19.*   | Pan Map                 | Drag the map to a new location                                |
+-------------------------------------------------------------+-------------------------+---------------------------------------------------------------+
| .. image:: /static/training/socialisation/Intro_QGIS_20.*   | Zoom In                 | Zoom in on the map                                            |
+-------------------------------------------------------------+-------------------------+---------------------------------------------------------------+
| .. image:: /static/training/socialisation/Intro_QGIS_21.*   | Zoom Out                | Zoom out on the map                                           |
+-------------------------------------------------------------+-------------------------+---------------------------------------------------------------+
| .. image:: /static/training/socialisation/Intro_QGIS_22.*   | Zoom Full               | Zoom so that all layers fit in the map window                 |
+-------------------------------------------------------------+-------------------------+---------------------------------------------------------------+
| .. image:: /static/training/socialisation/Intro_QGIS_23.*   | Identify features       | Identify the attribute of an active layer in the map canvas   |
+-------------------------------------------------------------+-------------------------+---------------------------------------------------------------+
| .. image:: /static/training/socialisation/Intro_QGIS_24.*   | Open Attribute Table    | Open a layer’s attribute table                                |
+-------------------------------------------------------------+-------------------------+---------------------------------------------------------------+
| .. image:: /static/training/socialisation/Intro_QGIS_25.*   | Select Single Feature   | Select a feature in the selected layer                        |
+-------------------------------------------------------------+-------------------------+---------------------------------------------------------------+

6. Navigating the map
.....................

Before we examine the attributes of individual features, let’s take a quick look at how to navigate the map.
The main controls for moving the map around and zooming in-and-out are on the panels at the top of QGIS by default.

.. image:: /static/training/socialisation/Intro_QGIS_26.*
   :align: center

When you click on one of these buttons, it changes the action of your mouse in the main map window.

-  Select the first button that looks like a hand. Now hold the left mouse button down
   and drag the mouse in the map window.
   This allows you to **pan** the map, or move it around.

-  Select the button that has a plus :guilabel:`(+)` sign inside a magnifying
   glass allows you to **zoom in** on the map. Using your mouse, draw a box
   around your area of interest and release your mouse.

-  The button that has a minus :guilabel:`(-)` sign inside a magnifying glass
   allows you to **zoom out** on the map. Select this button and click on the
   map.

-  The button that looks like a magnifying glass with blue arrows pointing away
   from it lets you **zoom to the full extent** of your map. Click this button
   to see all the data that is loaded in the project fit into the map canvas.

We can always change the QGIS projection based on the projection of the data.
It makes it easier to edit our data in further steps if QGIS has the same
projection as the data.

7. Hide and move layers
.......................

Sometimes if you handle many layers, you need to hide/unhide layers
to make the map canvas more organized. For example,
open the pre-saved QGIS project, :file:`DKI_Jakarta_Introduction.qgs`.
Once all the data are displayed on your map canvas, try toggling the layer,
**a flood similar to the 2007 Jakarta Event** by clicking on the checkbox
in the Layers Panel on the left side of your screen.

.. image:: /static/training/socialisation/Intro_QGIS_27.*
   :align: center

After you uncheck the check box, the layer will disappear from the map canvas.
This operation won’t remove your layer from the layers list but only hide it
temporarily until you recheck again the check box.
Try to turn ON the layer again to unhide the layer.

What if your layer does not appear in the map canvas even though you
already turned ON your layers? In this example,
the **Jakarta_roads_WGS84** layer didn’t appear in Map Canvas even though
it’s already turned ON. In this case, it’s related to layer order.
The layers in your Layers List are drawn on the map in a certain order.
The layer at the bottom of the list is drawn first,
and the layer at the top is drawn last.
By changing the order of the layers in the list,
you can change the order they are drawn in.

For example in this layer order...

.. image:: /static/training/socialisation/Intro_QGIS_28.*
   :align: center

… would result in **Jakarta_roads_WGS84** being hidden as they
position *underneath* **A Flood in Jakarta like 2013**.
To solve this problem, simply click the **Jakarta_roads_WGS84** layer
and drag to the top of the Layer List or reorder them to the correct order.

.. image:: /static/training/socialisation/Intro_QGIS_29.*
   :align: center

What do you see after you move the **Jakarta_roads_WGS84** layer?

You can see the road network now because the **Jakarta_roads_WGS84** layer is
shown above the other layers.

8. Symbolize layer
..................

The symbology of a layer is its visual appearance on the map.
One of the basic strengths of GIS is that you have a dynamic visual representation
of the data you’re working with. Therefore, the visual appearance of the map
(which depends on the symbology of the individual layers) is very important.
For example in the project that you currently have open, :file:`DKI_Jakarta_Introduction.qgs`,
you will see the **A Flood in Jakarta like 2013** layer covering the area of DKI Jakarta.
Did the flood really cover the whole of DKI Jakarta?

To answer this, let’s turn OFF the **Jakarta_roads_WGS84** and **A Flood Similar to the Jakarta 2007 event**
layers and open the attribute table of **A Flood in Jakarta like 2013** by right clicking the layer and
selecting :guilabel:`Open Attribute Table`. You will see there are 6 columns
in this table and one of the columns has the name ‘affected’ with values of 1 and 0.
A value of 1 represents an area that is flooded, while a value of 0 represents
an area that has not been flooded. Let’s select a feature in this layer and see
the highlighted feature in the attribute table.

.. image:: /static/training/socialisation/Intro_QGIS_30.*
   :align: center

What is the value of the selected feature in the attribute table?

Not all of the features in this dataset have a value of 1 (or flooded).
You need to see which features have a value of 1 to make it easier to interpret the hazard area.
To solve this problem, we will symbolize the data so it will only shows the flooded area.

1. Right click on the **A flood in Jakarta like 2013** layer and select :guilabel:`Properties`.

2. Go to the :guilabel:`Style` tab and and change :guilabel:`Single Symbol` into :guilabel:`Categorized`.

3. Select :guilabel:`affected` in Column as the column that we will use to categorize the data.

4. Click :guilabel:`classify` and turn off the values that have a value of 0 or no value.

5. Click OK

.. image:: /static/training/socialisation/Intro_QGIS_31.*

After you click :guilabel:`OK`, only features that have a value of 1
(flooded) will be displayed on the map canvas, the other values won’t be shown
on the map canvas because you turned OFF the symbol that represents a value of 0.
Symbology helps us better understand the data that we will work on.

9. InaSAFE installation and set up
..................................

As we know, the InaSAFE plugin has been built for QGIS. It is one of the plugins
which are available in the QGIS Repository. Make sure that you have a working
internet connection before you follow the steps below.
To get InaSAFE please follow these steps:

- Go to :menuselection:`Plugins -> Manage and install plugins` menu.

.. image:: /static/training/socialisation/Intro_QGIS_32.*

- Go to the search box and type :kbd:`InaSAFE`.

.. image:: /static/training/socialisation/Intro_QGIS_33.*

- Select InaSAFE and click :guilabel:`Install plugin` and 
   wait for a moment until the InaSAFE dock appears
   in the right side of QGIS main window.

- Close the plugin manager window.

Congratulations! Now you have InaSAFE installed in QGIS.

10. InaSAFE toolbars
....................

After successfully installing InaSAFE, you should now have an **InaSAFE dock**
on the right hand side of your screen. It should look like this:

.. image:: /static/training/socialisation/Intro_QGIS_34.*
   :align: center

InaSAFE also comes with a toolbar of its own! To retrieve the InaSAFE
toolbar, you can right-click on the top toolbar and check InaSAFE.

.. image:: /static/training/socialisation/Intro_QGIS_35.*
   :align: center

+--------------------------------------------------------------+----------------------------------+
| .. image:: /static/training/socialisation/Intro_QGIS_36.*    | InaSAFE Dock                     |
+--------------------------------------------------------------+----------------------------------+
| .. image:: /static/training/socialisation/Intro_QGIS_37.*    | Set Analysis Area                |
+--------------------------------------------------------------+----------------------------------+
| .. image:: /static/training/socialisation/Intro_QGIS_38.*    | Toggle Scenario Outline          |
+--------------------------------------------------------------+----------------------------------+
| .. image:: /static/training/socialisation/Intro_QGIS_39.*    | Keyword Creation Wizard          |
+--------------------------------------------------------------+----------------------------------+
| .. image:: /static/training/socialisation/Intro_QGIS_40.*    | Impact Function Centric Wizard   |
+--------------------------------------------------------------+----------------------------------+
| .. image:: /static/training/socialisation/Intro_QGIS_41.*    | OpenStreetMap Downloader         |
+--------------------------------------------------------------+----------------------------------+
| .. image:: /static/training/socialisation/Intro_QGIS_42.*    | Add OpenStreetMap Tile Layer     |
+--------------------------------------------------------------+----------------------------------+

Later we will explore and use these tools in **Run Basic InaSAFE** and **Intermediate Modules**.

Summary
-------

In this exercise you have learned about QGIS, the free and
open source software for processing spatial data.
You have learned where to get QGIS, how to install QGIS,
understand the QGIS layout and looked at some useful toolbars,
learning how to turn ON/OFF QGIS layers,
and learned how to symbolize the data layers.

We also learned how to install InaSAFE through the QGIS plugin manager.
Later on we will learn how to operate InaSAFE with DKI Jakarta flood scenario.

