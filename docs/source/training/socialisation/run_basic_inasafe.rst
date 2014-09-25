.. _run-basic-inasafe:

Run Basic |project_name|
========================

**Objectives:**

* To run |project_name| using a flood model & population and examine the
  results
* To create a impact map
* To modify the threshold of an impact function
* To run |project_name| using a flood model & building and examine the results

**Expected Results:**

Participants are able to:

* run and understand the results of an |project_name| using a flood model &
  population
* create an impact map using the |project_name| print button
* change the threshold of an impact function
* run and understand the results of an |project_name| using a flood model &
  building

**Data for Practical**

You can download the InaSAFEv2.0.zip from `InaSAFE Training Data Packages
<http://data.inasafe.org/TrainingDataPackages/>`_
or it will be provided to you during the training.

Introduction
------------

In this section we will run |project_name| using a scenario in Jakarta, Indonesia 
to determine the impact of a flood model on both Jakarta's population and buildings.

1. Go to :menuselection:`File --> Open Projects`.

2. If you have been following along in the previous sections a message box will appear 
   asking if you want to save the current project. Click :guilabel:`Discard`.

.. image:: /static/training/socialisation/028_saveproject.*
   :align: center

3. Navigate to the :file:`InaSAFE_project` folder and select
	 :file:`Jakarta_floods.qgs`, Click :guilabel:`Open`.

The project looks something like this:

.. image:: /static/training/socialisation/029_jakartafloods.*
   :align: center


People need evacuating
----------------------

As you can see the |project_name| panel has the first three drop down menus
filled in already:

* a flood similar to the 2007 Jakarta event
* buildings
* Be Flooded

4. In the |project_name| panel click on :guilabel:`buildings` and
select :guilabel:`people` instead. It should now have:

* a flood similar to the 2007 Jakarta event
* people
* Need evacuation

.. image:: /static/training/socialisation/030_showpeople.*
   :align: center

.. note:: Notice that the impact function below :guilabel:`Might` automatically
   changed from :guilabel:`Be flooded` to :guilabel:`Need evacuation`. This is changed
   because of the new combination of the hazard and exposure layers.

5. Lets run this scenario first. Click :guilabel:`Run` in the bottom right
   hand corner of the |project_name| panel.

.. image:: /static/training/socialisation/031_run.png
   :align: center

A new layer should appear in the layer panel called *Population which needs
evacuating*.

.. image:: /static/training/socialisation/032_results.*
   :align: center

In the |project_name| panel we now see text and
statistics, which we will explore further.

.. image:: /static/training/socialisation/033_peoplefloodresult.*
   :align: center

**Evacuation:** There are 1,109,000 people that are located in water deeper than
one metre. It is assumed that all of these people will need to evacuate their
homes.  The threshold of one metre can be changed (see Changing Threshold below).

**Minimum needs:** is calculated using the above number of evacuated people to
estimate the amount of food, water and other products that the refugees will
need to survive. The figures are based on an Indonesian policy.

**Action checklist:** designed to make disaster managers think about what
they need to do to prepare for the event.

**Notes:** explains the total people in the map canvas, the threshold of water
depth that requires evacuation and the source of the minimum needs assessment.

**Detailed gender and age report:** Statistical breakdown of the number of
females, minimum needs for womens' hygiene and pregnant women, as
well as a statistical breakdown of Youth, Adults and Elderly.

**Source:** where the exposure and hazard data originally came from.

Print Results
.............

.. note:: You can choose whether you want print the whole analysis or the current
   map extent. You also can pick an existing print template or you can navigate to your own
   QGIS template (.qpt). For more information about printing Click
   :guilabel:`Help` in the print window.

6. Click :guilabel:`Print` at the bottom the |project_name| panel.

.. image:: /static/training/socialisation/034_print.*
   :align: center

7. A window will pop up as shown below. Ensure that :guilabel:`Analysis extent`
   is selected under :guilabel:`Area to print` and :guilabel:`inasafe...` is chosen
   under :guilabel:`Template to use`. Click :guilabel:`Open PDF`.

.. image:: /static/training/socialisation/034a_impact_report.*
   :align: center

8. Navigate to where you would like to save the PDF
   and type :file:`Jakartaflood_evacuation_1m`. Click :guilabel:`Save`.

.. image:: /static/training/socialisation/034b_save_report.*
   :align: center

Two PDFs will be generated, which contain a map and a table of information about the impact.

.. image:: /static/training/socialisation/035_People_in_need_of_evacuation_1m.*
   :align: center

.. note:: In the future version of |project_name| the developers will make improvements
   to the layout of these PDF files. *If you have time during this course please
   proved us with your ideas on how the print map and table should look!*

Changing threshold
..................

What if the disaster manager decides that people should be evacuated if they
are in 80cm or more of water? In this case we will need to change the water threshold
at which level people should be evacuated.

9. Click :guilabel:`Show question form` found at the top of the |project_name| panel.

.. image:: /static/training/socialisation/036_showquestion.*
   :align: center

10. To change the impact function click the :guilabel:`Options...` button next to
    the :guilabel:`Need evacuation`.

.. image:: /static/training/socialisation/037_functionchange.*
   :align: center

11. Type :kbd:`0.8` in the :guilabel:`Thresholds` field.

.. image:: /static/training/socialisation/038_configure.*
   :align: center

12. Click :guilabel:`OK`.

13. Click :guilabel:`Run` to process the scenario with the new water threshold.

.. image:: /static/training/socialisation/031_run.*
   :align: center

When the function completes, take a look at the new numbers
in the |project_name| panel. How have they changed?

.. todo:: How many people need to be evacuated?
   **Answer:** ______________________
   Is this the answer you were expecting?
   **Answer:** _____________________

14. Click :guilabel:`Print` at the bottom the |project_name| panel.

.. image:: /static/training/socialisation/034_print.*
   :align: center

15. A window will pop up as shown below. Ensure that :guilabel:`Analysis extent`
   is selected under :guilabel:`Area to print` and :guilabel:`inasafe...` is chosen
   under :guilabel:`Template to use`. Click :guilabel:`Open PDF`.

.. image:: /static/training/socialisation/034a_impact_report.*
   :align: center

16. Navigate to where you would like to save the pdf
   and type :file:`Jakartaflood_evacuation_80cm`. Click :guilabel:`Save`.

17. Next we will run the |project_name| analysis on buildings, but first let's turn 
    some layers off. In the Layers panel there should now be five layers. Uncheck 
    everything except:

* a flood similar to the 2007 Jakarta event
* buildings

.. image:: /static/training/socialisation/039_buildingflood.*
   :align: center

Buildings Affected
------------------

18. Confirm that the |project_name| panel is the same as the image below

.. image:: /static/training/socialisation/040_inasafebuidlingflood.png
   :align: center

19. Notice that if you click on the dropdown box with :guilabel:`Buildings`,
    the people option is not available. This is because :guilabel:`people` 
    is not checked in the Layers panel.

.. note:: If you want to be able to select layers within the
   |project_name| panel that are not checked in the **Layer List** you can
   modify the |project_name| options.
   For more information on |project_name| options, see the user documentation here: 
   :doc:`../../user-docs/application-help/options`.
   The option menu is also discussed later in this tutorial in :doc:`helpful_hints_and_tips`.

20. Click :guilabel:`Run` to process the new scenario.

.. image:: /static/training/socialisation/041_buildingfloodresults.png
   :align: center

In this scenario approximately 1,434 buildings could be affected out of 31,515
buildings.

Due to the provincial BPBD work in OpenStreetMap they have mapped all
important buildings (and then some!).

Important buildings are defined as:

* Clinic/doctors
* Fire stations
* Government
* Hospitals
* Place of Worship
* Police stations
* Residential
* Schools
* Sports Facilities
* Univeristy/college

**Action Checklist:** A different set of actions have been identified to
relate to structures.

**Note:** Similar to the last |project_name| analysis, this analysis also
assumes impact is in water above one metre.

**Detailed building type report:** This is a breakdown of important
infrastructure, when you choose to aggregate (we will do this later) this
table will show the number of buildings by aggregation boundary.

**Source:** of the Hazard and Population Datasets


21. Click :guilabel:`Print` at the bottom the |project_name| panel.

.. image:: /static/training/socialisation/034_print.png
   :align: center

22. A window will pop up as shown below. Ensure that :guilabel:`Analysis extent`
   is selected under :guilabel:`Area to print` and :guilabel:`inasafe...` is chosen
   under :guilabel:`Template to use`. Click :guilabel:`Open PDF`.

.. image:: /static/training/socialisation/034a_impact_report.*
   :align: center

23. Navigate to where you would like to save the PDF
   and type :file:`Jakartaflood_inundated_1m`. Click :guilabel:`Save`.


(Optional) Change the threshold to 0.8
......................................

You may try running this scenario again with a water threshold of 0.8 metres.

24. Check that |project_name| has the following in the drop-down boxes:

* a flood similar to the 2007 Jakarta event
* Buildings
* Be flooded

25. To change the impact function click the :guilabel:`Options...` button next to
    the :guilabel:`Be flooded`.

26. Type :kbd:`0.8` in the :guilabel:`Thresholds` field.

27. Click :guilabel:`Run` to process the scenario with the new water threshold.

28. Click :guilabel:`Print` and save PDFs the same way as before.

