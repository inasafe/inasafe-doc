.. _keywords_editor:

The Keywords Editor
===================

The keywords editor provides a free form user interface for creating keywords.
If you are a new user, you should probably use the
   :ref:`Keywords Wizard <keywords_wizard>` in preference to the keywords
editor as it provides more hand holding and you are less likely to specify
invalid keywords.

For more general discussion on the keywords system used by InaSAFE, please
see the :ref:`keywords system <keywords_system>` documentation.

The keywords editor graphical user interface
--------------------------------------------

The graphical user interface for keyword editing is divided into two parts:

1) **Minimal mode**: In this mode, only following options are provided:

   * **Title** - a 'friendly' name for the dataset which will be displayed in
     reports, the user interface and so on
   * **Source** - a field to inform from whom/where the dataset is obtained.
   * **Category** - A mandatory choice between 'hazard' and 'exposure'.
   * **Subcategory** - An amalgamated subcategory/units picklist
     (in the case of hazard) or amalgamated subcategory/datatype (in the case
     of exposure).
     In this case, the secondary characteristic (units or datatype) are
     shown in square brackets after the subcategory name e.g.
     :samp:`flood [m]` is used for subcategory 'flood', units 'm'.

An example of the keywords editor in minimal mode is shown below.

.. figure:: /static/user-docs/keyword-editor-simple.*
   :scale: 75 %
   :align: center
   :alt: Opened keyword editor window

   Opened keyword editor window

2) **Advanced mode**: In this mode several extra options are provided in
   addition to the minimal mode options.
   Unlike minimal mode, in advanced mode only basic validation is performed
   and the user is given more flexibility to manually define and remove
   key/value pairs.
   Three sections are provided for this:

  * **Predefined** - In this section, the user selects from a constrained list
    of keywords, enters a free-form value and then adds the key/value pair to
    the keywords list (see below).
  * **User defined** - In this section, there is no constraint on the keywords
    entered - any single lower case word will be accepted for both the key and
    the value components.
  * **Current keywords** - In this area a complete list of all the keywords
    for the dataset are displayed.
    The keywords list here is updated when any changes are made in both the
    simple and advanced mode editors.
    It is also possible in this area to manually remove unwanted keywords
    using the 'remove selected' button.
    Multiple keywords can be removed in a single operation by
    :kbd:`Control-clicking` on multiple keyword entries in the current
    keyword list and then clicking :guilabel:`Remove selected`

.. figure:: /static/user-docs/keyword-editor-advanced.*
   :scale: 75 %
   :align: center
   :alt: Advanced mode of keyword editor

   Advanced mode of keyword editor


.. note:: Switching from hazard to exposure will clear parts of the GUI since in
  general most keywords are category dependent.
  In particular, selecting **'hazard'** will remove the **'datatype'**
  key/value pair, and selecting **'exposure'** will remove the **'units'**
  key value pair.

Invoking the keywords editor
----------------------------
The keyword editor can easily be invoked by **selecting any layer** in the
QGIS layers list, and then using the plugin menu to start the editor
(:menuselection:`Plugins --> InaSAFE --> Keyword Editor`).
Alternatively, you may use the keywords editor icon on the plugins toolbar as
illustrated below.

.. figure:: /static/user-docs/keyword-editor-icon.*
   :scale: 100 %
   :align: center
   :alt: Keyword editor icon

   Keyword editor icon

.. note:: If you have not selected a layer in the QGIS legend,
   the keyword editor icon in the toolbar and menus will
   **be disabled** and appear greyed out.

Saving your edits
-----------------

To save your keyword edits, simply press the :guilabel:`OK` button and the
:file:`*.keywords` file will be written to disk.

Cancelling your edits
---------------------

You can cancel your changes at any time by pressing the :guilabel:`Cancel`
button.
No changes will be written to disk and your :file:`*.keywords` file will
remain in its original state.
