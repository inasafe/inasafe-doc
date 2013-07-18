#!/usr/bin/env python
"""**Generating impact function documentation**

"""

__author__ = 'Ismail Sunni <ismailsunni@yahoo.co.id>'
__version__ = '1.0.0'
__revision__ = '$Format:%H$'
__date__ = '17/09/2012'
__license__ = "GPL"
__copyright__ = 'Copyright 2012, Australia Indonesia Facility for '
__copyright__ += 'Disaster Reduction'

import os
from shutil import rmtree
from safe.api import (
    get_metadata,
    get_plugins,
    is_function_enabled,
    get_doc_string)
from gen_rst_script import (create_dirs, write_rst_file, get_inasafe_code_path)
from third_party.odict import OrderedDict

doc_dir = os.path.join('docs', 'source', 'user-docs')
impact_func_doc_dir = 'impact_function_docs'


def pretty_key(key):
    """Pretty key for documentation - removes underscore and capitalize.

    :param key: Key to format.
    :type key: str

    :returns: A nicely formatted string.
    :rtype: str
    """
    pretty_key = key.replace('_', ' ').title()
    return pretty_key


def gen_rst_doc(metadata, doc_strings):
    """Generates an .rst file for an impact function.

    The .rst file will contain the docstring and the standard metadata fields
    for the impact function.

    :param metadata: Key value pairs containing function documentation.
    :type metadata: dict

    :param doc_strings: Key Value Pair where the key is an impact function
        name and the value is the docstring for that impact function.
    :type doc_strings: dict
    """
    impact_func_doc_path = os.path.join(
        get_inasafe_code_path(), doc_dir, impact_func_doc_dir)

    for name, docstring in metadata.items():
        content_rst = name
        content_rst += '\n' + '=' * len(name) + '\n\n'
        # provide documentation
        content_rst += 'Overview'
        content_rst += '\n' + '-' * len('Overview') + '\n\n'
        if type(docstring) is dict or type(docstring) is OrderedDict:
            for mykey, myValue in docstring.items():
                if mykey == 'detailed_description':
                    continue
                my_pretty_key = pretty_key(mykey)
                content_rst += '**' + my_pretty_key + '**' + ': \n'
                if myValue is None or len(myValue) == 0:
                    content_rst += 'No documentation found'
                else:
                    content_rst += myValue
                content_rst += '\n\n'
            content_rst += 'Details'
            content_rst += '\n' + '-' * len('Details') + '\n\n'
            if ('detailed_description' in docstring.keys()) and \
                    (len(docstring['detailed_description']) > 0):
                content_rst += docstring['detailed_description']
            else:
                content_rst += 'No documentation found'
        else:
            content_rst += 'No documentation found'
        if name in doc_strings:
            my_doc_str = doc_strings[name]
            content_rst += '\n\nDocstring'
            content_rst += '\n' + '-' * len('Doc String') + '\n\n'
            content_rst += my_doc_str

        write_rst_file(
            impact_func_doc_path,
            name.replace(' ', ''),
            content_rst)


def gen_impact_func_index(list_unique_identifier=None):
    """Generate impact function index
    """
    if list_unique_identifier is None:
        list_unique_identifier = []
    content_rst = ''
    title_page = 'Impact Functions Documentation'
    content_rst += '=' * len(title_page) + '\n'
    content_rst += title_page + '\n'
    content_rst += '=' * len(title_page) + '\n\n'

    content_rst += (
        'This document explains the purpose of impact functions and lists the '
        'different available impact function and the requirements each has to '
        'be used effectively.\n\n')

    content_rst += '.. toctree::\n'
    content_rst += '   :maxdepth: 2\n\n'

    # list impact function
    for identifier in list_unique_identifier:
        content_rst += ('   %s%s%s\n' % (
            impact_func_doc_dir, os.sep, identifier.replace(' ', '')))

    write_rst_file(
        os.path.join(get_inasafe_code_path(), doc_dir),
        'impact_functions_doc',
        content_rst)


if __name__ == "__main__":
    # remove old files, in case you disabled or remove impact function
    impact_func_doc_dir_path = (
        os.path.join(get_inasafe_code_path(), doc_dir, impact_func_doc_dir))
    if os.path.exists(impact_func_doc_dir_path):
        rmtree(impact_func_doc_dir_path)

    metadata = {}
    doc_strings = {}
    # Get all impact functions
    plugins_dict = get_plugins()
    for myKey, myFunc in plugins_dict.iteritems():
        if not is_function_enabled(myFunc):
            continue
        metadata[myKey] = get_metadata(myKey)
        doc_strings[myKey] = get_doc_string(myFunc)
    list_unique_identifier = [x['unique_identifier']
                              for x in metadata.values()]
    gen_impact_func_index(list_unique_identifier)

    create_dirs(impact_func_doc_dir_path)
    gen_rst_doc(metadata, doc_strings)
