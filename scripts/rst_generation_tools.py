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
        """Constructor

        :param default_length: The default (min) character length of the column
        :type default_length: int
        """
        self.length = default_length

    def column_width(self, column_content):
        """Determine the column width, by passing the column content.

        :param column_content: The content of the column
        :type column_content: list
        """
        for entry in column_content:
            if isinstance(entry, basestring):
                self.length = max(len(entry), self.length)
            else:
                self.length = max(len('%s' % entry), self.length)

    def __call__(self):
        """Generate the horizontal border for a given column

        :return: sequence of '=' with an offset
        :rtype: str
        """
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
    def __init__(self, heading=None, rows=None):
        """Instantiate the object with optionally heading and rows.

        :param heading: The heading
        :type heading: list, None

        :param rows: The rows
        :type rows: list, None
        """
        if not heading:
            heading = []
        else:
            self.heading = self._stringify(heading)
        if not rows:
            rows = []
        else:
            self.rows = [self._stringify(row) for row in rows]

    def add_heading(self, heading):
        """Add a heading to this table.

        :param heading: The heading.
        :type heading; list
        """
        self.heading = self._stringify(heading)

    def add_row(self, row):
        """Add a row to this table.

        :param row: The row.
        :type row: list
        """
        self.rows.append(self._stringify(row))
    @staticmethod
    def _stringify(row):
        """Convert the objects in the row to strings

        :param row: The row
        :type row: list

        :return: Row with each element formatted to a string
        :rtype: list
        """
        return ['%s' % r for r in row]

    @staticmethod
    def _left_fill(row, boarders):
        """Fill each element of the row to the same size as the row of borders

        :param row: The row to be updated
        :type row: list

        :param boarders: The row of borders
        :type: list

        :return: The update row.
        :rtype: list
        """
        return [r.ljust(len(b)) for (r, b) in zip(row, boarders)]

    def __call__(self):
        """ Get the table

        :return: RST formatted table.
        :rtype: str
        """
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
    """Make all markers in the text the same.

    :param text: The text to be updated.
    :type text: str

    :param markers: The markers to be made uniform.
    :type markers: list

    :param placeholder: The optional placeholder marker
    :type placeholder: str, None

    :return: The updated text.
    :rtype: str
    """
    placeholder = placeholder or markers[0]
    for marker in markers[1:]:
        text = text.replace(marker, placeholder)
    return text


def replace_bold(text):
    """Convert html bold to rst bold in text.

    :param text: The text to be updated.
    :type text: str

    :return: The updated text.
    :rtype: str
    """
    text = uniform_markers(text, ['<b>', '</b>', '<strong>', '</strong>'])
    return text.replace('<b>', '**')


def replace_italic(text):
    """Convert html italic to rst italic in text.

    :param text: The text to be updated.
    :type text: str

    :return: The updated text.
    :rtype: str
    """
    text = uniform_markers(text, ['<i>', '</i>', '<em>', '</em>'])
    return text.replace('<i>', '*')


def format_rst_paragraph(paragraph, prefix=None, width=79):
    """ Convert a paragraph, with html formatting to rst.

    :param paragraph: The paragraph to be formatted.
    :type paragraph: str

    :param prefix: Text to highlight and prefix to paragraph.
    :type prefix: str, None

    :param width: The width of the paragraph.
    :type width: int

    :return: The formatted paragraph.
    :rtype: str
    """
    paragraph = replace_bold(paragraph)
    paragraph = replace_italic(paragraph)
    if prefix:
        paragraph = '**%s**: %s' % (prefix, paragraph)
    paragraph = wrap(paragraph, width)
    return '\n'.join(paragraph)



