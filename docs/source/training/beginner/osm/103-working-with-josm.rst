.. image:: /static/training/beginner/osm/image6.*

..  _working-with-josm:

Module 3: Working with JOSM
===========================

**Learning Objectives**

- Download JOSM                           
- Install JOSM                            
- Set JOSM preferences                    
- Use basic tools                         
- Draw nodes and ways in JOSM             
- Change objects                          
- Add tags to objects using presets menu

In this module we will learn step by step how to download and install JOSM,
the Java OpenStreetMap editor. We will change some of the settings in JOSM
to make it easier to use. Then we will open a sample map and learn some of
the basic operations of the software. Remember in Module 1 when we asked you
to draw a map of your town or village? We will conclude this module by
drawing your map again, this time digitally. After this you should have a
good understanding of how to draw maps in JOSM.

1. Download JOSM
----------------

- There is a copy of JOSM in the :file:`software` folder that of the package that
  accompanies this guide.  If you don’t have this or would like the most
  up-to-date version, follow the instructions here.  Otherwise skip 
  to :ref:`install-josm`.
- Open your web browser - this may be Firefox, Chrome, Opera,
  or Internet Explorer.
- In the address bar at the top of the window, enter the following text and
  press Enter: `josm.openstreetmap.de <http://josm.openstreetmap.de>`_
- You can also find this website by searching for JOSM.

- The website should look something like this:

.. image:: /static/training/beginner/osm/image17.*
   :align: center

- If you have Windows installed on your computer, click
  :guilabel:`Windows Installer` to download JOSM. If you have a different
  operating system, click on the link for your system. Your download should
  begin. In this module we will assume that you are using Windows, but the
  instructions are similar for other operating systems.

..  _install-josm:

2. Install JOSM
---------------

- You may have problems installing JOSM if Java is not already installed on
  your computer.  You can install Java by running :file:`jre-7u21-windows-i586`
  in the :file:`software` folder.  You can also download it here:
  `http://www.java.com/en/download/ <http://www.java.com/en/download/>`_
- Find the JOSM install file on your computer.  It should be named
  :file:`josm-setup.exe`. Double-click it to begin setup.
- Click :guilabel:`OK`, :guilabel:`Next`, :guilabel:`I Agree`, and
  :guilabel:`Install`. When the installation is complete, click
  :guilabel:`Finish` to launch JOSM for the first time. Later, when you want
  to start JOSM, you can do so by clicking on the :guilabel:`Start Menu` in
  the lower left corner of your computer, and clicking the program JOSM.
- You may see a window pop up that asks if you want to update the software.
  You don’t need to update it since it is new.  Press the button that says
  :guilabel:`Cancel`. If you don’t ever want to see this message again,
  check the box at the bottom before pressing :guilabel:`Cancel`
- When JOSM starts, it will look something like this:

.. image:: /static/training/beginner/osm/image18.*
   :align: center

3. Change JOSM Settings
-----------------------

Before we begin using JOSM, it’s a good idea to change some of the settings
so that it will be easier to use. To change the settings,
go to :menuselection:`Edit -> Preferences`.

.. image:: /static/training/beginner/osm/image19.*
   :align: center

3.1. Add Bing Imagery
.....................

.. note:: This may be unnecessary if Bing Imagery is already activated in your
   copy of JOSM.

- We want to be able to use satellite imagery when we are making our maps,
  so let’s add that from the Preferences window. On the left side of the
  Preferences window there are different icons for different settings. Click
  on the icon that says :guilabel:`WMS TMS`. You may need to click on the down
  arrow to find it:

.. image:: /static/training/beginner/osm/image20.*
   :align: center

.. image:: /static/training/beginner/osm/image21.*
   :align: center

- Click on :guilabel:`Bing Sat`. Then Click :guilabel:`Activate`.

.. image:: /static/training/beginner/osm/image22.*
   :align: center

- You should now see :guilabel:`Bing Sat` in the list below the
  :guilabel:`Activate` button.

3.2. Add Presets
................

- We will be using presets so that we can add special data to OpenStreetMap.
  Don’t worry if this is unclear right now - we will learn more about it as
  we go along.
- You should still have the Preferences window open. If you don’t,
  click :menuselection:`Edit ‣ Preferences` to open the window.
- On the left side, click the icon that looks like a grid.

 .. image:: /static/training/beginner/osm/image23.*
    :align: center

- Click the tab at the top that reads :guilabel:`Tagging Presets`.
- Under ':guilabel:`Available Presets` find and select the entry labelled
  :kbd:`Buildings Indonesia` Then click the blue arrow to the right of this box.

.. image:: /static/training/beginner/osm/image24.*
   :align: center

- Click :guilabel:`OK`.

3.3. Add Plugins
................

- Plugins provide extra functionality for specific purposes. JOSM has many 
  plugins that can be downloaded.
- To download the plugins that we need, we must first open the Preferences
  window.
- In the Preferences window, click the :guilabel:`Plugin` icon to
  the left:

.. image:: /static/training/beginner/osm/image25.*
   :align: center

- On the plugin tab, first you need to download the plugin list by
  clicking :guilabel:`Download list`. It may take a few minutes.
- After the plugin list appears, type the name of the plugin you want to
  download in the :guilabel:`Search` box.

.. image:: /static/training/beginner/osm/image26.*
   :align: center

- When the plugin is found, check the box to the left of the plugin name.
- Click :guilabel:`OK` to download and install the plugins.

.. note:: Skim through the list to see what sort of additional
   features are available through plugins.

3.4. Change Language
....................

- JOSM has been translated into many languages. If it has been translated
  into your language, you can change it in the Preferences.
- If you don’t have the Preferences window open, click
  :menuselection:`Edit ‣ Preferences`.
- On the left side, click the icon that looks like a paint can and paintbrush.
- At the top of the window, click the tab that says :guilabel:`Look and Feel`.
- Choose your language in the dropdown box next to the word :guilabel:`Language`.
- Click :guilabel:`OK`.

.. image:: /static/training/beginner/osm/image27.*
   :align: center

- You need to restart JOSM to save your settings. Go 
  to :menuselection:`File -> Exit`.
- Start JOSM again by going to the Windows :guilabel:`Start Menu` in the
  bottom left corner. Find JOSM and click on it to start.

4. Learn Basic Drawing with JOSM
--------------------------------

- Now let’s open up a sample OSM file which we will use to learn the basic
  ways to draw maps with JOSM. Note that this map is not real,
  in that it is not a real map of a real place, so we will not save it on
  OpenStreetMap.
- The file is located in :file:`osm` and is named :file:`sample.osm`.
- Let’s open the sample map file in JOSM. Open JOSM. Go 
  to :menuselection:`Open`.

 .. image:: /static/training/beginner/osm/image28.*
    :align: center

- Find the file :file:`sample.osm`. Click on it, and then click :guilabel:`Open`.
- You should now see a sample map, similar to this:

.. image:: /static/training/beginner/osm/image29.*
   :align: center

4.1. Basic Operations
.....................

- To move the map left or right, up or down, hold your right mouse button
  down, and move your mouse.
- There are several ways to zoom in and out of the map. If you have a mouse,
  you can use your scroll wheel to zoom in and out. If you are using a laptop
  and don’t have a mouse, you can zoom in and out using the scale bar in the
  upper left of the map window. Drag the bar left and right by holding your
  left mouse down and moving the bar left or right with your mouse.

.. image:: /static/training/beginner/osm/image30.*
   :align: center

- Look at the sample map. There are a few different types of objects here. There
  is a river, a forest, some buildings, several roads, and a couple of shops.
  To select an object, click on it with your left mouse button.

4.2. Points, Lines, and Shapes (polygon)
........................................

- As you click different objects on the sample map, notice that there are
  three different types of objects on the map. There are points, lines,
  and shapes. In mapping, shapes are usually called *polygons*.
- Points are a single location, represented by symbols. On this sample map,
  there are two points, a clothing shop and a market. The clothing shop is
  represented by a shirt symbol, and the market is represented by a shopping
  cart.
- There are several lines on the map as well, which represent roads. If you
  look closely you will see that within the lines, there are points as well.
  These points don’t have any symbols or other information associated with
  them, but they help to define where the line is located.
- Lastly, there are numerous shapes on the sample map,
  representing different places - a forest, a river, and buildings. A shape
  generally represents an area, like a field or a building. A shape is
  exactly like a line - the only difference is that the line begins at the
  same point where it ends.
- You may notice that when you select an object, a list appears to the right
  of the map in a window called :guilabel:`Properties`. These are known as tags.
  **Tags** are information that is tied to a point, line or shape that describes
  what it is. For now all you need to know is that this information helps
  describe whether our object is a forest, a river, a building, or something
  else.
- Think about drawing a map by hand, and how you are also drawing points,
  lines, and shapes. What other places are best represented by points? Lines?
  Shapes?

Now, let’s try to practice drawing an object (point, line and shape).

- On the left side of JOSM is a column of buttons. Many of these buttons
  open new panels on the right side that provide more information about the
  map. The most important buttons are at the top of the column.
  These buttons change what you can do with your mouse.
- The top four buttons in this column are the most important. They allow you
  to: :guilabel:`Select`, :guilabel:`Draw`, :guilabel:`Zoom in`,
  :guilabel:`Delete`
- Until now, you have been using the :guilabel:`Select` tool, which looks like
  this:

.. image:: /static/training/beginner/osm/image31.*
   :align: center

- Before you draw, you need to make sure that nothing is selected. Click in
  the black space on the map, where it is empty, to make sure nothing is
  selected.
- Click on the second button, the :guilabel:`Draw` tool.

.. image:: /static/training/beginner/osm/image32.*
   :align: center

- Find an empty area on the map, and double-click with your mouse.
  This will draw a single point.
- To draw a line, single-click with your mouse. Move your mouse and
  click again. Continue until you are happy with your line. To end the line,
  double-click your mouse.
- Draw a shape the same way that you draw a line, but finish the shape by
  double-clicking on the point where you started the line.

4.3. Changing Objects
.....................

- Select the forest on the left side of the map. Be sure to click on the
  line around the forest, not one of the points on the line. Now hold your
  left mouse button down and drag your mouse. You should be able to move the
  forest to a new location on the map.
- Click on one of the points on the line around the forest. Hold your left
  mouse button down and drag your mouse. You should be able to move the point.
  This is how you can change the shape of an object, or move a point.

4.4. Add Presets
................

- Now we know how to draw points, lines and shapes,
  but we still haven’t defined what they represent. We want to be able to say
  that our points are shops, schools, or something else,
  and whether our shapes are fields, buildings, or something else.
- Click on the :guilabel:`Select` tool, in the column of buttons on the left.

.. image:: /static/training/beginner/osm/image31.*
   :align: center

- Select one of the objects that you drew with the :guilabel:`Draw tool`. On the
  top menu, click :menuselection:`Presets`. Move your mouse through the sub-menu
  to the type of location you would like to define.
- When you click on a preset, a form will pop up asking you for more
  information. You do not have to fill in every field, but you may wish to add
  some of the important fields, such as the name of the object.
- When you are finished entering the information, click :guilabel:`Apply Preset`
  . If everything went well, your point, line, or shape should change colors or
  show a symbol. This is because you have defined what it is.

Exercise:
.........

Now let’s draw a map in order to practice the techniques you have learned.
You may wish to redraw the map that you drew on paper in Module 1.

- Drag the window away from the sample map by holding the right mouse button and
  dragging your mouse, until you have a nice empty area to draw on.
- Use the Draw tool to create points, lines, and shapes. Describe what your
  objects are by selecting from the Presets menu.
- When you are finished, you should have your own map,
  similar to the sample map that we opened in :file:`sample.osm`.

:ref:`Go to next module --> <using-gps>`
