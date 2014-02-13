.. _writing_api_doc:

Writing API documentation
=========================

For writing documentation in Restructured Text you should first read
:doc:`../user-docs/writing_documentation`.

.. _api-documentation-howto-label:

Creating API Documentation
--------------------------

Each API Function needs to be documented according to the |project_name|
:doc:`coding_standards`.

For that each class method and function in the code base must include a
docstring explaining its usage and purpose as per the example listed below
::

        """Setup internationalisation for the plugin.

        See if QGIS wants to override the system locale
        and then see if we can get a valid translation file
        for whatever locale is effectively being used.

        :param preferred_locale: Override any other way of determining locale.
        :type preferred_local: str
        """

For a more detailed example see :ref:`doc-strings-label`.

There should be a blank line between each paragraph and before the Args option.

Where multiple inputs or outputs are used, a blank line should separate them.

.. note:: You can use any ReSTructured text within the docstring to deliver
   rich markup in the final API documentation outputs.

In order for a new module's documentation to appear in the API docs, the
following steps are required:

.. note:: The steps below are automated using the
   :file:`scripts/create_api_docs.py` file available in the inasafe-doc repo.

This manual steps are only here for historical purposes,
everything is done by a script in the documentation repository now.

* Create a new file in :file:`docs/source/api-docs/<package_name>`
  named after the module.
  For example, for the gui/riab.py module we would create
  :file:`docs/source/api-docs/gui/riab.rst` (note the .rst extension).
  See below for an example of its contents.
* Add the new file to the API docs master index
  (:file:`docs/source/api-docs/index.rst`).
  The .rst extension is not needed or desired when adding to the index list.
* Add the new .rst file to the revision control system.

An example of the contents of a module's API .rst if provided below::

    Module:  safe.common.polygon
    ============================

    .. automodule:: safe.common.polygon
          :members:

This module forms part of the `InaSAFE <http://inasafe.org>`_ tool.

A couple of things should be noted here:

* Sphinx provides automodule and autoclass directives. We have opted to use
  **automodule** for all API documentation because autoclass requires that
  each class be enumerated and anonymous functions need to be explicitly listed.
* Automodule must point to a fully qualified python module path.
* The **members** directive instructs autodocs to enumerate all classes and
  functions in that module.

Once the new document has been added and the documentation generated, you
should see it appear in the API section of the |project_name| documentation.

.. _documenting-new-features-howto-label:

Documenting new features
------------------------

New features should be well documented and that documentation should be made
available under the :file:`user-docs` subfolder of the sphinx sources tree.

For example, when the keywords editor dialog feature was introduced, we created
a new sphinx document :file:`docs/sources/user-docs/dock.rst` which
documents this new feature.
Additionally, the help button is set to launch the help dialog in the context
of the new help document e.g.::

    from safe_qgis.utilities.help import show_context_help

    def show_help(self):
        """Load the help text into the system browser."""
        show_context_help(context='dock')

Where the 'dock' parameter indicates the user-docs/\*.rst document that
should be opened when the help button is clicked.
The general style and approach used in existing documentation should inform
your documentation process so that all the documentation is consistent.
