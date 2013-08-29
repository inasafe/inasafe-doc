.. _converter:

Converter
=========

Shakemaps are useful for carrying out contingency planning for the event of an
earthquake. Normally these are distributed as grid.xml files which are not
usable in |project_name| or QGIS. This tool will import a grid.xml file as a
GEOTIFF file from where it can be used within |project_name|.

Two different interpolation algorithms can be used during the import process -
``Nearest Neighbour`` and ``Inverse Distance``. After the conversion, the tool
automatically creates |project_name| keyword metadata for the layer so that
it can be used immediately for analysis.

.. figure:: /static/user-docs/converter.*
   :scale: 75 %
   :alt: Converter
   :align: center

   Converter

To use this tool effectively:

 * Select a grid.xml for the input layer.
 * Choose where to write the output layer to.
 * Choose the interpolation algorithm that should be used when converting the
   xml grid to a raster. If unsure keep the default.

You can obtain shake data for free from the `USGS
shakemap site <http://earthquake.usgs.gov/earthquakes/shakemap/list.php?y=2013>`_.

If you download the grid file, you should right-click on it and choose
:menuselection:`Save as` in order to ensure that it is saved properly. OSX and
Linux users may also consider using command line tools to fetch the grid file:

OSX::

   curl -O http://earthquake.usgs.gov/earthquakes/shakemap/global/shake/<shake id>/download/grid.xml

Linux::

   wget -C http://earthquake.usgs.gov/earthquakes/shakemap/global/shake/<shake id>/download/grid.xml

.. note:: Replace the <shake id> in the commands above with the actual shake id.



