.. image:: /static/training/intermediate/qgis-inasafe/image7.*

..  _planning-evacuation-route:

Module 4: Planning an Evacuation Route Based on Hazard Information
==================================================================

**Learning Objectives**

- Understand the concept of shortest path and fastest route
- Using the Road Graph plugin
- Set up speed and road direction
- Determine start and destination points
- Conduct route analysis and selection

By now you should have a pretty good understanding of how |project_name|
works and its operations.

You know how to add layers, and how to define keywords
so that |project_name| can recognise layers appropriately.
Now that we can use |project_name| effectively to run scenario analyses,
we will look at other QGIS functionality that will help us in preparing
contingency plans.

In this module, we will learn how to perform a GIS analysis in order to
determine an appropriate evacuation route in the event of a disaster.

The term **fastest route** indicates the route a person can take between
point A and point B that will allow them to cover the distance in the least
amount of time.

Similarly, **shortest path** indicates the route that will allow a person to
get from point A to point B with the least distance traveled.
In theory, this would be a straight line between point A and point B,
but in reality this is impractical, because traveling in a straight lines
means climbing hills and going around buildings and fences. Of course this
is why we use roads, and why we calculate fastest and shortest routes using
roads.

We will use the Road Graph plugin in this module, which does just that.
If we provide two points, the plugin is able to calculate either the fastest
route or the shortest path between them.

1. Road Graph plugin
--------------------

We will be continuing with the previous example, which you should have
saved. We won’t be using the |project_name| plugin in this module,
so you may close the panel if you like.

1. Open the project in QGIS.
   
2. We will use a pre-prepared roads layer in this module, which may
   be slightly more detailed than OpenStreetMap.
   Remove the :guilabel:`planet_osm_roads` layer and add 
   :guilabel:`Jalan_Sirahan`,
   which is located in the :file:`qgis/Sirahan/` directory.
   You should have the following layers:

.. image:: /static/training/intermediate/qgis-inasafe/image72.*
   :align: center

3. We will be using a plugin that comes installed with QGIS.
   Right-click on the toolbars to see which toolbars are activated, and select
   :guilabel:`Shortest path`.

.. image:: /static/training/intermediate/qgis-inasafe/image73.*
   :align: center

4. A new plugin window will appear in your project window that looks like this:

.. image:: /static/training/intermediate/qgis-inasafe/image74.*
   :align: center

2. Edit plugin settings
-----------------------

5. We must edit some settings in order for the :guilabel:`Shortest path` plugin
   to work.
   Go to :menuselection:`Vector ‣ Road graph ‣ Settings`.

.. image:: /static/training/intermediate/qgis-inasafe/image75.*
   :align: center

6. Make sure that :guilabel:`hour` and :guilabel:`kilometer` are selected 
   as the units.

7. Set :guilabel:`Topology tolerance` to :kbd:`4`.

8. On the :guilabel:`Transportation layer` tab, select :guilabel:`Jalan_Sirahan` 
   as the layer. This layer contains the streets that the plugin will use to calculate
   routes. The rest will remain the same. It should look like this:

.. image:: /static/training/intermediate/qgis-inasafe/image76.*
   :align: center

9. On the :guilabel:`Default settings` tab, we must fill in the direction and
   speed. Choose :guilabel:`two-way direction` and :kbd:`25` for the speed 
   (meaning 25 km/hr).
   This assumes that traffic can go in both directions at a maximum speed of
   25 km/hr.

.. image:: /static/training/intermediate/qgis-inasafe/image77.*

10. Click :guilabel:`OK`.

3. Choose start and destination points
--------------------------------------

The Road Graph plugin calculates either the shortest or fastest route between
two points, so we need to provide a start point and an end point for an
evacuation route.

Of course an evacuation route should be for all people in an area,
but we can experiment with different start points and see if evacuation
routes will be different in different areas.

11. On the Road Graph panel, click on the plus button next to :guilabel:`Start`
    and then click somewhere on the map to indicate the first point of your
    evacuation route. This would be the initial point for the evacuation route
    in the time of a disaster.

.. image:: /static/training/intermediate/qgis-inasafe/image78.*
   :align: center

Your starting point will be marked as a green point and the coordinates of
the point will be recorded in the :guilabel:`Start` input box.

Now we need to assign the destination of our evacuation route.
Where will people be evacuated to?
Because this is an example, we don’t have a great idea of where an
appropriate place would be. We might use GIS to determine appropriate
locations, which would most likely be high ground in the event of a flood.
For this example, we will choose a destination at the south-east corner of the
village.

12. Click the plus sign next to :guilabel:`Stop` and click somewhere on the map.
    The destination will be marked with a red point.

.. image:: /static/training/intermediate/qgis-inasafe/image79.*
   :align: center

13. Choose :guilabel:`Length` or :guilabel:`Time` next to :guilabel:`Criterion`.
    This determines whether Road Graph will look for the shortest distance or
    the shortest amount of time.

14. Click :guilabel:`Calculate`.

15. The time and distance required for the evacuation route will be displayed.

.. image:: /static/training/intermediate/qgis-inasafe/image80.*
   :align: center

In this example, the length of the fastest route between our two points is
about 1.97 kilometres and the travel time is 0.0788 hours, which is about 5
minutes. The time in our example is determined by the distance and our default
speed of 25 km/hr. The speed can be changed, and can even be set to different
amounts for each segment of road.

The route appears on our map:

.. image:: /static/training/intermediate/qgis-inasafe/image81.*
   :align: center

16. To save the evacuation route as a separate layer, go to
    :menuselection:`Export ‣ New temporary layer`, and click :guilabel:`OK`.

.. image:: /static/training/intermediate/qgis-inasafe/image82.*
   :align: center

17. You may need to choose a CRS for the new layer.
    UTM zone 49S should work fine.

18. The layer will be added to your Layers panel as :guilabel:`shortest_path`, 
    but you still need to save the layer.

19. To save, right-click on the layer and click :guilabel:`Save as…`

Summary
-------

In this module we’ve learned how to calculate the shortest distance between
two points using the Road Graph plugin. Using this you can easily determine
evacuation routes from various areas. Evacuation routes are important for
contingency plans, and those living in threatened areas can be educated with
the quickest and safest routes to take in the event of an emergency.


:ref:`Go to next module --> <calculating-damages-and-losses>`