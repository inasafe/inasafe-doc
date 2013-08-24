# -*- coding: utf-8 -*-
#
#################################################

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(os.path.abspath('../..'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = []


# Add any paths that contain templates here, relative to this directory.
templates_path = ['../../templates']


# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toc tree document. Changed by Tim from index to contents so we can
# have our own front page
master_doc = 'index'

# General information about the project.
project = u'InaSAFE Documentation'
copyright = u'2013, InaSAFE project'

version = '1.2'
release = '1.2.0'
exclude_patterns = ['build']
pygments_style = 'sphinx'

rst_prolog = """
.. role:: disclaimer
.. |updatedisclaimer| replace:: :disclaimer:`DISCLAIMER: This section of the documentation needs updating.`
"""

rst_epilog = """
.. |project_name| replace:: InaSAFE
.. |AIFDR| replace:: AIFDR_
.. _AIFDR: http://www.aifdr.org/
.. |BNPB| replace:: BNPB_
.. _BNPB: http://www.bnpb.go.id/
.. |AusAID| replace:: AusAID_
.. _AusAID: http://www.ausaid.gov.au/
.. |GFDRR| replace:: GFDRR_
.. _GFDRR: http://www.gfdrr.org/
"""
html_theme = 'inasafe-theme'
html_theme_path = ['../../../themes_application_docs']
html_short_title = 'InaSAFE Docs'
html_favicon = 'favicon.ico'
html_static_path = ['static']
html_sidebars = {
    'index': ['globaltoc.html'],
    'user-docs/**': ['globaltoc.html'], }

html_additional_pages = {}
html_use_modindex = False
html_use_index = True
# If true, the index is split into individual pages for each letter.
#html_split_index = False
html_show_sourcelink = False
htmlhelp_basename = 'InaSAFEUserGuide'
html_show_sphinx = False
html_show_copyright = False

locale_dirs = ['/tmp/inasafe-user-docs-i18n']
# create 1 po file per rst file instead of one po file per module
gettext_compact = False
