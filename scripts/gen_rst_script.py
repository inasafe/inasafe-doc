#!/usr/bin/env python
"""**Generating rst file for documentation**

"""

__author__ = 'Ismail Sunni <ismailsunni@yahoo.co.id>'
__revision__ = '$Format:%H$'
__date__ = '16/08/2012'
__license__ = 'GPL'
__copyright__ = 'Copyright 2012, Australia Indonesia Facility for '
__copyright__ += 'Disaster Reduction'

import os
from shutil import rmtree
import string
import sys

# Text
index_header = 'InaSAFE API documentation\n'
index_header += '===========================\n\n'
index_header += 'This is the API documentation for the InaSAFE project.\n'
index_header += 'You can find out more about the InaSAFE project by visiting\n'
index_header += '`inasafe.org <http://www.inasafe.org/>`_.\n\n'


def create_top_level_index_entry(title, max_depth, subtitles):
    """Function for creating a text entry in index.rst for its content.
        title : Title for the content
        max_depth : max depth
        subtitles : list of subtitles that is available.
    """

    return_text = title + '\n'
    dash = '-' * len(title) + '\n'

    return_text += dash + '\n'
    return_text += '.. toctree::' + '\n'
    return_text += '   :maxdepth: ' + str(max_depth) + '\n\n'

    for subtitle in subtitles:
        return_text += '   ' + subtitle + '\n\n'
    return return_text


def create_package_level_rst_index_file(
        package_name, max_depth, modules, inner_packages=None):
    """Function for creating text for index for a package.
        package_name : name of the package
        max_depth : maxdepth
        modules : list of module in the package.
    """

    excluded_packages = ['i18n', 'test', 'converter_data']
    excluded_modules = ['converter_data']
    if inner_packages is None:
        inner_packages = []
    return_text = 'Package::' + package_name
    dash = '=' * len(return_text)
    return_text += '\n' + dash + '\n\n'
    return_text += '.. toctree::' + '\n'
    return_text += '   :maxdepth: ' + str(max_depth) + '\n\n'
    upper_package = package_name.split('.')[-1]
    for module in modules:
        if module in excluded_modules:
            continue
        return_text += '   ' + upper_package + os.sep + module[:-3] + '\n'
    for inner_package in inner_packages:
        if inner_package in excluded_packages:
            continue
        return_text += '   ' + upper_package + os.sep + inner_package + '\n'

    return return_text


def create_module_rst_file(module_name):
    """Function for creating text in each .rst file for each module.
        module_name : name of the module.
    """

    return_text = 'Module:  ' + module_name[:-3]
    dash = '=' * len(return_text)
    return_text += '\n' + dash + '\n\n'
    return_text += '.. automodule:: ' + module_name[:-3] + '\n\n'
    return_text += '      :members:\n\n'
    return_text += 'This module forms part of the `InaSAFE '
    return_text += '<http://inasafe.org>`_ tool.'

    return return_text


def create_dirs(path):
    """Shorter function for creating directory(s).
    """

    if not os.path.exists(path):
        os.makedirs(path)


def write_rst_file(path_file, file_name, content):
    """Shorter procedure for creating rst file
    """

    create_dirs(os.path.split(os.path.join(path_file, file_name))[0])
    try:
        fl = open(os.path.join(path_file, file_name + '.rst'), 'w+')
        fl.write(content)
        fl.close()

    except Exception, e:
        print 'Creating ', os.path.join(path_file, file_name + '.rst'), \
              ' failed: ', e


def get_python_files_from_list(files, excluded_files=None):
    """Return list of python file from files, without excluded files.
    """

    if excluded_files is None:
        excluded_files = ['__init__.py']
    python_files = []
    for fl in files:
        if fl.endswith('.py') and not fl in excluded_files:
            python_files.append(fl)

    return python_files


def create_top_level_index(inasafe_docs_path, max_depth=2):
    #assemble a list of python files in the safe_qgis Package

    # Write top level index file entries for safe_qgis, safe and Unit Tests
    safe_qgis_text = create_top_level_index_entry(
        title='Package safe_qgis',
        max_depth=max_depth,
        subtitles=['safe_qgis'])
    safe_qgis_tests_text = create_top_level_index_entry(
        title='Unit Tests',
        max_depth=max_depth,
        subtitles=['safe_qgis_tests'])
    safe_package_text = create_top_level_index_entry(
        title='Packages safe',
        max_depth=max_depth,
        subtitles=['safe'])
    index_content = ('%s\n%s\n%s\n%s\n' % (
        index_header, safe_qgis_text, safe_package_text, safe_qgis_tests_text))
    write_rst_file(
        inasafe_docs_path, 'index',
        index_content)


def get_safe_qgis_files(inasafe_code_path):
    safe_qgis_package_path = os.path.join(inasafe_code_path, 'safe_qgis')
    safe_qgis_file_list = os.listdir(safe_qgis_package_path)
    python_module_files = []
    python_test_files = []
    python_files = get_python_files_from_list(safe_qgis_file_list)
    for python_file in python_files:
        if python_file.startswith('test'):
            python_test_files.append(python_file)
        else:
            python_module_files.append(python_file)
    return python_module_files, python_test_files


def get_inasafe_code_path():
    # determine the path to inasafe code using default or argv as needed
    inasafe_code_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', '..', 'inasafe-dev'))
    if len(sys.argv) > 2:
        sys.exit(
            'Usage:\n%s [optional path to inasafe directory]\n'
            % (sys.argv[0]))
    elif len(sys.argv) == 2:
        print('Building rst files from %s' % sys.argv[1])
        inasafe_code_path = os.path.abspath(sys.argv[1])

    return inasafe_code_path


def clean_api_docs_dirs():
    # remove old api-docs if it exists and recreate it
    inasafe_docs_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), '..', 'docs', 'source', 'api-docs'))
    if os.path.exists(inasafe_docs_path):
        rmtree(inasafe_docs_path)
    create_dirs(inasafe_docs_path)
    return inasafe_docs_path


################################################################################


def create_api_docs(dir_path, doc_path, max_depth=2):
    """Function for generating .rst file for all .py file in dir_path folder.
        dir_path : path of the folder
    """

    dir_path_head = os.path.split(dir_path)[0]
    len_dir_path = len(dir_path_head) + 1
    doc_path = os.path.abspath(doc_path)
    for path, dirs, files in os.walk(dir_path):
        # Checking __init__.py file
        if '__init__.py' not in files:
            continue
        # Creating directory for the package

        new_dir = os.path.join(doc_path, path[len_dir_path:])
        create_dirs(new_dir)

        # Create index_file for the directory
        python_files = get_python_files_from_list(files)
        package = string.replace(path[len_dir_path:], os.sep, '.')
        index_file_text = create_package_level_rst_index_file(
            package, max_depth, python_files, dirs)
        write_rst_file(
            path_file=doc_path,
            file_name=package,
            content=index_file_text)

        # Creating .rst file for each .py file
        for py_file in python_files:
            py_module_text = \
                create_module_rst_file(string.replace(
                    path[len_dir_path:] + '.' + py_file, os.sep, '.'))
            write_rst_file(
                path_file=new_dir,
                file_name=py_file[:-3],
                content=py_module_text)


def create_safe_qgis_api_docs(inasafe_code_path, inasafe_docs_path, max_depth):

    python_module_files, python_test_files = get_safe_qgis_files(
        inasafe_code_path)
    safe_qgis_text = create_package_level_rst_index_file(
        package_name='safe_qgis',
        max_depth=max_depth,
        modules=python_module_files)
    write_rst_file(inasafe_docs_path, 'safe_qgis', safe_qgis_text)
    # Creating safe_qgis_tests.rst file
    safe_qgis_test_text = create_package_level_rst_index_file(
        package_name='safe_qgis_tests',
        max_depth=max_depth,
        modules=python_test_files)
    write_rst_file(inasafe_docs_path, 'safe_qgis_tests', safe_qgis_test_text)

    # Creating safe_qgis module docs
    docs_safe_qgis_path = os.path.join(inasafe_docs_path, 'safe_qgis')
    create_dirs(docs_safe_qgis_path)
    for module in python_module_files:
        safe_qgis_text = create_module_rst_file('safe_qgis.' + module)
        write_rst_file(docs_safe_qgis_path, module[:-3], safe_qgis_text)

    # Creating safe_qgis_test module docs
    docs_safe_qgis_tests_path = os.path.join(inasafe_docs_path,
                                             'safe_qgis_tests')
    create_dirs(docs_safe_qgis_tests_path)
    for module in python_test_files:
        safe_qgis_text = create_module_rst_file('safe_qgis.' + module)
        write_rst_file(docs_safe_qgis_tests_path, module[:-3], safe_qgis_text)


def main():

    inasafe_code_path = get_inasafe_code_path()
    inasafe_docs_path = clean_api_docs_dirs()
    max_depth = 2
    create_top_level_index(inasafe_docs_path, max_depth)
    create_safe_qgis_api_docs(inasafe_code_path, inasafe_docs_path, max_depth)
    # For general packages and modules in safe package
    create_api_docs(
        dir_path=os.path.join(inasafe_code_path, 'safe'),
        doc_path=inasafe_docs_path,
        max_depth=max_depth)


if __name__ == '__main__':
    main()
