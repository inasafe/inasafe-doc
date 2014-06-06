.. _keywords_system:

Keywords System
===============

This document describes the purpose and usage of the |project_name| *keywords*
system.

.. seealso:: Please also refer to the documentation on
    :ref:`the keywords Wizards <keywords_wizard>` and the
    :ref:`keywords editor <keywords_editor>` which are tools to help you
    to create keywords files.

Purpose
-------

The keywords system is used by the :ref:`Impact Functions <impact_functions>`
to determine the nature of the input layers that have been passed to them.

Each input GIS dataset used by |project_name| needs to have an accompanying
keywords file.
The purpose of the keywords file is to provide additional metadata needed by
the impact functions.
For example, the keywords file will indicate whether a given dataset should
be treated as a *hazard* or an *impact* layer.
It is also used to indicate the context of the layer (e.g. "it's a *flood*
layer", "it's an *earthquake* layer").

By convention and expectation, the keywords file should be named with the
same base name of the GIS datasource it accompanies.
For example a flood dataset saved as

:file:`C:\\gisdata\\flood.tif`

would need to have an accompanying keywords file saved as:

:file:`C:\\gisdata\\flood.keywords`

.. note:: We recommend to **avoid using spaces** in your file names and file
   paths!

The |project_name| QGIS plugin provides an editor for these keywords.
The purpose of this document is to describe the keywords editor and to
provide guidelines as to the use of keywords.

.. note:: Currently keywords are not validated by the library.
   This means if you for example misspell a keyword,
   use the wrong letter case (e.g. upper case instead of lower case) or
   provide the wrong keyword for the context (e.g. provide a subcategory of
   flood to an exposure category), the system will not be able to determine
   what to do with the file.
   For that reason you should follow the guidelines below carefully to ensure
   you have entered your keywords correctly.

Guidelines
----------

In this section we lay out the guidelines for keyword usage.

Category
........

Every dataset should have a category assigned to it.
Category should be written in lower case.

{{ category_table }}

Example keywords file entry
::

  category: hazard

Subcategory
...........

The selection of a subcategory value is dependent on the category:

Valid subcategories for category 'hazard':

{{ subcategrory_hazard_table }}

Where tephra is volcanic ashfall.

Valid subcategories for category 'exposure':

{{ subcategrory_exposure_table }}

Example keywords file entry
::

  category: hazard
  subcategory: flood

Units
.....

The units keyword is used to indicate the metric or imperial units represented
by each data entity (a grid cell or a vector feature) in a layer.

Example keywords file entry:

   ========  ================================  =======================
   Key       Allowed Values (pre InaSAFE 2.1)  Allowed Values (>= 2.1)
   ========  ================================  =======================
   units     m                                 metres_depth
   units
   exposure  road
   hazard
   ========  ================================  =======================

  category: hazard
  subcategory: flood
  units: m




In the above case there is a soft constraint to use a value for units of m,
feet or wet/dry as defined by the table below because the subcategory is
'flood'.
The following are the allowed units which are dependent on the subcategory
defined.

Valid subcategories for subcategory 'tsunami' or subcategory 'flood':

{{ units_inundation_table }}

In the case where the units are m (meters) or feet, the input dataset should be
a raster layer where each cell in the raster represents a depth in the units
specified.

In the case of wet/dry, the input dataset needs to be a vector polygon layer.
Any area that is inside a polygon is considered 'wet' and any area outside of
a polygon is considered to be 'dry'.

Valid subcategories for subcategory 'volcano'

.. table::

   =====  ==============
   Key    Allowed Values
   =====  ==============
   units  kg2/m2
   =====  ==============

In this case the dataset should be a raster layer where each cell represents
the kilograms per meters squared of ash fall on that cell.

.. note:: 'units' and 'datatype' (described below) should be considered to
   be mutually exclusive - i.e. they should not both be present in any given
   keywords file.

Datatype
........

The data type keyword indicate what kind of geospatial data is represented
(Numeric, Polygon, Line, Point).


Assumptions
-----------

The following assumptions are made about keywords, which may or may not be
programmatically enforced by the |project_name| library and GUI:

* There should only be **one keyword for a given key** in the keywords file.
* Keywords for **category** are **enforced** to be one of 'hazard' or
  'exposure' by the GUI.
* All keywords should be in **lower case**, **without spaces**
  with the exception of 'Title' whose value may contain both spaces and
  mixed case letters.
* Values for keywords should generally be lower case, with the exception of
  **datatype values may be in upper case** (e.g. MMI)
* Keys and values should **not contain colons**.
  In the keyword editor, any colons will be replaced with a full stop
  character.
* All other Keywords and values that do not fit the above domain lists may be
  used but they may produce undesired results.

Translations
------------

Although |project_name| is available in different languages, the 'key' in the
keywords files should always be written in english.

Keywords for remote and non-file based layers
---------------------------------------------

If you are using a PostgreSQL, WFS, Spatialite or other non-file based
resources, you can still create keywords.
In these circumstances the keywords will be written to a sqlite database - by
default this database is stored as :file:`keywords.db` within the
|project_name| plugin directory root.

You may wish to use a different location for the :file:`keywords.db` keywords
database - you can configure this by using the |project_name| options dialog.
The options dialog can be launched by clicking on the |project_name| plugin
toolbar's options icon (as shown below) or by doing
:menuselection:`Plugins --> InaSAFE --> InaSAFE Options`.

.. figure:: /static/user-docs/toolbar_options.*
   :scale: 100 %
   :align: center
   :alt: Options Icon

   Selecting the options icon

When the options dialog is opened, the keywords database path can be specified
under the tab :guilabel:`Advanced` using the
:guilabel:`keyword cache for remote datasources` option as shown below.

.. figure:: /static/user-docs/options-keyword-db-path.*
   :scale: 100 %
   :align: center
   :alt: Path to options database

   Path to options database

.. note::

   1. Support for remote and non-file based layers was added in |project_name|
      version 0.3.
   2. The database can be opened using a sqlite editor such as sqliteman,
      but the data in the keywords table is not intended to be human readable
      or edited.
      The table columns consist of an MD5 hash based on the URI for the
      datasource (typically the database connection details) and a blob
      which contains the keywords as a pickled python dictionary.

See the :doc:`./options` document for more information about the |project_name|
options dialog.

Sharing your keywords cache
---------------------------

In theory you can place the keywords file on a network share and create
a shared keyword repository in a multi-user environment, but you should note
that the layer URI hashes need to be identical in order for a layer's keyword
to be found.
This means that, for (contrived), example
::

   connection=postgresql,user=joe,password=secret,resource=osm_buildings

would not be considered the same as
::

   connection=postgresql,user=anne,password=secret,resource=osm_buildings

since the user credentials differ, resulting in a different URI.
To work around this you could create a common account so that every user will
effectively use the same URI to load that layer e.g.
::

   connection=postgresql,user=public,password=secret,resource=osm_buildings

For certain resources (e.g. ArcInfo coverages, Spatialite databases) where
the keywords cache is also used, you should take care to use a common mount
point or network share to access the data if you wish to successfully hit the
cache with the layer's URI.
For example you could have all users mount your data to the same place.
Under Unix like operating systems this could look something like this:

:file:`/mnt/gisdata/jk.sqlite`

Under Windows you could always the same drive letter and path the to share
e.g.:

:file:`Z:\\gisdata\\jk.sqlite`

Getting help
------------

If you need help using the keywords editor, you can click on the
:guilabel:`Help` button at the bottom of the dialog and this page will be
displayed.
