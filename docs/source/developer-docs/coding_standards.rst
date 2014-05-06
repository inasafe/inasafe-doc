.. _coding_standards:

Coding Standards
================

.. _general-approach-label:

General approach
----------------

* Use github for revision control, issue tracking and management.
* Adherence to regression/unit testing wherever possible (:samp:`make test`)
* Simple deployment procedure - all dependencies must be delivered with
  the plugin installer for QGIS or exist in standard QGIS installs.
* Develop in the spirit of XP/Agile, i.e. frequent releases, continuous
  integration and iterative development. The master branch should always
  be assumed to represent a working demo with all tests passing.
* If a method or function is longer than a single screen, it is probably a
  candidate for refactoring into smaller methods / functions. Writing smaller
  methods makes your code easier to read and to test.
* If you use a few lines of code in more than one place, refactor them into
  their own function.

.. _standards-compliance-label:

Compliance
----------

* Coding must follow a style guide. In case of Python it is
  `PEP8 <http://www.python.org/dev/peps/pep-0008>`_ and
  using the command line tool pep8 (or :samp:`make pep8`) to enforce this.
  The pep8 checks E121-E128 have been disabled until pep8 version 1.3 becomes
  widely available.
* `Python documentation guide <http://www.python.org/dev/peps/pep-0257>`_
* Code must pass a pylint validation
  (http://www.logilab.org/card/pylint_manual#what-is-pylint). You can test
  this using the make target ``make pylint``. In some cases you may wish to
  override a line or group of lines so that they are not validated by lint.
  You can do this by adding either::

     import foo  # pylint: disable=W1203

  or::

     # pylint: disable=W1234
     print 'hello'
     print 'goodbye'
     # pylint: enable=W1234

  The relevant id (W1234) is provided on the output of the above mentioned lint
  command's output. A complete list of codes is available at
  http://pylint-messages.wikidot.com/all-codes.

  .. note:: You can globally ignore messages by adding them to :file:`pylintrc`
     in the :samp:`[MESSAGES CONTROL]` section.

  The following pylint messages have been thus globally excluded from the
  check. For a discussion of these see also github issue
  https://github.com/AIFDR/inasafe/issues/245.

  * All type R: Refactor suggestions such as limiting the number of local
                variables. We may bring some back later.
  * All type I: Information only
  * W0142: Allow the Python feature F(\*args, \*\*kwargs)
  * W0201: Allow definition of class attributes outside the constructor.
  * W0212: Allow access to protected members (e.g. _show_system_info)
  * W0231: Allow classes without constructors.
  * W0232: Un-instantiated classes is a feature used in this project.
  * W0403: Relative imports are OK for modules that live in the same dir
  * W0511: Appearance of TODO and FIXME is not a sign of poor quality
  * E1101: Disable check for missing attributes.
  * E1103: This one does not understand numpy variables.
  * C0103: Allow mathematical variables such as x0 or A.
  * C0111: Allow missing docstrings in some cases
  * C0302: No restriction on the number of lines per module

  It is of course possible to run all pylint checks on any part of the code
  if desired: E.g pylint safe/storage/raster.py


.. _naming-conventions-label:

Naming conventions
------------------

Variable names should as far as possible follow python naming conventions (see
:ref:`Qt Notes <qt-label>` below for exceptions to this rule).

We reject the idea the code should be obfusicated with hard to understand
symbol names. For this reason all classes, methods, functions, variable names
should be written in full. At the same time overly verbose names should be
avoided. Here is an example of what we mean by this. Bad::

    cur_dpth = 0  # obscure
    currentDepth = 0  # camel case is not python standard
    content_of_page = 'foo'  # overly verbose

Good::

    current_depth = 0
    content_of_page = 'foo'  # overly verbose


Avoid 'yoda speak' in variable names. Bad::

    title_dialog = self.tr('Save Scenario')

Good::

    dialog_title = self.tr('Save Scenario')

This is a summary of the naming conventions you should use:

* **package dir name**: concise (preferably single word) lower case, underscore
  separated e.g. ``utilities``.
* **module file name**: concise (preferably single word) lower case, underscore
  separated e.g. ``utilities.py``.
* **class name**: Concise singular camel case phrase e.g. ``PrintDialog``.
* **method and function name**: Concise lower case underscore separated name
  .e.g. ``remove_entry``. Avoid java style *get* suffixes as it adds no
  useful meaning to a symbol name.
* **variable naming**: Concise, unabbreviated, lower case, underscore separated
  e.g. ``population_count``.

.. _code_formatting:

Code formatting
---------------

The guidelines above still leave substantial room for your own approach to
code style so the following provide some more explicit guidelines.

We follow a 'pull left' policy in our code. This means that instead of e.g.::

    def polygonize_thresholds(raster_file_name,
                          threshold_min=0.0,
                          threshold_max=float('inf')):

You should rather do this::

    def polygonize_thresholds(
        raster_file_name,
        threshold_min=0.0,
        threshold_max=float('inf')):

The same applies in all other contexts. For example, calling a function::

    clipped_exposure = clip_layer(
        layer=exposure_layer,
        extent=geo_extent,
        cell_size=cell_size,
        extra_keywords=extra_exposure_keywords,
        hard_clip_flag=self.clip_hard)

We do this because the 80 character line limit in PEP8 can cause visual clutter
in your code as you manage line breaks as you run up to the 80 column limit. By
always pulling code left as much as possible, we reduce the amount of line
continuation management we have to do.

.. _imports_ordering-label:

Ordering of imports
-------------------

When importing please adhere to the following rules:

Do not do ``*`` imports e.g. ``from PyQt4.QtGui import *`` is bad. Either
import the individual modules you need e.g.
``from PyQt4.QtGui import QProgressDialog`` or import the whole package and
use the namespace to reference a module e.g.::

    from PyQt4 import QtGui

    progress = QtGui.QProgressDialog()

Imports should be made in the following order:

* core python imports (e.g. ``import os``)
* third party imports (e.g. ``from PyQt4 import QtGui``)
* application imports (e.g. ``from foo import bar``)

InaSAFE specific notes
.........................

* We have two main packages: ``safe`` and ``safe_qgis``. The latter is a client
of the former. For this reason you should **never**  import ``safe_qgis`` from
``safe`` because you will create a circular import.

* When using ``safe`` from ``safe_qgis``, always access the API via
``safe.api``, never import functions directly from elsewhere in the package.
The ``api`` module provides a layer of abstraction, allowing us to move things
around in safe without breaking any third party code that may depend on the
API. Put another way, you can consider the ``safe.api`` to be stable in a minor
release, but the rest of the package is subject to change.

.. _doc-strings-label:

Doc strings and comments
------------------------

All code should be self documenting. Please take special note and follow
these PEP guidelines and sphinx documents:

* http://www.python.org/dev/peps/pep-0287/
* http://sphinx-doc.org/markup/desc.html#info-field-lists
* http://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html

We follow these specific guidelines for our code:

* Docstrings must triple quoted with :samp:`"""`
* Inline comments should start with a # and a single space.
* Comments should be complete sentences ending with a full stop / period.
* If a comment is a phrase or sentence, its first word should be capitalized,
  unless it is an identifier that begins with a lower case letter (never alter
  the case of identifiers!).

We use the following style for documenting functions and class methods::

    def set_keyword_db_path(self, path):
        """Set the path for the keyword database (sqlite).

        The file will be used to search for keywords for non local datasets.

        :param path: A valid path to a sqlite database. The database does
            not need to exist already, but the user should be able to write
            to the path provided.
        :type path: str

        :returns: Flag indicating if the path was set successfully.
        :rtype: boolean


        """
        self.keyword_db_path = str(path)


Another example::

    def add_layers(scenario_dir, paths):
        """Add the layers described in a scenario file to QGIS.

        :param scenario_dir: Base directory to find path.
        :type scenario_dir: str

        :param paths: Path of scenario file (or a list of paths).
        :type paths: str, list

        :raises: Exception, TypeError, FileNotFoundError

        Note:
            * Exception - occurs when paths have illegal extension
            * TypeError - occurs when paths is not string or list
            * FileNotFoundError - occurs when file not found
    """

Note the following in the above examples:

* The first line of a docstring should be a precis of the class/method/function
  expressed in less than 80 chars, terminated with a full stop and exclude
  redundant phrases such as 'Class to do x' or 'This method does...'.
* There should be an empty line following the first docstring line.
* More detailed explanation and usage examples can follow this first line. The
  detailed explanation should not repeat the information provided in the
  parameters and returns sections.
* A line break should follow the optional detailed description.
* **param** and **type** are grouped together with no line break between them.
* If the param description is more than one line, indent the successive lines
  with 4 spaces.
* A newline should be placed after each type and rtype.
* If multiple types are allowed, separate them with commas e.g. ``:rtype: str,
  boolean``.
* If a function or method returns nothing, no **returns** section is used.
* If a function or method does not raise anything explicitly, no raises section
  is used.
* If a function or method is extremely obvious there is no need to have
  anything more than a single line docstring.
* If a function or method returns a tuple it should be be documented as
  ``:rtype: (<type>, <type>, ..)`` e.g. ``:rtype: (int, int)``.

Please also see the :ref:`api-documentation-howto-label` section for more
information on how to document your code properly.

Annotating API changes and additions
------------------------------------

Whenever you add or change a module, class, function or method, you should
annotate it accordingly. The method for doing this is described on the
`Sphinx paragraph markup page <http://sphinx-doc.org/markup/para.html>`_. Here
are a couple of examples:

Adding a new module::

    """Impact function utilities.

    .. versionadded:: 2.1
    ""'

Adding a new method to a class::

    """Computes the number of affected people.

    .. versionadded:: 2.1
    """

Changing an existing method API::

    def show_static_message(self, message, foo):
    """Send a static message to the message viewer.

    .. versionchanged:: 2.1
        Added foo parameter.

    Static messages cause any previous content in the MessageViewer to be
    replaced with new content.

    :param message: An instance of our rich message class.
    :type message: Message

    :param foo: Some new parameter.
    :type foo: str

    """
    dispatcher.send(
        signal=STATIC_MESSAGE_SIGNAL,
        sender=self,
        message=message)



.. _strings-and-internationalisation-label:

Strings and internationalisation
--------------------------------

* Simple strings in source code should be quoted with :samp:`'`
* Favour interpolation over concatenation. For example this is bad::

    world = 'World'
    foo = 'Hello ' + world

And this is good::

    world = 'World'
    food = 'Hello %s' % world

* Use parenthesis for long strings. For example this is bad::

    foo = 'The quick brown fox jumps over the lazy dog. ' +
          'The slow fat rat runs around the mouldy cheese.'

And this is good::

    bar = (
        'The quick brown fox jumps over the lazy dog. '
        'The slow fat rat runs around the mouldy cheese.')

.. note:: The good example above follows the 'pull left' principle.

* All strings should be internationalisation enabled. Please see :doc:`i18n`
  for details.
* When using gettext, alias the uggettext as tr, and do not use the common
  convention of ``_('foo')`` as the underscore trips up some tools like pylint,
  sphinx. Also using ``tr`` makes it easy to migrate code to and from Qt's
  translation system and gettext.

* If you use a literal string or expression in more than one place, refactor
  it into a function or variable.

.. _module-header-label:

Standard headers
----------------

Each source file should include a standard header containing copyright,
authorship and version metadata as shown in the exampled below.

**Example standard header**::

    # -*- coding: utf-8 -*-
    """**One line description.**

    .. tip::
       Detailed multi-paragraph description...

    """

    __author__ = 'Ole Nielsen <ole.moller.nielsen@gmail.com>'
    __revision__ = '$Format:%H$'
    __date__ = '01/11/2010'
    __license__ = "GPL"
    __copyright__ = 'Copyright 2012, Australia Indonesia Facility for '
    __copyright__ += 'Disaster Reduction'


.. note::
   Please see :ref:`faq_developer` for details on how the revision tag
   is replaced with the SHA1 for the file when the release packages are made.

.. _qt-label:

Qt Guidelines
.............

Compile UI files at run time. There is no need to precompile UI files using
pyuic4. Rather you can dynamically compile them using this technique (see
technical docs
`here <http://pyqt.sourceforge.net/Docs/PyQt4/designer.html#the-uic-module>`_ ::

    import os
    from PyQt4 import QtGui, uic

    BASE_CLASS = uic.loadUiType(os.path.join(
        os.path.dirname(__file__), 'foo_dialog_base.ui'))[0]


    class FooDialog(QtGui.QDialog, BASE_CLASS):
        """Dialog for defining the plugin properties.

        """
        def __init__(self, parent=None):
            """Constructor."""
            super(FooDialog, self).__init__(parent)
            # Set up the user interface from Designer.
            self.setupUi(self)


Don't use old style signal/slot connectors::

    button = self.help_button
    QtCore.QObject.connect(
        help_button, QtCore.SIGNAL('clicked()'), self.show_help)

Use new style connectors::

    self.help_button.clicked.connect(self.show_help)


Use multi-inheritance for designer based classes so that we can use autoconnect
slots.::

    class FooDialog(QtGui.QDialog, Ui_FooBase):
        """Dialog to prompt for widget names."""

        def __init__(self, parent=None):
            """Constructor for the dialog.

            This dialog will allow the user to select foo names from  a list.

            :param parent: Optional widget to use as parent
            :type parent: QWidget
            """
            QtGui.QDialog.__init__(self, parent)
            # Set up the user interface from Designer.
            self.setupUi(self)
            # ... further implementation here ...

Then we can do this to listen for a click on button bar.::

    def on_bar_clicked(self):
        """Auto slot to listen for button click."""
        pass

The callback above is called when the button is clicked simply by virtue of the
fact that it uses the naming convention ``on_<object>_clicked``.

Note that in some cases you need to explicitly specify which signature is being
listened for by using the pyqtSignature decorator.::

    @pyqtSignature('int')
    def on_polygon_layers_combo_currentIndexChanged(self, theIndex=None):
        """Automatic slot executed when the layer is changed to update fields.

        :param theIndex: Passed by the signal that triggers this slot.
        :type theIndex: int
        """
        layerId = self.polygon_layers_combo.itemData(
            theIndex, QtCore.Qt.UserRole)
        return layer_id

Failure to do this may result in the slot being called multiple times per event
which is usually undesirable.

Also in some cases using the Qt API will lead you into conflict with our PEP8
naming conventions for methods and variables. This is unavoidable but should
be used only in these specific instances e.g.::

    def on_foo_indexChanged():
        pass


Qt's naming convention causes a bit of a clash when using with 'normal' python
underscore names. For this reason we adopt the following strategy:

* in designer use underscore based naming for objects
* in your concrete implementations you should be able to then use mostly
  underscore separated names except in cases where using autoconnect slots.
* in designer you should call the form a name ending in Base e.g.
  **FooDialogBase**. By convention the concrete implementation is called the
  same sans the Base suffix e.g. **FooDialog**.

.. _hig-label:

Human Interface Guidelines
---------------------------

For consistency of user experience, the user interfaces should adhere to the QGIS Human Interface Guidelines (HIG) which
are listed here for your convenience:

+ Group related elements using group boxes:
  Try to identify elements that can be grouped together and then use group
  boxes with a label to identify the topic of that group.  Avoid using group
  boxes with only a single widget / item inside.
+ Capitalise first letter only in labels:
  Labels (and group box labels) should be written as a phrase with leading
  capital letter, and all remaining words written with lower case first letters
+ Do not end labels for widgets or group boxes with a colon:
  Adding a colon causes visual noise and does not impart additional meaning,
  so don't use them. An exception to this rule is when you have two labels next
  to each other e.g.: Label1 [Plugin Path:] Label2 [/path/to/plugins]
+ Keep harmful actions away from harmless ones:
  If you have actions for 'delete', 'remove' etc, try to impose adequate space
  between the harmful action and innocuous actions so that the users is less
  likely to inadvertently click on the harmful action.
+ Always use a QButtonBox for 'OK', 'Cancel' etc buttons:
  Using a button box will ensure that the order of 'OK' and 'Cancel' etc,
  buttons is consistent with the operating system / locale / desktop
  environment that the user is using.
+ Tabs should not be nested. If you use tabs, follow the style of the
  tabs used in QgsVectorLayerProperties / QgsProjectProperties etc.
  i.e. tabs at top with icons at 22x22.
+ Widget stacks should be avoided if at all possible. They cause problems with
  layouts and inexplicable (to the user) resizing of dialogs to accommodate
  widgets that are not visible.
+ Try to avoid technical terms and rather use a laymans equivalent e.g. use
  the word 'Transparency' rather than 'Alpha Channel' (contrived example),
  'Text' instead of 'String' and so on.
+ Use consistent iconography. If you need an icon or icon elements, please
  contact Robert Szczepanek on the mailing list for assistance.
+ Place long lists of widgets into scroll boxes. No dialog should exceed 580
  pixels in height and 1000 pixels in width.
+ Separate advanced options from basic ones. Novice users should be able to
  quickly access the items needed for basic activities without needing to
  concern themselves with complexity of advanced features. Advanced features
  should either be located below a dividing line, or placed onto a separate tab.
+ Don't add options for the sake of having lots of options. Strive to keep the
  user interface minimalistic and use sensible defaults.
+ If clicking a button will spawn a new dialog, an ellipsis (...) should be
  suffixed to the button text.

Code statistics
...............

* https://www.ohloh.net/p/inasafe/analyses/latest
* https://github.com/AIFDR/inasafe/network
* https://github.com/AIFDR/inasafe/graphs
