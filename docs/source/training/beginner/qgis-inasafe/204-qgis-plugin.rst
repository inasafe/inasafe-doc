.. image:: /static/beginner/qgis-inasafe/image6.png

********
Module 4
********
QGIS Plugin
===========

**Learning Objectives**

- Understand the Concept of Plugins
- Install QGIS Plugins
- Add satellite imagery via OpenLayers

QGIS has core functionality, which we will continue to explore in this guide, but it also allows the use of additional plugins, which allow you to add functionality to the software.  Again, these plugins are free.  To use them, you simply need to connect to the internet and install.  In this chapter we will learn how to install QGIS plugins, using one plugin to add a satellite imagery layer to our QGIS project.
If you have closed QGIS since completing the previous chapter, start it again and open up the project that you saved at the end of the chapter.  If you didn’t save where we left off, don’t worry, simply open the project named sleman_2_3.qgs in the qgis/ folder.

Note that you must be connected to the internet to follow the exercises in this chapter.

**1. Managing Plugins**

To install new plugins, they first need to be downloaded, and then activated.  Some plugins are already downloaded and available, and you can see them by going to Plugins ‣ Manage Plugins.

.. image:: /static/beginner/qgis-inasafe/image42.png
 
This displays a list of plugins that have already been downloaded and can be activated.  To enable a plugin, check the box next to it in this menu and press OK.  For now, let’s leave all the plugins as they are.  We’re going to download and activate a new plugin in the next section.

.. image:: /static/beginner/qgis-inasafe/image43.png
 
**2. Installing Plugins**

There are many more plugins, but they must first be downloaded.  To download a plugin, go to Plugins ‣ Fetch Python Plugins.  This will load available plugin repositories, and you will see a list of all available plugins for download.

.. image:: /static/beginner/qgis-inasafe/image44.png
 
Note that plugins which have already been downloaded can be activated or deactivated from the “Manage Plugins” menu.  If it has not yet been downloaded, downloading a plugin from the “Fetch Python Plugins” menu will automatically activate it.

**3. The OpenLayers Plugin**

The OpenLayers plugin allows you to view various web maps as a layer in QGIS.  This means that you can access the OSM slippy map, Google Maps, and Bing maps, from within QGIS.  Follow along and we’ll see what this means.

- Go to Plugins ‣ Fetch Python Plugins and type “openlayers” into the Filter box.
 
.. image:: /static/beginner/qgis-inasafe/image45.png

- Select “OpenLayers Plugin” from the list and click “Install plugin.”

.. image:: /static/beginner/qgis-inasafe/image46.png
 
- It may take a few minutes to download.

.. image:: /static/beginner/qgis-inasafe/image47.png
 
- When the download finishes click OK.

.. image:: /static/beginner/qgis-inasafe/image48.png
 
- Click “Close” on the Fetch Plugins window.
- Now the OpenLayers plugin is installed and activated.  If you go to Plugins ‣ Manage Plugins... you will see it now in your list of active plugins.

.. image:: /static/beginner/qgis-inasafe/image49.png
 
- Now we have new menus options that offer extra functionality. Go to Plugins ‣ OpenLayers plugin and you will see various options of map layers that you can load.

.. image:: /static/beginner/qgis-inasafe/image50.png 

- Click on “Bing Aerial layer.”  A new layer, called “Bing Aerial” will be added to your layers list, and the imagery will load on your map canvas.  If the layer is above your other layers, drag it to the bottom of the layers list. 

.. image:: /static/beginner/qgis-inasafe/image51.png
 
- Your project should now look like this:

.. image:: /static/beginner/qgis-inasafe/image52.png
 

- Adding a layer such as Bing Aerial Imagery will change the Coordinate Reference System, or CRS, of your project. Essentially this means that your project is not using longitude and latitude coordinates anymore. This shouldn’t affect you right now, but it will make sense later when we cover CRSes.
- If the map data does not appear to match up with the aerial imagery, it may be due to different CRSes.  You can fix this problem by going to Settings ‣ Project Properties... and checking the box next to “Enable ‘on the fly’ CRS Transformation.”
- Cool!  Now we can see our map data on top of an aerial photograph of the earth!  Note that this is the same imagery provided by Microsoft Bing that you would load for editing in JOSM.  Try unchecking the box next to the layer Kecamatan_Sleman so that you can see the area better.  If you zoom in close you can see detailed imagery with our streets and railway layers displayed on top.

.. image:: /static/beginner/qgis-inasafe/image53.png
 
- Remove the Bing Aerial layer by right-clicking it in the layers list and selecting “Remove.”
- Try out other layers that are available to you from the Plugins ‣ OpenLayers plugin menu.







 

 