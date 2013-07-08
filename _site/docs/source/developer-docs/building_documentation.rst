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

pre_translate.sh
git commit new translation files
scripts/create-transifex-resources.sh
tx pull
post_translate.sh
git commit

Building documentation locally
..............................

To be up to date with transifex and local translations and to be able to look
at your newly created Documentation with a browser locally on your filesystem
you should basically follow this workflow:

Inside the inasafe-doc directory do
::

  tx pull           (for pulling new translations)
  git commit        to update the local translations with that from transifex
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
