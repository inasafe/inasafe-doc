.. _introduction-of-qgis:

Introduction to QGIS
====================

.. image:: /static/training/socialisation/010_qgis_logo.png
   :align: left

**Objectives:**

* Basic understanding of QGIS and its layout
* Basic setup of QGIS
* Installation of |project_name| Plugins
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

Quantum GIS (QGIS) is a user friendly Open Source Geographic Information
System (GIS).  It runs on Linux, Unix, Mac OSX, Windows and Android and
supports numerous vector, raster, and database formats and functionality.
`<http://www.qgis.org>`_

Quantum GIS provides a continuously growing number of capabilities provided
by core functions and plugins. You can visualize, manage, edit, analyse data,
and compose printable maps.
QGIS is also the platform of |project_name|, and hence the basic of QGIS will
be taught in the workshop.

Why QGIS?
---------

As information becomes increasingly spatially aware, there is no shortage of
tools able to full fill some or all commonly used GIS functions. Why should
anyone be using QGIS over some other GIS software package?

Here are only some of the reasons:

* It's free, as in lunch. Installing and using the QGIS program costs you a
  grand total of zero money. No initial fee, no recurring fee, nothing.
* It's free, as in liberty. If you need extra functionality in QGIS,
  you can do more than just hope it will be included in the next release. You
  can sponsor the development of a feature, or add it yourself if you are
  familiar with programming.
* It's constantly developing. Because anyone can add new features and improve
  on existing ones, QGIS never stagnates. The development of a new tool can
  happen as quickly as you need it to.
* Extensive help and documentation is available. If you're stuck with
  anything, you can turn to the extensive documentation,
  your fellow QGIS users, or even the developers.
* Cross-platform. QGIS can be installed on MacOS, Windows and Linux.

An overview of the Interface
----------------------------

The elements identified in the figure below are:

1. Layers list
2. Toolbars
3. Map canvas
4. Status bar

.. image:: /static/training/socialisation/011_interface.PNG
   :align: center

===================
Begin Practical
===================

Setup QGIS
----------

#. :guilabel:`Open Quantum GIS Desktop (1.8.0)` - This should be located on
   your desktop, or you can find it in your start menu.

.. image:: /static/training/socialisation/012_qgis_desktop.png
   :align: center

#. A hint window will come up, :guilabel:`Click Ok`.

.. image:: /static/training/socialisation/013_tips.png
   :align: center

Clean up tool bar
.................

To provide more space for your map canvas we will uncheck the tools we will not be 
using today.

#. :guilabel:`Right Click` the toolbar and :guilabel: `Uncheck`, *Advance Digitising*,
   *Database*, *Digitising*, *File*, *Grass*, *OpenStreetMap*, *Raster*,
   *Vector*, *Web*.
#. Rearrange toolbar so its just one line, `Left Click` and `Hold`
   the vertical dots on the left hand side of the tool.  
   Drag to the first line of the toolbar.

.. image:: /static/training/socialisation/014_verticaldots.PNG
   :align: center

.. Note:: For future work you may want to add these tool back into your
   toolbar, this is as simple as right clicking on the toolbar and turning it
   back on.

Your QGIS toolbar should go from 3 lines to 1 line:

.. image:: /static/training/socialisation/015_toolbar_clean.PNG
   :align: center

Option Window
.............

To change the projection settings and acknowledge that QGIS is multilingual

#. Go to Options window: :menuselection:`Settings --> Options`
#. :guilabel:`Select` the **CRS** tab of the options menu

.. image:: /static/training/socialisation/016_crs.PNG
   :align: center

#. :guilabel:`Check` *Enable on the fly reprojection by default* - This will
   enable that all spatial layers irrespective of their projection will
   follow the CRS allocated above

.. image:: /static/training/socialisation/017_onthefly.PNG
   :align: center

.. Note:: This  will become default in the new version of QGIS 2.0

#. :guilabel:`Select` on the **Locale** tab of the options menu

.. image:: /static/training/socialisation/018_locale.PNG
   :align: center

#. :guilabel:`Check` *Override system locale*, scroll through all the languages
   that QGIS have been translated into! We will stick with english for this
   training, so no action is needed - :guilabel:`Uncheck` *Override system locale*.

.. image:: /static/training/socialisation/019_locale_select.PNG
   :align: center

.. Note:: |project_name| is dependent on Locale, but it has only been
   translated into bahasa Indonesian so far. World Bank is currently funding
   for the translation of |project_name| into French and Portugal

#. :guilabel:`Ok` in the bottom right corner of the Options window


Installing Plugins
------------------

|project_name|
..............

Installing |project_name| through the QGIS plugin repository

.. Note:: You must be connected to the internet for this section

#. Go to :menuselection:`Plugins --> Fetch Python Plugins...` 
   This will take a couple of minutes for QGIS to contact its repository and 
   show the list of plugins available

#. Type :kbd:`inasafe` into the filter box

.. image:: /static/training/socialisation/020_inasafe_plugin.png
   :align: center

#. :guilabel:`Select` |project_name| and :guilabel:`Install plugin` -
   this will take a couple of minutes for the plugin to download and install.
   
#. A window should pop up saying: "Plugin installed successfully" :guilabel:`Ok`
   and :guilabel:`Close` the *QGIS Python Plugin Installer* window.

#. You should now have an |project_name| panel on the right hand side of your
   screen.

.. image:: /static/training/socialisation/021_inasafe_gettingstarted.png
   :align: center

|project_name| also comes with a toolbar of its own

#. To retrieve the |project_name| toolbar, :guilabel:`Right Click` on the top
   tool bar and :guilabel:`Recheck` *plugin*

.. image:: /static/training/socialisation/022_inasafetoolbar.png
   :align: center

============================================    ====================================
**Symbol**										**Name**
--------------------------------------------	------------------------------------
.. image:: /static/general/icon_dock			Toggle Dock
.. image:: /static/general/icon_keywords		Keyword Editor
.. image:: /static/general/icon_rest			Reset Dock
.. image:: /static/general/icon_options			Options
.. image:: /static/general/icon_impactfunctions	Impact Functions Browser
.. image:: /static/general/icon_minimumneeds	Minimum Needs Tool
.. image:: /static/general/icon_converter		Converter
.. image:: /static/general/icon_batch			Batch Runner
.. image:: /static/general/icon_save			Save Current Scenario
.. image:: /static/general/icon_osm				OpenStreetMap downloader
============================================    ====================================

.. Note:: Later we will explore and use these tools.

For more information :doc:`../user-docs/toolbar`

OpenLayer Plugin
.................

Installing OpenLayer through the QGIS plugin repository

#. Go to :menuselection:`Plugins --> Fetch Python Plugins`. This will take a
   couple of minutes for QGIS to contact its repository and show the list of
   plugins available.
#. Type :kbd:`openlayers` into the filter box.
#. :guilabel:`Select` *OpenLayer Plugin* then :guilabel: `Install plugin` - this will
   take a couple of minutes for the plugin to download and install.
#. A window should pop up saying: "Plugin installed successfully"  :guilabel:`Ok`
   and :guilabel:`Close` the *QGIS Python Plugin Installer* window.
#. Hover mouse over :menuselection:`Plugins --> OpenLayer Plugin`

.. image:: /static/training/socialisation/023_openlayer.PNG
   :align: center

#. :guilabel:`Select` *Add Bing Aerial layer*

.. image:: /static/training/socialisation/024_aerial_bing.png
   :align: center

.. Note:: If you are familiar with Goggle Earth, navigating this imagery
   should be very similar.

**Activity:** Navigate to your home
...................................

Using the navigation tools below, zoom into your home.

============================================    ====================================
**Symbol**										**Name**
--------------------------------------------	------------------------------------
.. image:: /static/general/icon_pan				Pan Map
.. image:: /static/general/icon_zoomin			Zoom In
.. image:: /static/general/icon_zoomout			Zoom Out
.. image:: /static/general/icon_zoomfull		Zoom to Full
.. image:: /static/general/icon_zoomlast		Zoom Last
.. image:: /static/general/icon_zoomnext		Zoom Next
============================================    ====================================

#. :guilabel:`Click` *zoom In*, draw a box (click and drag) over your country.

#. :guilabel:`Click` *Pan Map*, shift the map so your country is in the
   centre of the screen.

.. Note:: If you make a mistake in your zooming, use *Zoom Last* tool.

#. Navigate to your own house or work 

**Indonesia**

.. image:: /static/training/socialisation/025_indonesia.png
   :align: center

**Jakarta**

.. image:: /static/training/socialisation/026_jakarta.png
   :align: center
   
**Menara Thamrin**
.. image:: /static/training/socialisation/027_mt.png
   :align: center

.. Note:: To use openlayers you must have connection to the Internet!
