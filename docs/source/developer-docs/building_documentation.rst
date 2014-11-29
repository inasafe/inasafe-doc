.. _building_documentation:

Building the Documentation
==========================

Building the documentation means that you must have inasafe-doc AND inasafe
(-dev) cloned to your local computer because inasafe-doc takes some API
Information out of inasafe-dev to produce the API Documentation.

To do that you only have to enter this on the command line of a terminal::

  mkdir -p $HOME/dev/python
  cd $HOME/dev/python
  git clone https://github.com/AIFDR/inasafe.git inasafe-dev
  https://github.com/AIFDR/inasafe-doc.git inasafe-doc

You have to follow this directory structure because some scripts building the
documentation assume to have the source code available in this structure.

Now that you have the source code available we need to make sure to have all
packages that are needed to build the documentation.

All of the Documentation is written in reStructuredText (.rst) files.
You can find an overview about rst at their webpage:
http://docutils.sourceforge.net/rst.html

Obviously you have to install docutils and as we heavily rely on
`Sphinx <http://sphinx-doc.org/>`_ for compiling our Documentation you will
also need Sphinx.

By the time of writing the minimum version numbers that you have to use are:

* docutils: docutils (0.10)
* Sphinx: Sphinx (1.2b1)

updated versions of docutils and Sphinx can be easily installed with `pip
<https://pypi.python.org/pypi/pip>`_ by doing:

:command:`pip install --upgrade docutils`
and
:command:`pip install --upgrade Sphinx`

at the command line.

pip itself should be available as a package in linux (depending on the
distribution you use).

There are several other files that will help you to update and build the
documentation.
They are all located in the :file:`scripts` directory.
::

  pre_translate.sh will create and prepare the translations
  create-transifex-resources.sh to create translation files for other
     languages out of the source files

A closer look in how to use this tools can be read in the next chapter.

Building documentation locally
..............................

To be up to date with transifex and local translations and to be able to look
at your newly created Documentation locally on your filesystem with a browser
you should basically follow this workflow:

Inside the inasafe-doc directory do::

  tx pull           (for pulling new translations)
                    to update the local translations with that from transifex
  git commit        to commit your local changes into your local branch
  git push          (not necessary to push it up to the repository esp. if
                     you do not have write access to master)
  ./scripts/post-translate.sh (actually creates the documentation in the
                              output folder under docs where you should than
                              find a html and a pdf folder.

Updating the webpage
--------------------

As the webpage is also written in ReSTructured text and managed within github
the deployment of the webpage requires the following steps:

* Update the documentation as needed
* Commit/push to master/your master
* Optionally do a pull request
* If the pull request is accepted or you are able to push directly to the
  repository the documentation webpage should be updated within 20min

After this the changes should be visible here http://inasafe.org.
