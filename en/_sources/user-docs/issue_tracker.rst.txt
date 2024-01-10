.. _issue_howto:

Submit an Issue
===============

You are more than welcome to let us know when you have found a bug or an
issue in |project_name|.

Issues are documented on |github|. You can report here on any issues, taking
advantage of markdown to make your report clear and visible to the
developers.

To be able to track your issue best we have created the following rules so that
the issue will be easily recognised by a developer and hopefully
solved as fast as possible:

1. Check if the issue is already documented (search existing issues)
2. If it is documented, add a comment to the issue; otherwise create a new issue
3. When creating a new issue, the format should typically be:

 * # Problem
 * # Expected Outcome
 * # Example (with data or images)
 * # Solution (if possible)
 * # Version and OS – (if necessary) InaSAFE/QGIS version and operating
   system
 * Task a developer to it (if you know who might solve it)
 * Add tags and milestones (if possible)

To track the issue down it would be even more helpful if you:

* Take screenshots to illustrate the issue; you can drag and drop
  the screenshot into the ticket (on |github|).
* If you can, cut and paste an error message text or similar textual output,
  we prefer that over a screenshot.
* If you are pasting verbatim text, place it inside three backticks like so:

::

  ```
  Some text output from InaSAFE
  ```

* Add a # CC section and include others who may be interested in following
  the ticket if needed:

::

  # CC

  @timlinux
  @vanpuk

* Add a # See Also section to cross reference to other tickets or commits if
  needed:

::

  # See also
  ticket number #123    (note there is no space between # and ticket number)
  commit ef42f1df  (First 8 chars or so of a commit hash - GitHub will turn it
  into a
  link)

If you don't know what to do, have a look at the already existing issues and
copy the necessary parts to your issue.
