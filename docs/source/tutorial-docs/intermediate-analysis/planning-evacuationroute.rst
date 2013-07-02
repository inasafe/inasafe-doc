Planning an Evacuation Route
============================

Learning Objectives
--------------------
* Understand the concept of shortest path and fastest route
* Use the Road Graph Plugin
* Set up speed and road direction
* Determine start and destination point
* Conduct route analysis and selection


Introduction
-------------
By now you should have a pretty good understanding of how InaSAFE works and its operations.  You know how to add the appropriate layers, and how to define keywords to the layers so that InaSAFE can recognize them appropriately.  Now that we can use InaSAFE effectively to run scenario analyses, we will look at other QGIS functionality that will help us in preparing contingency plans.  In this chapter, we will learn how to perform a GIS analysis in order to determine an appropriate evacuation route in the event of a disaster.


The term fastest route indicates the route a person can take between point A and point B that will allow them to cover the distance in the least amount of time.  Similarly, shortest path indicates the route that will allow a person to get from point A to point B with the least distance traveled.  In theory, this would be a straight line between point A and point B, but in reality this is impractical, because traveling in a straight lines means climbing hills and going around buildings and fences.  Of course this is why we use roads, and why we calculate fastest and shortest routes using roads.  We will use the Road Graph plugin in this chapter, which does just that.  If we provide two points, the plugin is able to calculate either the fastest route or the shortest path between them.


### 1.  Road Graph Plugin

* We will be continuing with the previous example, which you should have saved.  Open the project in QGIS.  We won’t be using the InaSAFE plugin in this chapter, so you may close the panel if you like.
* Also, we will be using a pre-prepared roads layer in this section, which may be slightly more detailed than OpenStreetMap.  Remove the planet_osm_roads layer and add Jalan_Sirahan, which is located in the qgis/Sirahan/ directory.  You should have the following layers:
.. image:: /static/tutorial/intermediate-analysis/4_layer.png
* We will be using a plugin that has already come installed with QGIS.  Right-click on the toolbars to see which toolbars are activated, and select “Shortest path.”
.. image:: /static/tutorial/intermediate-analysis/4_shortestpath.png
* A new plugin window will appear in your project window that looks like this:
.. image:: /static/tutorial/intermediate-analysis/4_shortestpathbox.png


### 2.  Edit Plugin Settings

* We must edit some settings in order for the “Shortest path” plugin to work.  Go to Vector ? Road graph ? Settings.
.. image:: /static/tutorial/intermediate-analysis/4_vector.png
* Make sure that “hour” and “kilometer” are selected as the units.
* “Topology tolerance” should be set to 4.
* On the “Transportation layer” tab, select ***Jalan_Sirahan*** as the layer.  This layer contains the streets that the plugin will use to calculate routes.  The rest will remain the same.  It should look like this:
.. image:: /static/tutorial/intermediate-analysis/4_roadgraph1.png


* On the “Default settings” tab, we must fill in the direction and speed.  Choose “two-way direction” and 25 for the speed (meaning 25 km/hr).  This assumes that traffic can go in both directions and a maximum speed of 25 km/hr.
.. image:: /static/tutorial/intermediate-analysis/4_roadgraph2.png


* Click OK.


### 3.  Choose Start and End Points

The Road Graph plugin calculates either the shortest or fastest route between two points, so we need to provide a start point and an end point for an evacuation route.  Of course an evacuation route should be for all people in an area, but we can experiment with different start points and see if evacuation routes will be different in different areas.

* On the Road Graph panel, click on the plus button next to “Start” and then click somewhere on the map to indicate the first point of your evacuation route.  This would be the initial point for the evacuation route in the time of a disaster.
.. image:: /static/tutorial/intermediate-analysis/4_start.png
* Your starting point will be marked as a green point and the coordinates of the point will be recorded in the “Start” input box.
* Now we need to assign the destination of our evacuation route.  Where will people be evacuated to?  Because this is an example, we don’t have a great idea of where an appropriate place would be.  We might use GIS to determine appropriate locations, which would most likely be high ground in the event of a flood.  For this example, we will choose a destination at the SouthEast corner of the village.
* Click the plus sign next to “Stop” and click somewhere on the map.  The destination will be marked with a red point.
.. image:: /static/tutorial/intermediate-analysis/4_stop.png
* You can choose “Length” or “Time” next to Criterion.  This determines whether Road Graph will look for shortest distance or shortest amount of time.
* Click “Calculate.”
* The time and distance required for the evacuation route will be displayed.
.. image:: /static/tutorial/intermediate-analysis/4_length.png


* In this example, the length of the fastest route between our two points is about 1.97 kilometers and the travel time is 0.0788 hours, which is about 5 minutes.  This time in our example is determined by the distance and our default speed of 25 km/hr.  This speed can be changed, and can even be set to different amount for each segment of road.
* The route is also drawn on our map
.. image:: /static/tutorial/intermediate-analysis/4_route.png


* To save the evacuation route as a separate layer, click on Export ? New temporary layer, and click OK.
.. image:: /static/tutorial/intermediate-analysis/4_exportfeature.png


* You may need to choose a CRS for the new layer.  UTM zone 49S should work fine.
* The layer will be added to your Layers list as shortest_path, but you still need to save the layer.
* To save, right-click on the layer and click “Save as…”
 
**Summary**
In this chapter we’ve learned how to calculate the shortest distance between two points using the Road Graph plugin.  Using this you can easily determine evacuation routes from various areas.  Evacuation routes are important for contingency plans, and those living in threatened areas can be educated with the quickest and safest routes to take in the event of an emergency.