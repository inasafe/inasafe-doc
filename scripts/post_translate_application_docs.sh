#!/bin/bash

# Exit on first error
set -e
# Based off the script from QGIS by Tim Sutton and Richard Duivenvoorde

INASAFE_DEV_PATH=$HOME/dev/python/inasafe-dev/

# Name of the dir containing static files
STATIC=_static
# Path to the documentation root relative to script execution dir
DOCROOT=docs/source/user-docs
# Path from execution dir of this script to docs sources
SOURCE=source/user-docs

pushd .
cd $DOCROOT

SPHINXBUILD=`which sphinx-build`

# GENERATE HTML FOR FOLLOWING LOCALES (EN IS ALWAYS GENERATED)
LOCALES='id'

if [ $1 ]; then
  LOCALES=$1
fi

BUILDDIR=`pwd`/../../build-appdocs
# be sure to remove an old build dir
rm -rf ${BUILDDIR}
mkdir -p ${BUILDDIR}

# output dirs
HTMLDIR=`pwd`/../../output-app-docs/html
mkdir -p ${HTMLDIR}

VERSION=`cat conf.py | grep "version = '.*'" | grep -o "[0-9].[0-9]"`

if [[ $1 = "en" ]]; then
  echo "Not running localization for English."
else
  for LOCALE in ${LOCALES}
  do
    for POFILE in `find ../../i18n/${LOCALE}/LC_MESSAGES/user-docs -type f -name '*.po'`
    do
      MOFILE=`echo ${POFILE} | sed -e 's,\.po,\.mo,'`
      # Compile the translated strings
      echo "Compiling messages to ${MOFILE}"
      msgfmt --statistics -o ${MOFILE} ${POFILE}
    done
  done
fi

# We need to flush the build dir or the translations don't come through
rm -rf ${BUILDDIR}
mkdir ${BUILDDIR}
#Add english to the list and generated docs
LOCALES+=' en'

if [ $1 ]; then
  LOCALES=$1
fi

echo "Locales: $LOCALES"

for LOCALE in ${LOCALES}
# Compile the html docs for this locale
do
  # cleanup all images for the other locale
  rm -rf /tmp/source/static
  mkdir -p /tmp/source/static
  # copy english (base) resources to the static dir
  cp -r ../../resources/en/user-docs /tmp/source/static
  # now overwrite possible available (localised) resources over the english ones
  cp -r ../../resources/${LOCALE}/user-docs* /tmp/source/static

  rm -rf /tmp/inasafe-user-docs-i18n
  mkdir -p /tmp/inasafe-user-docs-i18n/${LOCALE}/LC_MESSAGES
  cp -r ../../i18n/${LOCALE}/LC_MESSAGES/user-docs/* \
        /tmp/inasafe-user-docs-i18n/${LOCALE}/LC_MESSAGES

  #################################
  #
  #        HTML Generation
  #
  #################################

  echo "Building HTML for locale '${LOCALE}'..."
  LOG=/tmp/sphinx-app-docs-${LOCALE}-$$.log
  ${SPHINXBUILD} -d ${BUILDDIR}/doctrees -D language=${LOCALE} -b html . ${HTMLDIR}/${LOCALE} > $LOG

  # Some manual cleanups
  rm -rf $HTMLDIR/$LOCALE/_static/img/carousel

done



rm -rf /tmp/source/static
rm -rf ${BUILDDIR}

popd
