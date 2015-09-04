.. image:: /static/training/old-training/beginner/qgis-inasafe/image7.*

..  _basics-of-qgis:

Module 3: The Basics of QGIS
============================

**Learning Objectives**

- Download QGIS
- Install QGIS
- Open a previously created QGIS project
- Understand the layers panel
- Access basic tools through the toolbar
- Clean up the toolbar
- Show a map in the map window
- Get information on an active map through the status bar

In this module we begin using QGIS.
We’ll see how to install the software and
understand the layout, interface and core functions of the software.
By the end of this module, you’ll be on your way to becoming a competent GIS
user!

Note that if you have previously installed QGIS, feel free to skip ahead to 
:ref:`section three <terminology-of-gis>`.
Otherwise, let’s start here and get QGIS installed.

1. Getting QGIS
---------------
1. Open your web browser and in the address bar at the top of the window,
   type :kbd:`qgis.org`.
   Press :guilabel:`Enter`.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image9.*
   :align: center

The QGIS website will look something like this:

.. image:: /static/training/old-training/beginner/qgis-inasafe/image10.*
   :align: center

2. Click :guilabel:`Download Now`.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image11.*
   :align: center

3. If you are using Windows click
   :guilabel:`QGIS Standalone Installer Version 2.8 (32 bit)`.
   Your exact version number may be different.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image12.*
   :align: center

4. If you are not using Windows, select your operating system from the menu.
   Follow the installation instructions.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image13.*
   :align: center

5. When the file is downloaded, run it and follow the instructions to install
   QGIS.

2. Installing QGIS
------------------

6. Open the folder where you have the QGIS installation file.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image14.*
   :align: center

7. Run the installation file. If you are installing QGIS version 2.x,
   it should look like this:

.. image:: /static/training/old-training/beginner/qgis-inasafe/image15.*
   :align: center

8. Click :guilabel:`Next`.

9. Click :guilabel:`I Agree` to agree with the conditions in the licence
   agreement.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image16.*
   :align: center

10. The next window asks where you would like to install QGIS.
    In most cases, the default should be fine.
    Click :guilabel:`Next`.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image17.*
   :align: center

11. In the next window, Click :guilabel:`Install` without checking any of the
    boxes.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image18.*
   :align: center

QGIS will begin to install. It may take a few minutes to complete.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image19.*
   :align: center

12. Click :guilabel:`Finish` to complete the installation.
    Your computer will automatically reboot.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image20.*
   :align: center

13. Now open QGIS from the Start Menu.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image21.*
   :align: center

QGIS will look something like this:

.. image:: /static/training/old-training/beginner/qgis-inasafe/image22.*
   :align: center

..  _terminology-of-gis:

3. Terminology of Geographic Information Systems (GIS)
------------------------------------------------------

Next we will open up a QGIS project, and take a look at the
different pieces of the QGIS interface.
If you installed |project_name| previously, make sure it is closed by
clicking on the X in the upper right corner of the |project_name| panel.
If it isn’t open or you haven’t installed it yet, carry on.
We will come back to this later.

14. Click on the folder icon on the upper toolbar or go to
    :menuselection:`Project ‣ Open...`

.. image:: /static/training/old-training/beginner/qgis-inasafe/image23.*
   :align: center

15. Navigate to the tutorial files and go into the :file:`qgis/` directory.
    Open the file named :file:`sleman_2_2.qgs`.

QGIS should now look something like the following image.
Let’s pause for a moment and go over the various components of the QGIS
interface.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image24.*
   :align: center

Map canvas
..........
This is the window where the map is shown.
Our project has two different files open, one which shows districts of the
Sleman regency, and another that shows the railway line running through the
area.
Both of these files are drawn together in the map canvas.

Layers panel
............
On the left side of QGIS is the layers panel.
This lists the layers, or files, that are loaded into our QGIS project.
In this project, we have two layers, :file:`Kecamatan_Sleman` and
:file:`railway_Sleman_OSM`.

The layers panel not only shows all the files that are currently open,
it also determines the order that they will be drawn on the map canvas.
A layer that is at the bottom of the list will be drawn first, and any layers
above it will be drawn on top.

16. Click on the layer :guilabel:`railway_Sleman_OSM` and drag it below the layer
    named :guilabel:`Kecamatan_Sleman`.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image25.*
   :align: center

Notice how the map canvas changes.
The railway layer is now shown below the district layer,
and part of the railway is now obscured.
A map should never show railway hidden beneath district areas,
so go ahead and move the layers back.

17. Uncheck the box next to a layer’s name.
    It will be hidden from the map canvas.

18. Expand collapsed items by clicking the arrow or plus symbol beside them.
    This will provide you with more information on the layer’s current
    appearance.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image26.*
   :align: center

19. Right-click on a layer to view a menu with extra options.
    You’ll be using some of them before long, so take a look around!

Toolbars
........
At the top of QGIS are a large number of tools, which are contained within
various “toolbars”.
For example, the :guilabel:`File` toolbar allows you to save, load, print
and start a new project.
We already used one of these tools when we opened this project.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image27.*
   :align: center

By hovering your mouse over an icon, the name of the tool will appear to
help you identify each tool.
The number of tools (buttons) can seem a bit overwhelming at first,
but you will gradually get to know them.
The tools are grouped into related functions on toolbars.
If you look closely you can see a vertical array of ten dots to the left of
each toolbar.
By grabbing these with your mouse, you can move the toolbar to a more
convenient location, or separate it so that it sits on its own.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image28.*
   :align: center

If you feel overwhelmed by the number of toolbars, you can customise the
interface to see only the tools you use most often,
adding or removing toolbars as necessary.

20. To add or remove a toolbar, right-click on any of the toolbars,
    or go to :menuselection:`View ‣ Toolbars`.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image29.*
   :align: center

21. Let’s remove some of the toolbars that we will not be using in this
    training, to make the interface a bit cleaner.
    Right-click on the toolbar, and uncheck the boxes next to the following
    toolbars:

    1. Advanced Digitising
    2. Database
    3. GRASS
    4. Label
    5. Raster
    6. Vector

22. After removing these toolbars and moving them around,
    your tools should look like this:

.. image:: /static/training/old-training/beginner/qgis-inasafe/image30.*
   :align: center

Even if they are not visible in a toolbar, all of your tools will remain
accessible via the menus.
For example, if you remove the :guilabel:`File` toolbar (which contains the 
:guilabel:`Save` button), you can still save your map by going to 
:menuselection:`Project ‣ Save`.

Status Bar
..........
The status bar shows information about the current map.
It allows you to adjust the map scale and see the mouse cursor’s coordinates
on the map.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image31.*
   :align: center

The coordinates of this map are the same type of coordinates that are
recorded by GPS devices.
The status bar shows the longitude and latitude of your mouse cursor.

This may not all be clear right now, but as you progress in your knowledge
of GIS, this will make more and more sense.

..  _adding-vector-layer:

4. Adding a vector layer
------------------------
Now we will add an additional layer containing roads to our project.

23. Click on the :guilabel:`Add Vector Layer` button on the toolbar.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image32.*
   :align: center

24. A dialog box will open. Click the :guilabel:`Browse` button.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image33.*
   :align: center

25. Navigate to the file :file:`qgis/Sleman/Jalan_Sleman_OSM.shp` (you may need
    to unzip the file :file:`Sleman.zip` first). Select the file and 
    click :guilabel:`Open`.

.. note::
   One of the most common file formats are shapefiles,
   which end with the extension :file:`.shp`.
   Shapefiles are often used to save geodata, and are commonly used with
   GIS applications like QGIS.

26. You should now see your new layer appear both in the map canvas and in the
    layers panel.
    It should be drawn above both the district and railway layers.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image34.*
   :align: center

5. Basic QGIS tools
-------------------
We’ve already taken a look at the QGIS toolbar and seen the tools for
opening a project and adding a new layer.
Here’s a list of some other commonly used tools.
Feel free to play around with them if you like.
The important thing for now is to start getting familiar with QGIS.

+-------------------------------------------------------------+--------------------------------------+----------------------------------+
|.. image:: /static/training/old-training/beginner/qgis-inasafe/image35.*  | Toggle Editing                       | Edit features in a layer         |
+-------------------------------------------------------------+--------------------------------------+----------------------------------+
|.. image:: /static/training/old-training/beginner/qgis-inasafe/image36.*  | Pan Map                              | Drag the map into new location   |
+-------------------------------------------------------------+--------------------------------------+----------------------------------+
|.. image:: /static/training/old-training/beginner/qgis-inasafe/image37.*  | Zoom In                              | Zoom in on the map               |
+-------------------------------------------------------------+--------------------------------------+----------------------------------+
|.. image:: /static/training/old-training/beginner/qgis-inasafe/image38.*  | Zoom Out                             | Zoom out on the map              |
+-------------------------------------------------------------+--------------------------------------+----------------------------------+
|.. image:: /static/training/old-training/beginner/qgis-inasafe/image39.*  | Zoom Full                            | Zoom so that all layers fit in   |
|                                                             |                                      | the map window                   |
+-------------------------------------------------------------+--------------------------------------+----------------------------------+
|.. image:: /static/training/old-training/beginner/qgis-inasafe/image40.*  | Open Attribute Table                 | Open a layer's attribute table   |
+-------------------------------------------------------------+--------------------------------------+----------------------------------+
|.. image:: /static/training/old-training/beginner/qgis-inasafe/image41.*  | Select Single Feature                | Select a feature in selected     |
|                                                             |                                      | layer                            |
+-------------------------------------------------------------+--------------------------------------+----------------------------------+

6. Navigating the map
---------------------
Before we examine the attributes of individual features,
let’s take a quick look at how to navigate the map.
The main controls for moving the map around and zooming in and out are by
default on the panels at the top of QGIS.

.. image:: /static/training/old-training/beginner/qgis-inasafe/image42.*
   :align: center

When you click on one of these buttons, it changes what you can do with
your mouse in the main map window.

27. Select the first button that looks like a hand.
    Now hold the left mouse button down and drag the mouse in the map window.
    This allows you to pan the map, or move it around.

28. The button that has a plus sign below a magnifying glass
    allows you to zoom in on the map.
    Select this button.
    Using your mouse, draw a box around an area where you want to zoom in,
    and release your mouse.

29. The button that has a minus sign below a magnifying glass
    allows you to zoom out on the map.
    Select this button and click on the map.

30. The button that looks like a magnifying glass with red arrows pointing
    away from it lets you zoom to the full extent of your map.
    Click this button to see all of the data that
    is loaded in the project fit into the map canvas.


:ref:`Go to next module --> <qgis-plugins>`
