.. image:: /static/training/beginner/qgis-inasafe/image7.*

Module 3: The Basics of QGIS
============================

**Learning Objectives**

- Downloading QGIS
- Install QGIS
- Open a previously created QGIS project
- See the list of all layers available at layer list.
- Access basic tools through ‘toolbar’
- Clean up the toolbar
- Show a map through map window
- Get information on an active map through status bar

In this chapter, we will get started using QGIS. You’ll see
how to install the software (if you haven’t already), understand the layout
and interface, and other core functions of the software. By the end of this
chapter, you’ll be on your way to becoming a competent GIS user!

Note that if you followed along with the instructions in the introduction to
this guide, you may have already installed QGIS and InaSAFE.  If so,
feel free to skip ahead to section three in this chapter.  Otherwise,
let’s start here and get QGIS installed.

**1. Get QGIS**

- The QGIS installer is contained in the file package that comes with
  this guide, in :file:`...software/QGIS-OSGeo4W-2.0.x-2-Setup.exe`.  If you
  have this file, skip to section 2.  Otherwise you can download it from the
  QGIS website.
- Open your web browser and in the address bar at the top of the window,
  type :kbd:`qgis.org`.  Press :guilabel:`Enter`.

.. image:: /static/training/beginner/qgis-inasafe/image9.*
   :align: center

- The QGIS website will look something like this:

.. image:: /static/training/beginner/qgis-inasafe/image10.*
   :align: center

- Click :guilabel:`Download Now!`

.. image:: /static/training/beginner/qgis-inasafe/image11.*
   :align: center

- If you are using Windows click on 
  :guilabel:`QGIS Standalone Installer Version 2.0.1 (32 bit)`

.. image:: /static/training/beginner/qgis-inasafe/image12.*
   :align: center

- If you are not using Windows, select your Operating System from the menu.
- Click on :guilabel:`Download QGIS`

.. image:: /static/training/beginner/qgis-inasafe/image13.*
   :align: center

- When the file is downloaded, run it and follow the instructions to install
  QGIS.

**2. Install QGIS**

- Open the folder where you have the QGIS installation file.

.. image:: /static/training/beginner/qgis-inasafe/image14.*
   :align: center

- Run the installation file. If you are installing QGIS version 2.0.x,
  it should look like this:

.. image:: /static/training/beginner/qgis-inasafe/image15.*
   :align: center

- Click :guilabel:`Next`.
- Click :guilabel:`I Agree` to agree with the conditions in the license
  agreement.

.. image:: /static/training/beginner/qgis-inasafe/image16.*
   :align: center

- The next window asks where you would like to install QGIS.  In most cases,
  the default should be fine.  Click :guilabel:`Next`.

.. image:: /static/training/beginner/qgis-inasafe/image17.*
   :align: center

- In the next window, Click :guilabel:`Install` without checking any of the
  boxes.

.. image:: /static/training/beginner/qgis-inasafe/image18.*
   :align: center

- QGIS will begin to install.  It may take a few minutes to complete.

.. image:: /static/training/beginner/qgis-inasafe/image19.*
   :align: center

- Click :guilabel:`Finish` to complete the installation. Then your computer will 
  automatically reboot.

.. image:: /static/training/beginner/qgis-inasafe/image20.*
   :align: center

- You can now open QGIS from your Start Menu.
  
.. image:: /static/training/beginner/qgis-inasafe/image21.*
   :align: center

- QGIS will look something like this:

.. image:: /static/training/beginner/qgis-inasafe/image22.*
   :align: center

**3. Terminology of Geographic Information System (GIS)**

In this section we will open up a QGIS project, and take a look at the
different pieces of the QGIS interface.  If you installed InaSAFE
previously, make sure it is closed by clicking on the X in the upper right
corner of the InaSAFE panel.  If  it isn’t open or you haven’t installed it
yet, carry on.  We will come back to this later.

- Click on the folder icon on the upper toolbar or go to
  :menuselection:`File ‣ Open Project...`

.. image:: /static/training/beginner/qgis-inasafe/image23.*
   :align: center

- Navigate to the tutorial files and go into the :file:`qgis/` directory.
  Open the file named :file:`sleman_2_2.qgs`.
- QGIS should now look something like the following image.  Let’s pause for
  a moment and go over the various components of the QGIS interface.

.. image:: /static/training/beginner/qgis-inasafe/image24.*
   :align: center

**Map Canvas**

This is the window where the map is shown.  Our project has two different
files open, one which shows districts of the Sleman regency,
and another that shows the railway line running through the area.  You can
see both of these files are drawn together in the map canvas.

**Layers List**

On the left side of QGIS is the layers list.
This lists the layers, or files, that are loaded into our QGIS project.
In this project, we have two layers, :file:`Kecamatan_Sleman` and
:file:`railway_Sleman_OSM`.

The layers panel not only shows all the files that are currently open,
it also determines the order that they will be drawn on the map canvas.
A layer that is at the bottom of the list will be drawn first, and any layers
above it will be drawn on top.

- Click on the layer :guilabel:`railway_Sleman_OSM` and drag it below the layer
  named Kecamatan_Sleman.

.. image:: /static/training/beginner/qgis-inasafe/image25.*
   :align: center

- Notice how the map canvas changes.  The railway layer is now shown below
  the district layer, and part of the railway is now obscured.  A map will
  never show railway hidden beneath district areas, so go ahead and move the
  layers back.
- Uncheck the box next to a layer’s name.  It will be hidden from the map
  canvas.
- You can expand collapsed items by clicking the arrow or plus symbol beside
  them.  This will provide you with more information on the layer’s current
  appearance.

.. image:: /static/training/beginner/qgis-inasafe/image26.*
   :align: center

- Right-click on a layer to view a menu with menu extra options.  You’ll be
  using some of them before long, so take a look around!

**Toolbars**

At the top of QGIS are a large number of tools, which are contained within
various “toolbars”.  For example, the File toolbar allows you to save, load,
print, and start a new project.  We already used one of these tools when we
opened this project.

.. image:: /static/training/beginner/qgis-inasafe/image27.*
   :align: center

- By hovering your mouse over an icon, the name of the tool will appear to
  help you identify each tool.
- The number of tools (buttons) can seem a bit overwhelming at first,
  but you will gradually get to know them.  The tools are grouped into related
  functions on toolbars.  If you look closed you can see a vertical array of
  ten dots to the left of each toolbar.  If you grab these with your mouse,
  you can move the toolbar to a more convenient location,
  or separate it so that it sits on its own.

.. image:: /static/training/beginner/qgis-inasafe/image28.*
   :align: center

- If you feel overwhelmed by the number of toolbars, you can customize the
  interface to see only the tools you use most often,
  adding or removing toolbars as necessary.  To add or remove a toolbar,
  right-click on any of the toolbars, or go to :menuselection:`View ‣ Toolbars`.

.. image:: /static/training/beginner/qgis-inasafe/image29.*
   :align: center

- Let’s remove some of the toolbars that we will not be using in this
  training, to make the interface a bit cleaner.  Right-click on the toolbar,
  and uncheck the boxes next to the following toolbars:

    1) Advanced Digitizing
    2) Database
    3) GRASS
    4) Label
    5) Raster
    6) Vector

- After removing these toolbars and moving them around,
  your tools should look like this:

.. image:: /static/training/beginner/qgis-inasafe/image30.*
   :align: center

Even if they are not visible in a toolbar, all of your tools will remain
accessible via the menus. For example, if you remove the **File toolbar** (which
contains the **Save** button), you can still save your map by clicking on the
:guilabel:`File` menu and then clicking on :guilabel:`Save`.

**Status Bar**

This shows information about the current map.  It allows you to adjust the
map scale and see the mouse cursor’s coordinates on the map.

.. image:: /static/training/beginner/qgis-inasafe/image31.*
   :align: center

The coordinates of this map are the same type of coordinates that you
learned about when learning about GPS devices.  The status bar show shows
the longitude and latitude of your mouse cursor.

This may not all be clear right now, but as you progress in your knowledge
of GIS is will make more and more sense.

**4. Add Vector Layer**

Now we will add an additional layer containing roads to our project.

- Click on the :guilabel:`Add Vector Layer` button on the toolbar.

.. image:: /static/training/beginner/qgis-inasafe/image32.*
   :align: center

- A dialog box will open.  Click the :guilabel:`Browse` button.

.. image:: /static/training/beginner/qgis-inasafe/image33.*
   :align: center

- Navigate to the file :file:`qgis/Sleman/Jalan_Sleman_OSM.shp` (in the
  training directory). Select the file and click :guilabel:`Open`.

.. note::  One of the most common file formats are shapefiles,
   which end with the extension .shp.
   Shapefiles are often used to save geodata, and are commonly used with
   GIS applications like QGIS.

- You should now see your new layer appear both in the map canvas and in the
  layers list.  It should be drawn above both the district and railway layers.

.. image:: /static/training/beginner/qgis-inasafe/image34.*
   :align: center

**5. Basic QGIS Tools**

We’ve already taken a look at the QGIS toolbar and seen the tools for
opening a project and adding a new layer.  Here’s a list of some other
commonly used tools.  Feel free to play around with them if you like.  The
important thing for now is to start getting familiar with QGIS.

+-------------------------------------------------------------+--------------------------------------+----------------------------------+
|.. image:: /static/training/beginner/qgis-inasafe/image35.*  | Toggle Editing                       | Edit features in a layer         |
+-------------------------------------------------------------+--------------------------------------+----------------------------------+
|.. image:: /static/training/beginner/qgis-inasafe/image36.*  | Pan Map                              | Drag the map into new location   |
+-------------------------------------------------------------+--------------------------------------+----------------------------------+
|.. image:: /static/training/beginner/qgis-inasafe/image37.*  | Zoom In                              | Zoom in on the Map               |
+-------------------------------------------------------------+--------------------------------------+----------------------------------+
|.. image:: /static/training/beginner/qgis-inasafe/image38.*  | Zoom out                             | Zoom out on the Map              |
+-------------------------------------------------------------+--------------------------------------+----------------------------------+
|.. image:: /static/training/beginner/qgis-inasafe/image39.*  | Zoom Full                            | Zoom so that all layers fit in   |
|                                                             |                                      | the map Window                   |
+-------------------------------------------------------------+--------------------------------------+----------------------------------+
|.. image:: /static/training/beginner/qgis-inasafe/image40.*  | Open Attribute Table                 | Open a layer's attribute table   |
+-------------------------------------------------------------+--------------------------------------+----------------------------------+
|.. image:: /static/training/beginner/qgis-inasafe/image41.*  | Select single feature                | Select a feature in selected     |
|                                                             |                                      | layer                            |
+-------------------------------------------------------------+--------------------------------------+----------------------------------+

**6. Navigate the Map**

- Before we examine the attributes of individual features,
  let’s take a quick look at how to navigate the map.  The main controls for
  moving the map around and zooming in and out are by default on the panels at
  the top of QGIS.

.. image:: /static/training/beginner/qgis-inasafe/image42.*
   :align: center

- When you click on one of these buttons, it changes what you can do with
  your mouse in the main map window.
- Select the first button that looks like a hand.  Now hold your left mouse
  button down and drag your mouse in the map window.  This allows you to pan
  the map, or move it around.
- The button which has a plus sign below a magnifying glass,
  allows you to zoom in on the map.  Select this button.  Using your mouse,
  draw a box around an area that you want to zoom in on,
  and release your mouse.
- The button which has a minus sign below a magnifying glass,
  allows you to zoom out on the map.  Select this button and click on the map.
  This allows you to zoom out.
- The button that looks like a magnifying glass with red arrows pointing
  away from it lets you zoom to the full extent of your map.  When you click
  this button, you will be able to see all of the data that you have loaded
  in your project fit into the map canvas.
