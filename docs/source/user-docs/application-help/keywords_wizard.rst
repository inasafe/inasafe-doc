.. _keywords_wizard:

Keywords Wizard
===============

This wizard will lead you through the process of defining keywords for an
exposure, hazard or aggregation layer. Unlike the
:ref:`keywords editor <keywords_editor>`, the keywords wizard 'understands'
the constraints and rules that determine which keywords can be applied to any
given layer. For example, if you have a raster layer, the keywords wizard will
use impact function metadata to prevent you declaring that the layer contains
road exposure data since by definition, such data must be vector line data.

Each impact function includes metadata that defines what rules should apply to
data that will be used with that impact function. At startup, the wizard scans
these metadata and uses it to define its rules.

For more general discussion on the keywords system used by InaSAFE, please
see the :ref:`keywords system <keywords_system>` documentation.

Invoking the wizard
-------------------

You can run the wizard by clicking on the icon in the InaSAFE toolbar that
looks like this:

.. figure:: /static/user-docs/keyword-wizard-icon.*
   :scale: 100 %
   :alt: InaSAFE Keywords Wizard Icon
   :align: center

.. note:: You should have at least one layer loaded and active in QGIS before
    attempting to launch the keywords wizard.

Once loaded the wizard will appear:

.. figure:: /static/user-docs/keyword-wizard-exposure.*
   :scale: 75 %
   :alt: InaSAFE Keywords Wizard Icon
   :align: center

.. note:: If the layer already has keywords assigned to it, the wizard will
    default to existing keywords on each step (where applicable).

Cancelling the wizard
---------------------

The wizard can be cancelled at any time by pressing the :guilabel:`Cancel`
button at the bottom of the wizard. No changes will be written to the
keywords file if the wizard is cancelled.


Using the wizard
----------------

To use the wizard, simple follow the prompts presented on each page of the
wizard. There are three standard forms of user input expected in the wizard:

1.) List selection. In this case options are provided in a list. Clicking on
an item will usually display additional helpful text in the information area
of the dialog.


.. figure:: /static/user-docs/wizard_gui_list.*
   :scale: 75 %
   :alt: InaSAFE Keywords Wizard List Selection
   :align: center

2) Field selection. Whilst it appears to look like the list selection above,
in this case the list is automatically generated from the available attributes
of the layer.

.. figure:: /static/user-docs/wizard_field_list.*
   :scale: 75 %
   :alt: InaSAFE Keywords Wizard Attribute List Selection
   :align: center

3) Free form text. In some cases you may be prompted to enter free form text
in order to define some additional metadata.

.. figure:: /static/user-docs/wizard_lineedit.*
   :scale: 75 %
   :alt: InaSAFE Keywords Wizard Free Form Text
   :align: center

4) Drag and drop list. In this context the user should make concept mappings
by dragging items from the left list (represented by unique field values from
the attributes table) onto concepts in the right hand tree. For example below
we see the user mapping all polygons that have their 'floodprone' field value
as 'YES' or 'yes' onto the 'wet' concept in the tree view on the right.


.. figure:: /static/user-docs/wizard_dual_list.*
   :scale: 75 %
   :alt: InaSAFE Keywords Wizard Free Form Text
   :align: center

Completing the wizard
---------------------

On completion of the keywords wizard, a .keywords file will be written to disk
and the keywords for the layer will be displayed in the dock area when that
layer is active in QGIS.

.. figure:: /static/user-docs/wizard_result.*
   :scale: 75 %
   :alt: InaSAFE Keywords Listing
   :align: center


.. note:: **A note on keyword compatibility:** The keywords wizard will
    generate keywords that are note compatible with versions of InaSAFE older
    than 2.1.
