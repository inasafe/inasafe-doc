.. _introduction-to-qgis:

Introduction to QGIS
====================

.. image:: /static/training/socialisation/010_qgis_logo.png
   :align: right
   :scale: 30 %

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

|QGIS| is a user friendly Open Source Geographic Information System (GIS).
It runs on Linux, Unix, Mac OSX, Windows and Android and supports numerous
vector, raster, and database formats and functionality.
`<http://www.qgis.org>`_

|QGIS| provides a continuously growing number of capabilities provided
by core functions and plugins.
You can visualize, manage, edit, analyse data, and compose printable maps.
|QGIS| is also the platform of |project_name|, and hence the basic of |QGIS|
will be taught in the workshop.

Why |QGIS|?
-----------

As information becomes increasingly spatially aware, there is no shortage of
tools able to full fill some or all commonly used GIS functions. Why should
anyone be using |QGIS| over some other GIS software package?

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

**1. Layers list**
**2. Toolbars**
**3. Map canvas**
**4. Status bar**

.. image:: /static/training/socialisation/011_interface.*
   :align: center



Start of Practical
===================

Setup QGIS
----------

1. :guilabel:`Open QGIS Desktop (2.0.1)` - This should be located on
your desktop, or you can find it in your start menu.

.. image:: /static/training/socialisation/012_qgis_desktop.*
   :align: center

2. A hint window will come up, close the window by clicking :guilabel:`OK`.

.. image:: /static/training/socialisation/013_tips.*
   :align: center

.. Note:: At a later date I recommend you read through these hints by
   clicking on *Next*

Clean up tool bar
.................

To provide more space for your map canvas we will uncheck the tools we will not be
using today.

3. :guilabel:`Right Click` the toolbar and :guilabel:`Uncheck`,

* Advance Digitising
* Database
* Digitising
* File
* Grass
* OpenStreetMap
* Raster
* Vector
* Web

4. Rearrange toolbar so its just one line, :guilabel:`Left Click` and
   :guilabel:`Hold` the vertical dots on the left hand side of the tool. Drag
   to the first line of the toolbar.

.. image:: /static/training/socialisation/014_verticaldots.*
   :align: center

.. Note:: For future work you may want to add these tool back into your
   toolbar, this is as simple as :guilabel:`Right Clicking` on the toolbar and turning it
   back on.

Your QGIS toolbar should go from 3 lines to 1 line:

.. image:: /static/training/socialisation/015_toolbar_clean.*
   :align: center


Option Window
.............

To change the projection settings and acknowledge that QGIS is multilingual

5. Go to Options window: :menuselection:`Settings --> Options`

6. :guilabel:`Select` the **CRS** tab of the options menu

.. image:: /static/training/socialisation/016_crs.*
   :align: center

7. :guilabel:`Check` *Enable on the fly reprojection by default*.
   This will enable that all spatial layers irrespective of their projection
   will follow the CRS allocated above

.. image:: /static/training/socialisation/017_onthefly.*
   :align: center

8. :guilabel:`Select` on the **Locale** tab of the options menu

.. image:: /static/training/socialisation/018_locale.*
   :align: center

9. :guilabel:`Check` *Override system locale*, scroll through all the
   languages that QGIS have been translated into! We will stick with english
   for this training, so no action is needed -
   :guilabel:`Uncheck` *Override system locale*.

.. image:: /static/training/socialisation/019_locale_select.*
   :align: center

.. note::
   |project_name| is dependent on Locale, but it has only been translated
   into bahasa Indonesian so far.
   World Bank is currently funding for the translation of |project_name| into
   French and Portugal

10. :guilabel:`Ok` in the bottom right corner of the Options window

Installing Plugins
------------------

|project_name|
..............

Installing |project_name| through the QGIS plugin repository

.. note:: You must be connected to the internet for this section

.. note:: Currently InaSAFE v2.0 has not been released,
hence please follow instructions to download the InaSAFE experimental
:ref:`install` and skip steps 11-14.

11. Go to :menuselection:`Plugins --> Manage and Install Plugins` This will
take a couple of minutes for QGIS to contact its repository and show the list
 of plugins available

12. Go to :guilabel:`New` tab. Type :kbd:`inasafe` into the filter box

.. image:: /static/training/socialisation/020_inasafe_plugin.*
   :align: center

13. :guilabel:`Select` |project_name| and :guilabel:`Install` - this
    will take a couple of minutes for the plugin to download and install.

14. A window should pop up saying: "Plugin installed successfully"
    :guilabel:`Ok` and :guilabel:`Close` the *QGIS Plugin Manager*
    window.

15. You should now have an |project_name| panel on the right hand side of
    your screen.

.. image:: /static/training/socialisation/021_insafe_gettingstarted.*
   :align: center

|project_name| also comes with a toolbar of its own!

16. To retrieve the |project_name| toolbar, :guilabel:`Right Click` on the
    top tool bar and :guilabel:`Recheck` **plugin**

.. image:: /static/training/socialisation/022_inasafetoolbar.*
   :align: left

=================================================   ========================
**Symbol**                                          **Name**
-------------------------------------------------   ------------------------
.. image:: /static/general/icon_dock.*              Toggle Dock
.. image:: /static/general/icon_keywords.*          Keyword Editor
.. image:: /static/general/icon_reset.*             Reset Dock
.. image:: /static/general/icon_options.*           Options
.. image:: /static/general/icon_impactfunctions.*   Impact Functions Browser
.. image:: /static/general/icon_minimumneeds.*      Minimum Needs Tool
.. image:: /static/general/icon_converter.*         Converter
.. image:: /static/general/icon_batch.*             Batch Runner
.. image:: /static/general/icon_save.*              Save Current Scenario
.. image:: /static/general/icon_osm.*               OpenStreetMap downloader
.. image:: /static/general/icon_merge.*             Impact Layer Merge
=================================================   ========================

.. Note:: Later we will explore and use these tools.  For more information
  :doc:`../../user-docs/toolbar`

OpenLayers Plugin
.................

Installing OpenLayers through the QGIS plugin repository

.. note:: To use openlayers you must have connection to the Internet at all
   times!


17. Go to :menuselection:`Plugins --> Manage and Install Plugin`.
    This will take a couple of minutes for QGIS to contact its repository and
    show the list of plugins available.

18. Type :kbd:`openlayers` into the filter box.

19. :guilabel:`Select` *OpenLayer Plugin* then :guilabel:`Install plugin` -
    this will take a couple of minutes for the plugin to download and install.

20. A window should pop up saying: "Plugin installed successfully"
    :guilabel:`Ok` and :guilabel:`Close` the *QGIS Python Plugin Installer*
    window.

21. Hover mouse over :menuselection:`Plugins --> OpenLayer Plugin`

.. image:: /static/training/socialisation/023_openlayers.*
   :align: center

22. :guilabel:`Select` *Add Bing Aerial layer*

.. image:: /static/training/socialisation/024_aerial_bing.*
   :align: center

.. note:: If you are familiar with Goggle Earth, navigating this imagery
   should be very similar.

**Activity:** Navigate to your home or office
.............................................

Using the navigation tools below, zoom into your home.

==========================================  ============
**Symbol**                                  **Name**
------------------------------------------  ------------
.. image:: /static/general/icon_pan.*       Pan Map
.. image:: /static/general/icon_zoomin.*    Zoom In
.. image:: /static/general/icon_zoomout.*   Zoom Out
.. image:: /static/general/icon_zoomfull.*  Zoom to Full
.. image:: /static/general/icon_zoomlast.*  Zoom Last
.. image:: /static/general/icon_zoomnext.*  Zoom Next
==========================================  ============

23. :guilabel:`Click` *zoom In*, draw a box (click and drag) over your country.

24. :guilabel:`Click` *Pan Map*, shift the map so your country is in the
    centre of the screen.

.. Note:: If you make a mistake in your zooming, use *Zoom Last* tool.

25. Navigate to your own house or work

**Indonesia**

.. image:: /static/training/socialisation/025_indonesia.*
   :align: center

**Jakarta**

.. image:: /static/training/socialisation/026_jakarta.*
   :align: center

**Menara Thamrin**

.. image:: /static/training/socialisation/027_mt.*
   :align: center
