Introduction to QGIS
====================

.. image:: /static/socialisation/qgis_logo.png
   :align: center
  
**Objectives:**

* Basic understanding of QGIS and its layout
* Basic setup of QGIS
* Installation of InaSAFE Plugins
* Installation of OpenLayers Plugin
* Navigation of QGIS using Microsoft bing imagery

**Expected Results:**

Participants are able to:

* Identify basic elements of QGIS layout
* Customise toolbar
* Enable "on the fly reprojection by default"
* Change QGIS to a different language
* Install plugin
* Use the navigational toolset

Introduction
------------

Quantum GIS (QGIS) is a user friendly Open Source Geographic Information System (GIS).  It runs on Linux, Unix, Mac OSX, Windows and Android and supports numerous vector, raster, and database formats and functionality. `<http://www.qgis.org>`_

Quantum GIS provides a continuously growing number of capabilities provided by core functions and plugins. You can visualize, manage, edit, analyse data, and compose printable maps.

QGIS is also the platform of InaSAFE, and hence the basic of QGIS will be taught in the workshop.

Why QGIS?
---------

As information becomes increasingly spatially aware, there is no shortage of tools able to full fill some or all commonly used GIS functions. Why should anyone be using QGIS over some other GIS software package?

Here are only some of the reasons:

* It's free, as in lunch. Installing and using the QGIS program costs you a grand total of zero money. No initial fee, no recurring fee, nothing.
* It's free, as in liberty. If you need extra functionality in QGIS, you can do more than just hope it will be included in the next release. You can sponsor the development of a feature, or add it yourself if you are familiar with programming.
* It's constantly developing. Because anyone can add new features and improve on existing ones, QGIS never stagnates. The development of a new tool can happen as quickly as you need it to.
* Extensive help and documentation is available. If you're stuck with anything, you can turn to the extensive documentation, your fellow QGIS users, or even the developers.
* Cross-platform. QGIS can be installed on MacOS, Windows and Linux.

An overview of the Interface
----------------------------

The elements identified in the figure below are:

1. Layers list
2. Toolbars
3. Map canvas
4. Status bar

.. image:: /static/socialisation/interface.PNG
   :align: center
   
Setup QGIS
----------

#. :guilabel:`Open Quantum GIS Desktop (1.8.0)` - This should be located on your desktop, or you can find it in your start menu.

.. image:: /static/socialisation/qgis.png
   :align: center

#. A hint window will come up, :guilabel:`click okay`.

.. image:: /static/socialisation/tips.png
   :align: center

Clean up tool bar
.................

To provide more space for your map canvas you will now choose to display the tools we will use today.

#. :guilabel:`Right click` the toolbar and unmark, *Advance Digitising*, *Database*, *Digitising*, *File*, *Grass*, *OpenStreetMap*, *Raster*, *Vector*, *Web*.
#. Rearrange toolbar so its just one line, by holding down the left mouse button over the dots on the left hans side of the tool, and dragging the bar to where ever you would like to put it.

.. image:: /static/socialisation/toolbar.PNG
   :align: center
   
.. Note:: For future work you may want to add these tool back into your toolbar, this is as simple as right clicking on the toolbar and turning it back on.

Your QGIS should now look like this:

.. image:: /static/socialisation/toolbar_2.PNG
   :align: center
   
Option Window
.............

To change the projection settings and acknowledge that QGIS is multilingual

1. Go to Options window: **Settings/options**
2. :guilabel:`Click` on the CRS tab

.. image:: /static/socialisation/crs.PNG
   :align: center
   
3. :guilabel:`Check Enable` 'on the fly' reprojection by default - This will enable that all spatial layers irrespective of their projection will follow the CRS allocated above

.. image:: /static/socialisation/enable.PNG
   :align: center
   
.. Note:: This  will become default in the new version of QGIS (2.0),

4. :guilabel:`Click` on the Locale tab

.. image:: /static/socialisation/locale.PNG
   :align: center
   
5. :guilabel:`Check` Override system locale, scroll through all the languages that QGIS have been translated into! We will stick with english for this training, so no action is needed - un-check Override system locale.

.. image:: /static/socialisation/options2.PNG
   :align: center
   
.. Note:: InaSAFE is dependent on Locale, but it has only been translated into bahasa Indonesian so far. World Bank is currently funding for the translation of InaSAFE into French and Portugal

6. :guilabel:`Click` "Okay" in the bottom right corner of the Options window


Installing Plugins
------------------

InaSAFE
........

Installing InaSAFE through the QGIS plugin repository

.. Note:: You must be connected to the internet for this section

1. Go to **Plugins/Fetch Python Plugins...** This will take a couple of minutes for QGIS to contact its repository and show the list of plugins available
2. Type *inasafe* into the filter box

.. image:: /static/socialisation/inasafe_plugin.png
   :align: center

3. :guilabel:`Select` InaSAFE and :guilabel:`click Install plugin` - this will take a couple of minutes for the plugin to download and install
4. A window should pop up saying: "Plugin installed successfully" - Click okay and then close the QGIS python plugin installer window
5. You should now have an InaSAFE panel on the right hand side of your screen

.. image:: /static/socialisation/inasafe_tools.png
	:align: center
	
InaSAFE also comes with a toolbar of its own

6. To retrieve the InaSAFE toolbar, :guilabel:`right click` on the top tool bar and :guilabel:`recheck "plugin"`

.. image:: /static/socialisation/tools_inasafe.png
   :align: center
	
7. Read to below to familiarise yourself with the InaSAFE tool set 

.. image:: /static/socialisation/inasafe_toolbar2.PNG
   :align: center

.. Note:: Later we will explore and use these tools

OpenLayer Plugin
.................

Installing OpenLayer through the QGIS plugin repository

1. Go to :menuselection:`Plugins --> Fetch Python Plugins`. This will take a couple of minutes for QGIS to contact its repository and show the list of plugins available
2. Type openlayers into the filter box
3. :guilabel:`Select` "OpenLayer Plugin" and click Install plugin - this will take a couple of minutes for the plugin to download and install
4. A window should pop up saying: "Plugin installed successfully" - Click okay and then close the QGIS python plugin installer window
5. :guilabel:`Click on Plugins`, and hover your mouse over OpenLayers plugin

.. image:: /static/socialisation/openlayer1.PNG
   :align: center
   
6. Select **Add Bing Aerial layer**

.. image:: /static/socialisation/aerial_bing.png
   :align: center
	
.. Note:: If you are familiar with Goggle Earth, navigating this imagery should be very similar

7. :guilabel:`Click` on the zoom in tool, then draw a box (click and drag) over your country.
8. Click on the Pan Map tool to shift the map so your country is in the centre of the screen

.. Note:: If you make a mistake in your zooming, use zoom to last tool

9. Now navigate to your own house. (optional)

.. image:: /static/socialisation/navigation.PNG
   :align: center

Indonesia

.. image:: /static/socialisation/indonesia.png
   :align: center
	
My home in Jakarta

.. image:: /static/socialisation/home.png
   :align: center
	
.. Note:: To use openlayers you must have connection to the Internet!
