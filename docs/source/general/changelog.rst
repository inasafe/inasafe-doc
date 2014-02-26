.. _changelog:

Changelog
=========

Changelog for version |release|
-------------------------------

* Changes from a user point of view:

  * Users are able to select their own hazard and exposure attribute.
  * Simple wizards to walk new users through the software.
  * Power users are able to configure their own action checklist and
    "minimum needs".
  * Report view in your web browser:
    If you find the dock panel too small to show all the report details,
    or if you want to open it in your browser to quickly print the tabular
    report, you can now do so by right clicking on the report area of the
    |project_name| dock and choose Open in web browser.
  * Custom logo selection:
    As well as the new report template capabilities, you can now also set your
    organisation logo in the |project_name| options dialog.
  * Template based reports:
    This new feature means that you can now place your own logos in the
    report and customise the arrangement of the various report elements on
    the page.
  * Options dialog overhaul:
    We have overhauled the options dialog to make it easier to navigate and
    hide away advanced options into their own panel.

* New Functionality in |project_name|:

  * Routing
  * Evacuation routes
  * Transportation from A to B
  * Multiple Hazard Analysis
  * Damage and Loss Assessment (DALA)
  * Percentage of affected area by aggregation
  * Polygon flood impact on roads impact function added
  * Impact merge tool:
    This tool will allow you to merge the output from two impact assessments
    covering the same geographic extent and aggregated by the same areas.
  * OSM Roads downloader:
    In |project_name| 1.2 we introduced the new OSM downloader tool for
    buildings data.
    Beside a lot of improvements now roads can be downloaded too and at
    the same time the correct keywords will be assigned to the data.

* Changes in the code:

  * Port to QGIS 2.0: we have ported our code base to work with the new
    version of QGIS. Please note: QGIS 1.x releases will no longer be supported
    in this and future releases on |project_name| (starting from 2.0).
  * Support for PostGIS layers: You can now use PostGIS vector layers as
    input data for running impact functions.
  * Splitting Test Suite
  * Reviewing Impact Functions
  * Automatically run test on pull request
  * Easy to write impact functions

* Visible changes in Documentation and Webpage:

  * Update User and Developer Documentation
  * Update Training Materials: The tutorials section has been overhauled.
  * Track where |project_name| events are occurring
  * News Articles
  * Translation into other languages
  * New User Map:
    We have added a community map to our web site. Please take a moment to
    register yourself there as an |project_name| User, Developer or Trainer!
    See http://users.inasafe.org

Changelog for version 1.2.0
---------------------------

* User Interface

  * Improvements to |project_name| :ref:`panel <tb_dock>`: overhauled
    panel with improved messaging system.
  * Icon and branding overhaul: updated branding with a new Icon.

* Impact Functions

  * Aggregation and post-processing: added support for aggregation,
    that allows you to break down the results.
  * :ref:`Minimum needs <minimum_needs>`: population was calculated in Perka
    7 standard. Now it is configurable.

* Tools

  * New configuration options: selectable backend for zonal stats,
    developer mode to view source output.
  * :ref:`Minimum needs tool <minimum_needs>`: new tool for computing minimum
    needs for persons.
  * Shakemap importer: will import a :file:`grid.xml` as GEOTIFF in
    earthquake scenarios.
  * :ref:`Save scenario <save_scenario>`: new tool to save a scenario as a
    recallable text file.
  * :ref:`OSM Buildings Downloader <openstreetmap_downloader>`: will fetch
    OSM data from the web.
  * :ref:`Batch runner <batch_runner>`: ability to setup and run numerous saved scenarios in one go.

* Website

  * New website launched

Changelog for version 1.1.0
---------------------------

* Flood assessment using polygons now generates evacuation totals based
  on percent of affected people (defaults to 1%).
* Improvements to error handling with more informative messages to user.
* Memory requirements prediction to try to warn a user when they might not
  have enough RAM. See https://github.com/AIFDR/|project_name|/issues/476.
* Remote logging support. This **opt in** feature lets you submit useful
  diagnostic information to our fault logger at http://sentry.linfiniti.com.
* Support for automatic creation of packages in a test repository for
  early adopters to test with.
* Fix for 2D geometries - closes https://github.com/AIFDR/|project_name|/issues/471
* Default dock panel to right of QGIS. Closes
  https://github.com/AIFDR/|project_name|/issues/326
* Fix https://github.com/AIFDR/|project_name|/issues/358
* Many small 'under the hood' improvements.
* Realtime quake mapping support. This is available in source tree only
  and is a server side installable application. Indonesia specific.
* Realtime flood mapping support. This is available in source tree only
  and provides an experimental implementation for production of floodmaps.
  Jakarta specific.

Changelog for version 1.0.1
---------------------------

* Fix https://github.com/AIFDR/|project_name|/issues/374
* Fix https://github.com/AIFDR/|project_name|/issues/375

Changelog for version 1.0.0
---------------------------

* Added post processor infrastructure including gender and age specific
  indicators
* Added data source attribution
* Various GUI updates
* Added use of transparency in generated maps
* Added an earthquake impact function
* Documentation updates
* Many bugfixes and architectural improvements
* Better internationalisation support

Changelog for version 0.5.2
---------------------------

* This is a bugfix update to address some minor translation issues in the
  |project_name| package.

Changelog for version 0.5.1
---------------------------

* This is a bugfix update to reduce the size of the |project_name| package.

Changelog for version 0.5.0
---------------------------

* Better documentation. See http://|project_name|.org/contents.html
* Time stamp and other metadata added to generated map PDF.
* Initial support for parameterisation of impact functions.
* Updated logging infrastructure including support for logging to the
  QGIS log panel.
* Fixed missing |project_name| icon in QGIS plugin manager.
* Fixes for help system under windows.
* Multi-page support for generated report PDF (which is now created as a
  separate document).
* Ability to combine polygon hazard  (such as flood prone areas) with
  population density.
* Option to use entire intersection of hazard and exposure instead of clipping
  to the somewhat arbitrary viewport (the training revealed that this was a bit
  confusing)
* Aggregation of raster impact layers by arbitrary polygon layers (such as
  kelurahan boundaries)
* Limited support for runtime configuration of impact functions (e.g. by
  changing thresholds). This is an interim measure while the team is working
  on a GUI to manipulate impact functions more generally.
* More DRR actions added to impact function reports (such as how will warnings
  be disseminated, how will we reach stranded people etc.)
* Volcanic (zonal hazard) impact assessments on building and population
* New function table view that lists all the available impact functions and
  allows them to be filtered by different criteria.
* Lots of small improvements to error reporting, GUI, translations and code
  quality.

Changelog for version 0.4.1
...........................

* This is a minor bugfix release with packaging and documentation related
  changes only so that |project_name| can be deployed via the official QGIS
  repository.
* Added |project_name| tutorial to sphinx documentation

Changelog for version 0.4.0
...........................
* Ability to automatically handle multipart vector data:
  https://github.com/AIFDR/|project_name|/issues/160
* Better error reporting:

 * https://github.com/AIFDR/|project_name|/issues/170
 * https://github.com/AIFDR/|project_name|/issues/161
 * https://github.com/AIFDR/|project_name|/issues/157

* Bug fixing:

 * https://github.com/AIFDR/|project_name|/issues/159
 * https://github.com/AIFDR/|project_name|/issues/156
 * https://github.com/AIFDR/|project_name|/issues/173
 * https://github.com/AIFDR/|project_name|/issues/166
 * https://github.com/AIFDR/|project_name|/issues/162

* |project_name| APIs better defined: https://github.com/AIFDR/|project_name|/issues/134
* Release procedure developed: https://github.com/AIFDR/|project_name|/issues/109
* Added estimate of displaced people to earthquake fatality model:
  https://github.com/AIFDR/|project_name|/commit/04f0e1d
* Achieved 100% translation for Bahasa Indonesia
* Made bundled test and demo data public with associated license information
* Added AusAid and World Bank logos to dock
* Fixed bug with flood population evacuation reporting units



Changelog for version 0.3.0
...........................
* Documentation updates - extended guides for using the |project_name| dock and
  keyword editors.
* Support for remote layers in keywords editor and scenario modelling
* Added options dialog
* Support for using all layers in hazard and exposure combos, not just visible
  ones (configurable in options dialog)
* Support for displaying keywords title in QGIS layer list (configurable in
  options dialog)
* When selecting a hazard or exposure layer, its keywords are now displayed
  in the results area.
* Performance improvements when toggling layer visibility and adding and
  removing layers.
* Support for QGIS 1.8 when it is released
* Numerous other 'under the hood' bug fixes and improvements
* Migrated code base from RIAB to |project_name| and restructured the code base
* Added additional tests

Changelog for version 0.2.1:
............................
* Correct translation of 'run' in indonesian. Closes #128
* Updated so that version number is shown in dock
* Removed generated file from polygon test
* Removed the -dev designation from branch releases
* Fix indent error causing noise to show in qgis plugin manager
* Fixed typo - BNPD to |BNPB|
* Fixed bug where close button does not dispose of the help dialog
* Fixed an issue that prevented the use of earthquake functions when using
  keywords with lowercase mmi. Closes #142
* Fix for mac clipping issues - the plugin should work on OSX now. Closes #141.
  Note that OSX users should upgrade to GDAL 1.9 available here:
  http://www.kyngchaos.com/software/qgis

Changelog for version 0.2.1:
............................

* Map printing support
* Improved translation support and Indonesian translation updates
* Rebranded from Risk in a Box to |project_name|
* Documentation updates and documented windows developer procedures
* Support for generating documentation and running tests under Windows
* Scripts for semi-automatic packaging of a release
* Improvements to Impact calculator algorithms

Changelog for version 0.1.0:
............................

* First QGIS plugin implementation of |project_name|.
* Migrated calculation engine from Risiko project.
* Implemented support for polygon hazard layers.
* Added dock widget for designing and executing a scenario model.
* Added the keyword editor for assigning metadata to input files.
* Added integrated context help tool.
* Removed django specific dependencies from the |project_name| libs.
* removed dependency on SciPy
* Support for internationalisation.
* Comprehensive documentation system.
