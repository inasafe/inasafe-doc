.. _release:

Release Procedure
=================

When each new version of |project_name| is released it must adhere to the
following stringent quality measures:

**Testing:** At least 2/3rds of all lines of code must be successfully
exercised by a regression test suite which is distributed alongside the
software itself.

**Clarity:** The software complies with the appropriate development
standards for the language used, i.e. the coding style guide (http://www
.python.org/dev/peps/pep-0008) and has been peer reviewed.

**Disclaimer:** The software includes a clear Disclaimer of Warranty and
appropriate Limitation of Liability clause.
In this case this is achieved by using the GNU General Public Use v3 License
(http://www.gnu.org/copyleft/gpl.html).

**History:** The software is maintained in a source control system which
allows full visibility of its history, tracking of issue resolution and
potential reversal of past changes.

**Authenticity:** Source control system codes uniquely identify each
individual version of the software making it possible to verify its origin.

After these stringent quality measures have been met there must be signature
from the majority of the allocated committee.

* For a **Major release** it requires approval and signature from a
  **majority** of the **PSC**
* For a **Minor release** it requires approval from a **majority** of the
  **TWG**.
* For a **Point release** it requires only approval from **any** of the
  **TWG members**.


**Definition of software release levels for the** |project_name| **project**

|project_name| is built as an add-on to QGIS so has adopted the conventions
used in QGIS:

* Major releases are versions that provide significant improvements to the
  software.
  A major release may change both the user interface and the underlying
  programming interface.
  Major releases are numbered as 1.0.0, 2.0.0, …

* Minor releases provide extensions and improvements to the software.
  They possibly modify the user interface but must maintain compatibility
  with the existing programming interface.
  Minor releases are numbered as 1.1.0, 1.2.0, …

* Point releases contain corrections of errors, optimisations and small
  improvements that maintain compatibility with both the user interface and
  the programming interface.
  Point releases are numbered as 1.1.1, 1.1.2, …
