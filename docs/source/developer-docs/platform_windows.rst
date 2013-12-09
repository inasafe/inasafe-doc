.. _development_under_windows:

Development under Windows
=========================

Overview
--------

In this document we will walk you through the different activities you will
need to do as a windows developer wishing to work on the |project_name|
codebase.
There are a number of steps that need to be performed in order to have a
usable development environment for |project_name| under Windows:

* Install a GIT client.
* Checkout the |project_name| code and the |project_name| standard test data.
* Install QGIS.
* Install a 32 bit version of python (windows 64 bit users only).
* Install pip and other requirements for running tests.
* Create a custom shell launcher with a python prompt.
* Setup your IDE (Eclipse PyDev or PyCharm).

.. note:: If you only want to run only the jenkins test suite there is no need
   to checkout the project code. This is task to be done by Jenkins than.
   You may also wish to read :doc:`jenkins_ci_windows_slave` if you wish to
   set up automated test suite running using Jenkins.

Installation of version control tools
-------------------------------------

Setup GitHub for windows
........................

To check out the code for development, you first need to install a git client.
We cover `GitHub for Windows <http://windows.github.com/>`_  but you can use
another client if you prefer.

The download size for this client will be at least 40mb and will vary
depending if you have the application requirements installed (the installer
will download and install the appropriate .NET framework if needed).

After downloading run the installer and follow the prompts as directed.

We recommend that you create an account on |github| as it will make it
possible to submit bug reports and generally participate in the
|project_name| project.

Enter your account details in the GitHub git client as directed.

Configure the default git shell
...............................

Next set your preferred shell to 'git bash' by going to the GitHub window  home
screen (if needed, press the left facing arrow in the top left of the GitHub
windows panel repeatedly until the arrow disappears).

Now use :menuselection:`tools --> options` (in the top center of the window),
to move to the options panel.

In the :guilabel:`default shell` section, select :menuselection:`Git Bash`.

Now click :guilabel:`update` and close the GitHub windows application.

Verify your git shell
.....................

We will do all the remaining tasks using the command line git client as it gives
more accurate control over git and the procedure is more closely aligned to that
of other operating systems.
So let us verify that your shell is available:

:menuselection:`Windows Start --> All Programs --> GitHub Inc. --> Git Shell`

Confirm that the window title for the window that appears starts with
'MINGWIN32'.

From now on use this shell for all the commands that follow below.

.. note:: Create a shortcut on your start button to the github shell as you will
   use if often!

Check out code and test data
----------------------------

In this section we actually check out the source code and the test data using
the tools we installed above.

Clone the code repository
.........................

First open a GIT bash prompt as described above.
The repository can now be cloned by issuing these commands:

Users on windows < Windows 7::

   cd  C:/Documents and Settings/<your username>/

Windows 7 or newer::

   cd  C:/Users/<your username>/

All windows versions::

   mkdir -p .qgis2/python/plugins
   cd .qgis2/python/plugins/
   git clone https://<your username>@github.com/AIFDR/inasafe.git inasafe-dev

.. note:: The items in angle brackets above should be replaced with your
   personal details as required.

When the final command above runs, you should see something like this in the
console when the clone process is completed::

   $ git clone https://<your username>@github.com/AIFDR/inasafe.git inasafe-dev
   Cloning into 'inasafe'...
   remote: Counting objects: 5002, done.
   remote: Compressing objects: 100% (1526/1526), done.
   remote: Total 5002 (delta 3505), reused 4835 (delta 3338)
   Receiving objects: 100% (5002/5002), 2.38 MiB | 7 KiB/s, done.
   Resolving deltas: 100% (3505/3505), done.

.. note:: Why do we check it out as inasafe-dev?
   We do this so that the standard release package can be used on the same
   system using the QGIS plugin manager.

Checkout the test data
......................

To check out the test data from git, first open a GIT bash prompt as
illustrated below:

The repository can now be cloned by issuing the commands listed below.
(Already completed in previous step):

Users on windows < Windows 7::

   cd  C:/Documents and Settings/<your username>/.qgis2/python/plugins/

Windows 7 or newer::

   cd  C:/Users/<your username>/.qgis2/python/plugins/

All windows versions::

   git clone https://<your username>@github.com/AIFDR/inasafe_data.git inasafe_data

.. note:: The items in angle brackets above should be replaced with your
   personal details as required.

When the final command above runs, you should see something like this in the
console when the clone process is completed::

   $ git clone https://<your username>@github.com/AIFDR/inasafe_data.git inasafe_data
   Cloning into 'inasafe_data'...
   remote: Counting objects: 5002, done.
   remote: Compressing objects: 100% (1526/1526), done.
   remote: Total 5002 (delta 3505), reused 4835 (delta 3338)
   Receiving objects: 100% (5002/5002), 2.38 MiB | 7 KiB/s, done.
   Resolving deltas: 100% (3505/3505), done.

Install QGIS
............

Download the latest QGIS 'standalone' installer from http://download.qgis.org
and install it by running the installation wizard and accepting the defaults
throughout.

After opening QGIS
(:menuselection:`Start-->All Programs-->QGIS Dufour-->QGIS Desktop (2.0.1)`)
you need to enable the plugin from the plugin menu by doing
:menuselection:`Plugins --> Manage and Install Plugins...`.
Then search the list for the |project_name| plugin and enable it.

Windows Caveats
...............

Our primary development platform is Linux (specifically Ubuntu Linux).
Some features of the development environment - particularly the **Make**
tools do not run on Windows.
Some helper scripts have been written to substitute for make but they do not
have feature parity with the make scripts.

.. _windows-commandline_setup:

Command line setup
------------------

.. _windows_shell_launcher-label:

Create a shell launcher
.......................

A command line environment is useful for running unit tests and for developing
and testing standalone scripts written to use the |project_name| libraries.

We will create a custom shell launcher that will give you a python
shell environment using the python that comes bundled with QGIS, and that sets
various paths and environment variables so everything works as expected.
Find out the PATHs by using the command 'dir /x'.
Save the following listing in <QGIS Install Dir>/bin/python-shell.bat::

   @echo off
   SET OSGEO4W_ROOT=C:\PROGRA~1\QGISDU~1
   call "%OSGEO4W_ROOT%"\bin\o4w_env.bat
   call "%OSGEO4W_ROOT%"\apps\grass\grass-6.4.3\etc\env.bat
   @echo off
   SET GDAL_DRIVER_PATH=%OSGEO4W_ROOT%\bin\gdalplugins
   path %PATH%;%OSGEO4W_ROOT%\apps\qgis\bin
   path %PATH%;%OSGEO4W_ROOT%\apps\grass\grass-6.4.3\lib
   path %PATH%;"%OSGEO4W_ROOT%\apps\Python27\Scripts\"

   set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis\python;
   set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\Python27\Lib\site-packages
   set QGIS_PREFIX_PATH=%OSGEO4W_ROOT%\apps\qgis
   cd "%HOMEPATH%\.qgis2\python\plugins\inasafe"
   start "QGIS Shell" /B "cmd.exe" %*

.. note:: The QGIS_PREFIX_PATH environment variable should be unquoted!.

.. note:: You may need to replace PROGRA~1 above with PROGRA~2 if you are
   on 64bit windows and using the 32bit QGIS Version.

.. note:: This script is for QGIS 2.0.
   You may need to do some adjustment if you are using another version of QGIS.

For easy access to this shell launcher, right click on the qgis-shell.bat
script and (without releasing your initial right click) drag with the file
onto your start / windows button in the bottom left corner of the screen.

Verifying your system path
..........................

To verify your path, launch your python shell (by clicking the python-shell
.bat) and then start a python shell.
Don't be alarmed when it says "The system cannot find the path specified." It
should work anyway.

Now enter the follow simple script::

   import sys
   for item in sys.path:
       print item

Which should produce output like this::

   C:\Users\inasafe\.qgis2\python\plugins\inasafe-dev
   C:\PROGRA~1\QGISDU~1\apps\qgis\python
   C:\PROGRA~1\QGISDU~1\apps\Python27\Lib\site-packages
   C:\PROGRA~1\QGISDU~1\bin\python27.zip
   C:\PROGRA~1\QGISDU~1\apps\Python27\DLLs
   C:\PROGRA~1\QGISDU~1\apps\Python27\lib
   C:\PROGRA~1\QGISDU~1\apps\Python27\lib\plat-win
   C:\PROGRA~1\QGISDU~1\apps\Python27\lib\lib-tk
   C:\PROGRA~1\QGISDU~1\bin
   C:\PROGRA~1\QGISDU~1\apps\Python27
   C:\PROGRA~1\QGISDU~1\apps\Python27\lib\site-packages\PIL
   C:\PROGRA~1\QGISDU~1\apps\Python27\lib\site-packages\win32
   C:\PROGRA~1\QGISDU~1\apps\Python27\lib\site-packages\win32\lib
   C:\PROGRA~1\QGISDU~1\apps\Python27\lib\site-packages\Pythonwin
   C:\PROGRA~1\QGISDU~1\apps\Python27\lib\site-packages\wx-2.8-msw-unicode

It is particularly the second and third lines that you need to have in place
so that the QGIS libs can be found. Now do a simple test to see if you can
import the QGIS libs::

   from qgis.core import *
   exit()

Assuming you get no error messages, you have a functional python command
line environment which you can use to test QGIS functionality with.

.. _windows-nose-setup:

Nose testing tools
------------------

.. _windows-pip-setup:

Installing pip
..............

We need to install easy_install so that we can install pip to install
nosetests and other python tools.

Under Windows you need to run a little script to install easy_install and
then use easy_install to install pypi.

Download the script on
`this page <http://pypi.python.org/pypi/setuptools#windows>`_ called
ez_setup.py and save it somewhere familiar e.g. :samp:`c:\temp`.

.. note:: If you use windows 32bit, do not download the .exe file as described
   on `this page <http://pypi.python.org/pypi/setuptools#windows>`_, rather
   just download the ez_setup.py

For both 32 and 64 bit
^^^^^^^^^^^^^^^^^^^^^^

Next launch the shell (python-shell.bat as described in
:ref:`windows-commandline_setup`) **as administrator** (by right clicking the
file and choosing run as administrator).
Then from the command line, launch :command:`ez_setup.py` by typing this::

   python c:\temp\ez_setup.py

.. note:: You will need to launch the shell as administrator whenever you
   need to install python packages by pypi.

Now in the same shell, use easy setup to install pip (make sure you have added
the QGIS scripts dir to your shell launcher's - which should be the case if
you have followed the notes in :ref:`windows-commandline_setup`)::

   easy_install pip

If the installation goes successfully, you should see output like this::

   Searching for pip
   Reading http://pypi.python.org/simple/pip/
   Reading http://pip.openplans.org
   Reading http://www.pip-installer.org
   Best match: pip 1.1
   Downloading http://pypi.python.org/packages/source/p/pip/pip-1.1.tar.gz#md5=62a9f08dd5dc69d76734568a6c040508
   Processing pip-1.1.tar.gz
   Running pip-1.1\setup.py -q bdist_egg --dist-dir c:\users\timsut~1\appdata\local
   \temp\easy_install--zkw-t\pip-1.1\egg-dist-tmp-mgb9he
   warning: no files found matching '*.html' under directory 'docs'
   warning: no previously-included files matching '*.txt' found under directory 'docs\_build'
   no previously-included directories found matching 'docs\_build\_sources'
   Adding pip 1.1 to easy-install.pth file
   Installing pip-script.py script to C:\PROGRA~2\QGISDU~1\apps\Python25\Scripts
   Installing pip.exe script to C:\PROGRA~2\QGISDU~1\apps\Python25\Scripts
   Installing pip.exe.manifest script to C:\PROGRA~2\QGISDU~1\apps\Python25\Scripts
   Installing pip-2.5-script.py script to C:\PROGRA~2\QGISDU~1\apps\Python25\Scripts
   Installing pip-2.5.exe script to C:\PROGRA~2\QGISDU~1\apps\Python25\Scripts
   Installing pip-2.5.exe.manifest script to C:\PROGRA~2\QGISDU~1\apps\Python25\Scripts

   Installed C:\PROGRA~2\QGISDU~1\apps\python25\lib\site-packages\pip-1.1-py2.5
   .egg
   Processing dependencies for pip
   Finished processing dependencies for pip

Installing nose
...............

`Nose <http://somethingaboutorange.com/mrl/projects/nose/>`_ is a tool for
automation of running python unit tests. With nose you can run a whole batch
of tests in one go.
With the nosecover plugin you can also generate coverage reports which will
indicate how many lines of your code actually have been tested.

To install these tools, launch your python prompt as administrator and then
do::

   pip install nose nose-cov

Running tests using nose
........................

Once they are installed, you can run the nose tests from windows by going to
the plugin directory/inasafe-dev folder (in your python-shell.bat shell
session) and running::

   run-tests-win.bat

.. _developing_using_pycharm:

Developing using PyCharm
------------------------

.. note:: This is optional - you can use any environment you like for editing
   python, or even a simple text editor.

.. note:: PyCharm is unfortunately not FOSS (Free and Open Source Software),
   however they do support the OpenSource Community by providing a "Free
   Community Edition" of PyCharm (http://www.jetbrains.com/pycharm/)

Download and Install
....................

Download PyCharm from their
`download page <http://www.jetbrains.com/pycharm/download/index.html>`_ and
install it taking all the defaults.
Note that the download is approximately 100 MB.

Once the installation is complete, start PyCharm and accept all the defaults
for the first-run wizard.
You may be prompted to restart pycharm at the end of that process - which you
should do.

Making PyCharm 'QGIS Aware'
...........................

We need to have various environment variables set in the PyCharm context in
a similar way we do with :ref:`windows-commandline_setup`.
Make a copy of your qgis-shell batch file and call it qgis-pycharm.bat.

Now alter the last line so that it launches pycharm instead of a shell as
per this example below::

  @echo off
  SET OSGEO4W_ROOT=C:\PROGRA~2\QGISDU~1
  call "%OSGEO4W_ROOT%"\bin\o4w_env.bat
  call "%OSGEO4W_ROOT%"\apps\grass\grass-6.4.2\etc\env.bat
  @echo off
  SET GDAL_DRIVER_PATH=%OSGEO4W_ROOT%\bin\gdalplugins\1.9
  path %PATH%;%OSGEO4W_ROOT%\apps\qgis\bin
  path %PATH%;%OSGEO4W_ROOT%\apps\grass\grass-6.4.2\lib
  path %PATH%;"%OSGEO4W_ROOT%\apps\Python27\Scripts\"

  set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis\python;
  set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\Python27\Lib\site-packages
  set QGIS_PREFIX_PATH=%OSGEO4W_ROOT%\apps\qgis
  cd "%HOMEPATH%\.qgis2\python\plugins\inasafe-dev"
  set PATH=c:\python27;%PATH%
  start "PyCharm aware of Quantum GIS" /B "C:\Program Files (x86)\JetBrains\PyCharm 2.7.3\bin\pycharm.exe" %*

Now use this PyCharm launcher whenever you need to do development work on
|project_name|.

.. note:: Right drag the batch file onto your start menu to make an easily
   accessible shortcut to your custom PyCharm launcher.

Setup |project_name| project
............................

On the PyCharm welcome screen, choose :guilabel:`Open Directory` and open the
git checkout you made i.e.::

   c:\Users\<username>\.qgis2\python\plugins\inasafe-dev"

Again, note that you should replace **<username>** with the appropriate name
for your user account.

Verifying that your environment is correct
..........................................

Open one of the source files that references QGIS e.g. :file:`safe_qgis/widgets/dock.py`
and ensure that the import statements near the top of the file are not underlined in
red. Note that you should wait a few minutes until PyCharm indicates it has completed
updating its indexes in the status bar at the bottom of the PyCharm window.

Running Tests
.............

To run individual tests (or all tests within a package and its subpackages)
simply :menuselection:`right-click` on any package containing test modules
or on an individual test module and choose
:menuselection:`Run Nosetests in ...`.

Developing using Eclipse
------------------------

.. warning:: We have standardised on using PyCharm for
   |project_name| development see :ref:`developing_using_pycharm`.
   This section of documentation is left here for reference purposes in the
   hopes that it may help die-hard PyDev fans, but it will no longer be
   maintained.

.. note:: This is optional - you can use any environment you like for editing
   python, or even a simple text editor.

If you wish to use an IDE for development, please refer to
`this article <http://linfiniti.com/2011/12/remote-debugging-qgis-python-plugins-with-pydev/>`_
for detailed information on how to get the basic Eclipse with PyDev setup.

Installing Eclipse
..................

You can download and install eclipse by getting the latest installer at
`eclipse.org <http://eclipse.org>`_.
Just run the installer accepting all defaults.

Installing PyDev
................

With Eclipse running, click  on :menuselection:`Help --> Eclipse Marketplace`
and from the resulting dialog that appears, type :kbd:`PyDev` into the search
box and then click :guilabel:`Go`.
On the search results page, choose PyDev and click the :guilabel:`Install`
button next to it.
Agree to the license terms and accept the aptana certificate,
then restart Eclipse as requested.

Custom Eclipse Launcher
.......................

You need to create a custom Eclipse launcher in order to use Eclipse PyDev.
The process is similar to :ref:`windows-commandline_setup` in that you need to
create a custom batch file that launches eclipse only after the OSGEO4W
environment has been imported.
Here are the typical contexts of the file::

   @echo off

   SET OSGEO4W_ROOT=C:\PROGRA~2\QGISDU~1
   call "%OSGEO4W_ROOT%"\bin\o4w_env.bat
   call "%OSGEO4W_ROOT%"\apps\grass\grass-6.4.3\etc\env.bat
   @echo off
   SET GDAL_DRIVER_PATH=%OSGEO4W_ROOT%\bin\gdalplugins
   path %PATH%;%OSGEO4W_ROOT%\apps\qgis\bin;%OSGEO4W_ROOT%\apps\grass\grass-6.4.3\lib
   set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis\python;
   set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\Python27\Lib\site-packages
   set QGIS_PREFIX_PATH=%OSGEO4W_ROOT%\apps\qgis
   "C:\Progra~2\eclipse\eclipse.exe"

.. note:: Use the path where your eclipse was extracted.
   Also note that PROGRA~2 may be PROGRA~1 in 32bit windows.

Save this file under <QGIS Install Dir>/bin/python-shell.bat and then
right-drag it from explorer to your Windows start button to create an easily
accessible shortcut to eclipse.

Creating a project
..................

The procedure for doing this is to do:
:menuselection:`File --> New --> Project...` and
then from the resulting dialog do :menuselection:`PyDev --> PyDev Project`.

In the resulting project dialog, set the following details:

* :guilabel:`Project name:` : :kbd:`inasafe`
* :guilabel:`Use default` : :kbd:`uncheck`
* :guilabel (windows):`Directory` :
  :kbd:`C:\\Users\\<user>\\.qgis2\\python\\plugins\\inasafe\\`
* :guilabel:`Choose project type` : :kbd:`Python`
* :guilabel:`Grammar Version` : :kbd:`2.7`
* :guilabel:`Add project directory to PYTHONPATH?` : :kbd:`check`

.. note:: The python shipped with QGIS for windows is version 2.7 so you
   should avoid using any additions to the python spec introduced in later
   versions.

At this point you should should click the link entitled 'Please configure an interpreter
in related preferences before continuing.' And on the resulting dialog do:

* :guilabel:`Python Interpreters: New...` : :kbd:`click this button`

In the dialog that appears do:

* :guilabel:`Interpreter Name` : :kbd:`QGIS Python 2.7`
* :guilabel:`Interpreter Executable` :
  :kbd:`C:\\Program Files (x86)\\QGIS Doufur\\bin\\python.exe`
* :guilabel:`OK Button` : :kbd:`click this button`

Another dialog will appear.
Tick the first entry in the list that points to your::

      C:\\Users\\inasafe\\Downloads\\eclipse\\plugins\\org.python.pydev_2.6.0.2012062818\\pysrc

The resulting list of python paths should look something like this::

   C:\Program Files\eclipse\plugins\org.python.pydev_2.6.0.2012062818\pysrc
   C:\PROGRA~1\QGIS Dufour\apps\Python27\DLLs
   C:\PROGRA~1\QGIS Dufour\apps\Python27\lib
   C:\PROGRA~1\QGIS Dufour\apps\Python27\lib\plat-win
   C:\PROGRA~1\QGIS Dufour\apps\Python27\lib\lib-tk
   C:\PROGRA~1\QGIS Dufour\apps\Python27
   C:\PROGRA~1\QGIS Dufour\apps\Python27\lib\site-packages
   C:\PROGRA~1\QGIS Dufour\apps\Python27\lib\site-packages\win32
   C:\PROGRA~1\QGIS Dufour\apps\Python27\lib\site-packages\win32\lib
   C:\PROGRA~1\QGIS Dufour\apps\Python27\lib\site-packages\Pythonwin
   C:\PROGRA~1\QGIS Dufour\apps\Python27\lib\site-packages\wx-2.8-msw-unicode

Click on the :guilabel:`New folder` button and add the QGIS python dir::

   C:\Program Files\QGIS Dufour\apps\qgis\python

* :guilabel:`OK Button` : :kbd:`click this button`

You will be returned to the Python Interpreters list and should see an entry
for **QGIS Python 2.7** listed there.
Now do in the **Environment** tab:

:guilabel:`New`

In the dialog that appears

:guilabel:`Name` : :kbd:`QGIS_PREFIX_PATH`
:guilabel:`Value` : :kbd:`C:\\PROGRA~1\\QGISDU~1\\apps\\qgis`

Then click ok to close the environment variable editor.

* :guilabel:`Ok` : :kbd:`click this button`

Then click :guilabel:`Finish` to finish the new project dialog.

Remote Debugging with Eclipse
.............................

For remote debugging, you should add pydevd to your PYTHONPATH before starting
*QGIS*.
Under Windows, the best way to do this is to add the following line to
:command:`qgis.bat` under C:\Program Files (x86)\QGIS Dufour\bin::

   SET PYTHONPATH=%PYTHONPATH%;C:\Progra~1\eclipse\plugins\org.python.pydev.debug_2.3.0.2011121518\pysrc

.. note::
     (1) You need to add a settrace() line at the point in your code where
     you would like to initiate remote debugging.
     After that, you can insert eclipse debugger breakpoints as per normal.

     (2) If you are running with remote debugging enabled, be sure to start the
     PyDev debug server first before launching the |project_name| QGIS plugin
     otherwise QGIS will likely crash when it can't find the debug server.

     (3) Place the above PYTHONPATH command before the final line that launches
     QGIS!

     (4) The exact path used will vary on your system - check in your eclipse
     plugins folder for "org.python.pydev.debug_<some date> to identify the
     correct path.

To initiate a remote debugging session, add the settrace() directive to your
source file and then start the python remote debugging service from the PyDev
debug perspective.
Then launch QGIS (or your command line application) and use the application
until the settrace line is encountered.
QGIS will appear to freeze - this is normal.
Now switch to Eclipse and you should see the settrace line has been
highlighted in green and you can step through the code using standard Eclipse
debugging tools (done most easily from the debugging perspective).

.. note:: Always remove or comment out settrace() when are done debugging!

Running Unit tests from the IDE
...............................

Using PyDev's build in test runner
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python has very good integrated support for unit testing.
The first thing you should do after setting up the IDE project is to run the
tests.
You can run tests in the following ways:

* For the entire |project_name| package
* For individual sub packages (e.g. engine, gui, storage, impact_functions)
* for an individual test module within a package
* for an class within a test module
* for an individual method within a test class

You can view these individual entities by browsing and expanding nodes in the
project panel in the left of the IDE.

.. note:: If you run the test suite for the entire |project_name| package, it
   will mistakenly treat the sphinx documentation :file:`conf.py` (docs.source
   .conf) as a test and fail for that test.
   This is 'normal' and can be ignored.

Setting PyDev to use the Nose test runner
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also configure Eclipse to run the tests using nose (which is
recommended).
To do this first do:

:menuselection:`Window --> Preferences --> PyDev -- PyUnit`

Now set :guilabel:`TestRunner` to :kbd:`Nosetests` and set the following
options::

    -v --with-id --with-coverage --cover-package=storage,engine,impact_functions,gui

As with using Pydev's built in test runner, you can also run any module, class
etc. while using the nose test runner by right clicking on the item in the
PyDev package explorer.

.. note:: Actually, we can run the test runner until this step.
   But, we got a problem, so you need to install python in your windows
   machine.
