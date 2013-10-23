.. _bug_reporting:

Reporting bugs and getting help
===============================

We are very open to ideas, suggestions and patches to improve this software -
it is open source after all!

.. _issue_report:

Issue report (suggestion and patches)
-------------------------------------

If you have any wishes or suggestions to improve the software (new ideas,
better menus) you can create an `issue report <issue_write_report>`_

To be able to handle an issue report in the best way, the report itself
should be as detailed as possible including:

- What is not working.
- How to reproduce it.
- If possible make sample files to reproduce the issue available.

If you are a developer and found/fixed a bug there is the possibility to
create a pull request to get it included into |project_name|.

Bearing that all in mind you have to create an
`issue report <issue_write_report>`_ to make the Developers aware of you
improvements.


.. _issue_write_report:

How to write an issue report
----------------------------

At first please use the search function to search through the already
existing issues. There is a possibility that someone else already found your
issue and reported it or already had the same suggestion as you.

The issue is related to
.......................

You have to think about is where the issue you would like to
report is taking place:

There are three possibilities:

1. The |project_name| software itself: report an issue on
   `the project <https://github.com/AIFDR/inasafe/issues>`_
2. The Documentation of |project_name| (would mainly mean the Webpage):
   report an issue
   `in documentation <https://github.com/AIFDR/inasafe-doc/issues>`_
3. Found some problems in the infrastructure: report an issue
   `in infrastructure <https://github.com/AIFDR/inasafe-infrastructure/issues>`_

Issue report in detail
......................

You can find the green button called :guilabel:`New Issue` on the top right
corner of the screen.
Click on it and you will be sent to a new Page.

In the line with "Title" try to enter a self speaking description of your
problem/suggestion. Try only to use a few words there.

In the TAB :guilabel:`Write` you can enter the long description of what you
want to tell.
Following the guidelines it is recommended to separate your issue into the
parts of

1. Problem/Suggestion
2. Proposed Solution
3. Expected outcome

To make your issue report even better readable it is also recommended to use
the MD markup language in this report (nothing to be scared of,
it is easy to learn and you only need a few basic terms).

.. _example_of_issue_report:

Example of a good issue report
..............................

The basic construct of a "perfect" issue report will look like this

::

 # Problem/Suggestion
 Please add the feature xyz to the project

 # Proposed Solution
 The feature would work like this: ....
 And it would be similar like feature requested in #689 which is documented
 in AIFDR/inasafe-doc#46

 # Expected outcome
 People working with this feature would have the following benefits of it:
 As already done in commit @ae56eg which is documented in
 AIFDR/inasafe-doc@4a78fe i reference here


Tips and Tricks for reporting
.............................

Hints for writing a good issue report:
(most examples are covered in the `example <example_of_issue_report>`_)

- use the buttons available under :guilabel:`Add Labels` on the right side of
  your issue report.
- link already existing and related issues to yours by adding a issue number
  like #608
- link commits already done by entering commit @SHA like @ae67fa
-

Add Labels
^^^^^^^^^^
An important thing you can do while reporting an issue is the
:guilabel:`Add Labels` section on the right side of the newly created issue.
It is a good idea to mark your issue with the correct Label so that it is
clearly visible to developers in which section this issue report belongs to.

Always bear in mind that just because you currently need this feature
very urgent does not necessarily mean that it deserves the Label
:guilabel:`\* Highest Priority` or :guilabel:`\* Release Blocker`.

Search through all the labels and click the one you want to assign to your
report.
For example if you request a new feature and you describe your requested
feature in the issue report, it is very likely that you want to mark it as
:guilabel:`\* Request for Comments` to be commented and probably extended by
others as well before being implemented as a well prepared feature.
