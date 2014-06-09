# -*- coding: utf-8 -*-
"""General tools for formatting rst.

.. tip::
   Common tools used when generating rst formatted data.
"""

__author__ = 'Christian Christelis <christian@linfiniti.com>'
__revision__ = '$Format:%H$'
__date__ = '06/06/2014'
__license__ = "GPL"
__copyright__ = 'Copyright 2014, Australia Indonesia Facility for '
__copyright__ += 'Disaster Reduction'

from textwrap import wrap


class HorizontalBorder(object):
    """Manage the border elements of a simple rst table those are the: ======
    """
    def __init__(self, default_length=5):
        self.length = default_length

    def column_width(self, column_content):
        for entry in column_content:
            if isinstance(entry, basestring):
                self.length = max(len(entry), self.length)
            else:
                self.length = max(len('%s' % entry), self.length)

    def __call__(self):
        return '%s  ' % ('=' * self.length)


class SimpleRstTableFormatter(object):
    """Create a simple rst table the table conforms to:

    .. table::

       ===========  ==============
       Key          Allowed Values
       ===========  ==============
       subcategory  tsunami
       subcategory  flood
       subcategory  volcano
       subcategory  earthquake
       ===========  ==============

    """
    def __init__(self, heading=[], rows=[]):
        """Instantiate the object with optionalrly heading and rows.
        """
        self.heading = self._stringify(heading)
        self.rows = [self._stringify(row) for row in rows]
    def add_heading(self, heading):
        self.heading = self._stringify(heading)
    def add_row(self, row):
        self.rows.append(self._stringify(row))
    @staticmethod
    def _stringify(row):
        return ['%s' % r for r in row]
    @staticmethod
    def _left_fill(row, boarders):
        return [r.ljust(len(b)) for (r,b) in zip(row, boarders)]
    def __call__(self):
        if not self.heading or not self.rows:
            raise ReferenceError
        column_count = len(self.heading)
        borders = []
        for count in range(column_count):
            border = HorizontalBorder()
            column = [self.heading[count]] + [row[count] for row in self.rows]
            border.column_width(column)
            borders.append(border())
        table = '.. table::\n\n'
        for row in [borders, self.heading, borders] + self.rows + [borders]:
            row = self._left_fill(row, borders)
            table += '   %s\n' % '  '.join(row)
        return table


def uniform_markers(text, markers, placeholder=None):
    placeholder = placeholder or markers[0]
    for marker in markers[1:]:
        text = text.replace(marker, placeholder)
    return text


def replace_bold(text):
    text = uniform_markers(text, ['<b>', '</b>', '<strong>', '</strong>'])
    return text.replace('<b>', '**')


def replace_italic(text):
    text = uniform_markers(text, ['<i>', '</i>', '<em>', '</em>'])
    return text.replace('<i>', '*')


def format_rst_paragraph(paragraph, width=79):
    paragraph = replace_bold(paragraph)
    paragraph = replace_italic(paragraph)
    paragraph = wrap(paragraph, width)
    return '\n'.join(paragraph)



