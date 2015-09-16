[![][InaSAFEImage]][website]

[![Build Status](http://jenkins.inasafe.org/buildStatus/icon?job=InaSAFE-Website-Test-develop)](http://jenkins.inasafe.org/job/InaSAFE-Website-Test-develop/)

InaSAFE Documentation
=====================

PDF versions of the Documentation are available here: http://inasafe.org/pdf/

Tools you need to install, if you want to work on the documentation
-------------------------------------------------------------------

If you plan to update or translate the manual locally, you will need to 'build'
the docs like we do on the servers. You build it using 'Sphinx', and 
there are two options:

- building using a Docker image on your machine (easiest, on Linux and Windows)
- have al the tools on your local machine (Linux only)

You always start with having or creating a github account

Docker build on your machine
============================

First: install Docker. 

On Linux: use your package-manager.

On Windows: install boot2docker from: http://boot2docker.io/
Some notes: you need admin rights to do this: the install script will generate some keys, just accept all defaults.
If it does not work the first time, check if you need to 'enable virtualisation' in your BIOS (eg Lenovo disables it  by default).

Start a command box (on Windows: double click the boot2docker icon on desktop, you will get a terminal):

Verify that Docker/Boot2docker is working by typing:

    docker run hello-world
  
If all goes ok, it will download a small Docker image and you will have output like this:

    richard@kwik~$ docker run hello-world
    Unable to find image 'hello-world:latest' locally
    latest: Pulling from hello-world
    ....
    Hello from Docker.
    This message shows that your installation appears to be working correctly.

Now we are going to create a working directory and pull the Inasafe-doc sources from github:

    # cd to your home dir
    cd
    # create a dev dir and move into it
    mkdir dev
    cd dev
    # clone/copy the sources into it and go into the dir
    git clone https://github.com/AIFDR/inasafe-doc
    cd inasafe-doc
    # check your current path
    pwd
    # ^^^ that shows your current path, with me on Linux it is:
    /home/richard/dev/qgis/git/inasafe-doc
    # on Win7 and Win8 I had:
    /c/Users/richard/dev/inasafe-doc
 
We are now going to use that inasafe-doc directory as source and output directory for the 
Docker 'virtual machine' that will build the docs.
We will start this Docker container with a command line like below:

    docker run -t -i -v /home/richard/dev/qgis/git/inasafe-doc:/inasafe-doc -w=/inasafe-doc --rm=true qgis/sphinx_html ./scripts/post_translate.sh en
 
Where "docker run -t -i qgis/sphinx_html ./scripts/post_translate.sh en" means: "run a Docker container/proces based on the qgis/sphinx_html image available online, call the scripts/post_translate.sh in the working directory of the container, with parameter 'en', meaning: only build english"

"-v /home/richard/dev/qgis/git/inasafe-doc:/inasafe-doc" means: use the directory "/home/richard/dev/qgis/git/inasafe-doc" as a virtual directory in the container and name it '/inasafe-doc'
  
"-w=/inasafe-doc" means that it is to be used as thee working dir of Docker

"--rm=true" means remove the container after the build

Now the actual command lines:

On linux (use your own inasafe-doc path here!):

    # only html
    docker run -t -i -v /home/richard/dev/qgis/git/inasafe-doc:/inasafe-doc -w=/inasafe-doc --rm=true qgis/sphinx_html ./scripts/post_translate.sh en
    # pdf plus html
    docker run -t -i -v /home/richard/dev/qgis/git/inasafe-doc:/inasafe-doc -w=/inasafe-doc --rm=true qgis/sphinx_pdf ./scripts/post_translate.sh en

On windows (tested on Win7 and Win8), use your own inasafe-doc path here!

IMPORTANT you need 2x a double // in the command !!!   Without it you will get an error message about a wrong working directory:

    docker run -t -i -v //c/Users/richard/dev/inasafe-doc:/inasafe-doc -w=//inasafe-doc --rm=true qgis/sphinx_html ./scripts/post_translate.sh en

Note: only the first time it will pull the qgis/sphinx_html image (>300Mb) from the online repository https://hub.docker.com/u/qgis/

Local build
===========

install the following tools:

* git (from packagemanager) to clone/download the source from Github.com
* gettext (from packagemanager) for translation tools
* texlive (from packagemanager: on Arch, it is texlive-core and texlive-bin)
* texlive-fonts-recommended (Ubuntu: from packagemanager)
* in debian you'll need 'texlive-latex-extra': sudo apt-get install
  texlive-latex-extra (texlive-latexextra on Arch)
* python-pip python installation (via sudo apt-get install python-pip)
* sphinx (via 'sudo pip install sphinx'; on Arch install python-sphinx)
* texi2pdf (from packagemanager: in Ubuntu it is in package 'texinfo')
* dvi2png (from packagemanager: in Ubuntu it is in package 'dvipng')


Working on the english Documentation
====================================

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

You can now edit the rst files in the folder ./docs/source/general/,
e.g.::

* cd /docs/source/general/
* gedit news.rst

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

* git commit /docs/source/general/news.rst -m 'updated news'
* git push

In your github account you can now open a pull request to merge your changes
from your forked to the official Documentation repository.

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

Workflow for adding a new language
----------------------------------

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

[InaSAFEImage]: http://inasafe.org/en/_static/img/logo.png
[website]: http://inasafe.org/
