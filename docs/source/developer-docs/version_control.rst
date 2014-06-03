.. _version_control:

Version Control
===============

We are using git for version control. You can find all the latest source code
here: https://github.com/AIFDR/inasafe

Branching guide
---------------

|project_name| follows the following simple branching model:

.. figure:: /static/release-workflow.png
   :align:   center


*New development* takes place in *develop*. Master should always be maintained
in a usable state with tests passing and the code functional so that we can
create a new release from master at short notice.

*Releases* are tags on the master branch and named according the the version
number (we follow the `semantic versioning scheme <http://semver.org/>`_).
So for example the first release would be version 0.1.0 and would be a tag
called *release-0_1_0*.

After the release, **no** development should take place in master. If a fix
needs to be made against master, a short lived branch should be made in the
developer's personal fork of the repository and then a GitHub Pull Request
issued requesting to merge that fix into master. Such fixes should always also
be applied to develop unless the development branch has diverged sufficiently
in order to render the hot fix obselete.

All development can also be carried out in independent forks of the
|project_name| repository and then merged into develop when they are ready via
a pull request or patch. The general workflow for working with git should be as
follows:

.. figure:: /static/general-workflow.png
   :align:   center

Please see the `gitflow web site <http://nvie.com/posts/a-successful-git-branching-model/>`_
for more in-depth discussion of how gitflow works. Also see
`RFC #821 <https://github.com/AIFDR/inasafe/issues/821>`_ where the rationale
for using gitflow is discussed in more detail.

Process for developers adding a new feature
-------------------------------------------

Create a feature branch::

    git checkout -b <featurebranch> master

Write new code and tests
    ...

Publish (if unfinished)::

    git commit -a -m "I did something wonderful"
    git push origin <featurebranch>

To keep branch up to date::

    git checkout <featurebranch>
    git merge origin develop
    (possibly resolve conflict and verify test suite runs)
    git push origin <featurebranch>

When all tests pass, issue a pull request through github.

To delete when branch is no longer needed (though it is preferable to do
such work in a fork of the official repo).
::

    git push origin :<featurebranch>

Process for checking out the develop branch and applying a fix:
---------------------------------------------------------------

Create a local
`tracking branch <http://book.git-scm.com/4_tracking_branches.html>`_
::

   git fetch
   git branch --track develop origin/develop
   git checkout inasafe-issue-553

553 being the issue number you are fixing. Now apply your fix, test and commit::

   git commit -m "Fix issue #22 - results do not display"
   git push

Now go to your own page in github and issue a pull request.

To checkout someone else's fork:
--------------------------------

Example::

   git remote add jeff git://githup.com/jj0hns0n/riab.git
   git remote update
   git checkout -b impact_map jeff/impact_map

Windows Specific Notes:
-----------------------

**Note:** The notes below are not maintained - we recommend using github for
windows which includes a command line client.

To Switch branches using TortoiseGIT:

* Navigate to the |project_name| plugin folder
* Right click on any whitespace
* From the context menu choose :menuselection:`TortoiseGIT --> Switch/Checkout`
* Tick 'Branch radio button and choose 'master' from the list
* Click :guilabel:`OK`

To update the master branch:

* Right click on the whitespace again
* :menuselection:`TortoiseGIT --> Pull` from the context menu
* Tick the remote radio
* Set remote to origin
* Tick the ellipses button next to :guilabel:`Remote Branch`
* Choose :guilabel:`master` from the list
* Click :guilabel:`OK`

For subsequent pull requests on that branch you can just do
:menuselection:`TortoiseGIT --> Pull` from the context menu and press
:guilabel:`OK`
