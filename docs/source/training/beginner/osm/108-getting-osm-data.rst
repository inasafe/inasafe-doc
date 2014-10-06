.. image:: /static/training/beginner/osm/image6.*

..  _getting-osm-data:

Module 8: Getting OSM Data
==========================

**Learning Objectives**

- Downloading OpenStreetMap data from the
  `Geofabrik <http://download.geofabrik.de/openstreetmap/>`_ website
- Downloading OpenStreetMap data in according to region and necessary data
  by using Hot-Export

After you learn how to add and edit data in OpenStreetMap (OSM),
now maybe you want the data obtained as a back up or if you want the
Geography Information System software that Open Source is |QGIS|
(http://qgis.org).

1. Getting OSM Data on Geofabrik Website
----------------------------------------

- The OSM data can be obtained easily by downloading it at the following
  website:

http://download.geofabrik.de/openstreetmap/

.. image:: /static/training/beginner/osm/image131.*
   :align: center

- The data is divided into several regions, for Indonesia you can find at the
  part of Asia by clicking on the Asia sub region on the blue table,
  then the page will appear like this.

.. image:: /static/training/beginner/osm/image132.*
   :align: center

- After appearing at the top of the page look like the sub region divides
  into countries at Asia, to get the data you need to click the Indonesian
  state on the blue table and will appear like this.

.. image:: /static/training/beginner/osm/image133.*
   :align: center

- Then if you want to obtain the Indonesian data with shapefile (.shp)
  format, you click on the :guilabel:`indonesia-latest.shp.zip` link and the
  file will be downloaded. There are several formats that can be downloaded one
  popular formats such as shapefile (shp) with  points, polyline, and
  polygon layer.

You can check the last time data is updated. Please note,
the server usually update the data once every 24 hours,
so if you just upload data to OSM, the data does not appear automatically
when you download it but you have to wait for the latest updates from the
server.

2. Getting OSM Data on HOT-Export Website
-----------------------------------------

If you just want to download a particular specific area with a particular
attribute, you can use the Hot-Exports data download service.

- Open hot-export.geofabrik.de so it will appear like this:

.. image:: /static/training/beginner/osm/image134.*
   :align: center

- To obtain the data from this website you must have an account first,
  if you don’t have account you must create one. The first step by clicking
  :guilabel:`Create Account` in the bottom left corner, then fill your email,
  password, and confirmation password, after filling with complete click
  :guilabel:`Create Account`.  Then you will see a message like this *“A message
  with a confirmation link has been sent to your email address. Please open the
  link to activate your account.”* indicating that your account has been
  successfully created and you have your activation email.

.. image:: /static/training/beginner/osm/image135.*
   :align: center

- After that log in using your account that you have created. Filled in the
  column email and password then click :guilabel:`Login`.

.. image:: /static/training/beginner/osm/image136.*
   :align: center

- If you have successfully successfully into the website,
  to obtain the data you want click :guilabel:`New Job`, then fill in your name
  and the job description. Furthermore, to select the area you are getting,
  look at the box OpenStreetMap maps of the box you can select the area you
  want to get with the highlight area to choose select area with the arrow
  symbol. Then click :guilabel:`Save`.

.. image:: /static/training/beginner/osm/image137.*
   :align: center

- After saved, the next step you fill the column :guilabel:`Select Preset File`
  or you can ignore with fill No file if the preset file that need not exist. Then
  the file translation filled with No file if the translation you need is not
  there and save it.

.. image:: /static/training/beginner/osm/image138.*
   :align: center

- Then the server will immediately process your request. The process depends
  on the area you choose and the server capacity. After that you can select
  the file format you want to download such as ESRI Shapefile. All download
  requests that you create will appear on the :guilabel:`Job`. So if any time
  you want to download on the same area, you can search the name job for the
  previous job name that you have created and you can download it again without
  having to click on :guilabel:`New Job`.

.. image:: /static/training/beginner/osm/image139.*
   :align: center
