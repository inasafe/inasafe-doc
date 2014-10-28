.. image:: /static/training/beginner/qgis-inasafe/image7.*

..  _qgis-plugins:

Module 4: QGIS Plugins
======================

**Learning Objectives**

- Understand the concept of plugins
- Install QGIS plugins
- Add satellite imagery via OpenLayers

QGIS has core functionality, which we will continue to explore in this guide,
but it also allows the use of plugins, which add
functionality to the software.
Again, these plugins are free. To use them, we simply need to connect to the
internet and install.
In this chapter we will learn how to install QGIS plugins,
using one plugin to add a satellite imagery layer to our QGIS project.

1. If you have closed QGIS since completing the previous module, start QGIS and
   open the project :file:`named sleman_2_3.qgs` in the :file:`qgis/` folder.

Note that you must be connected to the internet to follow the exercises in this
chapter.

1. Managing plugins
-------------------
To install new plugins, they first need to be downloaded, and then activated.
Some plugins are already downloaded and available.

2. Go to :menuselection:`Plugins ‣ Manage and Install Plugins...` to view them.

.. image:: /static/training/beginner/qgis-inasafe/image43.*
   :align: center

3. This displays a list of plugins that have already been downloaded and can be
   activated. To enable a plugin, check the box next to it in this menu and 
   press :guilabel:`OK`. For now, let’s leave all the plugins as they are. 
   We’re going to download and activate a new plugin in the next section.

.. image:: /static/training/beginner/qgis-inasafe/image44.*
   :align: center

..  _installing-plugins:

2. Installing plugins
---------------------
4. There are many more plugins, but they must first be downloaded.  To download 
   a plugin, click the :guilabel:`New` tab. This will load available plugin 
   repositories, and you will see a list of all available plugins for download.

.. image:: /static/training/beginner/qgis-inasafe/image45.*
   :align: center

Note that plugins which have already been downloaded can be activated or
deactivated from the :guilabel:`Installed` tab.  If it has not yet
been downloaded, downloading a plugin from the
:guilabel:`New` tab will automatically activate it.

3. The OpenLayers plugin
------------------------
The OpenLayers plugin allows you to view various web maps as a layer in QGIS.
This means that you can access the OSM slippy map, Google Maps and Bing Maps
from within QGIS. Follow along and we’ll see how this works.

5. Go to :menuselection:`Plugins ‣ Manage and Install Plugins` and click on the
   :guilabel:`New` tab. Type :kbd:`openlayers` into the Search box.

.. image:: /static/training/beginner/qgis-inasafe/image46.*
   :align: center

6. Select :guilabel:`OpenLayers Plugin` from the list and click
   :guilabel:`Install plugin`.

.. image:: /static/training/beginner/qgis-inasafe/image47.*
   :align: center

It may take a few minutes to download.

.. image:: /static/training/beginner/qgis-inasafe/image48.*
   :align: center

7. When the download finishes click :guilabel:`OK`.

.. image:: /static/training/beginner/qgis-inasafe/image49.*
   :align: center

8. Now the OpenLayers plugin is installed and activated. Click the 
   :guilabel:`Installed` tab to see it in your list of active plugins. 
   Click :guilabel:`Close` when you are finished.

.. image:: /static/training/beginner/qgis-inasafe/image50.*
   :align: center

9. The new plugin provides a menu which offers extra functionality. Go to 
   :menuselection:`Plugins ‣ OpenLayers plugin` to see various
   map layers that can be loaded.

.. image:: /static/training/beginner/qgis-inasafe/image51.*
   :align: center

10. Click :menuselection:`Bing Aerial layer`. A new layer called “Bing Aerial”
    will be added to the layers list, and the imagery will load in the map
    canvas. If the layer is above your other layers, drag it to the bottom of the
    layers list.

.. image:: /static/training/beginner/qgis-inasafe/image52.*
   :align: center

Your project should now look like this:

.. image:: /static/training/beginner/qgis-inasafe/image53.*
   :align: center

If you pay attention, there is something wrong with the map. Can you guess
what it is? All three layers above Bing Aerial layers should be shown on the 
map.

11. To fix this, go to :menuselection:`View ‣ Panels` and check the box next
    to :menuselection:`Layer order`.

.. image:: /static/training/beginner/qgis-inasafe/image54.*
   :align: center

12. The Layer order panel will appear next to the Layers panel (1). Click it
    and uncheck :guilabel:`Control Rendering Order`.

.. image:: /static/training/beginner/qgis-inasafe/image55.*
   :align: center

13. Return to the Layers panel. The map layers should now appear in the correct
    order. All layers above Bing Aerial will show up on the map canvas as in
    the image below.

.. image:: /static/training/beginner/qgis-inasafe/image56.*
   :align: center

Adding a layer such as Bing Aerial will change the Coordinate
Reference System, or CRS, of your project. Essentially this means that your
project is not using longitude and latitude coordinates anymore. This
shouldn’t affect you right now, but it will make sense later when we cover
CRSes.

14. If the map data does not appear to match up correctly with the aerial 
    imagery, it may be due to different CRSes.  You can fix this problem by 
    going to :menuselection:`Project ‣ Project Properties` and checking the 
    box next to :guilabel:`Enable ‘on the fly’ CRS transformation`.

.. image:: /static/training/beginner/qgis-inasafe/image57.*
   :align: center

.. image:: /static/training/beginner/qgis-inasafe/image58.*
   :align: center

15. Great! Now we can see our map data on top of an aerial photograph of the
    Earth. Note that this is the same imagery provided by Microsoft Bing that 
    you would load for editing in JOSM. Try unchecking the box next to the 
    layer :guilabel:`Kecamatan_Sleman` so that you can see the area better. 
    Zoom in close to see detailed imagery with our street and railway layers 
    displayed on top.

.. image:: /static/training/beginner/qgis-inasafe/image59.*
   :align: center

16. Remove the Bing Aerial layer by right-clicking it in the Layers panel and
    clicking :guilabel:`Remove`.

17. Try out other layers that are available from the
    :menuselection:`Plugins ‣ OpenLayers plugin` menu.


:ref:`Go to next module --> <map-projection-basics>`
