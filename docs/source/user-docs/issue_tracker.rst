.. _issue_howto:

Submit an Issue
===============

You are more than welcome to let us know when you have found a bug or an
issue in |project_name|.

You can take the advantage of using MD language on |github| to make your report
looking more nicely and better visible to the developers.

To be able to track your issue best we have the following rules that make
clear that the issue will be easily recognised by a developer and probably
solved as fast as possible:

1. Check if the issue is already documented – best using the search
2. If Documented – add comment to issue – If not create new issue
3. For a new issue the set up should be

 * # Problem
 * # Expected Outcome
 * # Example (with data or images)
 * # Solution (if possible)
 * # Version and OS – (If necessary) InaSAFE/QGIS version and operating
   system
 * Task a developer to it (if you know who might solve it)
 * Additionally add tags and milestones (if possible).

To track the issue down it would be even more helpful if you:

* Take screenshots where they help to illustrate the issue and drag and drop
  the screenshot into the ticket.
* If you can, cut and paste an error message text or similar textual output,
  we prefer that over a screenshot.
* If you are pasting verbatim text, place it inside three backticks like so:

::

  ```
  Some text output from InaSAFE
  ```

* Add a # CC section and include others who may be interested in following
  the ticket if needed e.g.

::

  # CC

  @timlinux
  @vanpuk

* Add a # See Also section to cross reference to other tickets or commits if
  needed e.g.

::

  # See also
  ticket number #123    (note there is no space between # and ticket number)
  commit ef42f1df  (First 8 chars or so of a commit hash - GitHub will turn it
  into a
  link)

If you don't know what to do, have a look at the already existing issues and
copy the necessary parts to your issue.
