.. image:: /static/training/beginner/qgis-inasafe/image7.*

Module 4: QGIS Plugin
=====================

**Learning Objectives**

- Understand the Concept of Plugins
- Install QGIS Plugins
- Add satellite imagery via OpenLayers

QGIS has core functionality, which we will continue to explore in this guide,
but it also allows the use of additional plugins, which allow you to add
functionality to the software.
Again, these plugins are free. To use them, you simply need to connect to the
internet and install.
In this chapter we will learn how to install QGIS plugins,
using one plugin to add a satellite imagery layer to our QGIS project.
If you have closed QGIS since completing the previous chapter,
start it again and open up the project that you saved at the end of the
chapter.
If you didn’t save where we left off, don’t worry, simply open the project
:file:`named sleman_2_3.qgs` in the :file:`qgis/ folder`.

Note that you must be connected to the internet to follow the exercises in this
chapter.

**1. Managing Plugins**

To install new plugins, they first need to be downloaded, and then activated.
Some plugins are already downloaded and available, and you can see them by going
to :menuselection:`Plugins ‣ Manage and Install Plugins`.

.. image:: /static/training/beginner/qgis-inasafe/image43.*
   :align: center

This displays a list of plugins that have already been downloaded and can be
activated.  To enable a plugin, check the box next to it in this menu and press
OK.  For now, let’s leave all the plugins as they are.  We’re going to download
and activate a new plugin in the next section.

.. image:: /static/training/beginner/qgis-inasafe/image44.*
   :align: center

**2. Installing Plugins**

There are many more plugins, but they must first be downloaded.  To download a
plugin, go to :menuselection:`New`.  This will load available plugin repositories, and you will see a list of all available plugins for download.

.. image:: /static/training/beginner/qgis-inasafe/image45.*
   :align: center

Note that plugins which have already been downloaded can be activated or
deactivated from the :menuselection:`Installed` menu.  If it has not yet
been downloaded, downloading a plugin from the
:menuselection:`New` menu will automatically activate it.

**3. The OpenLayers Plugin**

The OpenLayers plugin allows you to view various web maps as a layer in QGIS.
This means that you can access the OSM slippy map, Google Maps, and Bing maps,
from within QGIS.  Follow along and we’ll see what this means.

- Go to :menuselection:`Plugins ‣ Manage and Install Plugins ‣ New ` and type
  :kbd:`openlayers` into the Filter box.

.. image:: /static/training/beginner/qgis-inasafe/image46.*
   :align: center

- Select :guilabel:`OpenLayers Plugin` from the list and click
  :guilabel:`Install plugin`.

.. image:: /static/training/beginner/qgis-inasafe/image47.*
   :align: center

- It may take a few minutes to download.

.. image:: /static/training/beginner/qgis-inasafe/image48.*
   :align: center

- When the download finishes click :guilabel:`OK`.

.. image:: /static/training/beginner/qgis-inasafe/image49.*
   :align: center

- Now the OpenLayers plugin is installed and activated.  If you go Installed
  you will see it now in your list of active plugins. Click close after you finished.

.. image:: /static/training/beginner/qgis-inasafe/image50.*
   :align: center

- Now we have new menus options that offer extra functionality.
  :menuselection:`Go to Plugins ‣ OpenLayers plugin` and you will see various
  options of map layers that you can load.

.. image:: /static/training/beginner/qgis-inasafe/image51.*
   :align: center

- Click on :menuselection:`Bing Aerial layer`. A new layer, called “Bing Aerial”
  will be added to your layers list, and the imagery will load on your map
  canvas.  If the layer is above your other layers, drag it to the bottom of the
  layers list.

.. image:: /static/training/beginner/qgis-inasafe/image52.*
   :align: center

- Your project should now look like this:

.. image:: /static/training/beginner/qgis-inasafe/image53.*
   :align: center


- If you pay attention, there is something wrong with the maps. Can you guess
  what is it? All three layers above Bing Aerial layers should be shown on the 
  map. It is not shown because of Rendering Order setting on Layer Order Panel. 
  To fix this, go to :menuselection:`View → Panel`, Activate 
  :guilabel:`Layer order` panel

.. image:: /static/training/beginner/qgis-inasafe/image54.*
   :align: center

- Then, Layer order panel will shows next to Layers panel (1). Click that panel 
  and Uncheck Control Rendering Order to fix the problem (2)

.. image:: /static/training/beginner/qgis-inasafe/image55.*
   :align: center

- Then back to Layers panel, and you can see the map should shows in correct 
  order. All layers above Bing Aerial will shows up on the map canvas like 
  image below.

.. image:: /static/training/beginner/qgis-inasafe/image56.*
   :align: center

- Adding a layer such as Bing Aerial Imagery will change the Coordinate
  Reference System, or CRS, of your project. Essentially this means that your
  project is not using longitude and latitude coordinates anymore. This
  shouldn’t affect you right now, but it will make sense later when we cover
  CRSes.
- If the map data does not appear to match up with the aerial imagery, it may be
  due to different CRSes.  You can fix this problem by going to
  :menuselection:`Project ‣ Project Properties` and checking the box next to
  :guilabel:`Enable ‘on the fly’ CRS` Transformation`.

.. image:: /static/training/beginner/qgis-inasafe/image57.*
   :align: center

.. image:: /static/training/beginner/qgis-inasafe/image58.*
   :align: center

- Cool!  Now we can see our map data on top of an aerial photograph of the
  earth!  Note that this is the same imagery provided by Microsoft Bing that you
  would load for editing in JOSM.  Try unchecking the box next to the layer
  Kecamatan_Sleman so that you can see the area better.  If you zoom in close
  you can see detailed imagery with our streets and railway layers displayed on
  top.

.. image:: /static/training/beginner/qgis-inasafe/image59.*
   :align: center

- Remove the Bing Aerial layer by right-clicking it in the layers list and
  selecting :guilabel:`Remove`.

- Try out other layers that are available to you from the
  :menuselection:`Plugins ‣ OpenLayers plugin` menu.
