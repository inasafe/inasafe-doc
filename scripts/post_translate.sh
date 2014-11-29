#!/bin/bash
# Next line is a trick to get absolute path from relative path
# http://stackoverflow.com/questions/4045253/converting-relative-path-into-absolute-path
if [ "$USER" == "jenkins" ]
then
    # Next line is a trick to get absolute path from relative path
    # http://stackoverflow.com/questions/4045253/converting-relative-path-into-absolute-path
    INASAFE_DEV_PATH=`cd "../../inasafe-qgis2/workspace"; pwd`
else
    INASAFE_DEV_PATH=`cd "../inasafe-dev"; pwd`
fi
export QGIS_PREFIX_PATH=/usr/local/qgis-2.6

if [ -d $INASAFE_DEV_PATH ]
then
  echo 'Using InaSAFE-dev in' $INASAFE_DEV_PATH
else
    # check the repo out since it does not exist
    pushd .
    mkdir -p $INASAFE_DEV_PATH
    cd $INASAFE_DEV_PATH
    git clone --depth 1 git://github.com/AIFDR/inasafe.git inasafe-dev
    popd
fi

export LD_LIBRARY_PATH=$QGIS_PREFIX_PATH/lib
export PYTHONPATH=$QGIS_PREFIX_PATH/share/qgis/python:$INASAFE_DEV_PATH:$QGIS_PREFIX_PATH/share/qgis/python/plugins:$PYTHONPATH
export QGIS_DEBUG=0
export QGIS_LOG_FILE=/dev/null
export QGIS_DEBUG_FILE=/dev/null

echo "LIBRARY_PATH="$LD_LIBRARY_PATH
echo "PYTHONPATH="$PYTHONPATH

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

# GENERATE PDF AND HTML FOR FOLLOWING LOCALES (EN IS ALWAYS GENERATED)
LOCALES='id fr'

if [ $1 ]; then
  LOCALES=$1
fi

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

if [[ $1 = "en" ]]; then
  echo "Not running localization for English."
else
  for LOCALE in ${LOCALES}
  do
    for POFILE in `find i18n/${LOCALE}/LC_MESSAGES/ -type f -name '*.po'`
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

for LOCALE in ${LOCALES}
# Compile the html docs for this locale
do
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
  cp templates/index-${LOCALE}.html templates/index.html
  cp templates/irchat-${LOCALE}.html templates/irchat.html

  echo "Building HTML for locale '${LOCALE}'..."
  LOG=/tmp/sphinx$$.log
  ${SPHINXBUILD} -d ${BUILDDIR}/doctrees -D language=${LOCALE} -b html source ${HTMLDIR}/${LOCALE} > $LOG
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
  rpl -q '#/../search.html' 'search.html' ./output/html/${LOCALE}/contents.html
  # same applies for having the IRC-Chat Navigation Link
  rpl -q '#/../irchat.html' 'irchat.html' ./output/html/${LOCALE}/contents.html

  #################################
  #
  #         PDF Generation
  #
  #################################
  # experimental sphinxbuild using rst2pdf...
  #${SPHINXBUILD} -d ${BUILDDIR}/doctrees -D language=${LOCALE} -b pdf source ${BUILDDIR}/latex/${LOCALE}

  # Traditional using texi2pdf....
  # Compile the latex docs for that locale
  ${SPHINXBUILD} -d ${BUILDDIR}/doctrees -D language=${LOCALE} -b latex source ${BUILDDIR}/latex/${LOCALE}  > /dev/null 2>&1
  # Compile the pdf docs for that locale
  # we use texi2pdf since latexpdf target is not available via
  # sphinx-build which we need to use since we need to pass language flag
  pushd .
  cp resources/InaSAFE_footer.png ${BUILDDIR}/latex/${LOCALE}/
  cd ${BUILDDIR}/latex/${LOCALE}/
  # Manipulate our latex a little - first add a standard footer

  FOOTER1="\usepackage{wallpaper}"
  FOOTER2="\LRCornerWallPaper{1}{InaSAFE_footer.png}"

  # need to build 3x to have proper toc and index
  if [ -z $TEXI2PDF ]
    then
      echo You do not have texinfo package installed. Please install!
      exit 1
  fi

  texi2pdf --quiet InaSAFE-Documentation.tex > /dev/null 2>&1
  texi2pdf --quiet InaSAFE-Documentation.tex > /dev/null 2>&1
  texi2pdf --quiet InaSAFE-Documentation.tex > /dev/null 2>&1
  mv InaSAFE-Documentation.pdf ${PDFDIR}/InaSAFE-${VERSION}-Documentation-${LOCALE}.pdf
  popd
done

rm -rf source/static
rm -rf ${BUILDDIR}

popd
