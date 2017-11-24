#!/bin/bash

# This script is used to register InaSAFE translatable resources with Transifex
# http://transifex.com
#
# Note that this script updates or creates entries in .tx/config file
#
# Tim Sutton, March 2013

#
# Sphinx documentation first
#

LOCALES=`ls ../docs/i18n`

# We do not translate developer docs as development is mostly done in english
# We do not translate api-docs

for ITEM in user-docs training
do
  for POFILE in `find ../docs/i18n/en/LC_MESSAGES/${ITEM}/ -type f -name '*.po'`
  do
    # get the po file replacing 'en' with '<lang>'
    GENERICFILE=`echo $POFILE | sed 's/\/en\//\/<lang>\//g' | sed 's/\/\//\//g'`
    echo $GENERICFILE
    # Get the filename only part of the po file so we can use that
    # name when registering the resource
    BASE=`basename $GENERICFILE .po`
    BASE=`echo $BASE | sed 's/_/-/g' | sed 's/ /-/g'`
    RESOURCE=inasafe-doc.${ITEM}-$BASE
    
    #
    # Register each po file as a transifex resource (an individual translatable file)
    #
    #set -x
    #--source  this is the source language from which other tranlations are done
    #-t this is a PO file that contains translation strings
    #--auto-local  automatically add to the local .tx/config file
    #GENERICFILE  the pattern to use when matching for other translation files
    #--source-lang  the language of the original source file
    # add it to the config file
    #set -x
    tx set --source \
      -t PO \
      -r $RESOURCE \
      -l en "$GENERICFILE" \
      --source-lang en \
      --auto-local \
      --execute \
      --source-file=$POFILE
    #set +x
    # Now register the language translations for the localised po file against
    # this resource.
    for LOCALE in $LOCALES
    do
       LOCALEFILE=`echo $POFILE | sed "s/\/en\//\/$LOCALE\//g"`
       tx set -r $RESOURCE -l $LOCALE  "$LOCALEFILE"
    done
    # When we are done in this block we should have created a section in the
    # .tx/config file that looks like this:
    #
    #
    #	[inasafe-develop.user-docs-faq]
    #	file_filter = docs/i18n/<lang>/LC_MESSAGES/user-docs/faq.po
    #	source_file = docs/i18n/en/LC_MESSAGES/user-docs/faq.po
    #	source_lang = en
    #	trans.id = docs/i18n/id/LC_MESSAGES/user-docs/faq.po
    #	type = PO
  done
done


#Print out a listing of all registered resources
tx status

# Push all the resources to the tx server
#tx push -s
