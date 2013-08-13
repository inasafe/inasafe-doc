..
  This is basically a Copy & Paste Section from user-manual/options.rst but
  it should be kept here to have the socialisation short-manual available as
  compact as possible. The Option Section should be kept up to date in the
  User manual and should be copy/pasted after updating it there.

.. _helpful-hints-and-tips:

Helpful Hints And Tips
======================
**Objectives:**

* To read through the |project_name| option menu
* To know where to go for help
* To go through some frequently asked questions

**Expected Results:**

Participants are able to:

* customise the |project_name| option menu
* know where to go for help


You have now gone through |project_name| using 4 different natural hazards,
changing a variety of parameters and analysing the results. This chapter has
been designed to help you understand a little more about |project_name| as
well as where you can go for help.

|project_name| option menu
--------------------------

The detailed description of the |project_name| Options can be found in the
:ref:`toolbar-options` Section of the User Manual.

We encourage you to check (in addition to the default ones):

* When clipping, also clip features (e.g. will clip polygon smaller)
* Help to improve |project_name| by submitting errors to a remote server

|project_name| Website
----------------------

This manual is by no far the only documentation on |project_name|.  Within
the |project_name| website you can find not only documentation on training,
but all user documentation and developer documentation.  This website is also
updated with every new release.

.. image:: /static/socialisation/inasafe_mainpage.*

Click on the :guilabel:`Content` to find out more

.. image:: /static/socialisation/inasafe_content.*

Frequently Asked Questions
--------------------------

**Do I need to pay to use InaSAFE?**
No, the software is completely Free and Open Source.

**What license is InaSAFE published under?**
|project_name| is published under the GPL version 2 license,
the full text of which is available at www.gnu.org/licenses/gpl-2.0.txt.
Under the terms of the license of you may freely copy,
share and modify the software, as long as you make it available under the
same license.

**How is the project funded?**
The project is being developed for the good of humanity and has been jointly
developed by |BNPB|, AusAid & the World Bank.

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
As explained in |project_name| functionality chapter (page 13),
you are able to get open exposure data from  www.asiapop.org for population
and  from OpenStreetMap for structures (however you may need to still
digitise the structures go to www.learnosm.org for more details). To download
OSM data see Appendix :guilabel:`Getting OpenStreetMap Data` (page 56).
For hazard information it is best to approach your government science
agencies or local universities to model earthquake,
tsunami or floods. However if it floods regularly in your region you could
also develop a community flood-prone footprint.

**Why does the plugin not show up in my QGIS Plugin Manager?**
One common issue is that if you upgraded from QGIS 1.7.x to 1.8 you may not
get the new plugin repo added to your repo list. To fix this you can do:

#. open :guilabel:`QGIS`
#. Go :guilabel:`Plugins` -> Fetch Python Plugins
#. click :guilabel:`Repositories` tab
#. click :guilabel:`add`
#. Name: Official QGIS Repository
#. Url: http://plugins.qgis.org/plugins/plugins.xml
#. :guilabel:`Save` it and the plugin repo list should update. If it does not,
   close and open QGIS to force an update.
#. In the :guilabel:`python plugin manager` main tab now you should find
   |project_name| available

Thank you for attending this course.
If you would like to contact me directly my email address is
kristy.vanputten@gmail.com
