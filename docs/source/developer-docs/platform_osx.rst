.. _development_under_osx:

Development under OSX
=====================

In this document we will walk you through the different activities you will
need to do as an OSX developer wishing to work on the |project_name| codebase.

Installation of version control tools
-------------------------------------

Setup GitHub for OSX
.....................

To check out the code for development, you first need to install a git client.
You can get detailed instructions including a native OSX client here:
https://help.github.com/articles/set-up-git#platform-mac


Check out the code and the test data
------------------------------------

In this section we actually check out the source code and the test data
using the tools we installed above.

Clone the code repository
.........................

First open a bash prompt. The repository can now be cloned by issuing the
commands listed below.::

   cd ~
   mkdir -p .qgis/python/plugins
   cd .qgis/python/plugins/
   git clone https://<your username>@github.com/AIFDR/inasafe.git inasafe-dev

.. note:: The items in angle brackets above should be replaced with your
   personal details as required.

When the final command above runs, you should see something like this in the
console when the clone process is completed::

   $ git clone https://timlinux@github.com/AIFDR/inasafe.git inasafe-dev
   Cloning into 'inasafe'...
   remote: Counting objects: 5002, done.
   remote: Compressing objects: 100% (1526/1526), done.
   remote: Total 5002 (delta 3505), reused 4835 (delta 3338)
   Receiving objects: 100% (5002/5002), 2.38 MiB | 7 KiB/s, done.
   Resolving deltas: 100% (3505/3505), done.

Checkout the test data
......................

The repository can now be cloned by issuing the commands listed below.::

   cd  ~/.qgis/python/plugins/
   git clone https://<your username>@github.com/AIFDR/inasafe_data.git inasafe_data

.. note:: The items in angle brackets above should be replaced with your
   personal details as required.

When the final command above runs, you should see something like this in the
console when the clone process is completed::

   $ git clone https://timlinux@github.com/AIFDR/inasafe_data.git inasafe_data
   Cloning into 'inasafe_data'...
   remote: Counting objects: 5002, done.
   remote: Compressing objects: 100% (1526/1526), done.
   remote: Total 5002 (delta 3505), reused 4835 (delta 3338)
   Receiving objects: 100% (5002/5002), 2.38 MiB | 7 KiB/s, done.
   Resolving deltas: 100% (3505/3505), done.

Install QGIS
............

Download the latest stable QGIS installer by carefully following the instructions at
http://hub.qgis.org/projects/quantum-gis/wiki/Download#41-Release.

After opening QGIS you need to enable the plugin from the plugin menu by doing
:menuselection:`Plugins --> Manage Plugins` and then search for the
|project_name| plugin in the list and enable it.

OSX Caveats
...............

Our primary development platform is Linux (specifically Ubuntu Linux). Some
features of the development environment - particularly the **Make** tools do not
run on OSX without first installing XCode and the XCode command line tools. Even with
make installed the OSX environment does not yes have feature parity with the
Linux platform.

.. _osx-commandline_setup:

Command line environment setup
------------------------------

.. _osx_shell_launcher-label:

Create a shell launcher
.......................

A command line environment is useful for running unit tests and for developing
and testing standalone scripts written to use the |project_name| libraries. Under
OSX you need to ensure that your environment is properly configured in order to
find QGIS and its libraries.

We have provided scripts that do this as :file:`runmake-osx.sh`,
:file:`runtest-osx.sh` and :file:`runshell-osx.sh`.

.. note:: These scripts may need some adjustment if you are using newer versions
    of GDAL.

The first two scripts mentioned above can be used to run make commands (e.g.
```./runmake-osx.sh pylint``` will do the pylint checks). The last script can be
used to add the QGIS options needed to use QGIS python bindings to your python path
like this::

    source runshell-osx.sh

Which should produce output like this::

    QGIS PATH: /Applications/QGIS.app/contents/MacOS
    PYTHON PATH: :/Applications/QGIS.app/Contents/Resources/python:/Library/Frameworks/
    GDAL.framework/Versions/1.9/Python/2.7/site-packages

Verifying your system path
..........................

To verify your path, launch your python shell (by typing ```python``` at the prompt).
Now enter the follow simple script which will do a simple test to see if you can import
the QGIS libs::

   from qgis.core import *
   exit()

Assuming you get no error messages, you have a functional python command
line environment which you can use to test QGIS functionality with.

.. _osx-nose-setup:

Nose testing tools
------------------

.. _osx-pip-setup:

Installing pip
..............

Use easy setup to install pip (assuming it is not already present)::

   sudo easy_install pip


Installing nose
...............

`Nose <http://somethingaboutorange.com/mrl/projects/nose/>`_ is a tool for
automation of running python unit tests. With nose you can run a whole batch
of tests in one go. With the nosecover plugin you can also generate coverage
reports which will indicate how many lines of your code actually have been
tested.

To install these tools do::

   sudo pip install nose nose-cov

Running tests using nose
........................

Once they are installed, you can run the nose tests from OSX by going to
the plugin directory/inasafe-dev folder and running::

   ./runtests-osx.sh

.. note:: The tests do not all run successfully on OSX yet - we are working
   to remedy this.

PyCharm Setup
-------------

`PyCharm <http://www.jetbrains.com/pycharm/>`_ is our preferred and supported
IDE for InaSAFE. Although the software is not free, as InaSAFE is an open source
project, InaSAFE developers may use PyCharm without charge - please contact
the project team for details on how to activate your copy.

To set up PyCharm on OSX you should first download and install your copy as per the
instructions on the PyCharm web site as linked in the paragraph above.

We store the PyCharm .idea directory in the source of InaSAFE so using InaSAFE should
simply be a question of opening the inasafe-dev directory that you checked out
earlier and making the following small configuration changes:


1) Create a new python environment profile in
:menuselection:`Settings --> Project Interpreter --> Python Interpreters` called
:kbd:`Python with QGIS 1.8 libs` and add the following paths to it::

  /Applications/QGIS.app/Contents/Resources/python
  <path to your inasafe checkout>/third_party

2) Edit your unittest defaults and ensure the key / value pairs below are added.
:menuselection:`Run --> Edit Configurations --> Defaults --> Python Tests --> Unit tests`
and click the ellipses (...) next to :guilabel:`Environment Variables` ::

  PYTHONPATH : /Applications/QGIS.app/Contents/Resources/python
  QGIS_PREFIX_PATH : /Applications/QGIS.app/contents/MacOS
  QGIS_PATH : /Applications/QGIS.app

