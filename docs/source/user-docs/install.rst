.. _installation:

============
Installation
============

.. note::
   |project_name| is a plugin for `Quantum GIS <http://qgis.org>`_ (QGIS), so
   QGIS must be installed first via QGIS Python Plugin Repository

To install |project_name|, use the plugin manager in QGIS:

    :menuselection:`Plugins --> Fetch Python Plugins`

Search for '|project_name|', select it and click the install button.
The plugin will now be added to your plugins menu.

From Zip Archive
----------------

.. warning:: This installation method is not recommended unless you have no
   internet access or wish to use a specific version of |project_name|.
   Please install using the plugin repository described above rather.

We make regular releases of the |project_name| plugin and they are available at
http://plugins.qgis.org/plugins/inasafe/. Simply choose the most recent (i.e.
the one with the largest version number) and save it to your hard disk.

Now extract the zip file into the QGIS plugins directory. Under windows the
plugins directory is under:

:file:`C:\\Users\\<your username>\\.qgis\\python\\plugins`.

After extracting the plugin, it should be available as:

:file:`C:\\Users\\<your username>\\.qgis\\python\\plugins\\inasafe\\`.

Mac and Linux users need to follow the same procedure but instead the plugin
directory will be under the $HOME directory:

:file:`~/.qgis/python/plugins/`

Once the plugin is extracted, start QGIS and enable it from the plugin manager.
To do this open the plugin manager
:menuselection:`Plugins --> Manage plugins...` and type :samp:`insafe` into
the filter box.
You should see the |project_name| plugin appear in the list.
Now tick the checkbox next to it to enable the plugin.

.. figure:: /static/user-docs/plugin-manager.png
   :align: center

System Requirements
-------------------

 - A standard PC with at least 4GB of RAM running Windows, Linux or Mac OS X
 - The Open Source Geographic Information System QGIS (http://www.qgis.org).
   |project_name| requires QGIS version 1.7 or newer.
