.. _test_data:

Test Data
==========

Availability
------------

|project_name| provides a huge bunch of Test Data available on the net.
If you want to select only a specific training dataset you can easily go to
http://data.inasafe.org and download the package you need.

For areas with bad internet connection (and for people who want to download
everything in one go) we make the whole data available with
:ref:`Bittorrent Sync <btsync>`.

.. _btsync:

Bittorrent Sync
---------------

To download everything in one go you need to install BT Sync from their
homepage at http://www.bittorrent.com/sync

If you are using Windows or MacOS just download the package,
follow their install instructions and use

SECRET: BSU2UCAVRV7P4CHRYOZGIRQ2VN6CH4JP3

as the SECRET to enter.
Select the folder where you wish to sync the data and press :guilabel:`OK` to
start downloading.

If you are using Linux you can either basically do the same with the
exception that you will have to connect to a port (mostly 8888) on your
localhost and add the SECRET and the folder to sync to there.

Or you can give `docker <http://www.docker.io>` a try and checkout the
`inasafe-infrastructure <https://github.com/AIFDR/inasafe-infrastructure>`
repository with its btsync Dockerfile.

If you only want to clone the data you just have to run the
::

  rundocker.sh

command in a shell.
This will automatically start a docker container, download and run Bittorrent
Sync with the Read Only Secret and Sync all data to
:file:`/var/docker/volumes/btsync` directory.

The Path where to sync to is configurable by adjusting the Variable in the
:command:`rundocker.sh` script which is called DATADIR.

At the same place you can also change the name of the Docker Container.

If you just want to start a sync container with any other secret start
:command:`rundocker.sh` with an added SECRET afterwards
::

  ./rundocker.sh THISISMYSECRET

