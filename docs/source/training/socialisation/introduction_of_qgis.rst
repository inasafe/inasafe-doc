.. _introduction-to-qgis:

Getting Started
===============

.. image:: /static/training/socialisation/010_qgis_logo.*
   :align: right
   :scale: 30 %

In this section we introduce |QGIS| and set it up for this
|project_name| practical. If you are already familiar with
QGIS, feel free to skip below to the QGIS setup and plugin installation.

**Learning Objectives:**

* Understand QGIS and its layout
* Set up QGIS
* Customise toolbar
* Change QGIS to a different language
* Install |project_name| plugin
* Install OpenLayers plugin
* Navigate QGIS using Microsoft Bing imagery


Introduction to QGIS
--------------------

QGIS is a user-friendly open source Geographic Information System (GIS).
It runs on Linux, OS X, Windows and Android, and supports numerous
vector, raster, and database formats and functionality.
`<http://www.qgis.org>`_

QGIS provides a continuously growing number of capabilities provided
by core functions and plugins.
You can visualise, manage, edit, analyse data and compose printable maps.
QGIS is also the platform which |project_name| is built on, and so the basics of QGIS
will be taught in this practical.

Why QGIS?
...........

As information becomes increasingly spatially linked, many tools have been developed
to complete commonly used GIS functions. Why use
QGIS over some other GIS software package?

* It's free, as in lunch. Installing and using the QGIS program costs you
  zero money. No initial fee, no recurring fee, nothing.
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
* Cross-platform. QGIS can be installed on OS X, Windows, Linux and Android.

An overview of the interface
............................

The elements identified in the figure below are:

1. Layers panel
2. Toolbars
3. Map canvas
4. Status bar

.. image:: /static/training/socialisation/011_interface.*
   :align: center


Set up QGIS
-----------

1. Open :guilabel:`QGIS Desktop (2.8.1)` - This should be located on
your desktop, or you can find it in your start menu.

.. image:: /static/training/socialisation/012_qgis_desktop.*
   :align: center

.. Note:: Your exact version number of QGIS may be different. This tutorial has
   been designed with QGIS 2.8.1 or above.
   If you don't find QGIS 2.8.1 icon, you can go to :file:`Progam Files -> QGIS Wien`.

2. A hint window will appear. Close the window by clicking :guilabel:`OK`.

.. image:: /static/training/socialisation/013_tips.*
   :align: center

Clean up toolbar
.................

To provide more space for your map canvas uncheck the tools which are not
needed for this tutorial.

3. Right-click the toolbar and uncheck the following:

  * Advance Digitizing
  * Database
  * Digitizing
  * File
  * Grass
  * OpenStreetMap
  * Raster
  * Vector
  * Web

4. Rearrange the toolbar so that it's on one line. Left-click and
   hold the vertical dots on the left hand side of the tool. Drag
   to the first line of the toolbar.

.. image:: /static/training/socialisation/014_verticaldots.*
   :align: center

.. Note:: For future work you may want to add these tools back into your
   toolbar - this is as simple as right-clicking on the toolbar and turning them
   back on.

Your QGIS toolbar should go from three lines to one line:

.. image:: /static/training/socialisation/015_toolbar_clean.*
   :align: center


Set up QGIS options
...................

Next change the project's projection settings and QGIS language settings:

5. Open the settings window by clicking on :menuselection:`Settings --> Options`.

6. Select the :guilabel:`CRS` tab from the options menu.

.. image:: /static/training/socialisation/016_crs.*
   :align: center

7. Check :guilabel:`Enable on the fly reprojection by default`.
   This will ensure that all spatial layers irrespective of their projection
   will follow the CRS displayed above.

.. image:: /static/training/socialisation/017_onthefly.*
   :align: center

8. Select the :guilabel:`Locale` tab.

.. image:: /static/training/socialisation/018_locale.*
   :align: center

9. Check :guilabel:`Override system locale`. You may choose any language 
   that QGIS has been translated into. We will stay with English
   for this tutorial, so no action is needed.
   Uncheck :guilabel:`Override system locale`.

.. image:: /static/training/socialisation/019_locale_select.*
   :align: center

.. note::
   |project_name| is dependent on the locale, but it has only been translated
   into Bahasa Indonesian so far.
   World Bank is currently funding the translation of |project_name| into
   French and Portuguese.

10. Click :guilabel:`OK` in the bottom right corner of the Options window.

Installing Plugins
------------------

Next we will install the two plugins used in this tutorial, |project_name| and
OpenLayers, using the QGIS plugin repository.

|project_name|
..............

.. note:: You must be connected to the internet for this section.

11. Go to :menuselection:`Plugins --> Manage and Install Plugins`. It may
    take a couple of minutes for QGIS to contact its repository and show the
    list of available plugins.

12. Go to the :guilabel:`New` tab. Type :kbd:`inasafe` into the filter box

.. image:: /static/training/socialisation/020_inasafe_plugin.*
   :align: center

13. Select |project_name| and click :guilabel:`Install plugin` - it
    may take a couple of minutes for the plugin to download and install.

.. note::
   If your internet using a proxy, you need to setting the proxy from 
   :menuselection:`Settings --> Options --> Network`

14. A window should pop up saying: "Plugin installed successfully"
    Click :guilabel:`Ok` and click :guilabel:`Close` to exit the *QGIS Plugin Manager*
    window.

15. You should now have an |project_name| panel on the right hand side of
    your screen.

.. image:: /static/training/socialisation/021_insafe_gettingstarted.*
   :align: center

|project_name| also comes with a toolbar of its own!

.. image:: /static/training/socialisation/022_inasafetoolbar.*
   :align: left

16. To retrieve the |project_name| toolbar, right-click on the
    top toolbar and check :guilabel:`InaSAFE`.

================================================================   ===============================
**Symbol**                                                         **Name**
----------------------------------------------------------------   -------------------------------
.. image:: /static/training/socialisation/icon_dock.*              Toggle Dock
.. image:: /static/training/socialisation/icon_keywords_wiz.*      Keyword Creation Wizard
.. image:: /static/training/socialisation/icon_func_centric.*      Impact Function Centric Wizard
.. image:: /static/training/socialisation/icon_osm.*               OpenStreetMap downloader
.. image:: /static/training/socialisation/icon_toggle_outline.*    Toggle Scenario Outline
.. image:: /static/training/socialisation/icon_set_area.*          Set Analysis Area
================================================================   ===============================

.. Note:: Later we will explore and use these tools. For more information on the 
  |project_name| toolbar see :doc:`../../user-docs/toolbar`.

OpenLayers Plugin
.................

.. note:: To use the OpenLayers plugin you must have connection to the internet at all
   times.

17. Go to :menuselection:`Plugins --> Manage and Install Plugin`.
    It may take a couple of minutes for QGIS to contact its repository and
    show the list of plugins available.

18. Type :kbd:`openlayers` into the filter box.

19. Select OpenLayers Plugin and click :guilabel:`Install plugin` 
    - it may take a couple of minutes for the plugin to download and install.

20. A window should pop up saying: "Plugin installed successfully"
    Click :guilabel:`Ok` and click :guilabel:`Close` to exit the *QGIS Plugin Manager*
    window.

21. Go to :menuselection:`Web --> OpenLayers plugin`

.. image:: /static/training/socialisation/023_openlayers.*
   :align: center

22. Select :guilabel:`Add Bing Aerial layer`.

.. image:: /static/training/socialisation/024_aerial_bing.*
   :align: center

.. note:: If you are familiar with Google Earth, navigating this imagery
   should be very similar.

**Activity:** Navigate to your home or office
.............................................

Using the navigation tools below, zoom to your home.

=========================================================  ============
**Symbol**                                                 **Name**
---------------------------------------------------------  ------------
.. image:: /static/training/socialisation/icon_pan.*       Pan Map
.. image:: /static/training/socialisation/icon_zoomin.*    Zoom In
.. image:: /static/training/socialisation/icon_zoomout.*   Zoom Out
.. image:: /static/training/socialisation/icon_zoomfull.*  Zoom to Full
.. image:: /static/training/socialisation/icon_zoomlast.*  Zoom Last
.. image:: /static/training/socialisation/icon_zoomnext.*  Zoom Next
=========================================================  ============

23. Click the Zoom In button and draw a box (click and drag the mouse) over your 
    country.

24. Click the Pan Map button and drag the map so that your country is in the
    centre of the screen.

.. note:: If you make a mistake in your zooming, click the :guilabel:`Zoom Last` 
   button to go back.

25. Navigate to your own house or workplace.

**Indonesia**

.. image:: /static/training/socialisation/025_indonesia.*
   :align: center

**Jakarta**

.. image:: /static/training/socialisation/026_jakarta.*
   :align: center

**Menara Thamrin**, a building in Jakarta

.. image:: /static/training/socialisation/027_mt.*
   :align: center


:ref:`Go to next module --> <raster-vs-vector>`
