.. _minimum_needs:

Minimum Needs Tool
==================

The purpose of the minimum needs tool is to provide a quick method of
calculating support requirements (in terms of food, water etc.) for displaced
persons.

The minimum needs are based on 'Perka 7/2008' according to the following
default formulas:

* 400g rice per person per day (2.8kg per week).
* 2.5l drinking water per person per day (17.5l per week).
* 15l clean water per person per day (105l per week).
* 1 family kit per family per week (assumes 5 people per family which is
  not specified in perka).
* 20 people per toilet.

.. note:: In the current version of InaSAFE, these guidelines cannot be
    adjusted by the user. In a future version we will provide this facility.

In order to use this tool, you need to first load a polygon layer in QGIS that
contains areas (e.g. administrative areas) with an attribute that represents
the number of displaced people in each area.

When the layer is loaded, click on the :guilabel:`Minimum Needs` tool in the
toolbar:

.. figure:: /static/user-docs/minimum_needs_tool.*
   :scale: 75 %
   :alt: Minimum Needs Tool
   :align: center

   Minimum Needs Tool

In the dialog that appears, choose the QGIS layer that contains the
administrative boundaries and then select the attribute in that layer that
represents the number of displaced people.

When you are ready, press the :guilabel:`OK` button on the dialog.

After the analysis is completed, new keywords will be associated with the
layer that indicate the needs according to the formulas defined above.
