.. _helpful-hints-and-tips:

Helpful Hints And Tips
======================

**Learning Objectives:**

* Customise the |project_name| option menu
* Know where to go for help
* Review frequently asked questions

You have now gone through |project_name| using four different natural hazards,
changing a variety of parameters and analysing the results. This module has
been designed to help you understand a little more about |project_name| as
well as where you can go for help.

|project_name| option menu
--------------------------

A detailed description of the |project_name| Options can be found in the
:ref:`toolbar_options` section of the User Manual.

It is recommended to check (in addition to the defaults) the boxes next to:

    * *When clipping, also clip features (i.e. will clip polygon smaller)*
    * *Help to improve InaSAFE by submitting errors to a remote server*

|project_name| Website
----------------------

This tutorial is not the only documentation on |project_name|. Within
the |project_name| website you can find, not only more training documentation,
but all user and developer documentation. This website is
updated with each new release.

.. image:: /static/training/socialisation/077_website.*
   :align: center

Click on the :guilabel:`Table of Contents` to see all materials.

.. image:: /static/training/socialisation/078_websitedoc.*
   :align: center

Frequently Asked Questions
--------------------------

**Do I need to pay to use** |project_name| ?
No, the software is completely Free and Open Source.

**What licence is** |project_name| **published under?**
|project_name| is published under the GPL version 3 licence,
the full text of which is available at www.gnu.org/licenses/gpl-3.0.txt.
Under the terms of the licence of you may freely copy,
share and modify the software, as long as you make it available under the
same licence.

**How is the project funded?**
The project is being developed for the good of humanity and has been jointly
developed by |BNPB|, |GoA| & the World Bank.

**I found a bug, how should I report it?**
We manage the project issues using a GitHub issue tracker. The |project_name|
issue tracker is open to everyone, though you will first need to register a
(free) account on GitHub to use it. You can find the GitHub self-registration
page https://github.com/signup/free.
Otherwise email inasafe-users@googlegroups.com

**Could we request a new feature?**
If you have a feature request, please use the issue tracker to let us know
about it, using the same procedure as for bug reporting.
Otherwise email inasafe-users@googlegroups.com

**Where do I get Hazard and Exposure data from?**
Some data sources are described in the section on Functionality and Datasets.
You can get open exposure data from  http://www.asiapop.org for population
and from OpenStreetMap, for building structures (however you still may need to
digitise the structures). To download OSM data use the |project_name| 
OSM Download tool as described in :ref:`other-hazards`.
For hazard information it is best to approach your government science
agencies or local universities to model earthquakes,
tsunamis or floods. If it floods regularly in your region you could
also develop a community flood-prone footprint.

**Why does the plugin not show up in my QGIS Plugin Manager?**
One common issue is that if you upgraded from QGIS 2.2.x to 2.8.x you may not
get the new plugin repo added to your repo list. To fix this you can do 
the following:

#. Open :guilabel:`QGIS`.
#. Go to :menuselection:`Plugins -> Fetch Python Plugins`.
#. Click the :guilabel:`Repositories` tab.
#. Click :guilabel:`Add`.
#. Enter next to Name: :kbd:`Official QGIS Repository`.
#. Enter next to Url: :kbd:`http://plugins.qgis.org/plugins/plugins.xml`.
#. Click :guilabel:`Save` and the plugin repo list should update. If it does not,
   close and re-open QGIS to force an update.
#. In the Python Plugin Manager main tab now you should find
   |project_name| available.

