.. _minimum_needs_manager:

Minimum Needs Manager
=====================

As of version 2.2, the minimum needs system have received a major overhaul.
The minimum needs manager is a new tool that allows you to define 'profiles'
of minimum needs to make them relevant to your country or region.

.. figure:: /static/user-docs/minimum_needs_manager.*
   :scale: 75 %
   :alt: Minimum Needs Manager
   :align: center

   Minimum Needs Manager

We ship |project_name| with standard profiles for:

* Indonesia - based on 'Perka 7/2008'
* Philippines (based on 'Guidelines on Evacuation Center Coordination and
  Management Joint Memorandom Circular No. Series of 2013')

There are two key concepts to be aware of in the minimum needs manager:

* profiles
* resources

Minimum needs profiles
----------------------

A profile is a collection of resources that define the minimum needs for
a particular country or region. Typically a profile should be based on a
regional, national or international standard. The actual definition of
which resources are needed in a given profile is dependent on the local
conditions and customs for the area where the contingency plan is being
devised.

For example in the middle east, rice is a staple food whereas in South Africa,
maize meal is a staple food and thus the contingency planning should take
these localised needs into account.

Minimum needs resources
-----------------------

Each item in a minimum needs **profile** is a resource. Each resource is
described as a simple natural language sentance e.g.:

"Each person should be provided with 2.8 kilograms of Rice weekly."

By clicking on a resource entry in the profile window, and then clicking the
:guilabel:`black pencil` icon you will be able to edit the resource using the resource
editor. Alternatively you can create a new resource for a profile by clicking
on the black :guilabel:`+` icon in the profile manager. You can also remove any
resource from a profile using the :guilabel:`-` icon in the profile manager.

.. figure:: /static/user-docs/resource-editor.*
   :scale: 75 %
   :alt: Resource Editor
   :align: center

   Resource editor

When switching to edit or add resource mode, the minimum needs manager will
be updated to look like the screenshot above. Each resource is described in
terms of:

* resource name e.g. Rice
* a description of the resource e.g. Basic food
* unit in which the resource is provided e.g. kilogram
* pluralised form of the units e.g. kilograms
* abbreviation for the unit e.g. kg
* the default allocation for the resource e.g. 2.8. This number can be
  overridden on a per-analysis basis.
* minimum allowed which is used to prevent allocating e.g. no drinking water
  to displaced persons
* maximum allowed which is used to set a sensible upper limit for the resource
* a readable sentence which is used to compile the sentence describing the
  resource in reports.

These parameters are probably all fairly self explanatory, but the readable
sentence probably needs further detail. The sentence is compiled using a simple
keyword token replacement system. The following tokens can be used:

* ``{{ Default }}``
* ``{{ Unit }}``
* ``{{ Units }}``
* ``{{ Unit abbreviation }}``
* ``{{ Resource name }}``
* ``{{ Frequency }}``
* ``{{ Minimum allowed }}``
* ``{{ Maximum allowed }}``

When the token is placed in the sentence it will be replaced with the actual
value at report generation time. This contrived example shows a
tokenised sentence that includes all possible keywords::

    A displaced person should be provided with {{ Default }}
    {{ Unit }}/{{ Units }}/{{ Unit abbreviation }} of {{ Resource name }}.
    Though no less than {{ Minimum allowed }} and no more than
    {{ Maximum allowed }}. This should be provided {{ Frequency }}.

Would generate a human readable sentence like this::

    A displaced person should be provided with 2.8
    kilogram/kilograms/kg of rice.
    Though no less than 0 and no more than
    100. This should be provided daily.

Once you have populated the resource elements, click the :guilabel:`Save
resource` button to return to the profile view. You will see the new resource
added in the profile's resource list.


Managing profiles
-----------------

In addition to the profiles that come as standard with |project_name|, you can create
new ones, either from scratch, or based on an existing one (which you can
then modify).

Use the :guilabel:`New` button to create new profile. When prompted, give your
profile a name e.g. :kdb:`JakartaProfile`.

**Note:** The profile must be saved in your home directory under :file:`.qgis2/minimum_needs`
in order for |project_name| to successfully detect it.

An alternative way to create a new profile is to use the :guilabel:`Save as`
to clone an existing profile. The clone profile can then be edited according to your specific needs.

Active profile
--------------

It is important to note, that which ever profile you select in the :guilabel:`Profile`
pick list, will be considered **active** and will be used as the basis for all
minimum needs analysis.
