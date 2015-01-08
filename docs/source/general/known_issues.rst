.. _known_issues:

Known Issues
============

**Population density grids must be in geographic coordinates**

Currently, if population density grids are projected they won't
be scaled correctly if resampled.
See also ticket `#123 <https://github.com/AIFDR/inasafe/issues/123>`_

.. _limitations:

Limitations
===========

|project_name| is still a new project.
The current code development started in earnest in March 2011 and there is
still much to be done.
However, we work on the philosophy that stakeholders should have access to
the development and source code from the very beginning and invite comments,
suggestions and contributions.

As such, |project_name| currently has some limitations, including

* Polygon area analysis (such as land use) is not supported.
* Population grid data must be provided in WGS84 geographic coordinates
* Neither |AIFDR|, the World Bank, nor |GFDRR| take any responsibility for the
  correctness of outputs from |project_name| or decisions derived as a
  consequence
