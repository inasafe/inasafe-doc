.. _preparing_a_release:

Preparing a release
===================

This document outlines the steps that need to be carried out in order to
issue a new release of the |project_name| plugin.
The steps can be outlined as follows and are described in detail below:

* Identify what version number the new release will be assigned.
* Close all issues marked as blockers for the release.
* If needed, create a release branch
* Update all source files for PEP8 and PEP257 compliance.
* Ensure no assert statements are critical to code flow
* Ensure that Qt resources and user interface files have been compiled
* Ensure that user interface files meet HIG compliance
* Ensure all unit tests complete successfully and that tests that are expected
  to fail are documented.
* Ensure that user acceptance testing has been carried out.
* Ensure that all translation string lists have been updated and that the
  translation process has been carried out.
* Ensure that all new and existing features are adequately documented.
* Ensure that the API documentation is up to date.
* Update the changelog.
* Ensure that the sphinx documentation is compiled.
* Generate python optimised (.pyo) files for all sources.
* Update the plugin metadata to reflect current version.
* Generate a test package and validate in a clean room environment.
* Optionally branch the release in the revision control system.
* Tag the release in the revision control system.
* Upload the updated package zip file to old QGIS python plugin repository.
* Upload the updated package zip file to the new QGIS python plugin repository.
* Make announcements and press releases as needed.

Release numbering
-----------------

|project_name| will follow the
`semantic versioning system <http://semver.org/>`_.
Simply put, the following scheme should be applied to version numbers::

   ===================  ============================================================
   Version Increment    Intention
   ===================  ============================================================
   Major e.g 1.0.0      API incompatibility with the previous major release.
   Minor e.g. 1.1.0     API compatibility and extension over previous minor release.
   Point e.g. 1.1.1     API compatibility, bug fixes for previous point release.
   Alpha e.g. 1.0.0a    Feature incomplete preview of a minor or major release
   RC e.g. 1.1.0rc1     Feature complete preview of a minor or major release
   ===================  ============================================================

To identify the next release number, the table above can simply be applied.
Here are a couple of examples.

* You have fixed various bugs without adding new features or breaking the API,
  and you are ready to immediately publish your work.
  Result: **New point release.**
* You have implemented many new features, some of which required breaking API
  compatibility with the existing major release.
  Now you would like to make a public preview of your work before committing
  to a final release.
  Result: **New major release candidate.**

**Outcome:** A version number for the next release eg. 0.1.0.

Issue completion
----------------

Having determined the release number, you should use the GitHub *labels*
capability to assign a label matching the release to each blocking ticket.
There is no fixed rule on which tickets should be tagged for the release - the
best judgment of developers and managers should be used based on severity of
issues, available time to deadline, budget etc.

**Outcome:** At the end of  this step all
`issues <https://github.com/AIFDR/inasafe/issues>`_
tagged for the release should be closed.


PEP8 and PEP257 compliance
--------------------------

These **Python Enhancement Proposals** (PEP) relate to the formatting
of python source code.
In particular they mandate spacing, layout, line lengths and so on.
The outcome of PEP8 and PEP257 compliance is code that is consistently
formatted across the whole code base, regardless of authorship.

This consistency makes it easier to incorporate new members into the project
team and to collaborate effectively within the team.
A number of tools are available to help you to identify PEP8 and PEP257
transgressions, and there is a Makefile target (:command:`make pep8` which
will do a PEP8 test for you).
Under the Eclipse/PyDev IDE, there is also on the fly checking support which
can be enabled and that will notify you of any compliance issues as illustrated
in the screenshot below.

.. figure:: /static/pep8-highlighting.*
   :align:   center

**Outcome:** All source files for PEP8 and PEP257 compliance.

Check for assert statements
---------------------------

Using assert to raise exceptions in non test code can have bad side effects
because if python is run in optimised mode e.g. python -O, these lines are
ignored and the program logic will no longer work as expected.
On some platforms the use of python optimised code is mandated and we are
likely to get hard to investigate bug reports from end users at some
unspecified point in the future.

..  note:: This is a 'soft' requirement - since the python code for the plugin
   will be executed by the QGIS python internals, we can be fairly certain that
   python code will be executed with out the -O optimisation option for the
   short term.

**Outcome:** No assert statements used to control logic flow.

Compile Qt resources and user interface files
.............................................

The Qt4 resource and user interface definition files supplied with
|project_name| need to be compiled before they can be deployed.
There are two utility functions provided by Qt4 for this purpose:

* :command:`pyuic4` - A tool to compile Qt4 user interface definition files
  (.ui) into python source code.
  The .ui files contain xml which describes the placement of widgets within a
  user interface file.
* :command:`pyrcc4` - A tool to compile Qt4 resource files into python source
  code.
  Qt4 resources are 'in-code' representations of application resources needed
  at run time.
  These include images, icons, html, css etc. - whatever the application may
  need to use at runtime without resorting to retrieving assets from the
  filesystem.

The compilation of these resources if the default make target in the root and
*gui* python package.
To compile them simply do::

   cd <inasafe source>
   make

**Outcome:** Qt resources and user interface files have been compiled

HIG Compliance
..............

The |project_name| human interface guidelines (HIG) are described in the
:ref:`hig-label` document.
User interface should strive to comply with these guidelines.
As an over-arching principle, before any release, the user interface elements
that comprise that release should be tested both for usability and to ensure
that they are functional.

There is no automated test system for HIG.
Before making a release of HIG compliance, each dialog should be manually
tested and inspected.

**Outcome:** A consistent, user friendly and functional graphical user interface
environment for the software that comprises the releases.

Unit Testing
............

During the development process, unit tests should be written (following the
principles of test driven development).
A good test suite allows the code to be shipped with confidence knowing it
will behave as expected.
At the time of release, all the tests in the test suite should either pass or
have documented reasons as to why they fail, and that they are expected to
fail.

In addition, tests should provide a code coverage of 80% or better of the
shipped code base.
More information on running unit tests is included in
:ref:`running-tests-label`.

**Outcome:** All unit tests complete successfully, or when expected
to fail are documented accordingly.

User Acceptance Testing
-----------------------

While unit testing provides a quantitative measure of the code's robustness,
user acceptance testing provides a qualitative measure.
The plugin should be made available to 'invested' users to test with real
world data and in real world usage scenarios.
Any issues with workflow, ease of use, quality of model outputs and reports
etc. should be identified at this point and remedied.

**Outcome:** Software that works in real world usage.

Document new features
---------------------

New features in the release should be well documented using the procedure
described in :ref:`documenting-new-features-howto-label`.

**Outcome:** All new and existing features are adequately documented.

API Documentation
-----------------

In addition to documenting new features, any new python modules introduced
during the development work leading up to the release need to be included
in the API documentation.
This process is described in detail in the
:ref:`api-documentation-howto-label` document.

**Outcome:** The API is completely documented with rich,
relevant documentation.

Update the changelog
--------------------

A changelog is maintained in a number ok places:

The rst changelog
.................

In the ``inasafe-doc`` repository the :file:`changelog.rst` should be
maintained (:file:`inasafe-doc/docs/source/general/changelog.rst`)
that lists the key new features and improvements made with each release.
Use the :ref:`changelog` file to guide the style of any edits and additions made.

The changelog should not exhaustively list every commit that took place.
Rather it should list the key features and bug fixes that were made during the
release cycle.

.. note:: New release changesets should be introduced to this file
   **at the top** so that the newest release is always listed first.

**Outcome:** A succinct list of changes and improvements that were made during
the release cycle that will be visible on the InaSAFE web site.

The commit changelog
....................

This is an automatically generated changelog that enumerates every commit
that was made during the lifecycle of the release. It is stored as CHANGELOG
in the top level of the ``inasafe-dev`` source tree. To update the changelog
for the release simply run this make command::

    make changelog



Finalise translations
.....................

The |project_name| plugin is built from the ground up for internationalization.
In particular the following two languages are supported as part of this
project:

* English
* Bahasa Indonesia

There are three components of the project that require translation:

* The Graphical User Interface - primarily the :file:`gui` python package.
  Qt4 .ts files are used for these translations.
* The |project_name| libraries - these components provide the underlying
  functionality of the scenario assessment.
  Python gettext is used for these translations.
* The sphinx documentation - this is translated using gettext and uploaded to
  transifex for collaborative translation work.

The translation process for the first two items above is documented in
detail in :doc:`i18n`. The sphinx translation process is not yet well documented,
although it will be similar to the gettext process.

The final strings should be made available to translators before the release,
during which time a string freeze should be in effect on the release code tree.

Once the translation files have been updated, they should be converted to
compiled string lists (.qm and .mo files for Qt4 and gettext respectively) and
made available as part of the distribution.

**Outcome:** The released plugin will be multilingual supporting both
indonesian and english.

Compile the context help documentation
.......................................

Since version 2.0, the context help is generated from the master documentation
store in the ``inasafe-doc`` repository. See the
`InaSAFE Documentation Repository <https://github.com/AIFDR/inasafe-doc>`_
for more details, the specifics are not covered here.


You should have ``inasafe-doc`` checked out at the same directory level as
``inasafe-dev`` as the scripts used below depend on this filesystem layout.::

    ├── inasafe_data
    ├── inasafe-dev
    ├── inasafe-doc

You should write user documentation (explaining how the user interface etc.
work be adding to and editing the content found under:

:file:`docs/source/user-doc`

Once you have completed your work (which should be done against the ``develop``
branch of the ``inasafe-doc`` repo), you should commit it to your fork and then
issue a pull request for inclusion into the main repository.

To compile the documentation you need to have sphinx available on your
system. Under linux this is done as follows::

    sudo pip install sphinx

.. note:: You should install sphinx from pip rather than apt since the apt
    repo version will most likely be too old to compile the documentation
    properly.

Once documentation is checked out and updated with any specific information
pertinent to the release, it should be compiled using
:command:`scripts/post_translate_application_help.sh`. This will build all
the documentation under :file:`docs/source/user-docs` and copy them into
:file:`insafe-dev/docs` ready for deployment with the release package.

In :file:`inasafe-dev` subsequent to building the context documentation,
the :command:`git status` command should be used to
ensure that all generated documentation is also under version control and then
these files should be committed prior to tagging the release.

**Outcome:** Sphinx documentation is compiled providing complete documentation
to be shipped with the plugin.

Update plugin metadata and version number
.........................................

QGIS uses specific metadata to register the plugin.

* :file:`metadata.txt`

In this metadata you would typically update the version and status entries to::

    version=1.1.0
    # alpha, beta, rc or final
    status=beta

Immediately after tagging the previous release, and then change the status
designation to final just prior to tagging the release.

**Outcome:** The plugin metadata reflects the current version of
|project_name|.


Merge to master
---------------

When develop is in a release ready state, it should be merged to the master
branch and all tests should pass on the master jenkins instance. The best
way to facilitate the merge to master is to make a pull request from the
main repository's ``develop`` branch.

Tag the release
---------------

As of 2.0.0 we only tag releases, not branch them (in keeping with gitflow
methodology).


Prerequisite
............

As of version 1.1.0 we will be cryptographically signing the release
tags using GPG (Gnu Privacy Guard), and annotating the git tag. You should
ensure you have a GPG key set up in your user profile before tagging.

You need to have a GPG key already (google GPG to see how to create one).

You should register your key with git.
To do this, first identify what your key id is::

    gpg --list-sigs | grep tim

Which should produce something like this::

    uid                  Tim Sutton (QGIS Key) <tim@linfiniti.com>
    sig 3        97626237 2007-07-19  Tim Sutton (QGIS Key) <tim@linfiniti.com>

So in my case my GPG id is :samp:`97626237`. Now register that key with git::

    git config --global user.signingkey 97626237

Now when you tag (as shown below), your tag will be signed with your chosen
GPG key.

Tagging
.......

Tagging the release provides a 'known good' state for the software which
represents a point in time where all of the above items in this list have
been checked. The tag should be named after the major, minor and point release
for example :samp:`version-1_2_0`.

If the release is a release candidate or and alpha release the letters
:samp:`rc` or :samp:`a` respectively should be appended respectively,
along with the related number.

For example version 1.2.0 alpha 1 would be tagged as :samp:`version-1.2.0a1`.

To tag the release simply use the make target as illustrated below.::

    make tag

You will be prompted for the semantic versioning tag number, your local
git checkout will be tagged and then that tag will be pushed to the upstream
repository 'origin' (which should be linked to the main upstream repo).

.. warning:: Only run ``make tag`` when you are on the ``master`` branch as
    all tagged releases should be against ``master``.

.. note:: Depending on your operating system / desktop environment, you may be
    prompted for your GPG passphrase, or it will be automatically supplied if
    you are using an agent.

**Outcome:** The release is tagged in git and can be checked out at any point
in the future. The tagged source tree can easily be downloaded at any point by
visiting https://github.com/AIFDR/inasafe/tags

Generate a test package
-----------------------

At this point a package should be generated. To generate a test package, use
the :file:`scripts/release.sh` bash script.

For example to create a test package for version 1.2.0 of the software,
issue the following command::

   scripts/release.sh 1.2.0

The generated package will be placed in the /tmp directory of your linux
system.

Test the package locally by extracting the package contents your user
personal plugin directory. For example under Linux::

   mkdir -p ~/.qgis2/python/plugins
   cd ~/.qgis2/python/plugins
   unzip inasafe.1.2.0.zip

Now start QGIS and enable the plugin in the QGIS plugin manager (
:menuselection:`Plugins --> Manage Plugins`).

Upload the package
------------------

QGIS provides an online plugin repository that centralizes the distribution
and retrieval of plugins. It is the most efficient way to make your plugin
available to the world at large.

The plugin can be uploaded by going to the
`InaSAFE plugin page <ttp://plugins.qgis.org/plugins/inasafe/>`_, logging in
and creating a new version.

Press announcements
-------------------

Once the release has been made, an announcement should be made to inform
interested parties about the availability of the new software.
A proforma announcement is provided below::

   Dear |project_name| Users

   We are pleased to announce the immediate availability of the newest
   version of |project_name| (version X.X.X). This version includes numerous
   bug fixes and improvements over the previous release::

   ----- changelog goes here -------------

   We welcome any feedback you may have on this release. You can use our
   issue tracker (requires free account) to notify us of any issues you may
   have encountered whilst using the system. The tracker is available here:

   https://github.com/AIFDR/inasafe/issues

   This project is supported by the Australian Aid Agency and the World Bank.

   Best regards

   (Name of person)

A standard list of contacts should be compiled and the notification sent to
all those listed.

**Outcome:** Interested parties are informed about the availability of the
new release.
