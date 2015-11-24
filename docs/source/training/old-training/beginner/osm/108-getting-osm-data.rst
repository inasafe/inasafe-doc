.. image:: /static/training/old-training/beginner/osm/image6.*

..  _getting-osm-data:

Module 8: Getting OSM Data
==========================

**Learning Objectives**

- Download OpenStreetMap data from the
  `Geofabrik website <http://download.geofabrik.de/openstreetmap/>`_ 
- Download customised OpenStreetMap data using HOT Exports

Now that we have learned how to contribute data to the OpenStreetMap database,
let's see how we can access data for download in different formats.
You may want to download OSM data as a backup or for use in Geographic
Information System software such as |QGIS|.

1. Getting OSM data on Geofabrik website
----------------------------------------

The easiest way to get OSM data is to download a pre-processed data extract
from one of the various websites which offers up-to-date downloads. In this
section we will see how to download data from Geofabrik, a company which
offers free OSM downloads at the link below:

http://download.geofabrik.de/openstreetmap/

.. image:: /static/training/old-training/beginner/osm/image131.*
   :align: center

1. The data is divided into several regions. To access the data for Indonesia,
   click on the :guilabel:`Asia` region in the table.

.. image:: /static/training/old-training/beginner/osm/image132.*
   :align: center

2. Then click on :guilabel:`Indonesia`.

.. image:: /static/training/old-training/beginner/osm/image133.*
   :align: center

3. To obtain the Indonesian data in shapefile (.shp)
   format, click on :guilabel:`indonesia-latest.shp.zip` and the
   file will be downloaded. Several file formats are available - shapefiles
   are a popular GIS format which contain several different files with
   point, line and polygon data.

The website indicates the most recent time that the data was updated. Note that
the server usually updates the data once every 24 hours,
so if you have just made changes to OSM, don't expect them to appear in this
data immediately.

2. Getting OSM data from HOT Exports
------------------------------------

To download a specific area with a specific data attributes that you define,
HOT Exports is a more convenient tool for downloading data.

4. In your web browser, go to http://export.hotosm.org

.. image:: /static/training/old-training/beginner/osm/image134.*
   :align: center

5. To create a data processing job you must have an account. Click
   :guilabel:`Create Account` in the bottom left corner and enter your email
   address, a new password and password confirmation. Complete the registration
   by clicking :guilabel:`Create Account`. Open your email and click on the
   link that has been sent in order to activate your account.

.. image:: /static/training/old-training/beginner/osm/image135.*
   :align: center

6. Log in using the account that you have created.

.. image:: /static/training/old-training/beginner/osm/image136.*
   :align: center

7. When you are successfully logged in, click :guilabel:`New Job` in the upper
   right corner. 

8. Enter a name for the job (such as the name of the area you are downloading).
   Enter a description as well.

9. Zoom in on the map to the area that you want to download. 
   Click :guilabel:`Select Area` and draw a box around the area that you want.
   The box can be manipulated by dragging its corners and centre. When you
   finish, click :guilabel:`Create Job`.

.. image:: /static/training/old-training/beginner/osm/image137.*
   :align: center

Next, you may optionally select a presets file to include in your data
extract. Presets files are the same as those used in JOSM, and instruct
HOT Exports to extract specific data attributes in your custom download.
This is useful if the data you are accessing contains non-standard tags
that are not typically included in data extracts.

10. To add a presets file, click the drop-down menu next 
    to :guilabel:`Select Preset File` and choose one of the available
    options. Check the box next to :guilabel:`Add Default Tags?` to
    include the default attributes in the data extract.
  
.. image:: /static/training/old-training/beginner/osm/image138.*
   :align: center

11. Click :guilabel:`Save` and the server will begin to process your request.
    The length of the process depends on the area you choose and server 
    capacity. 

12. When the process is complete, the data can be downloaded in a variety
    of formats, including shapefiles, KML and database formats.

.. image:: /static/training/old-training/beginner/osm/image139.*
   :align: center

13. All jobs you create will appear in the list on the :guilabel:`Jobs` page.
    If any time you want to download the same area with up-to-date data, find
    the job on this page. Click :guilabel:`Start new run` to process the same
    extract again but with the most recent OSM data.
