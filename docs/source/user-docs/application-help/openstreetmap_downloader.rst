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

InaSAFE supports the use of building data in various impact functions. In
particular we support building footprints sourced from the
`OpenStreetMap <https://openstreetmap.org>`_ project (OSM). The tool
requires internet connection as it fetches the data via a web service running
on `Linfiniti's OSM Reporter <http://osm.linfiniti.com>`_ web site.

The data, once downloaded will be available to you as a shapefile. A style
file is automatically created so that it symbolises nicely in QGIS. In
addition, the correct keyword metadata is created for the downloaded dataset
so that it can be used directly in InaSAFE impact scenario analyses.

**Note:** The building downloader service has limitations as to the size of
datasets that can be retrieved. As such you may experience issues trying to
fetch e.g. country wide building footprint data. Generally datasets at a
city level and below should work well.

To use this tool effectively:

* Use QGIS to zoom in to the area for which you want building data to be
  retrieved.
* Check the output directory is correct. Note that the saved dataset
  will be called buildings.shp (and its associated files).
* Press the :guilabel:`OK Button` and wait for the data to be retrieved.


.. warning::
   If a dataset already exists in the output directory it will be overwritten.
   This tool requires a working internet connection and fetching buildings will
   consume your bandwidth.

.. note::
   Downloaded data is copyright OpenStreetMap contributors (click for more
   info).
