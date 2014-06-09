# -*- coding: utf-8 -*-
"""Use IF keywords to generate keywords.rst from template.

.. tip::
   The keywords_template.rst is rendered with data from Impact Functions
   Metadata. This result is written otu to a keywords.rst
"""

__author__ = 'Christian Christelis <christian@linfiniti.com>'
__revision__ = '$Format:%H$'
__date__ = '06/06/2014'
__license__ = "GPL"
__copyright__ = 'Copyright 2014, Australia Indonesia Facility for '
__copyright__ += 'Disaster Reduction'


from rst_generation_tools import SimpleRstTableFormatter as SRTF
from rst_generation_tools import format_rst_paragraph
from inasafe.safe.api import get_plugins
from jinja2 import Template
import os


class MetadataExtractor(object):
    """Helper class to extract our requeride metadata from the IF's metadata

    TODO: Add a rich description of which data is to be collected.
        (The logic is quite closely tied to the output
    """
    def __init__(self):
        self.plugin_metadata = []
        for plugin in get_plugins().values():
            if hasattr(plugin, 'Metadata'):
                self.plugin_metadata.append(plugin.Metadata().get_metadata())

    def get_categories(self):
        """Get a unique list of categories

        :rtype : list
        :return: A list of categories as they are will appear in the table body.
        """
        categories = []
        for metadata in self.plugin_metadata:
            keys = metadata['categories'].keys()
            for key in keys:
                categories.append(key)
        categories = list(set(categories))
        categories.sort()
        return [['category', category] for category in categories]

    def _collect_metadata(self, category, category_detail='', constraint=None):
        """Get a specic detail from a category

        :param category:
        :param category_detail:
        :param constraint:
        :return:
        """
        detail_collection = []
        for metadata in self.plugin_metadata:
            if category not in metadata['categories'].keys():
                continue
            if constraint:
                value = metadata['categories'][category][constraint['field']]
                value = value if type(value) == list else [value]
                values_match = any(
                    [(v['id'] in constraint['value']) for v in value])
                if not values_match:
                    continue
            detail = metadata['categories'][category][category_detail]
            if type(detail) != list:
                detail = [detail]
            for d in detail:
                detail_collection.append(d)
        return detail_collection

    def _make_unique(self, original):
        unique = []
        [unique.append(item) for item in original if item not in unique]
        return unique

    def get_subcategories(self, category):
        subcategory_data = self._collect_metadata(
            category, category_detail='subcategory')
        subcategory_names = [
            subcategory['name'] for subcategory in subcategory_data]
        subcategory_names = list(set(subcategory_names))
        subcategory_names.sort()
        return [
            ['subcategory', subcategory] for subcategory in subcategory_names]

    def get_units(self, category):
        units_data = self._collect_metadata(category, category_detail='units')
        units_names = [unit['name'] for unit in units_data]
        units_names = list(set(units_names))
        units_names.sort()
        return [['units', unit] for unit in units_names]

    def get_units_subcategory(self, category, subcategories):
        units_data = self._collect_metadata(
            category,
            category_detail='units',
            constraint={'field': 'subcategory', 'value': subcategories})
        units = [unit for unit in units_data]
        return self._make_unique(units)


if __name__ == "__main__":
    file_path = os.path.dirname(os.path.realpath(__file__))
    template_location = os.path.join(
        file_path, 'templates', 'keywords_template.rst')
    with open(template_location) as fd:
        template = Template(fd.read())

    me = MetadataExtractor()
    category_table = SRTF(['Key', 'Allowed Values'], me.get_categories())
    subcategrory_hazard_table = SRTF(['Key', 'Allowed Values'], me.get_subcategories('hazard'))
    subcategrory_exposure_table = SRTF(['Key', 'Allowed Values'], me.get_subcategories('exposure'))

    subcategories = []
    for subcategory in [['flood', 'tsunami'], ['volcano']]:
        units = me.get_units_subcategory('hazard', subcategory)
        units_content = [['units', unit['name']] for unit in units]
        units_description = [
            format_rst_paragraph(unit['description']) for unit in units]
        units_table = SRTF(['Key', 'Allowed Values'], units_content)

        subcategories.append({
            'names': subcategory,
            'table': units_table(),
            'description': units_description})

    context = {
        'category_table': category_table(),
        'subcategrory_hazard_table': subcategrory_hazard_table(),
        'subcategrory_exposure_table': subcategrory_exposure_table(),
        'subcategories': subcategories
    }
    inasafe_doc_root = os.path.dirname(file_path)
    destination_location = os.path.join(
        inasafe_doc_root,
        'docs/source/user-docs/application-help/keywords.rst')
    with open(destination_location, 'w') as fd:
        fd.write(template.render(**context))
