.. _faq:

Frequently asked Questions
==========================

Here you will find a lot of Questions answered which often appear on the
:ref:`google_group`.

**Where can I download the latest version?**

The latest version of |project_name| can be found following the
:ref:`installation` Guide.

**I found a bug, how should I report it?**

We manage the project issues using a GitHub issue tracker. The
`InaSAFE <https://github.com/AIFDR/inasafe/issues?direction=desc&sort=created&state=open>`_
issue tracker is open to everyone, though you will first need to register a
(free) account on GitHub to use it.
You can find the GitHub self-registration page
`here <https://github.com/signup/free>`_.

**Do I need to pay?**

No, the software is completely Free and Open Source.

**What license is it published under?**

|project_name| is published under the GPL version 3 license, the full text of
which is available at
`http://www.gnu.org/licenses/gpl-3.0.txt <http://www.gnu.org/licenses/gpl-3.0.txt>`_.

Under the terms of the license of you may freely copy, share and modify the
software, as long as you make it available under the same license.

**How is the project funded?**

The project is being developed 'for the good of humanity' and has been
jointly developed by |BNPB|, |GoA| & the
`World Bank <http://www.worldbank.org/>`_.

**Could we request a new feature?**

If you have a feature request, please use the
`issue tracker <https://github.com/AIFDR/inasafe/issues?direction=desc&sort=created&state=open>`_
to let us know about it, using the same procedure as for bug reporting.

**How do I rename a shape file and all the helper files?**

Use the rename command. rename [ -v ] [ -n ] [ -f ] perlexpr [ files ].
For example
::

    rename -v "s/^building/OSM_building_polygons_20110905/" building.*

**How do I reproject a spatial data file to WGS84 geographic coordinates?**

For raster data, use gdalwarp, for example
::

   gdalwarp -t_srs EPSG:4326 <source>.tif <target>.tif

For vector data use ogr2ogr. For example from TM-3 zone 48.2
::

   ogr2ogr -s_srs EPSG:23834 -t_srs EPSG:4326 <target>.shp <source>.shp


**How do I get OpenStreetMap building data?**

This tool will fetch building ('structure') and highway ('road') data from the 
OpenStreetMap project for you. For more information see 
:ref:`openstreetmap_downloader` section

**How do I take screen capture e.g. for use in a presentation?**

On Ubuntu, get the packages gtk-recordmydesktop and mencoder
Record using recordmydesktop (start and stop icon in the top bar)
Convert to other formats using mencoder, e.g
::

   mencoder -idx yogya_analysis-6.ogv -ovc lavc -oac lavc -lavcopts \
   vcodec=mpeg4:vpass=1 -of lavf -o yogya_analysis.avi

or

::

   mencoder -idx yogya_analysis-6.ogv -ovc lavc -oac lavc -lavcopts \
   vcodec=wmv2 -of lavf -o yogya_analysis.wmv

**How do I convert a vector hazard layer to a raster layer?**

For vector to raster conversion, use gdal_rasterize utility, for example
::

   gdal_rasterize -a <attribute_name> -l <source>.shp <destination>.tif


* Why does the plugin not show up in my QGIS Plugin Manager?

One common issue is that if you upgraded from QGIS 1.7.x to 1.8 you may not
get the new plugin repo added to your repo list. To fix this you can do:

* open QGIS
* Go :menuselection:`Plugins --> Fetch Python Plugins`
* Click :guilabel:`Repositories` tab
* Click :guilabel:`add`
* :guilabel:`Name`: Official QGIS Repository
* :guilabel:`Url`: http://plugins.qgis.org/plugins/plugins.xml
* Save it and the plugin repo list should update. If it doesn't,
  close and open QGIS to force an update.
* In the python plugin manager main tab now you should find |project_name|
  available

**How do I fix KeywordDbError on Windows?**

It’s an issue related to permission issue. Normally, it occurs when
the keyword.db is not writable by current user.
The thing that you have to do is re-run QGIS as Administrator or re-install
QGIS as Administrator.

Another way to solve it is deleting the registry of InaSAFE.
You can do it by opening :guilabel:`regedit` (Registry Editor).
To open regedit, you need to search it in :guilabel:`Start Menu` (it is
usually not shown in Start Menu).

Open regedit.

Find inasafe registry under :menuselection:`My Computer--> Software --> QGIS --> QGIS --> PythonPlugins`. After that,
right click on the inasafe, and click :guilabel:`Delete`. Restart QGIS and
try to run InaSAFE again to see if it works.

Please see `InaSAFE issue #459 <https://github.com/AIFDR/inasafe/issues/459>`_
, `InaSAFE issue #564 <https://github.com/AIFDR/inasafe/issues/564>`_, and
`InaSAFE issue #569 <https://github.com/AIFDR/inasafe/issues/569>`_ for
further information.
