.. _toolbar:

Toolbar
=======

This Section contains the explanation of the different icons in the Toolbar
and the function behind the icons.

Toggle |project_name| Dock
--------------------------

.. figure:: /static/user-docs/toolbar_toggle.*
   :scale: 75 %
   :align: center
   :alt: Toggle the Dock

   Toggle Dock

This button enables and hides the |project_name| dock. After enabling the
dock you are able to move it around your screen. Dock and undock it wherever
you want it to have and keep it even as a separated window.

You can find more Information about the dock itself in the
:ref:`using_the_plugin` section.

|project_name| Keyword Editor
-----------------------------

.. figure:: /static/user-docs/toolbar_keyword.*
   :scale: 75 %
   :align: center
   :alt: Keyword Editor

   Keyword Editor

The Keyword Editor button opens the Keyword editor which is described in
:ref:`keywords-system`. Basically it enables you to easily edit the Keywords
needed for |project_name| to create useful output.

Reset Dock
----------

.. figure:: /static/user-docs/toolbar_reset.*
   :scale: 75 %
   :align: center
   :alt: Reset Dock

   Reset Dock

The Name is self speaking. In Case of any drawing issue inside the dock this
button just resets/reloads the dock to its initial state.

|project_name| Options
----------------------

.. figure:: /static/user-docs/toolbar_options.*
   :scale: 75 %
   :align: center
   :alt: Options

   |project_name| Options

This button opens the Options window which is described in
:ref:`options-toolbar`

|project_name| Impact Functions Browser
---------------------------------------

.. figure:: /static/user-docs/toolbar_if_browser.*
   :scale: 75 %
   :align: center
   :alt: Impact Functions Browser

   |project_name| Impact Functions Browser

This button opens the Impact Function Browser. It basically enables you to
filter and browse impact functions that are available in |project_name|. More
information about that topic can be found in :ref:`impact_functions`.

.. _minimum_needs_tool:

|project_name| Minimum Needs Tool
----------------------------------

.. figure:: /static/user-docs/toolbar_needs.*
   :scale: 75 %
   :align: center
   :alt: Minimum needs tool

   |project_name| Minimum Needs Tool

This tool will calculated minimum needs for evacuated people.
To use this tool effectively:

Load a polygon layer in QGIS.
Typically the layer will represent administrative districts where people have
gone to an evacuation center.
Ensure that the layer has an INTEGER attribute for the number of displaced
people associated with each feature.
Use the pick lists below to select the layer and the population field and
then press 'OK'.
A new layer will be added to QGIS after the calculation is complete. The
layer will contain the minimum needs per district/administrative boundary.

|project_name| Converter
------------------------

.. figure:: /static/user-docs/toolbar_converter.*
   :scale: 75 %
   :align: center
   :alt: Converter

   |project_name| Converter

This tool will convert an earthquake 'shakemap' that is in grid xml format
to a GeoTIFF file. The imported file can be used in InaSAFE as an input for
impact functions that require and earthquake layer. To use this tool
effectively:

 * Select a grid.xml for the input layer.
 * Choose where to write the output layer to.
 * Choose the interpolation algorithm that should be used when converting the
   xml grid to a raster. If unsure keep the default.

If you want to obtain shake data you can get it for free from the USGS
shakemap site: http://earthquake.usgs.gov/earthquakes/shakemap/list.php?y=2013

.. _batch_runner:

|project_name| Batch Runner
---------------------------

.. figure:: /static/user-docs/toolbar_batch.*
   :scale: 75 %
   :align: center
   :alt: Converter

   |project_name| Converter

Before running the Batch Runner you might want to use the
:ref:`save_scenario` tool to first save some scenarios on which you can let
the batch runner do its work. This tool lets you run saved scenarios in one
go. It lets you select scenarios or let run all scenarios in one go.

.. _save_scenario:

Save current scenario
---------------------

.. figure:: /static/user-docs/toolbar_scenario.*
   :scale: 75 %
   :align: center
   :alt: Converter

   |project_name| Converter

This is the tool you need to prepare/save scenarios for the
:ref:`batch_runner` Tool. It lets you save the current visible scenario in
QGIS to a :file:`.txt` file. This file you can open as a scenario again in
Batch runner and recalculate it.

|project_name| OpenStreetMap Downloader
---------------------------------------

.. figure:: /static/user-docs/toolbar_osm.*
   :scale: 75 %
   :align: center
   :alt: OpenStreetMap downloader

   |project_name| OpenStreetMap downloader

This tool will fetch building ('structure') data from the OpenStreetMap
project for you.
The downloaded data will have |project_name| keywords defined and a default
QGIS style applied. To use this tool effectively:

Use QGIS to zoom in to the area for which you want building data to be
retrieved.
Check the output directory is correct. Note that the saved dataset
will be called buildings.shp (and its associated files).

.. warning::
   If a dataset already exists in the output directory it will be overwritten.
   This tool requires a working internet connection and fetching buildings will
   consume your bandwidth.

.. note::
   Downloaded data is copyright OpenStreetMap contributors (click for more
   info).
