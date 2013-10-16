.. image:: /static/training/intermediate/osm/image6.png


Module 1: Advanced Editing
==========================

**Learning Objectives**

- Use Advanced Editing Tools in JOSM
- Make relations among objects

Welcome to the intermediate guide for spatial data collection with OpenStreetMap.  In the previous unit you learned how to draw points, lines, and shapes in JOSM; how to open your GPS waypoints and tracks in JOSM; and how to download, edit, and upload your changes on OpenStreetMap. In this chapter, we will describe relations, JOSM editing tools and editing techniques in greater detail.

Note: While this chapter is not extremely advanced, it is a step higher than the previous chapters. If you don’t feel like you fully understand the lessons leading up to this, you may wish to practice a little bit more before continuing.

Topics covered in this chapter:

1. Advanced Editing Tools
2. Relations
3. Editing Techniques:  The Dos and Don’ts
4. Keyboard Shortcuts

**1. Advanced Editing Tools**

There are a few ways you can access more editing tools in JOSM.  We will look more at the default tools, some plug-ins and then keyboard editing shortcuts.

*1.1 Default Drawing tools*

JOSM has some additional tools to make it easier to draw lines and shapes. These tools are found in the “Tools” menu at the top of JOSM.

.. image:: /static/training/intermediate/osm/image7.png

In order to apply the functions in this menu, you must first select a point, line or shape in the map window. Some of the most useful functions are described here:

- **Split Way:** This allows you to divide a line into two separate lines. This is useful if you want to add different attributes to different parts of a road, such as a bridge. To use this function, select a point in the middle of the line that you want to split, Select Split Way from the Tools menu, and your line should be split in two.

.. image:: /static/training/intermediate/osm/image8.png

- **Combine Way:** This does the opposite of Split Way. To combine two lines into a single line, they must share a single point. To use this function, select both lines that you want to combine. You can select more than one object by holding the SHIFT key on your keyboard and clicking on each line. When you have selected both lines, select Combine Way from the Tools menu.

.. image:: /static/training/intermediate/osm/image9.png

Note that you are combining roads that have different directions, you might get this warning:

.. image:: /static/training/intermediate/osm/image10.png

If the roads are connected and go in the same direction, then choose “Reverse and Continue.”

- **Reverse Way:** This will change the direction of the line. If the line incorrectly represents a road or river that is one way, you may want to change its direction.  Unless someone has intentionally created a way to be one way you do not usually have to worry about altering the direction because ways in OSM default to both ways.

.. image:: /static/training/intermediate/osm/image11.png

- **Simplify Way:** If your line has too many points in it and you’d like to make it simpler, this will remove some of the points from a line.

.. image:: /static/training/intermediate/osm/image12.png

- **Create Circle OR Align Nodes in Circle:** If you are trying to make a circular shape, draw the circle as best you can and then select three nodes and the function. It will help arrange your points in a circle.

.. image:: /static/training/intermediate/osm/image13.png

- **Align Nodes in Line:** This function will align a series of points into a straight line.  With long lines it is best to select sections of the line to straighten.  Be careful as this does have the tendency to shift the line a little.

.. image:: /static/training/intermediate/osm/image14.png

- **Orthogonalize Shape:** This function is very useful for drawing regular shapes such as buildings. After you draw an area, this function will reshape it to have square corners. This feature is most useful for other regularly shaped features, such as tennis courts, or landuse areas. (Using the Building Plugin, which will be explained below, might be easier).

.. image:: /static/training/intermediate/osm/image15.png

- **Unglue way:** This tools allows you to detach nodes that are connected.

.. image:: /static/training/intermediate/osm/image16.png

Note that the line and node will not actually appear separate as the last screen shot implies.

*1.2 Plug-ins*

**Building Plug-in**

.. image:: /static/training/intermediate/osm/image17.png

This plug-in is by far one of the most useful tools for editing (digitizing).  Install it as with any other plugin.  It will appear as an icon on the left hand toolbar.  The functionality of this tool is explained here:

The Building tool allows you to create shapes with 90 degree corners with just three clicks.  First, you trace the edge of your building and then you drag out the line to make it a polygon.

.. image:: /static/training/intermediate/osm/image18.png


.. image:: /static/training/intermediate/osm/image19.png

You can also create more complicated buildings by using the merge option.  Create your building outline, select all of the polygons (press SHIFT to highlight them all) and then hit **SHIFT + J** to merge the objects.

.. image:: /static/training/intermediate/osm/image20.png

**Utilsplugin2 (More Tools)**

The plugin utilsplugin2 has several features that are also useful for editing.

.. image:: /static/training/intermediate/osm/image21.png

After you install this plugin, a new menu will appear called “More Tools.”

.. image:: /static/training/intermediate/osm/image22.png

The following tools are generally the most useful:

- **Add Nodes at Intersections:**  This tool is very helpful for adding missing nodes in intersections of selected ways.  It is good practice that roads and rivers should always have common nodes where they intersect.

.. image:: /static/training/intermediate/osm/image23.png

- **Copy Tags from Previous Selection:**  This function makes copying tags easier.  If you want to create many objects with the same tags, first draw the objects.  Then add the tags to one object.  Click on another object and press Shift + R to copy the tags from the previously selected object.  You can do this for all objects that you want to tag.  Remember that the tags will be copied from the previously selected object, so if you click on an untagged object and then another untagged object, you will not be able to copy any tags.

.. image:: /static/training/intermediate/osm/image24.png

- **Add Source Tag:** This tool simplifies adding a source tag.  It remembers the source that was specified last and adds it as remembered source tag to your objects.   You can insert the source with just one click.

- **Replace Geometry:** This tool is great if you want to redraw a poorly shaped object, but want to keep the history, attributes and ID number of that object.  For example, if you come across a building that is complicated and drawn in a poor fashion, then instead of painfully changing each node, you can (2) just draw the object again (3) select the old and new object (4) press ¨Replace Geometry¨ to transfer all the information over.

.. image:: /static/training/intermediate/osm/image25.png

**Utilsplugin2** also provides a new selection menu that provides more tools:

.. image:: /static/training/intermediate/osm/image26.png

These tools have proved to be the most useful:

- **Unselect Nodes:**  This tool allows you deselect nodes, which makes it useful for tagging the objects selected.  This tool is necessary if you have mapped several polygon objects with similar attributes and would like to tag the objects without tagging the nodes.  To do so, select all of the objects-- polygons, ways and relations-- unselect the nodes and tag appropriately.

.. image:: /static/training/intermediate/osm/image27.png

- **Select Last Modified Nodes:**  This tool permits you to go back to the nodes that you most recently changed.  It is like undo: node style.

**2.  Relations**

In the first unit we learned that there are three types of objects that can be drawn in OpenStreetMap - points (nodes), lines (ways), and polygons.  Lines contain numerous points, and the line itself carries the attributes that define what it represents.  Polygons are the same as lines, except that the the line must finish where it begins in order to form a shape.

In fact, there is one other type of object in OpenStreetMap, and these are called relations.  In the same way that a line consists of other points, a relation contains a group of other objects, be they points, lines, or polygons.  If you are looking to obtain advanced editing skills, then understanding and knowing how to properly edit relations is important.

For example, imagine that you want to map a building that has courtyards in the center.  You would need to draw a polygon around the outside of the building, and you would want a other polygons around the courtyards to indicate that they are not part of the building.  This is an example of a relation.  The relation would contain several polygons - and the attributes of the building would be attached to the relation, not the polygons.

.. image:: /static/training/intermediate/osm/image28.png

Relations are used to represent anything that requires a collection of objects to define.  Other examples are bus routes (a collections of lines), long and complex objects (rivers or roads), or multiple polygons that are all part of one location (like buildings in a university).

There are mainly four types of relations you will encounter in OSM: **Multipolygons, Routes, Boundaries and Restrictions** (such as, no left turns).  In this section we will go over Multipolygons and Routes.

*2.1 Editing Relations*

The multipolygon above contains a polygon for the outer limits of the building and two more to mark the inner courtyards. To create a relation from these three polygons you need to:

1. Select all of the polygons.
2. Go to Tools ‣ Create multipolygon

.. image:: /static/training/intermediate/osm/image29.png

3. The polygons should automatically be created as a multi-polygon.

.. image:: /static/training/intermediate/osm/image30.png

You will then see your building as a a solid shape with the inner polygons represented with gaps. The data behind the relation in this example is visible on OpenStreetMap:  You can see this multipologyon on OSM by going to http://www.openstreetmap.org/browse/relation/2435797. It will appear on OpenStreetMap like this:

.. image:: /static/training/intermediate/osm/image31.png

*2.2  Another MultiPolygon*

This river is another example of a multiploygon. Effectively it is the same as the building example, but with a greater number of members and covering a much larger area. It can be viewed on the OpenStreetMap site here: http://www.openstreetmap.org/browse/relation/1046961.

.. image:: /static/training/intermediate/osm/image32.png

.. image:: /static/training/intermediate/osm/image33.png

*This river contains ten ways that are connected like a long polygon.*

*2.3  Linestring Relations*

Relations are also very useful for creating, labeling and editing large linestrings; for example, bus routes, hiking trails, bicycle paths, etc.  These differ from multipolygons because they are relations with members, as supposed to complex areas.  A linestring could simply be one line with multiple members, these can be tagged as such. Additional features, such as bus stops represented by separate nodes can also be tagged as relation members.

.. image:: /static/training/intermediate/osm/image34.png

.. image:: /static/training/intermediate/osm/image35.png

1. Make sure that all of the ways in which the route runs along are appropriately tagged.  For example, **highway = footway**.
2. Select all of the highways or ways that the bus takes. If you would only like to select certain parts of the way, then, sadly, you must divide the way into the section you would like to select.  This creates more work, but you can easily do it with the  **¨Split Way¨** tool.  Once some or all of the ways are selected, click Edit in the relation panel.  The relation editing dialog will pop up.
3. Go to the Presets Menu and down at the bottom click ¨Public Transport¨ and then **¨Route¨** or **¨Route Master¨**.   Route master is the main route that a bus takes, while route is a variant path of the bus.

.. image:: /static/training/intermediate/osm/image36.png

4. Fill in the corresponding information about the bus route.

.. image:: /static/training/intermediate/osm/image37.png

Relations are difficult to understand and do not have to be used often, but they are necessary to know about.  As you get more developed with your OSM skills and want to create more complex building, river and routes, relations will be useful.

**3. Editing Tips**

In this section we will go over some common mistakes in JOSM and provide some editing tips for making your maps great!

*3.1  Some Objects Should Not Connect*

When you are creating polygons and lines that are not supposed to be connected, make sure that they are not merged together by sharing a node.  For example, highway nodes should not be snapped to buildings, because no one likes a road that leads directly into a wall!  If you want to disentangle two or more obejcts that share the same node, select the node and press **G**

.. image:: /static/training/intermediate/osm/image38.png

.. image:: /static/training/intermediate/osm/image39.png

*But, Some Objects Should Connect*

However, some objects **SHOULD connect!**  Road intersections should always be snapped together.  If two roads do not share a common node, then the computer has no way of knowing that the roads actually connect to each other.

.. image:: /static/training/intermediate/osm/image40.png

*3.2 Overlapping Objects*

A common error is to have overlapping polygons when the objects they represent do not overlap in real life.  A building cannot overlap another building.  This mistake is commonly made with buildings and landuse polygons.  For example, a polygon drawn to represent a park outside a building should not overlap with the building.  Instead it should be drawn next to the building.

There are some exceptions to this rule, such as schools.  Within a school yard you might identify individual buildings using polygons, yet you also might want to create a polygon around the entire school yard.  In this case it is fine for the polygons to overlap, but the rule to follow here is to make sure that the buildings are completely inside the landuse polygon.

.. image:: /static/training/intermediate/osm/image41.png

.. image:: /static/training/intermediate/osm/image42.png

We all make mistakes, and as you map more you will make less mistakes!  Just remember that even if you upload data that contains mistakes, it is simple to fix your mistakes and upload the change again.  This is what is great about OSM, you can always make it better!

*3.3  Tracing Correctly*

OSM can do amazing things with identifying where objects end and what labels these objects should have; however, it needs your help in doing so.  For example, if you create a road that turns into another road without a distinct node, then JOSM will continue labeling the road as the previous one.  Therefore, it is necessary that you make all of your roads and objects as clearly and rigid as possible.

.. image:: /static/training/intermediate/osm/image43.png

**4. Keyboard Shortcuts**

Lastly, let’s cover a topic that can save a lot of time when you’re editing.  Sometimes it can be annoying to repeatedly click to select different options and menus in JOSM.  Luckily there are shortcut keys on the keyboard that allow you to do many common tasks.  Here is a list of some of the most commonly used shortcut keys, along with what they do:

+----------------------------------------------------------+-------------------------------------+
| .. image:: /static/training/intermediate/osm/image44.png | Chooses the Select tool             |
+----------------------------------------------------------+-------------------------------------+
| .. image:: /static/training/intermediate/osm/image45.png | Deletes Selected Object             |
+----------------------------------------------------------+-------------------------------------+
| .. image:: /static/training/intermediate/osm/image46.png | Chooses the Draw Tool               |
+----------------------------------------------------------+-------------------------------------+
| .. image:: /static/training/intermediate/osm/image47.png | Chooses the Zoom tool               |
+----------------------------------------------------------+-------------------------------------+
| .. image:: /static/training/intermediate/osm/image48.png | Zoom in                             |
+----------------------------------------------------------+-------------------------------------+
| .. image:: /static/training/intermediate/osm/image49.png | Zoom out                            |
+----------------------------------------------------------+-------------------------------------+
| .. image:: /static/training/intermediate/osm/image50.png | Split way                           |
+----------------------------------------------------------+-------------------------------------+
| .. image:: /static/training/intermediate/osm/image51.png | Combine Way                         |
+----------------------------------------------------------+-------------------------------------+
| .. image:: /static/training/intermediate/osm/image52.png | Align in circle                     |
+----------------------------------------------------------+-------------------------------------+
| .. image:: /static/training/intermediate/osm/image53.png | Align in line                       |
+----------------------------------------------------------+-------------------------------------+
| .. image:: /static/training/intermediate/osm/image54.png | Orthogonalize (make a shape square) |
+----------------------------------------------------------+-------------------------------------+





 
