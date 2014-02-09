.. _openstreetmap_downloader:

OpenStreetMap Downloader
========================

This tool will fetch building ('structure') and highway ('road') data from the
OpenStreetMap project for you.

.. figure:: /static/user-docs/openstreetmap_downloader.*
   :scale: 75 %
   :alt: OpenStreetMap Downloader
   :align: center

   OpenStreetMap Downloader

The tool requires internet connection as it fetches the data via a web service
running on `Linfiniti's OSM Reporter <http://osm.linfiniti.com>`_ web site.

The data, once downloaded will be available to you as a shapefile. A style
file is automatically created so that it symbolises nicely in QGIS. In
addition, the correct keyword metadata is created for the downloaded dataset
so that it can be used directly in InaSAFE impact scenario analyses.

**Note:** The downloader service has limitations as to the size of
datasets that can be retrieved. As such you may experience issues trying to
fetch e.g. country wide building footprint data. Generally datasets at a
city level and below should work well.

To use this tool effectively:

* Use QGIS to zoom in to the area for which you want building data to be
  retrieved.
* Check the output directory is correct. Note that the saved datasets
  will be called buildings.shp and roads.shp (and their associated files).
* Press the :guilabel:`OK Button` and wait for the data to be retrieved.


.. warning::
   If a dataset already exists in the output directory it will be overwritten.
   This tool requires a working internet connection and fetching buildings will
   consume your bandwidth.

.. note::
   Downloaded data is copyright OpenStreetMap contributors (click for more
   info).


Building data
-------------

InaSAFE supports the use of building data in various impact functions. In
particular we support building footprints sourced from the
`OpenStreetMap <https://openstreetmap.org>`_ project (OSM).

The following building types are derived (depending on the various tags assigned
to them in OSM):

* School
* University/College
* Government
* Clinic/Doctor
* Hospital
* Fire Station
* Police Station
* Public Building
* Place of Worship - Islam
* Place of Worship - Unitarian
* Place of Worship - Buddhist
* Place of Worship - Unitarian
* Supermarket
* Residential
* Sports Facility
* Place of Worship
* Commercial
* Industrial

These derived types will be present in a field called 'type' when downloading
the building data.Note that depending on the area for which you have downloaded,
only some of these categories may be present in your buildings dataset.

Roads data
----------

InaSAFE supports the use of road data in various impact functions. In
particular we support roads sourced from the
`OpenStreetMap <https://openstreetmap.org>`_ project (OSM).

The following road types are derived (depending on the various tags assigned
to them in OSM):

ALTER TABLE planet_osm_line ADD COLUMN "type" VARCHAR(255) NULL;

* Motorway or highway (includes 'trunk' from OSM)
* Motorway link
* Primary road
* Primary link
* Tertiary
* Tertiary link
* Secondary
* Secondary link
* Road, residential, living street, etc. (includes all highways tagged with
  'living_street', 'residential', 'yes', 'road', 'unclassified', 'service', ''
  and NULL highways)
* Track'
* Cycleway, footpath, etc. (includes 'cycleway', 'footpath', 'pedestrian',
  'footway' and 'path' highway tags).
