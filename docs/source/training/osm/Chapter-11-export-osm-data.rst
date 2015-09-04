.. image:: /static/training/osm/1_000.*

..  _ch11-export-osm-data:

Chapter 11: Export OSM data
===========================

**Learning Objectives:**

- Learn how to use HOT Export
- Learn how to use overpass turbo

After you learn how to add and edit in *OpenStreetMap (OSM)*, 
you may want to export OSM data as back-up or for processing using GIS software
such as **QGIS** `www.qgis.org <http://www.qgis.org/>`_. 
In this chapter we will learn how to use nay

11.1 Hot Export Tool
--------------------

1. Open your browser and type `export.hotosom.org <http://export.hotosm.org/>`_ and it will show like this:

.. figure:: /static/training/osm/11_001.*
   :align: center
   
   *Hot Export front page*

2. To get data from this website, you will need to create an account first, 
   if you do not already have one. The first step is click :guilabel:`Create Account` 
   in the bottom left side of HOT Export page. 
   After that fill in your email, password and password confirmation. 
   Then click :guilabel:`Create Account` and open your email to confirm the email from HOT Export.

.. figure:: /static/training/osm/11_002.*
   :align: center
   
   *Screenshot in Create Account Page*

3. After you confirm the email, login with your account. 
   Fill in your email and password and then click :guilabel:`Log in`.

4. After you successfully log in to the website, click :guilabel:`New Job`

5. Fill in the name and job description. 
   Then define your area of interest in the box that displays OpenStreetMap. 
   From this box you can create an area of interest for export. 
   Click :guilabel:`Select Area` and draw a box around the area, 
   The box can be manipulated by dragging its corner and centre. 
   When you finish, click :guilabel:`Create Job`.

.. figure:: /static/training/osm/11_003.*
   :align: center
   
   *Create New Job in HOT Export*

6. Next, you need to fill **select preset** field as shown in the figure below, 
   or you can ignore it with select :guilabel:`no file` if preset file that you need is not available. 
   For translation file, you can fill with :guilabel:`no file` 
   if you don’t want to translate the preset. Click :guilabel:`Save` to continue.

.. figure:: /static/training/osm/11_004.*
   :align: center
   
   *Setting data configuration in HOT Export*

7. The server will process your request. The progress for your request is depend on 
   how big the area you choose and server capacity. 
   When the process is complete, You can choose file format that you want,
   for example ESRI Shapefile. All the request for HOT Export can be found in :guilabel:`Job` page.

.. figure:: /static/training/osm/11_005.*
   :align: center
   

11.2 Overpass-Turbo
-------------------

If you only want specific object in OSM data, the right choice is to use `Overpass Turbo <http://overpass-turbo.eu/>`_. 
For example you only need schools data in Jakarta and surrounding area. 
To download OpenStreetMap data using Overpass Turbo you can follow this step:

1. Point your web browser to `Overpass Turbo <http://overpass-turbo.eu/>`_

2. You can start find to your area of interest in OpenStreetMap using the Slippy Map in the right side. 
   You can drag and zoom in map with **(+)** and zoom out map using **(-)**. 
   You can also search directly with typing in search box as shown in the Jakarta example shown below.
   There will be several arear related to Jakarta and you can choose the right area that you want to download.

.. figure:: /static/training/osm/11_006.*
   :align: center
   

3. If you don’t want to download the larger area you can resize the area and draw a border by yourself 
   with click :guilabel:`manually select box` from the toolbar in the left side of the map. 
   Draw a box in the slippy map to define the target area.

.. figure:: /static/training/osm/11_007.*
   :align: center

   *Select area manually*

4. To download OSM data specific to one feature, for example schools, click :guilabel:`Wizard` menu. 
   In the Wizard menu, you can filter your data with using `JOSN <http://www.jsoniq.org/>`_ query, 
   in the simple way it can be a tag contains Key and Value, 
   for example if you want to download schools type :kbd:`amenity=school` in :guilabel:`Query Wizard`.

.. figure:: /static/training/osm/11_008.*
   :align: center
   
   *Query box in Overpass Turbo*

5. Click :guilabel:`Build and Run Query`, wait for a moment until school objects are displayed in the area of interest. 
   You should see something like the screenshot below which shows all the school objects in OSM in the area of interest.

.. figure:: /static/training/osm/11_009.*
   :align: center
   
6. If you only want data type in point/node format,
   you can specify that in the query box in the left side. 
   To do this, erase school with way and relation type, and then click :guilabel:`Run` menu in the top left side.
   The result will be a school objects with only point/node data type filtered. 
   You can also add more detailed query in the query box and then click :guilabel:`Run`.

.. figure:: /static/training/osm/11_010.*
   :align: center
   
   *Erase several query in query box*

7. To download the schools data you can click Export menu,
   there are several data formats that you can choose such as **geoJSON, GPX, KML, .osm**, etc. 
   If you not familiar with geoJSON, you can select :guilabel:`level0` to download .osm data format that you can use later with QGIS or other mapping software.

.. figure:: /static/training/osm/11_011.*
   :align: center
   
   *Export Overpass Turbo result*