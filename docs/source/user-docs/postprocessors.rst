.. _post_processor:

Post-processors
================

This document explains the purpose of post-processors and lists the
different available post-processors and the requirements each has to be
used effectively.

What is a post-processor?
-------------------------

A postprocessor is a function that takes the results from the impact function
and calculates derivative indicators, for example if you have an affected
population total, the **Gender** post-processor will calculate gender specific
indicators such as additional nutritional requirements for pregnant women

Selecting a post-processor
--------------------------

Post-processors and their settings can be edited in the user configurable
function parameters dialog. See :ref:`analysis_parameters` to find the
correct buttons.

To disable a post-processor simply go to the :guilabel:`Postprocessors` tab
and enable or disable any post-processor you like by clicking on the checkbox
next to it. You can even set the postprocessing values you like here by
entering the values in the fields.

The same is valid for any other setting you might encounter there.
If you don't see a post-processors field, it means that the impact function
you are trying to use does not support any post processor

.. figure:: /static/user-docs/postprocessor-config.*
   :scale: 75 %
   :alt: Post-processor configuration
   :align: center

   Post-processor configuration

Each activated post-processor will create an additional report in the dock and
in the printout. If problems arise while post processing, the system will
inform you and will skip post-processing.

Creating post-processors
------------------------

If you feel there is an important post-processor which is missing,
there are two avenues you can follow:

* You can develop it yourself or with the aid of a programmer who has a good
  understanding of the python programming language.
* You can file a ticket on our `issue tracking system
  <https://github.com/AIFDR/inasafe/issues>`_, and if time and resources allow
  we will implement it for you.
