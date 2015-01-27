.. _realtime:

|project_name| Realtime
=======================

|project_name| Realtime is a component of the |project_name| project designed
for deployment on a server and creation of Impact Maps a short interval after
an event occurs.

Currently the realtime system supports Earthquake fatality impact assessments,
though in future we envisage additional support for other disaster types being
facilitated.

.. note:: This work was funded by the Australian Government
    |GoA| and the World Bank-|GFDRR|.
    We thank you for your support.

Historical Note
---------------

The original prototype of the realtime system was implemented by Ole Nielsen
(|GoA|).
The subsequent port of the realtime system to |project_name| was implemented
by Tim Sutton (Linfiniti Consulting CC., funded by The World Bank ,
|AIFDR| and |GoA|).

Supported Platforms
-------------------

Currently only Ubuntu 14.04 is supported.

The software may work or can easily be made to work on other platforms but it
is untested.

Generated Products
------------------

For every shake event, the tool produces a number of GIS products:

* A raster layer interpolated from the original MMI point matrix and symbolized
  according to the MMI scale colours.
* A vector (shapefile) layer generated from the original MMI point matrix and
  symbolized according to the MMI scale colours.
* A vector (shapefile) layer depicting MMI isolines and symbolized according to
  the MMI scale colours.
* A cities layer (shapefile) which lists the affected cities along with key
  data such as distance from and direction to epicenter,
  number of people resident in the city, mmi exposure etc.

In addition to the above mentioned GIS products, the following 3 files are
created for each event:

* A PNG file containing a single page report as illustrated above.
* A large PNG image which contains exactly the same content as the pdf but in
  an image format.
* A thumbnail PNG image which contains a reduced size image of the report.

Architecture
------------

|project_name| Realtime is implemented by four main python modules:

* **sftp_client** - A generic tool to fetch directory listings and
  files from a remote server. There is also an ftp_client module for
  deployments where the shake maps are on an ftp server.

* **shake_data** - A mostly generic tool to fetch shake files from an ftp
  server. There is an expectation that the server layout follows a simple flat
  structure where files are named after the shake event and are in the format
  of shake data as provided by the USGS (XXXXXX TODO fact check XXXX).
  :samp:`ftp://118.97.83.243/20110413170148.inp.zip`

.. note:: This data is now no longer hosted via ftp and requires an ssh
    account in order to retrieve it.

* **shake_event** - A rather monolithic module that 'knows' how to
    fetch, unpack, process and generate a report for a quake event.
    The module logic is based on the standard shake data packaging
    format supplied by the USGS.
    We have restricted our implementation to require only the :file:`grid
    .xml` file.
* **make_map** - A simple python tool for running one or multiple shake
    analyses.

|project_name| has strong dependencies on QGIS (http://qgis.org) which is
used for much of the data processing and reporting functionality.

.. note:: Currently version 779e16603ee3fb8781c85a0e95913a1f6bbd2d6a is
    the 'known good' SHA1.

Two of these dependencies are a template QGIS project and a map composition
template.

We have designed the realtime reporting engine to allow end users to
customise the map report to their needs with little or no programming.
The primary way to achieve this is by opening the custom template
:file:`realtime/fixtures/realtime-template.qpt` in QGIS and modifying
its contents.

You could also build a new template from scratch provided the item IDs listed
in the section that follows are used.

Installation Overview
---------------------

The realtime system is deployed as a collection of http://docker.com
containers. The supported platform in the docker images is currently Ubuntu
14.04 LTS. The instructions provided below assume the host OS is Ubuntu 14.04,
although it should work on any platform where docker is supported (albeit with
some adaptions to fit your OS).

There are 4 docker images used for deployment

* **docker-realtime-inasafe:** An image containing the actual realtime software.
* **docker-realtime-sftp:** An image containing a simple ssh service for
  uploading shakemaps to.
* **docker-realtime-apache:** An image for apache to host the realtime front end.
* **docker-realtime-btsync:** An image containing the synchronised based data.
  sets needed for the realtime map products.


An additional git repository **docker-realtime-orchestration** contains helper
scripts that will orchestrate the deployment of the above.

We have tried in the design to keep as much of the logic in docker and
require as little configuration of the host system as possible. To begin you
need to have docker installed and we recommend to use the upstream docker
packages and not the ubuntu provided images::

    # Setup latest docker.io
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A
    echo "deb https://get.docker.io/ubuntu docker main " > /etc/apt/sources.list.d/docker.list
    apt-get update
    apt-get install lxc-docker


We also recommend adding the user administering the realtime deployment to the
docker group::

    sudo usermod -a -G docker <username>

Where ``username`` should be substituted with the user who will administer
the realtime system.

.. note:: You should log out and in again for the above command to take effect.


We have tried to build the system so that it can be generally installed and
maintained without having root access to the host on which it runs. The reason
for this is that it will be very likely installed on partner organisation's
hardware / software and we would prefer to limit the invasiveness and potential
for damaging other services. There are two installation tasks that you will need
root / sudo access for:

    * to set up an apache reverse proxy into the realtime apache container.
        We will explain this step further below.
    * to ensure that port 9222 is open on the host's firewall and is publicly
        accessible (it will provide access for pushing shakemap data to the
        host from a remote site).


Checkout and run the orchestration build script
-----------------------------------------------

You should first checkout the docker orchestration script. This is a small
repository that contains logic to build and deploy the full realtime
architecture.::

    mkdir -p ~/dev/docker
    cd ~/dev/docker
    git clone git@github.com:AIFDR/docker-realtime-orchestration.git
    cd docker-realtime-orchestration

Now run the build script.::

    ./build.sh

.. note:: You can also run the script with an optional argument which is a
    github username / organisation name. Use this argument when you wish
    to do testing by building against your own clones of each of the above
    mentioned repositories. One potential motivation for doing this is to
    use :kdb:`apt-cacher-ng` to cache installation packages and make them
    available to the build process.

The build script will take some time to run as it checks out a copy of
each docker repository and builds an image from it. In the case of the
docker-realtime-inasafe image a pruned clone of the entire inasafe-dev repo
is also made (which can take some time to checkout).

At the end of the build script, you should have a collection of docker images
something like this::

    REPOSITORY                      TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
    aifdr/docker-realtime-inasafe   latest              eeddc5ad569a        11 minutes ago      1.188 GB
    aifdr/docker-realtime-btsync    latest              9a4cdd32c449        49 minutes ago      234.8 MB
    aifdr/docker-realtime-sftp      latest              800a8d7a7d0e        52 minutes ago      245.2 MB
    aifdr/docker-realtime-apache    latest              25caae296541        55 minutes ago      259.4 MB

You can generate a list similar to above by running the :kbd:`docker images` command.


Deploy the docker containers as images
--------------------------------------

The above images need to be deployed into production - we do this by using
the :file:`deploy.sh` script provided in the orchestration repository::

    timlinux@overhang:~/dev/docker/docker-realtime-orchestration$ ./deploy.sh

    ----------------------------------------
    This script will deploy InaSAFE realtime
    images as a series of docker containers
    ----------------------------------------


    Running apache container
    =====================================
    docker-realtime-apache is not running
    5ac47064bf5d9d5d3a699c17373a971465e7da239e1ab0fb617c4d4e7e9af236

    Running SFTP Server container
    =====================================
    docker-realtime-sftp is not running
    86f3b480a5777267abe52ee7877161463f043ca6b82f646272663a48d2ad3714

    Running btsync container
    =====================================
    docker-realtime-btsync is not running
    41bc53a168252f0617ae3f8009beb2ecc3bea4cd34e7f3f2529ec1d6c2e86eda

    Login details for SFTP container:
    =====================================
    User: realtime Password: aHoo7eigu6Me


.. note:: You should make a careful note of the password provided under
    **Login details for SFTP container**


The deploy script runs a long running instance (container) of each of the
following images:

* btsync
* sftp
* apache

The ``docker-realtime-inasafe`` image will be run as a short running instance by
means of a cron job which we will explain below.


Reverse proxy and firewall access for 9222
------------------------------------------

Proxy
.....

For end user visbility of the apache container (which hosts the final shakemap
outputs), you should use apache or nginx on the host to act as a reverse proxy.
It is also possible to publish the apache service directly from the docker
apache using port forwarding from the docker container to the host's port 80
but we do not recommend it. We provide an example configuration below based
on nginx::

    upstream realtime.inasafe.org { server localhost:8080;}

    server {
        listen      80;
        server_name realtime.inasafe.org;
        location    / {
            proxy_pass  http://qgis-plugins;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $http_host;
            proxy_set_header X-Forwarded-For $remote_addr;
        }
    }

This will present incoming traffic to the host on port 80 for domain
`realtime.inasafe.org` as if it were a direct connection into the apache
container.

SFTP
....

For the sftp container you will need to ask the system administrator to open
port 9222 on the host. For example if they are using "uncomplicated firewall"
they could perform the following command to allow it::

    sudo ufw allow 9222

.. note:: The sysadmin may need to apply similar rules on other routing
    equipment such as routers, switches etc. within the organisational network
    where the host is running.


Run the orchestrated docker group
---------------------------------

We can run the ``docker-realtime-inasafe`` image as if it was an application
that will perform the complex of tasks needed to generate a new quake map should
any shakemap files be pending processing. This can be initiated by using the
:file:`run.sh` script provided in the orchestration repository - for example::

    ./run.sh

Which by default will produce no output since there are no shakemaps available::




Typically you will want to run this task every minute and process any new
shakemaps that have arrived by the sftp services::

    # m h  dom mon dow   command
    * * * * * /home/<user>/dev/docker/docker-realtime-orchestration/run.sh
    * * * * * date > /tmp/test.log

.. note:: You should substitute <user> in the snippet above with your own user
    name / the user name that runs the realtime services.



Additional realtime utilities
-----------------------------

The utilities listed below can all be used to perform various administrative
tasks within the realtime system::



Run the latest report::

  cd ~/dev/python/inasafe-realtime
  scripts/make-latest-shakemap.sh

Running all back reports
::

  cd ~/dev/python/inasafe-realtime
  scripts/make-all-shakemaps.sh

Listing shake files on s/ftp server
::

  cd ~/dev/python/inasafe-realtime
  scripts/make-list-shakes.sh



QGIS Map Template Elements
--------------------------

This section describes the various elements that comprise the standard map
template, and which you can modify directly in the template.
These fall into three groups:

* **Static elements**.
* **Elements containing tokens for replacement**.
* **Elements that are directly updated by the renderer**.

Static Elements
................

These are e.g. logos which are not touched by the realtime map renderer at all.
You can remove or replace them with your own elements as needed.

* **logo-left** - the logo element at the top left corner of the map layout.
* **right-logo** - the logo element at the top right corner of the map layout.
* **overview-map** - a map overview showing the locality of the event.
  This is the overview frame for map-0 (the main map in the layout).
  It is locked and limited to show the population layer only.
* **legend** - a map legend, by default configured to show only the layer for
  the population layer.
  It is locked and limited to the population layer.

Elements containing tokens for replacement
..........................................

In this case the element name is not significant, only the token(s) it
contains.
At render time any of the tokens in these elements will be replaced with
translated (if an alternative locale is in effect) content from the map
renderer according to the keywords listed below in this document.

    * **main-title** - the main title at the top of the page.
      By default this element contains the keyword:
      :samp:`[map-name]`.
    * **intensity-date** - the date and intensity of the event.
      By default this label contains the following replacement tokens:
      :samp:`M[mmi] [date] [time]`
    * **position-depth** - the position (lon, lat) and depth of the event.
      By default this label contains the following replacement tokens:
      :samp:`[longitude-name] [longitude-value] [latitude-name] [latitude-value] [depth-name] [depth-value] [depth-unit]`
    * **location-description** - the postion of the event described relative to
      the nearest major populated place.
      By default this label contains the following replacement tokens:
      :samp:`[located-label] [distance] [distance-unit], [bearing-degrees] [bearing-compass] [direction-relation] [place-name]`
    * **elapsed-time** - the time elapsed between the event and when this
      report was generated.
      By default this label contains the following replacement tokens:
      :samp:`[elapsed-time-label] [elapsed-time]`
    * **scalebar** - the scalebar which reflects the scale of the main map.
      This is **Currently disabled**.
    * **disclaimer** - A block of text for displaying caveats, cautionary notes,
      interpretive information and so on.
      This contains the following replacement tokens: :samp:`[limitations]`.
    * **credits** - A block of text for displaying credits on the map output.
      This contains the following replacement tokens: :samp:`[credits]`.

Elements that are directly updated by the renderer
..................................................

In this case any content that may be present in the element is completely
replaced by the realtime map renderer, although certain styling options
(e.g. graticule settings on the map) will remain in effect.

* **impacts-table** - a table generated by ShakeEvent which will list the
  number of modelled affected people in each of the MMI bands.
  This is an HTML element and output will fail if it is not present.
* **main-map** - primary map used to display the event and neighbouring towns.
  Developers can set a minimum number of neighbouring towns to display using
  the ShakeEvent api.
  This is a map element and output will fail if it is not present.
  This is an HTML element and output will fail if it is not present.
* **affected-cities** - a table generated by ShakeEvent which will list the
  closes N cities (configurable using the ShakeEvent api) listed in order of
  shake intensity then number of people likely to be affected.

Replaceable Keywords
---------------------

This section describes tokenised keywords that are passed to the map template.
To insert any of these keywords into the map template, simply enclose the
key in [] (e.g. [place-name]) and it will be replaced by the text value (e.g.
Tondano).
The list includes static phrases which have been internationalised (and so
will display in the language of the selected map local,
defaulting to English where no translation if available.
In cases where static definitions are used (e.g. [credits]) you can
substitute your own definitions by creating your own template.
More on that below in the next section.

* **map-name**: Estimated Earthquake Impact
* **exposure-table-name**: Estimated number of people exposed to each MMI level
* **city-table-name**: Places Affected
* **legend-name**: Population density
* **limitations**: This impact estimation is automatically generated and only
  takes into account the population and cities affected by different levels
  of ground shaking.
  The estimate is based on ground shaking data from BMKG,
  population density data from asiapop .org, place information from geonames
  .org and software developed by |BNPB|.
  Limitations in the estimates of ground shaking, population data and place
  names datasets may result in significant misrepresentation of the
  on-the-ground situation in the figures shown here.
  Consequently decisions should not be made solely on the information
  presented here and should always be verified by ground truthing and other
  reliable information sources.
* **credits**: Supported by the Australia-Indonesia Facility for Disaster
  Reduction and Geoscience Australia.
* **place-name**: Tondano
* **depth-name**: Depth
* **location-info**: M 5.0 26-7-2012 2:15:35 Latitude: 12 '36.00"S Longitude:
  124'27'0.00"E Depth: 11.0km Located 2.50km SSW of Tondano
* **depth-unit**: km
* **bearing-compass**: SSW
* **distance-unit**: km
* **mmi**: 5.0
* **longitude-name**: Longitude
* **date**: 26-7-2012
* **time**: 2:15:35
* **formatted-date-time**: 26-Jul-12 02:15:35
* **located-label**: Located
* **bearing-degrees**: -163.055923462
* **distance**: 2.50
* **direction-relation**: of
* **latitude-name**: Latitude
* **latitude-value**: 12'36.00"S
* **longitude-value**: 12'4'27.00
* **depth-value**: 11.0
* **version**: Version: 1.0.1
* **bearing-text**: bearing
* **elapsed-time-name**: Elapsed time
* **elapsed-time**: 26-Jul-12 02:15:35
* **fatalities-name**: Estimated Fatalities
* **fatalities-range**: 5 - 55
* **fatalities-count**: 55

Customising the template
------------------------

You have a few options to customise the template - we have gone to great
lengths to ensure that you can flexibly adjust the report composition
**without doing any programming**.

There are three primary ways you can achieve this:

* Moving replacement tags into different elements, or removing them completely.
* Moving the template elements themselves around or adding / removing them
  completely.
* Creating your own template from scratch and pointing the realtime tool to
  your preferred template.

The template is provided as :file:`realtime/fixtures/realtime-template.qpt`
and can be modified by opening the template using the QGIS map composer,
making your changes and then overwriting the template.
You should take care to test your template changes before deploying them to a
live server, and after deploying them to a live server.

If you wish to use your own custom template, you need to specify the
:samp:`INSAFE_REALTIME_TEMPLATE` environment variable, populating it with
the path to your preferred template file.

QGIS Realtime Project
---------------------

The cartography provided in the realtime maps is loaded from the
:file:`realtime/fixtures/realtime.qgs` QGIS project file.
You can open this file using QGIS, change the layers and their symbology,
and your changes will be reflected in the generated realtime shake report.

There are however some caveats to this:

* The overview map has locked layers
* The main map should always have a population layer with grayscale legend
  matching that provided in the original.
  If you do remove / change the population layer you should also remove /
  change the population layer legend.

If you wish to use your own custom project, you need to specify the
:samp:`INSAFE_REALTIME_PROJECT` environment variable, populating it with
the path to your preferred project file.

Configuration of population data
--------------------------------

Population data is used as the 'exposure' dataset for shake reports.
The following priority will be used to determine the path of the population
raster dataset.

1. the class attribute **self.populationRasterPath**
   will be checked and if not None it will be used.

2. the environment variable :samp:`INASAFE_POPULATION_PATH` will be
   checked if set it will be used.

3. A hard coded path of :file:`/fixtures/exposure/population.tif`
   will be checked.

4. A hard coded path of
   :file:`/usr/local/share/inasafe/exposure/population.tif` will be used.

Running a shake event
---------------------

To run a single event locally on a system with an X-Server you can
use the provided script :file:`scripts/make-shakemap.sh`.
The script can be used with the following options:

* **--list**: :samp:`scripts/make-shakemap.sh --list` - retrieve a list of
  all known shake events on the server.
  Events are listed as their full ftp url e.g.
  :file:`ftp://118.97.83.243/20121106084105.out.zip` and both *inp* and *out*
  files are listed.
* **[event id]**: :samp:`scripts/make-shakemap.sh 20121106084105` - retrieve
  and process a single shake event.
  A pdf, png and thumbnail will be produced.
* **--all**: :samp:`scripts/make-shakemap.sh --all` - process all identified
  events on the server in batch mode.
  **Note:** this is experimental and not production ready - we recommend to
  use the approach described in :ref:`realtime-batch`.
* **no parameters**: :samp:`scripts/make-shakemap.sh` - fetch and process
  the latest existing shake dataset.
  This is typically what you would want to use as the target of a cron job.

.. note:: The :file:`make_shakemap.sh` script is just a thin wrapper around
   the python :mod:`realtime.make_map` python module.

.. note:: An english local shakemap will always be generated regardless of
   the locale you have chosen (using the INASAFE_LOCALE env var).
   This en version will be in addition to your chosen locale.

Unit tests
-----------

A complete set of unit tests is provided with the realtime package for
|project_name|.
You can execute these tests like this
::

    nosetests -v --with-id --with-xcoverage --with-xunit --verbose \
        --cover-package=realtime realtime

There are also a number of Jenkins tasks provided in the Makefile for
|project_name| to automate testing on our continuous integration server.
You can view the current state of these tests by visiting this URL:

http://jenkins.inasafe.org/view/QGIS2-InaSAFE-master/

.. _realtime-batch:

Batch validation & running
---------------------------

The :file:`scripts/make-all-shakemaps.sh` provided in the |project_name|
source tree will automate the production of one shakemap report per event
found on the shake ftp server.

It contains a number of environment variable settings which can be used to
control batch execution. First a complete script listing
::

    #!/bin/bash

    export QGIS_DEBUG=0
    export QGIS_LOG_FILE=/tmp/inasafe/realtime/logs/qgis.log
    export QGIS_DEBUG_FILE=/tmp/inasafe/realtime/logs/qgis-debug.log
    export QGIS_PREFIX_PATH=/usr/local/qgis-realtime/
    export PYTHONPATH=/usr/local/qgis-realtime/share/qgis/python/:`pwd`
    export LD_LIBRARY_PATH=/usr/local/qgis-realtime/lib
    export INASAFE_WORK_DIR=/home/web/quake
    export SAFE_POPULATION_PATH=/var/lib/jenkins/jobs/InaSAFE-Realtime/exposure/population.tif
    for FILE in `xvfb-run -a --server-args="-screen 0, 1024x768x24" python realtime/make_map.py --list | grep -v inp | grep -v Proces`
    do
        FILE=`echo $FILE | sed 's/ftp:\/\/118.97.83.243\///g'`
        FILE=`echo $FILE | sed 's/.out.zip//g'`
        echo "Running: $FILE"
        xvfb-run -a --server-args="-screen 0, 1024x768x24" python realtime/make_map.py $FILE
    done
    exit

An example of the output produced from such a batch run is provided at:

http://realtime.inasafe.org/

.. note:: The resources used in the above examples are all available in the
    source code under :file:`realtime/fixtures/web`.
