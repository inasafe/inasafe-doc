.. _openstreetmap_downloader:

OpenStreetMap Downloader
========================

This tool will fetch building ('structure') data from the OpenStreetMap
project for you.

.. figure:: /static/user-docs/openstreetmap_downloader.*
   :scale: 75 %
   :alt: OpenStreetMap Downloader
   :align: center

   OpenStreetMap Downloader

The downloaded data will have |project_name| keywords defined and a default
QGIS style applied. To use this tool effectively:

To use this tool effectively:

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
