.. _toolbar_reports:

Reports
=======

Reports about the impact scenario project are generated using QGIS composer
templates.
The default template is shipped with the plugin,
but you can easily create your own templates in QGIS and use them as a 
basis for your reports.

Localised templates are supported via the following simple schema:

If there is a specified template called
:file:`/path/to/template/foo.qpt` then the plugin looks in the template
directory :file:`/path/to/template/` for a file called file
:file:`foo-LANG.qpt`, where "LANG" is the language code of the system locale.

If such a file exists it will be used for report creation,
otherwise the original template
:file:`/path/to/template/foo.qpt` will be used.

Report template elements
------------------------

A template contains the following types of elements:

* **Static elements**
* **Elements containing tokens for replacement**
* **Elements that are directly updated by the renderer**

Static Elements
...............

These are elements which are not changed during report generation, e.g. some
logos/images, additional texts, etc.
You can safely remove such elements or replace them with your own as needed.

Elements containing tokens for replacement
..........................................

In this case the element name is not significant, only the token(s) it
contains.
At render time any of the tokens in these elements will be replaced with
translated content (if an alternative locale is in effect) from the plugin
according to the keywords listed below in this document.

Elements that are directly updated by the renderer
..................................................

In this case any content that may be present in the element is completely
replaced by the realtime map renderer, although certain styling options
(e.g. graticule settings on the map) will remain in effect.

These elements are recognised by their IDs and currently the plugin supports
the following elements:

* **safe-logo** --- QGIS composer image, which is used for displaying the
  |project_name| logo with website url
* **organisation-logo** --- QGIS composer image, which is used for
  displaying organisation logo
  By default a combined supporters logo is used;
  To use a custom logo image, set the path to your PNG file in the plugin Options
  dialog (see :ref:`toolbar_options` for details).
* **impact-map** --- QGIS composer map, which is used for displaying the
  impact scenario
* **impact-legend** --- QGIS composer legend, which is used for displaying
  the legend of the impact scenario
* **impact-report** --- QGIS composer label, which is used for displaying
  the impact report table

  .. note:: As QGIS composer doesn't support automatic resizing of elements
     based on their contents, make sure that labels have dimensions large enough
     to show the full table.

Replaceable keywords
--------------------

This section describes tokenised keywords that are passed to the map template.
To insert any of these keywords into the map template, simply enclose the
key in [] (e.g. [place-name]) and it will be replaced by the text value (e.g.
Tondano).
The list includes static phrases which have been internationalised (and so
they will be displayed in the language of the selected map local,
defaulting to English where no translation is available).

The following tokenised keywords are supported:

* **impact-title** --- title of the impact scenario map
* **date** --- date of the assessment
* **time** --- time of the assessment
* **safe-version** --- version of the plugin used
* **disclaimer** --- disclaimer text;
  By default this text is used: "InaSAFE has been jointly developed by 
  Indonesian Government-BPNB, Australian Govenment-AIFDR and the World
  Bank-GFDRR. These agencies and the individual software developers of 
  InaSAFE take no responsibility for the correctness of outputs from 
  InaSAFE or decisions derived as a consequence."
  To use custom disclaimer text, enter desired text in the Options
  dialog (see :ref:`toolbar_options` for details).

Custom templates
----------------

You have a few options to customise the template **without doing any
programming**.
There are three primary ways you can achieve this:

* Moving replaceable keywords into different elements, or removing them
  completely
* Changing template elements look and feel (e.g. setting up fonts, colors,
  borders, etc.), moving the template elements themselves around or
  adding / removing them completely
* Creating your own template from scratch and using it instead of default one

The default template is provided as
:file:`inasafe/safe_qgis/resources/qgis-composer-templates/inasafe.qpt`
and can be modified by opening the template using the QGIS map composer,
making your changes and then overwriting the template or saving it in any
directory.

You should take care to test your template changes before using it in
a production environment.

In addition to the default template you can have as many custom templates as
you want.
Just create templates, put them in a folder and go
to :menuselection:`Plugins ‣ InaSAFE ‣ InaSAFE Options`
or click on the |project_name| plugin toolbar's :guilabel:`Options` button.
In the Options dialog specify the :guilabel:`Report template` setting.
It should contain the full path to the folder with your custom templates.
