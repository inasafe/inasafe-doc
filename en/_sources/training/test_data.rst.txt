.. _test_data:

Training Data
=============

Example data for use with |project_name| trainings is available for download via :ref:`direct download <directdownload>`, :ref:`Bittorrent Sync <btsync>`, or :ref:`Docker <usingdocker>`.

.. _directdownload:

Direct Download
---------------

To obtain a specific training dataset go to
http://data.inasafe.org and download the package you need.

.. _btsync:

BitTorrent Sync
---------------

The training data can be quite large in size, so if you have a bad internet connection (or want to download everything at once), all of the materials are also available with BitTorrent Sync.

To obtain the training data using BitTorrent Sync, first visit http://www.bittorrent.com/sync and download and install the software. Note that it is not necessary to provide your email address.

When installation is complete, open BitTorrent Sync. To download the training data to your computer, click on the :guilabel:`Options` button and then click :guilabel:`Enter a key...`

.. image:: /static/training/training-data/001_enter-a-key.png
   :align: center

Enter the following key: BSU2UCAVRV7P4CHRYOZGIRQ2VN6CH4JP3

After you enter the key you must choose a folder on your computer where you would like to synchronize the files. Create a new folder and select it.

The files will begin to synchronize with the folder on your computer. It may take awhile to download, depending on the speed of your connection.

.. note:: If you are using Linux the BitTorrent Sync interface will be available in your web browser at http://localhost:8888 after you start the application.

.. _usingdocker:

Using Docker
------------
If you are comfortable using `docker <http://www.docker.io>`_, you may clone the training data by using the btsync Dockerfile.

Copy the
`inasafe-infrastructure <https://github.com/AIFDR/inasafe-infrastructure>`_
git repository.

To clone the data files, run
::

  rundocker.sh

in a shell.

This will automatically start a docker container, download and run Bittorrent
Sync with the correct key and synchronize all data to the
:file:`/var/docker/volumes/btsync` directory.

The directory that docker will synchronize with is configurable by adjusting the DATADIR variable in the :file:`rundocker.sh` script.

To start a sync container with any other secret run :command:`rundocker.sh` with a KEY added as argument:
::

  ./rundocker.sh THISISMYSECRET

