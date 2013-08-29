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
# import string
import sys

# Text
INDEX_HEADER = 'API documentation\n'
INDEX_HEADER += '=================\n'
INDEX_HEADER += 'This is the API documentation for the InaSAFE project.\n'
INDEX_HEADER += 'You can find out more about the InaSAFE project by visiting\n'
INDEX_HEADER += '`inasafe.org <http://www.inasafe.org/>`_.\n\n'
EXCLUDED_PACKAGES = ['i18n', 'test', 'converter_data', 'ui', 'resources']


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
        if inner_package in EXCLUDED_PACKAGES:
            continue
        return_text += '   ' + upper_package + os.sep + inner_package + '\n'

    return return_text


def create_module_rst_file(module_name):
    """Function for creating text in each .rst file for each module.
        module_name : name of the module.
    """

    return_text = 'Module:  ' + module_name
    dash = '=' * len(return_text)
    return_text += '\n' + dash + '\n\n'
    return_text += '.. automodule:: ' + module_name + '\n'
    return_text += '   :members:\n\n'

    return return_text


def create_dirs(path):
    """Shorter function for creating directory(s).
    """

    if not os.path.exists(path):
        os.makedirs(path)


def write_rst_file(file_path, file_name, content):
    """Shorter procedure for creating rst file
    """

    create_dirs(os.path.split(os.path.join(file_path, file_name))[0])
    try:
        fl = open(os.path.join(file_path, file_name + '.rst'), 'w+')
        fl.write(content)
        fl.close()

    except Exception, e:
        print ('Creating %s failed' % os.path.join(
            file_path, file_name + '.rst'), e)


def get_python_files_from_list(files, excluded_files=None):
    """Return list of python file from files, without excluded files.
    """

    if excluded_files is None:
        excluded_files = ['__init__.py']
    python_files = []
    for fl in files:
        if (fl.endswith('.py') and not
                fl in excluded_files and not
                fl.startswith('test')):
            python_files.append(fl)

    return python_files


def create_top_level_index(inasafe_docs_path, packages, max_depth=2):
    #assemble a list of python files in the safe_qgis Package
    page_text = INDEX_HEADER
    for package in packages:
        # Write top level index file entries for safe_qgis, safe and Unit Tests
        text = create_top_level_index_entry(
            title='Package %s' % package,
            max_depth=max_depth,
            subtitles=[package])

        page_text += '%s\n' % text

    write_rst_file(
        inasafe_docs_path, 'index',
        page_text)


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


def get_inasafe_documentation_path():
    # determine the path to inasafe code using default or argv as needed
    inasafe_code_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', '..', 'inasafe-doc'))
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


def create_api_docs(code_path, inasafe_docs_path, max_depth=2):
    """Function for generating .rst file for all .py file in dir_path folder.
    :param code_path:
    :param inasafe_docs_path: path of the folder
    :param max_depth:
    """
    base_path = os.path.split(code_path)[0]
    for package, subpackages, candidate_files in os.walk(code_path):
        # Checking __init__.py file
        if '__init__.py' not in candidate_files:
            continue
        # Creating directory for the package
        package_relative_path = package.replace(base_path + os.sep, '')
        index_package_path = os.path.join(
            inasafe_docs_path, package_relative_path)
        # calculate dir one up from package to store the index in
        index_base_path, package_base_name = os.path.split(index_package_path)

        if package_base_name in EXCLUDED_PACKAGES:
            continue

        full_package_name = package_relative_path.replace(os.sep, '.')
        new_rst_dir = os.path.join(inasafe_docs_path, package_relative_path)
        create_dirs(new_rst_dir)

        # Create index_file for the directory
        modules = get_python_files_from_list(candidate_files)
        index_file_text = create_package_level_rst_index_file(
            package_name=full_package_name,
            max_depth=max_depth,
            modules=modules,
            inner_packages=subpackages)

        write_rst_file(
            file_path=index_base_path,
            file_name=package_base_name,
            content=index_file_text)

        # Creating .rst file for each .py file
        for module in modules:
            module = module[:-3]  # strip .py off the end
            py_module_text = create_module_rst_file(
                '%s.%s' % (full_package_name, module))
            write_rst_file(
                file_path=new_rst_dir,
                file_name=module,
                content=py_module_text)


def main():

    inasafe_code_path = get_inasafe_code_path()
    inasafe_docs_path = clean_api_docs_dirs()
    max_depth = 2
    packages = ['safe', 'safe_qgis']

    create_top_level_index(inasafe_docs_path, packages, max_depth)

    for package in packages:
        code_path = os.path.join(inasafe_code_path, package)
        create_api_docs(
            code_path=code_path,
            inasafe_docs_path=inasafe_docs_path,
            max_depth=max_depth)


if __name__ == '__main__':
    main()
