.. _batch_runner:

Batch Runner
============

.. figure:: /static/user-docs/batch_runner.*
   :scale: 75 %
   :alt: Batch Runner
   :align: center

   *Batch Runner*

With this tool you can set up numerous scenarios and run them all in one go.
For example, in a typical use case you might define a number of flood impact
scenarios all using a standard dataset, such as :file:`flood.shp`. As new flood 
data becomes available you replace :file:`flood.shp` and rerun the scenarios 
using the batch runner. Using this approach you can quickly produce regional 
contingency plans as your understanding of hazards changes. When you run the 
batch of scenarios, PDF reports are generated automatically and all placed in 
a single common directory making it easy for you to browse and disseminate the 
reports produced.

When the batch process completes, it will produce a summary report like
this::

    InaSAFE Batch Report File
    -----------------------------
    P: gempa bumi Sumatran fault (Mw7.8)
    P: gempa di Yogya tahun 2006
    P: banjir jakarta 2007
    P: Tsunami di Maumere (Mw 8.1)
    P: gempa Mw6.5 Palu-Koro Fault
    P: gunung merapi meletus
    -----------------------------
    Total passed: 6
    Total failed: 0
    Total tasks: 6
    -----------------------------


For advanced users there is also the ability to batch run python scripts using
this tool, but this should be considered an **experimental** feature currently.

Before running the Batch Runner you might want to use the
:ref:`tb_save_scenario` tool to first save some scenarios on which you
can let the batch runner do its work. This tool lets you run saved scenarios
in one go. It lets you select scenarios or run all scenarios in one go.
