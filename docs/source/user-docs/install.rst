.. _installation:


Installation
============


.. note::
   |project_name| is a plugin for Quantum GIS (|QGIS|), so
   QGIS must be installed first via QGIS Python Plugin Repository


To install |project_name|, use the plugin manager in QGIS:

    :menuselection:`Plugins --> Fetch Python Plugins`

Search for '|project_name|', select it and click the install button.
The plugin will now be added to your plugins menu.

For more information :doc:`../training/socialisation/introduction-of-qgis`


From InaSAFE test repository
----------------------------


During development of an InaSAFE version, developers make a test version of
the software for people to trial. Here are the instructions on how to install
this test version.

1. :menuselection:`Plugins --> Fetch Python Plugins`
2. :guilabel:`Click` on **Options** tab and :guilabel:`Check` *Show all plugins, even those marked as experimental*

.. image:: /static/user-docs/installer_options.*
   :align: center

3. :guilabel:`Click` on **Repository** tab and :guilabel:`Add` a new repository

.. image:: /static/user-docs/python_installer.*
   :align: center

4. Type the following into the Repository details

**Name:** 	InaSAFE Test
**URL:**	http://expertmental.inasafe.org/

.. image:: /static/user-docs/repository_details.*
   :align: center

5. :guilabel:`OK`

6. You should now have 2 repositories connected, :guilabel:`Click` on **Plugins**

.. image:: /static/user-docs/connected.*
   :align: center

7. :guilabel:`Upgrade plugin`

.. image:: /static/user-docs/upgradeable.*
   :align: center

8. InaSAFE has now been upgraded, all you need to do now is restart Quantum GIS

.. image:: /static/user-docs/restart.*
   :align: center

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
   :scale: 75 %
   :align: center
   :alt: Plugin Manager

   Plugin Manager

System Requirements
-------------------

 - A standard PC with at least 4GB of RAM running Windows, Linux or Mac OS X
 - The Open Source Geographic Information System QGIS (http://www.qgis.org).
   |project_name| requires QGIS version 1.7 or newer.

