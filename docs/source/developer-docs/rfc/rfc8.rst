.. _rfc8:

RFC #8
======

git workflow for InaSAFE Documentation
--------------------------------------

Link to github: https://github.com/AIFDR/inasafe-doc/issues/97

**Author(s):**
mach0

**Date:**

Status
......
Accepted Draft

Abstract
........
Currently everything in documentation of InaSAFE happens in "master" branch
of inasafe-doc without reflecting the different released versions of the
InaSAFE plugin.
We should switch to a slightly different git model to make it easier to
control the information that is available on the webpage and to make it
easier to create the new upcoming documentation for the next InaSAFE release
“behind the curtains”

Content
.......

The Documentation should always be in a good shape and reflect the current
released version of InaSAFE.
Therefore we have to change to “workflow” of documenting if we want to
provide the versioned Documentation.
Up to now everything that happened in the “master” branch (regardless of the
version of InaSAFE) was always “up to date” to the latest functions
available in the development of InaSAFE.

The git workflow to follow is based on the documentation from
http://nvie.com/posts/a-successful-git-branching-model/
Basically for documentation we will mainly use "master" and "develop" branch
out of this model but you are encouraged to branch if you start documenting
new features.

“master” branch in documentation tree from now on will always reflect what
the current release of InaSAFE provides.
Updates to the documentation-“master” branch will only happen when there is a
new release of InaSAFE published. (Except Hotfixes).
This is the branch that is going to be published on http://www.inasafe.org
and users expect it to reflect the status of the InaSAFE plugin that is
currently marked as “stable” in QGIS.
“develop” will be the documentation branch where all new features of the
upcoming next release of InaSAFE will be collected and documented that are
integrated by developers in InaSAFE.
This branch will show the current “up to date” status of the documentation as
it is following the development in InaSAFE and will be published on
http://test.inasafe.org.
Our proposal is to implement these steps in the workflow

git checkout -t origin/develop to checkout and switch to the new "develop"
branch to work on.
New features should only be documented in this branch.
Hotfixes like announcements of trainings, news ... should be merged into both
branches to immediately make them available also on the main webpage.
Still the encouragement to work in branches and merge the (local) branch
once a new feature is completely documented into develop.
Once InaSafe releases a new version, "master" will be tagged with the "old"
version number of InaSAFE and "develop" will be merged into master.

Future plans
^^^^^^^^^^^^
A more stricter approach of following the git workflow will also be
implemented in Inasafe development tree to sync InaSAFE and InaSAFE
Documentation.


Tables and Figures

**bold** *italics* the usual stuff


