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
In this chapter we will learn how to use these tools.

11.1 Hot Export Tool
--------------------

1. Open your browser and type `export.hotosom.org <http://export.hotosm.org/>`_ and it will show like this:

.. figure:: /static/training/osm/11_001.*
   :align: center
   
   *Hot Export front page*

2. To get data from this website, you will need to login into your OpenStreetMap account first before you can use HOT Export. Click :guilabel:`Login to OpenStreetMap`

.. figure:: /static/training/osm/11_002.*
   :align: center
   
   *Screenshot Login into OSM Account Page*

3. if you do not already have one, you have to create it.
The first step is you can click :guilabel:`here` in the sentence '**if you don't have an OpenStreetMap account you can register for one here**' of HOT Export front page.

.. figure:: /static/training/osm/11_003.*
   :align: center
   
   *Screenshot in Create OSM Account Page*

4. After that fill in your email, display name, password and password confirmation. Then click :guilabel:`Sign Up` and open your email to confirm the email from OpenStreetMap.

.. figure:: /static/training/osm/11_004.*
   :align: center
   
   *Screenshot in Create OSM Account Page*

5. After you confirm the email, come back to HOT Export front page and login with your OSM account. 
   Fill in your email and password and then click :guilabel:`Log in`.

6. After you successfully log in to the website, you automatically directed into New Export page.
In tab :guilabel:`Describe Export` you can fill your export file name, description about the export and the project name that using this export file.

7. In right side of the page, you can define the exported area.
You can search by type area name in **search box** or you can select manually by click :guilabel:`Export Area` and draw the area box.

.. figure:: /static/training/osm/11_005.*
   :align: center
   
   *Screenshot in New Export Page*

8. If you finish define name and area for your export, click :guilabel:`File Formats` tab to select file format for your export file.
There are some file format that you can select such as Esri SHP, Garmin File, Google KMZ, OSM OBF File and SQlite SQL.
For Esri SHP file, there are 2 format types which provide different data. OSM Schema will provide 3 type data OSM like point, line and polygon and Thematic Schema will provide data based on its type in OSM such as health, landuse, school, etc.

.. figure:: /static/training/osm/11_006.*
   :align: center
   
   *Screenshot in Export Format Page*

9. After select file format, you can click :guilabel:`Tree Tag` tab to chose feature for result data tag of your export.
There are 2 options that you can select. Humanitarian Data Model only export all tags that related with humanitarian information such as hazard, public services and utilities, whereas OSM Data Model export all tag in OSM.

.. figure:: /static/training/osm/11_007.*
   :align: center
   
   *Screenshot in Tree Tag Page*

10. Then, click :guilabel:`Preset File` tab add specific preset file if you have any. Using specific preset file will export your data with specific tag based on the presets. Moreover, tag from previous data model both Humanitarian and OSM Data Model will be cleared. However, if you do not have any specific preset you can skip this step.

.. figure:: /static/training/osm/11_008.*
   :align: center
   
   *Screenshot in Preset File Page*

11. Last step to make an export file in HOT Export is click :guilabel:`Export Details` tab and you can see summary of your export details file and please select at least one of three options in Export Options about how your export result will be share to other users.
If you finish, please click :guilabel:`Create Export` .
  
.. figure:: /static/training/osm/11_009.*
   :align: center
   
   *Screenshot in Export Details Page*

12. After the running process finished and export status is completed, you can download your export file result in some file format data which have been defined previously.
You also can delete, clone or rerun this export project if you want. All other request for HOT Export can be found in :guilabel:`Exports` menu.

.. figure:: /static/training/osm/11_010.*
   :align: center
   
   *Screenshot in Export Result Page*

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

.. figure:: /static/training/osm/11_011.*
   :align: center
   

3. If you don’t want to download the larger area you can resize the area and draw a border by yourself 
   with click :guilabel:`manually select box` from the toolbar in the left side of the map. 
   Draw a box in the slippy map to define the target area.

.. figure:: /static/training/osm/11_012.*
   :align: center

   *Select area manually*

4. To download OSM data specific to one feature, for example schools, click :guilabel:`Wizard` menu. 
   In the Wizard menu, you can filter your data with using `JOSN <http://www.jsoniq.org/>`_ query, 
   in the simple way it can be a tag contains Key and Value, 
   for example if you want to download schools type :kbd:`amenity=school` in :guilabel:`Query Wizard`.

.. figure:: /static/training/osm/11_013.*
   :align: center
   
   *Query box in Overpass Turbo*

5. Click :guilabel:`Build and Run Query`, wait for a moment until school objects are displayed in the area of interest. 
   You should see something like the screenshot below which shows all the school objects in OSM in the area of interest.

.. figure:: /static/training/osm/11_014.*
   :align: center
   
6. If you only want data type in point/node format,
   you can specify that in the query box in the left side. 
   To do this, erase school with way and relation type, and then click :guilabel:`Run` menu in the top left side.
   The result will be a school objects with only point/node data type filtered. 
   You can also add more detailed query in the query box and then click :guilabel:`Run`.

.. figure:: /static/training/osm/11_015.*
   :align: center
   
   *Erase several query in query box*

7. To download the schools data you can click Export menu,
   there are several data formats that you can choose such as **geoJSON, GPX, KML, .osm**, etc. 
   If you not familiar with geoJSON, you can select :guilabel:`level0` to download .osm data format that you can use later with QGIS or other mapping software.

.. figure:: /static/training/osm/11_016.*
   :align: center
   
   *Export Overpass Turbo result*