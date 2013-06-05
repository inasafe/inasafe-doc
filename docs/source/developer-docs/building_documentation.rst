==========================
Building the Documentation
==========================

Building the documentation means that you must have inasafe-doc AND inasafe
cloned to your local computer because inasafe-doc takes some API Information
out of inasafe-dev to Produce the API Documentation.

To do that you only have to enter this
::

  mkdir -p $HOME/dev/python
  cd $HOME/dev/python
  git clone https://github.com/AIFDR/inasafe.git inasafe-dev
  https://github.com/AIFDR/inasafe-doc.git inasafe-doc

You have to follow this directory structure because some scripts building the
documentation assume to have the source code available under this structure.

Now that you have the source code available we need to make sure to have all
packages that are needed to build the documentation.

UPDATE PACKAGE DEPENDENCIES


Updating the website
--------------------

Deployment of the site requires the following steps:

* Update the documentation as needed
* Commit/push to master/your master
* Optionally do a pull request
* If the pull request is accepted or you are able to push directly to the
  repository the documentation webpage should be updated within 20min

After this the changes should be visible here http://inasafe.org.
