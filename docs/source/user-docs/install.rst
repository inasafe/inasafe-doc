.. _installation:

Installation
============

.. note:: |project_name| is a plugin for |QGIS|, so QGIS must be installed 
   first via the QGIS Python Plugin Repository.

To install |project_name|, use the plugin manager in QGIS.

Go to :menuselection:`Plugins ‣ Fetch Python Plugins`
and search for :kbd:`inasafe`. Select it and click the :guilabel:`Install` 
button. |project_name| will now be added to the plugins menu.

For more information on |QGIS| and |project_name| 
see :doc:`../training/socialisation/introduction_of_qgis`.

From |project_name| test repository
-----------------------------------

During development of each version of |project_name|, the developers make an 
experimental version of the software available for users. To install the latest
test version of |project_name|, follow these instructions:

1. In QGIS, go to :menuselection:`Plugins ‣ Manage and Install Plugins`.

   .. image:: /static/user-docs/plugin_manager.*
      :align: center

2. Click on the :guilabel:`Settings` tab and check the box next to 
   :guilabel:`Show also experimental plugins`.

   .. image:: /static/user-docs/experimental.*
      :align: center

3. Click :guilabel:`Add...` at the bottom of the plugins window.

4. A :guilabel:`Repository details` window will open. Enter the following:

::

   Name:   InaSAFE Test
   URL:    http://experimental.inasafe.org/


.. image:: /static/user-docs/repository_details.*
   :align: center

5. Click :guilabel:`OK`.

   .. image:: /static/user-docs/connected.*
      :align: center

6. You will now see that two repositories are connected. Click the
   :guilabel:`Installed` tab and ensure that the |project_name| plugin is checked.

   .. image:: /static/user-docs/InaSAFE_installed.*
      :align: center

7. The experimental version of |project_name| is now installed. Restart QGIS
   before using |project_name|.

   .. image:: /static/user-docs/restart.*
      :align: center

From Zip Archive
----------------

.. warning:: This installation method is not recommended unless you have no
   internet access or wish to use a specific version of |project_name|.
   If this does not apply to you, use the plugin repository method
   described above.

We make regular releases of the |project_name| plugin and they are available at
http://plugins.qgis.org/plugins/inasafe/.
Simply choose the most recent (i.e. the one with the largest version number)
and save it to your hard disk.

Extract the zip file into the QGIS plugins directory.

.. note::
   Depending on your version of QGIS the plugin directory is either
   under a subdirectory of :file:`.qgis` (QGIS versions < 2.0) or 
   :file:`.qgis2` (QGIS version >= 2.0).

Depending on your Operating System (Windows, Linux,
OS X) and the version of QGIS, the directory containing the
plugins will be in:

- Windows: :file:`C:\\Users\\<your username>\\.qgis(2)\\python\\plugins\\`
- Linux: :file:`~/.qgis(2)/python/plugins/` (where "~" means
  :file:`/home/<your username>/`
- OS X: :file:`~/.qgis(2)/python/plugins/` (where "~" means
  :file:`/home/<your username>/`

.. note::
   :file:`.qgis(2)` means that the directory is either called
   :file:`.qgis` or :file:`.qgis2`.

If you are running Windows with QGIS 2.0, do the following:

1. Locate the directory
   :file:`C:\\Users\\<your username>\\.qgis2\\python\\plugins`.

2. Extract the plugin which you downloaded in this directory. It should be 
   available as
   :file:`C:\\Users\\<your username>\\.qgis2\\python\\plugins\\inasafe\\`.

OS X and Linux users must follow the same procedure but with the appropriate
directory, :file:`~/.qgis2/python/plugins/`.

Once the plugin is extracted, start QGIS and enable it from the plugin manager.

3. To do this go to :menuselection:`Plugins ‣ Manage plugins...` and type 
   :kbd:`inasafe` into the filter box.

4. You should see the |project_name| plugin appear in the list.
   Tick the checkbox next to it to enable the plugin.

.. figure:: /static/user-docs/plugin-manager.png
   :scale: 75 %
   :align: center
   :alt: Plugin Manager

   *Plugin Manager*

Downgrade the |project_name| plugin to a selected version
---------------------------------------------------------

If you are using an older version of QGIS or simply want to install a specific
version of the |project_name| plugin you must
perform the following steps:

1. Fetch the plugin manually from http://plugins.qgis.org/plugins/inasafe/. 
   Select your preferred version number and click :guilabel:`Download`.

2. Delete the :file:`inasafe` folder from your plugins directory. The location
   of this directory will vary depending on your operating system (see the
   previous section). 
   For Windows users the :file:`inasafe` directory would be in
   :file:`C:\\Users\\<your username>\\.qgis2\\python\\plugins`.

3. Extract the downloaded version into that folder, effectively replacing
   the previous version with whichever version you downloaded in step 1.

4. Restart QGIS.

System Requirements
-------------------

The requirements for running |project_name| are:

 - a standard PC with at least 4GB of RAM running Windows, Linux or OS X
 - the Open Source Geographic Information System QGIS (http://www.qgis.org);
   |project_name| requires QGIS version 1.7 or newer
