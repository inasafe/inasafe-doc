#!/usr/bin/env bash
# Based off the script from QGIS by Tim Sutton and Richard Duivenvoorde

# Name of the dir containing static files
STATIC=_static
# Path to the documentation root relative to script execution dir
DOCROOT=docs
# Path from execution dir of this script to docs sources (could be just
# '' depending on how your sphinx project is set up).
SOURCE=source

pushd .
cd $DOCROOT

SPHINXBUILD=`which sphinx-build`
TEXI2PDF=`which texi2pdf`
BUILDDIR=build
# be sure to remove an old build dir
rm -rf ${BUILDDIR}
mkdir -p ${BUILDDIR}

# output dirs
PDFDIR=`pwd`/output/pdf
HTMLDIR=`pwd`/output/html
mkdir -p ${PDFDIR}
mkdir -p ${HTMLDIR}

VERSION=`cat source/conf.py | grep "version = '.*'" | grep -o "[0-9]\.[0-9]"`

# We need to flush the build dir or the translations don't come through
rm -rf ${BUILDDIR}
mkdir ${BUILDDIR}

# cleanup all images for the other locale
rm -rf source/static
mkdir -p source/static
# copy english (base) resources to the static dir
cp -r resources/en/* source/static
# now overwrite possible available (localised) resources over the english ones
cp -r resources/${LOCALE}/* source/static

#################################
#
#        HTML Generation
#
#################################
# Now prepare the index/irchat-[locale] template which is a manually translated,
# unique per locale page that gets copied to index.html/irchat.html for the doc
# generation process.
cp templates/index-en.html templates/index.html
cp templates/irchat-en.html templates/irchat.html

echo "Building HTML for locale 'en'..."
LOG=/tmp/sphinx$$.log
#  -n   Run in nit-picky mode. Currently, this generates warnings for all missing references.
#  -W   Turn warnings into errors. This means that the build stops at the first warning and sphinx-build exits with exit status 1.
#${SPHINXBUILD} -nW -d ${BUILDDIR}/doctrees -D language=${LOCALE} -b html source ${HTMLDIR}/${LOCALE} > $LOG
${SPHINXBUILD} -d ${BUILDDIR}/doctrees -D language=en -b html source ${HTMLDIR}/en/ > $LOG
WARNINGS=`cat $LOG | grep warning`
ERRORS=`cat $LOG | grep ERROR`
if [[  $WARNINGS ]]
then
  echo "***********************************************"
  echo "* Sphinx build produces warnings - Please fix *"
  echo $WARNINGS
  echo "***********************************************"
  exit 1
fi
if [[  $ERRORS ]]
then
  echo "*********************************************"
  echo "* Sphinx build produces errors - Please fix *"
  echo $ERRORS
  echo "*********************************************"
  exit 1
fi

# Remove the static html copy again
rm templates/index.html
rm templates/irchat.html

# hack to avoid error when using Search in contents.html
rpl -q '#/../search.html' 'search.html' ./output/html/en/index.html
# same applies for having the IRC-Chat Navigation Link
rpl -q '#/../irchat.html' 'irchat.html' ./output/html/en/index.html


rm -rf source/static
rm -rf ${BUILDDIR}

popd
