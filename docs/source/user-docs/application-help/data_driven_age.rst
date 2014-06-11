.. _datadriven_age_post_processor:

Data Driven Age Post-processor
==============================

Purpose
-------
Data driven age is used carried out during aggregation to determine how many
people are affected by a hazard according to their age distribution (youth,
adult, elderly). This feature is similar to the gender post-processor.  With
data driven age, a custom age distribution ratio is used. This is specified
either by in the data attributes of the aggregation polygons, or by setting a
global ratio for the whole aggregator vector layer using the keywords editor or
keywords wizard.

This feature is used to specify and to give more information by giving number
of affected youth, adult and elderly in an area for example, the boundaries of
a village. To identify more where area should be priorities during rescue
operations and to give more attention on the vulnerable population (
e.g. elderly) and their needs.

Guidelines
----------

Data Needed
...........

The aggregator vector layer should contain percentage of age distribution
in the attribute table.

+-------+-------+---------+
| YOUTH | ADULT | ELDERLY |
+=======+=======+=========+
| 0.30  | 0.40  | 0.30    |
+-------+-------+---------+
| 0.25  | 0.65  | 0.10    |
+-------+-------+---------+

Category
--------

Ratio attributes or Ratio defaults should be populated up.

+-------------------------------------------------+-----------------+
| Key                                             | Allowed  Values |
+=================================================+=================+
| youth ratio attribute / youth ratio default     | youth           |
+-------------------------------------------------+-----------------+
| adult ratio attribute / adult ratio default     | adult           |
+-------------------------------------------------+-----------------+
| elderly ratio attribute / elderly ratio default | elderly/elder   |
+-------------------------------------------------+-----------------+

.. note: Allowed Values should be in percent value (e.g., 0.30, 0.70).

The keywords editor graphical user interface for Age Postprocessing.

There are two ways to specifying age postprocessing options:

1. Ratio Attributes: In this mode, data used for postprocessing is from the
attributes of the aggregator itself.

.. figure:: /static/user-docs/datadriven_postprocessing_config_by_attribute.*
   :scale: 75 %
   :alt: Age Post-processor configuration from layer attributes
   :align: center

2. Ratio Defaults: In this mode, the default values will be used.

.. figure:: /static/user-docs/datadriven_postprocessing_config_by_default.*
   :scale: 75 %
   :alt: Age Post-processor configuration using default values
   :align: center

A similar user interface is provided in the
:ref:`keywords wizard <keywords_wizard>` user interface.
