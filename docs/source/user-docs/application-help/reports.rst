.. _toolbar-reports:

Reports
=======

Reports about impact scenario project generated using QGIS composer templates.
Default template shipped with plugin, but you can easily create own templates
in QGIS and use them as basis for reports.

Localized templates supported via next simple schema: if specified template
:file:`/path/to/template/foo.qpt` then plugin look in template directory
:file:`/path/to/template/` for file :file:`foo-LANG.qpt`, where "LANG" is the
language code of the system locale. If such file exists, that it will be used
for report creation, otherwise original template
:file:`/path/to/template/foo.qpt` will be used.

Report Template Elements
------------------------

Template contain next three groups of elements:

* **Static elements**.
* **Elements containing tokens for replacement**.
* **Elements that are directly updated by the renderer**.

Static Elements
...............

These are elements which are not changed during report generation, e.g. some
logos/images, additional texts, etc. You can safely remove such elements or
replace them with your own as needed.

Elements containing tokens for replacement
..........................................

In this case the element name is not significant, only the token(s) it
contains. At render time any of the tokens in these elements will be replaced
with translated (if an alternative locale is in effect) content from the
plugin according to the keywords listed below in this document.

Elements that are directly updated by the renderer
..................................................

In this case any content that may be present in the element is completely
replaced by the realtime map renderer, although certain styling options
(e.g. graticule settings on the map) will remain in effect.

This elements recognized by their ID's and currently plugin supports next
elements:

* **safe-logo** --- QGIS composer image, which will be used for displaying
  organization logo. By default BNPB logo used. To use custom logo image, set
  path to PNG file in plugin Options dialog (see ref:`options` for details).
* **impact-map** --- QGIS composer map, which will be used for displaying the
  impact scenario.
* **impact-legend** --- QGIS composer legend, which will be used for displaying
  legend of the impact scenario.

Replaceable Keywords
--------------------

This section describes tokenised keywords that are passed to the map template.
To insert any of these keywords into the map template, simply enclose the
key in [] (e.g. [place-name]) and it will be replaced by the text value (e.g.
Tondano). The list includes static phrases which have been internationalised
(and so will display in the language of the selected map local, defaulting to
English where no translation if available.

The following tokenized keywords are supported:

* **impact-title** --- title of the impact scenario map.
* **date** --- date of the assesment.
* **time** --- time of the assesment.
* **safe-version** --- version of the plugin used.

Custom templates
----------------

You have a few options to customise the template **without doing any
programming**. There are three primary ways you can achieve this:

* Moving replaceable keywords into different elements, or removing them
  completely.
* Changing template elements look and feel (e.g. setting up fonts, colors,
  borders, etc), moving the template elements themselves around or
  adding / removing them completely.
* Creating your own template from scratch and using it instead of default one.

The template is provided as
:file:`inasafe/safe_qgis/resources/qgis-composer-templates/inasafe.qpt`
and can be modified by opening the template using the QGIS map composer,
making your changes and then overwriting the template or saving it in any
directory. You should take care to test your template changes before using it
in production environment.

To use custom template instead of default one, go to :menuselection:`Plugins
--> InaSAFE --> InaSAFE Options` or click on the |project_name| plugin
toolbar's options icon. In Options dialog specify :guilabel:`Report template`
setting. It should contain full path to your custom template.
