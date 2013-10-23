.. _osm_building_downloads:

Fetching Building data from OSM
===============================

This document describes in detail research into and procedures for downloading
building footprint data and converting it to a shapefile. The notes below will
be incorporated into a simple web app to provide this functionality.

Overpass Queries for Buildings
------------------------------

Get buildings for an area in osm xml
....................................

As xml::

  http://overpass-api.de/api/interpreter?data=(node["building"="yes"](-6.185440796831979,106.82374835014343,-6.178966266481431,106.83127999305725);way["building"="yes"](-6.185440796831979,106.82374835014343,-6.178966266481431,106.83127999305725);relation["building"="yes"](-6.185440796831979,106.82374835014343,-6.178966266481431,106.83127999305725););(._;>;);out body;

Get buildings for an area in geojson
.....................................

As json (not used but just here in case of future needs)::

  http://overpass-api.de/api/interpreter?data=[out:json];(node[%23building%22=%22yes%22](-6.185440796831979,106.82374835014343,-6.178966266481431,106.83127999305725);way[%22building%22=%22yes%22](-6.185440796831979,106.82374835014343,-6.178966266481431,106.83127999305725);relation[%22building%22=%22yes%22](-6.185440796831979,106.82374835014343,-6.178966266481431,106.83127999305725););(._;%3E;);out%20body;

Fetch with python
-----------------

Example python script to retrieve geometries::

  import urllib2
  params = {'xmin': -6.185440796831979, 'ymin': 106.82374835014343,'xmax': -6.178966266481431, 'ymax': 106.83127999305725}
  myOsmXmlUrlPath = ('http://overpass-api.de/api/interpreter?data=(node[%%22building%%22=%%22yes%22](%(xmin)s,%(ymin)s,%(xmax)s,%(ymax)s);way[%22building%22=%22yes%22](%(xmin)s,%(ymin)s,%(xmax)s,%(ymax)s);relation[%22building%22=%22yes%22](%(xmin)s,%(ymin)s,%(xmax)s,%(ymax)s););(._;%3E;);out%20body;' % params)
  # Note that osm json is NOT geojson!
  myOsmJsonUrlPath = ('http://overpass-api
  .de/api/interpreter?data=[out:json];(node[%22building%22=%22yes%22](%(xmin)s,%(ymin)s,%(xmax)s,%(ymax)s);way[%22building%22=%22yes%22](%(xmin)s,%(ymin)s,%(xmax)s,%(ymax)s);relation[%22building%22=%22yes%22](%(xmin)s,%(ymin)s,%(xmax)s,%(ymax)s););(._;%3E;);out%20body;' % params)
  myRequest = urllib2.Request(myOsmXmlUrlPath)
  try:
      myUrlHandle = urllib2.urlopen(myRequest, timeout=60)
      myFile = file('osm.xml', 'wb')
      myFile.write(myUrlHandle.read())
      myFile.close()
      except urllib2.URLError:
          raise

.. note:: you can html encode your overpass queries using this tool:
   http://meyerweb.com/eric/tools/dencoder/ also there is
   http://overpass-turbo.eu/ which is a really good tool for experimenting
   with overpass queries.

Get Dane Springmeyer's style converter
--------------------------------------

We want to convert the JOSM preset file (think of it as an xml file that will
generate a form in JOSM to ensure the correct attributes are captured) into as
shp2pgsql style file (which determines what the schema and rules are for
importing osm data into PostgreSQL). To do this we use a converter tool written
by Dane Springmeyer::

  curl -O https://raw.github.com/hotosm/scripts/master/preset2style.py

Get the JOSM preset
-------------------

For the JOSM preset mentioned above, we want to use one created by Kristy van
Puk::

  curl -o building-preset.xml -O http://hot-export.geofabrik.de/uploads/preset-19

Get the default OSM style
-------------------------

We need to have this for the JOSM conversion step coming up as it will be
merged in as the base style.

  curl -O http://svn.openstreetmap.org/applications/utils/export/osm2pgsql/default.style

Convert the JOSM preset to and OSM2PGSQL style
----------------------------------------------

The file downloaded above misses the group element so you should insert this
after the presets opening tag::

  <group name="HOT" fr.name="HOT" en.name="HOT">

and this before the presets closing tag::

  </group>

Now you can convert it using hte preset2style application we downloaded
previously::

  python preset2style.py -s default.style --preset building-preset.xml > building.style

Creating a shapefile
--------------------

You need to have postgresql / postgis installed and osm2pgsql. OSX users can
find precompiled binaries for osm2pgsql here: http://cl.ly/201r35290x0e

Save the above python script as fetch_osm_xml.py. To automate the process you
can do e.g.::

  #!/bin/bash
  rm buildings*
  rm osm.xml
  python fetch_osm_xml.py
  DBNAME=$$
  createdb -T template_postgis $DBNAME
  osm2pgsql -S building.style -d $DBNAME osm.xml
  pgsql2shp -f buildings.shp $DBNAME planet_osm_polygon
  dropdb $DBNAME

Then save it as a script and run it e.g.::

  ./fetch_osm_buildings.sh

