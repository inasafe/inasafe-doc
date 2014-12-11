.. _save_scenario:

Save Scenario
=============

The Save Current Scenario tool allows you to save scenarios
(:ref:`tb_save_scenario`) and batch run them again in the batch runner
tool (:ref:`batch_runner`) in one go:

.. figure:: /static/user-docs/save_scenario.*
   :scale: 75 %
   :alt: Save current scenario
   :align: center

   *Save current scenario*

This is the tool you need to prepare/save scenarios for the
:ref:`tb_batch_runner` Tool. It lets you save the current visible scenario
in QGIS to a :file:`.txt` file. Once saved you can reopen this file as a
scenario again in Batch runner and recalculate it.

A more detailed description of the batch runner is available in
:ref:`batch_runner`.

.. note:: This tool currently does not store the impact function parameters
   you may have set. Consequently all impact functions will run using their
   default options.
