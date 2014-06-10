.. _logging:

Logging
=======

|project_name| includes a logging subsystem that can be used to:

* record event messages in the QGIS Log Console
* record event messages to a file e.g.
  :file:`/tmp/inasafe/10-10-2012/timlinux/logs/inasafe.log`
* record exception details to a Sentry installation available at
  http://sentry.linfiniti.com/inasafe/
* email a developer a message when a logging event occurs (currently disabled)

In this section we describe best practices and procedures for logging in
|project_name|.

Getting and using the named Logger instance
-------------------------------------------

We use the '|project_name|' logger instance as standard for :samp:`safe` and
:samp:`safe_qgis` package. For :samp:`realtime` package, we use a different
logger set in :samp:`realtime/__init__.py` (see
:samp:`realtime.utilities.setup_logger`).
::

    from realtime.utilities import setup_logger
    setup_logger()

It is the responsibility of each
client package to setup the logger - typically in
the :samp:`__init__.py` for the package.

For the :samp:`safe` package, we need to use the :samp:`setup_logger` function
from :samp:`safe.common.custom_logging` (set in :samp:`safe/__init__.py`)
::

    from safe.common.custom_logging import setup_logger
    setup_logger()


For the :samp:`safe_qgis` package, we need to use :samp:`setup_logger` function
from :samp:`safe_qgis.utilities.custom_logging` (set in
:samp:`safe_qgis/__init__.py`)
::

    from safe_qgis.utilities.custom_logging import setup_logger
    setup_logger()


The logger will typically be assigned to a module variable :samp:`LOGGER`.
To actually use the logger in your :samp:`safe` and :samp:`safe_qgis` module
you need to do something like this:
::

    import logging
    LOGGER = logging.getLogger('InaSAFE')

    # And then in your class / method:
    LOGGER.debug('Hello world')


To use the logger in your :samp:`realtime` module you need to do something
like this:
::

    import logging
    from realtime.utilities import realtime_logger_name
    LOGGER = logging.getLogger(realtime_logger_name())

    # And then in your class / method:
    LOGGER.debug('Hello world')

Logging exceptions
------------------

It is recommended to log exceptions as per the following example
::

    try:
        1/0
    except Exception:
        LOGGER.exception('Something went terribly wrong')

The exception log type will cause the full traceback, the exception message
and the message provided to the LOGGER.exception call to all be logged e.g.
::

    2012-10-10 10:53:54,733 - InaSAFE - ERROR - Something went terribly wrong
    Traceback (most recent call last):
      File "<input>", line 2, in <module>
    ZeroDivisionError: integer division or modulo by zero

The above example was contrived in the QGIS python console.
When the exception originates inside a module, the traceback will include the
complete call tree.

Logging in loops
----------------

.. warning::
   Please be considerate when logging into loops as this can slow execution a
   lot.
   We had a spatial analysis loop with two logged messages and it took 15sec
   for 1000 iterations, removing logging brought it to 5sec.
   In another case, using 2700 aggregation units resulted in |project_name|
   blocking due to one single logging call.
   The issue is *probably* the refreshing of class QgsMessageLogViewer
   See also :ref:`profiling`

Remote logging
--------------

There is support for logging to a remote server.
This currently intended for developer use only and will provide ongoing
statistics about the number and nature of exceptions taking place in
|project_name|.

.. note:: For privacy / security reasons this is disabled by default and you
    need to jump through two hoops to make it work.

The remote server is available here: http://sentry.linfiniti.com/inasafe/

Remote logging is implemented using `raven <http://pypi.python.org/pypi/raven>`_
and `sentry <http://pypi.python.org/pypi/sentry>`_.
Raven needs to be installed on the local client.
On ubuntu you can install it by doing
::

    sudo pip install raven

To prevent user's unwittingly sending exception reports, it is required to
first set an environment variable before starting QGIS / running tests
::

    export INASAFE_SENTRY=1

.. note:: The sentry logger is set to only log exceptions.

Here is an example session which will install raven, enable sentry and then
launch QGIS
::

    sudo pip install raven
    export INASAFE_SENTRY=1
    /usr/local/bin/qgis

QGIS Log Messages
-----------------

For the :samp:`safe_qgis` package, log messages will also be written to the
QGIS log console under a tab labelled '|project_name|'.
You can view these messages by clicking on the small triangular icon in the
bottom right corner of the QGIS main window.

.. figure:: /static/log-notifications.png
   :align:   center

Clicking on the triangle indicated in red above will open the log dock window
in QGIS from where you can browse log messages conveniently.

.. figure:: /static/log-view.png
   :align:   center

.. note:: QGIS 1.8 or greater is required for this functionality.

Logging with third party applications
-------------------------------------

If you have written your one SAFE library client, you should set up your own
logger instance - just be sure that it is a named logger (called
:samp:`InaSAFE`) and any log messages from the safe library will be written
to your logger.
For inspiration on how to do this, take a look at the :func:`setup_logger`
function in :file:`safe_qgis/utilities/custom_logging.py`.
