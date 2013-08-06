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
user_home = os.environ["HOME"]

import sys
sys.path.append('%s/dev/python/inasafe-dev' % user_home)

from shutil import rmtree
from safe.api import (
    get_metadata,
    get_plugins,
    is_function_enabled,
    get_doc_string)
from create_api_docs import (create_dirs, write_rst_file,
                            get_inasafe_documentation_path)
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


def generate_documentation(metadata, doc_strings):
    """Generates an .rst file for each impact function.

    The .rst file will contain the docstring and the standard metadata fields
    for each impact function.

    :param metadata: Key value pairs containing function documentation.
    :type metadata: dict

    :param doc_strings: Key Value Pair where the key is an impact function
        name and the value is the docstring for that impact function.
    :type doc_strings: dict
    """
    impact_func_doc_path = os.path.join(
        get_inasafe_documentation_path(), doc_dir, impact_func_doc_dir)

    for name, docstring in metadata.items():
        rst_content = name
        rst_content += '\n' + '=' * len(name) + '\n\n'
        # provide documentation
        rst_content += 'Overview'
        rst_content += '\n' + '-' * len('Overview') + '\n\n'

        if type(docstring) is dict or type(docstring) is OrderedDict:
            for my_key, my_value in docstring.items():
                if my_key == 'detailed_description':
                    continue
                my_pretty_key = pretty_key(my_key)
                rst_content += ('**%s**: \n' % my_pretty_key)
                if my_value is None or len(my_value) == 0:
                    rst_content += 'No documentation found'
                else:
                    rst_content += my_value
                rst_content += '\n\n'
            rst_content += 'Details'
            rst_content += '\n' + '-' * len('Details') + '\n\n'
            if ('detailed_description' in docstring.keys()) and \
                    (len(docstring['detailed_description']) > 0):
                rst_content += docstring['detailed_description']
            else:
                rst_content += 'No documentation found'
        else:
            rst_content += 'No documentation found'

        if name in doc_strings:
            my_doc_str = doc_strings[name]
            rst_content += '\n\nDocstring'
            rst_content += '\n' + '-' * len('Doc String') + '\n\n'
            rst_content += my_doc_str

        write_rst_file(
            impact_func_doc_path,
            name.replace(' ', ''),
            rst_content)


def create_index(function_ids=None):
    """Generate impact function index.

    :param function_ids: A collection of function ids that will be listed in
        the index.rst.
    :type function_ids: list
    """
    if function_ids is None:
        function_ids = []
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
    for identifier in function_ids:
        content_rst += ('   %s%s%s\n' % (
            impact_func_doc_dir, os.sep, identifier.replace(' ', '')))

    index_path = os.path.join(get_inasafe_documentation_path(), doc_dir)
    write_rst_file(
        index_path,
        'impact_functions_doc',
        content_rst)


if __name__ == "__main__":
    # remove old files, in case you disabled or remove impact function
    documentation_path = (
        os.path.join(get_inasafe_documentation_path(), doc_dir,
                     impact_func_doc_dir))

    if os.path.exists(documentation_path):
        rmtree(documentation_path)

    metadata = {}
    doc_strings = {}
    # Get all impact functions
    plugins_dict = get_plugins()
    for myKey, myFunc in plugins_dict.iteritems():
        if not is_function_enabled(myFunc):
            continue
        metadata[myKey] = get_metadata(myKey)
        doc_strings[myKey] = get_doc_string(myFunc)
    function_ids = [x['unique_identifier']
                    for x in metadata.values()]
    create_index(function_ids)

    create_dirs(documentation_path)
    generate_documentation(metadata, doc_strings)
