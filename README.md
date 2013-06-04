[![][InaSAFEImage]][website]

InaSAFE Documentation
=====================

PDF versions of the Documentation are available here: http://inasafe.org/pdf/

Tools you need to install, if you want to work on the documentation
-------------------------------------------------------------------

If you plan to update or translate the manual locally, you will need to create a
github account and install the following tools:

* git (from packagemanager) to clone/download the source from Github.com
* gettext (from packagemanager) for translation tools
* texlive (from packagemanager: on Arch, it is texlive-core and texlive-bin)
* texlive-fonts-recommended (Ubuntu: from packagemanager)
* in debian you'll need 'texlive-latex-extra': sudo apt-get install
  texlive-latex-extra (texlive-latexextra on Arch)
* python-pip python installation (via sudo apt-get install python-pip)
* sphinx (via 'sudo pip install sphinx'; on Arch install python-sphinx)
* texi2pdf (from packagemanager: in Ubuntu it is in package 'texinfo')
* dvi2png (from packagemanager: in Ubuntu it is in package 'dvi2png')


Working on the english QGIS Documentation
=========================================

This section describes how to update/edit the english master documentation.

* get an account on github.com
* install required tools on your computer
* **login to github and create a fork of the [git@github.com:AIFDR/inasafe-doc.git](https://github.com/AIFDR/inasafe-doc)**
* git clone your forked InaSAFE-doc project to your computer
* run './scripts/post_translate.sh en' locally to build the english docs
* edit/update the rst files with the english documentation from ./docs/source/
* run './scripts/post_translate.sh en' locally again to check your changes
* commit your changes to your forked repository
* create a pull request to merge your changes into the official Documentation
  repository

Generation
----------

Git clone your personal forked project::

* git clone git@github.com:/user/inasafe-doc.git

to later update your tree do

* git pull --rebase origin master

Run post_translate.sh script to build the documentation::

* cd inasafe-doc

* sh ./scripts/post_translate.sh en

You can now edit the rst files in the folder ./docs/source/tutorial-docs/,
e.g.::

* cd /docs/source/tutorial-docs/
* gedit tutorial.rst

After editing the rst file, run 'post_translate.sh en' again to build the
english pdf and html files::

*  cd inasafe-doc
*  sh scripts/post_translate.sh en

.. note:: if you want to create docs in another language, use the locale code as
   parameter.

For example, to create indonesian docs::

* cd inasafe-doc
* sh scripts/post_translate.sh id

Now check, if the manual built correctly and commit and push your changes to
your forked repository::

* git commit /docs/source/tutorial-docs/tutorial.rst -m 'updated tutorial'
* git push

In your github account you can now open a pull request to merge your changes
from your forked to the official QGIS Documentation repository.

Translating the english InaSAFE Documentation
=============================================

Every language has it's own maintainer, please contact them,
if you want to help. You find a list of current language maintainers at the
end of this document. If your language is not listed, join our community by
sending a mail to <inasafe-users+subscribe@googlegroups.com> and ask for
help.

HowTo for language maintainers
------------------------------

* get an account on github.com
* install required tools on your computer
* login to github and create a fork of the inasafe-doc repository that other
  translators can work with.

Translators now can create their own fork from the forked repository of the
maintainer, commit their translations to their own forked repository and send
pull request to the language maintainer's repository. Once the maintainer
receives a pull request, he should check the changes, accept the pull request
and merge the changes with the official inasafe-doc repository.

If the maintainer needs to add a new language workflow
------------------------------------------------------

* add your locale code in the pre_translate.sh script in the line with 'LOCALE='
* run 'scripts/pre_translate.sh'. There will be a new directory in the i18n
  directory for your language, containing the po-files for all source files
* create an empty(!) directory in the resources directory for your language. The
  idea is to ONLY put images in exact the same directory structure if you
  want an image to be 'translated'. As default the english one will be used
  from the 'en' directory, and only if there is an translated one it will be
  found and used.
* add your locale code in the post_translate.sh script in the line with
  'LOCALE='

HowTo for translators
---------------------

* get an account on github.com
* install required tools on your computer
* login to github and create a fork of the inasafe-doc repository from your
  language maintainer.
* git clone your forked inasafe-doc repository to your computer
* run './scripts/pre_translate.sh &lt;language&gt;' locally to build the
  translation files
* translate the .po files locally and use an offline editor.
  [QtLinguist](https://code.google.com/p/qtlinguistdownload/)
  being the highly recommended choice.
* with the english documentation from ./docs/source/ run '
  ./scripts/post_translate.sh languagecode' locally again to check your
  translation
* files translated need to be "synchronized" with the ones in the directory of
  the forked repo. Commit your changes to your private forked repository and
  create a pull request on github. It means that you send a request to the
  owners of the repository you forked (language maintainer) asking him to
  accept your translations and move them to the "original repository". For
  doing that go on github.com, browse on the directory of your repository and
  click pull request (https://help.github.com/articles/using-pull-requests).
* your language maintainer will take care that every significant translation go
  into the master repository.
* Generally, as soon as you finish editing one or more .po files, you should
  commit as soon as possible the edits to the git repository,
  in order to minimize the possibility of conflicts.

The maintainer and translator should update and check the translations
regularly. Therefore you should 'git pull' when you start to work and run the
'scripts/pre_translate.sh &lt;language&gt;' and 'scripts/post_translate.sh
&lt;language&gt;' script after every significant change in the documentation.
This will generate and update the .po files needed for translations. If all
is fine, take care, that the translation go into the repository of your
language maintainer.

[InaSAFEImage]: http://inasafe.org/_static/icon.png
[website]: http://inasafe.org/
