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
2. :guilabel:`Click` on **Options** tab and :guilabel:`Check`
   *Show all plugins, even those marked as experimental*

   .. image:: /static/user-docs/installer_options.*
      :align: center

3. :guilabel:`Click` on **Repository** tab and :guilabel:`Add` a new repository

   .. image:: /static/user-docs/python_installer.*
      :align: center

4. Type the following into the Repository details

   **Name:**   InaSAFE Test
   **URL:**    http://experimental.inasafe.org/

   .. image:: /static/user-docs/repository_details.*
      :align: center

5. :guilabel:`OK`

6. You should now have 2 repositories connected, :guilabel:`Click` on
   **Plugins**

   .. image:: /static/user-docs/connected.*
      :align: center

7. :guilabel:`Upgrade plugin`

   .. image:: /static/user-docs/upgradeable.*
      :align: center

8. InaSAFE has now been upgraded, all you need to do now is restart QGIS

   .. image:: /static/user-docs/restart.*
      :align: center

From Zip Archive
----------------

.. warning:: This installation method is not recommended unless you have no
   internet access or wish to use a specific version of |project_name|.
   Please rather install using the plugin repository described above.

We make regular releases of the |project_name| plugin and they are available at
http://plugins.qgis.org/plugins/inasafe/.
Simply choose the most recent (i.e. the one with the largest version number)
and save it to your hard disk.

Now extract the zip file into the QGIS plugins directory.

.. warning::
   Depending on your version of QGIS the plugin directory is either
   under a subdirectory of .qgis (QGIS versions < 2.0) or .qgis2 (QGIS version
   >= 2.0).

That also means depending on your Operating System (Windows, Linux,
OSX) in combination with the version of QGIS, the directory containing the
plugins will be in:

- Windows: :file:`C:\\Users\\<your username>\\.qgis(2)\\python\\plugins\\`.
- Linux: :file:`~/.qgis(2)/python/plugins/` (where "~" means
  :file:`/home/<your username>/`
- OSX: TODO

.. note::
   :file:`.qgis(2)` means that the directory is either called
   :file:`.qgis` or :file:`.qgis2`.

Example:
In Windows Operating System using QGIS 2.0 you would do following:

Locate the directory
:file:`C:\\Users\\<your username>\\.qgis2\\python\\plugins`.

After extracting the plugin, it should be available as:

:file:`C:\\Users\\<your username>\\.qgis2\\python\\plugins\\inasafe\\`.

Mac and Linux users need to follow the same procedure but instead the plugin
directory will be under the $HOME directory:

:file:`~/.qgis2/python/plugins/`

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

Downgrade the |project_name| plugin to a selected version
---------------------------------------------------------

In case you have to use an older Version of QGIS or just want to
install a specific version of the |project_name| plugin into QGIS you have
to do the following steps:

1. Fetch the plugin manually from http://plugins.qgis.org/plugins/inasafe/ by
   clicking on your preferred version number then clicking download.
2. Remove your local copy from :file:`~/.qgis2/python/plugins/inasafe`
   That would mean delete the folder :file:`inasafe` which is inside your
   :file:`~/.qgis2/python/plugins` directory.
   For Windows user this :file:`inasafe` directory would be in
   :file:`C:\\Users\\<your username>\\.qgis2\\python\\plugins`
3. Extract the downloaded version into that folder (Means to create the
   :file:`inasafe` folder inside :file:`~/.qgis2/python/plugins` again
4. Restart QGIS

System Requirements
-------------------

 - A standard PC with at least 4GB of RAM running Windows, Linux or Mac OS X
 - The Open Source Geographic Information System QGIS (http://www.qgis.org).
   |project_name| requires QGIS version 1.7 or newer.

