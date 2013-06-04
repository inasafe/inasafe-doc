Run basic |project_name|
========================

**Objectives:**

* To run |project_name| using a flood model & population and examine the
  results
* To create a impact map
* To modify the threshold of an impact function
* To run |project_name| using a flood model & building and examine the results
* To run |project_name| with aggregation (optional)

**Expected Results:**

Participants are able to:

* run and understand the results of an |project_name| using a flood model &
  population
* create an impact map using the |project_name| print button
* change the threshold of an impact function
* run and understand the results of an |project_name| using a flood model &
  building
* run |project_name| with aggregation by district (optional)

Introduction
------------

In this chapter you will run |project_name| in Jakarta to determine the
impact of a flood model on Jakarta's population and buildings.

1. :guilabel:`Open` Jakarta_floods.qgs - File/Open Project... ,

2. :guilabel:`Click` on browse navigate to |project_name| projects and
   :guilabel:`Select` *Jakarta_floods*, :guilabel:`Click` open and then open
   again

.. image:: /static/socialisation/page_28.jpg
   :align: center


People need evacuating
----------------------

3. As you can see the |project_name| panel has the first three drop down
   menus filed in already:

* a flood similar to the 2007 Jakarta event
* buildings
* Be Flooded

4. :guilabel:`Click` the arrow next to buildings, :guilabel:`Select` people,
   it now should have:

* a flood similar to the 2007 Jakarta event
* people
* Need evacuating

.. image:: /static/socialisation/show_people.png
   :align: center

.. note:: You can see that the Impact function below ´Might´ automatically
   changes depending on the layers added

5. Lets run this scenario first - :guilabel:`Click` Run at the bottom right
   hand corner of the |project_name| panel.

.. image:: /static/socialisation/page_28_2.jpg
   :align: center

A new layer should appear in the layer panel called ´Population which needs
evacuating´ and in the |project_name| Panel, inside the main window you will
see text and statistics, lets explore this further.

 .. image:: /static/socialisation/inasafe_print2.jpg
   :align: center

In this scenario there are 1,109,000 people that could be exposed to more
than 1 meter of water, it is assumed that all of these people will need to
evacuate their homes.

The Minimum needs, is calculated using the above evacuation number to
estimate the amount of food, water and other products that the refugees will
need to survive.

Action list: designed to make disaster managers think about what they need
to do to prepare for the event.

.. note:: explains the total people in the map canvas,
   when evacuation is needed,  and source of the minimum needs assessment.

Source of the Hazard and Population Datasets

Statistical breakdown of the number of females, and added minimum needs for
women hygiene and pregnant women.

Statistical breakdown of Youth, Adults and Elderly.

Print Results
.............

6. :guilabel:`Click` the print button at the bottom the inasafe panel

.. image:: /static/socialisation/inasafe_print3.jpg
   :align: center

7. Navigate to where you would like to save the pdf, :guilabel:`Click` save

.. image:: /static/socialisation/inasafe_result.jpg
   :align: center

Two PDFs will be generated

.. note:: The result provides a map and a table of information about the impact.

.. image:: /static/socialisation/people_in_need_of_evacuation.jpg
   :align: center

**Help is needed to reconstruct the InaSAFE print output to be more
benefical to disaster managers**

.. image:: /static/socialisation/people_in_need_of_evacuation_table.jpg
   :align: center

**If you get time during this course please proved us with your ideas on how
the print map and table should look!**

Changing threshold
..................

What if the disaster manager has decided that actually anyone in more than
80cm of water should be evacuated?

8. :guilabel:`Click` the impact function editor button (the pencil icon next
   to ´Need Evacuation´)

.. image:: /static/socialisation/page_31.jpg
   :align: center

9. Type 0.8 next to Thresholds

.. image:: /static/socialisation/page_31_2.jpg
   :align: center

10. :guilabel:`Click` OK

11. :guilabel:`Click` the Run button

12. How many people need to be evacuated

Answer
......

13. :guilabel:`Click` |project_name| Print, save as ´people in need of
    evacuation above 80cm´

14. Before moving onto buildings, lets turn some layers off. In your Layer
    panel you will now have 5 layers, we are going to uncheck everything but:

* a flood similar to the 2007 Jakarta event
* buildings

.. image:: /static/socialisation/page_31_3.jpg
   :align: center

Buildings Affected
------------------

15. Check that buildings is in the drop down menu under ´How Many´

16. :guilabel:`Click` on the arrow, as you can see you can not
    :guilabel:`Select` people, as we have uncheck it in the layer panel

.. image:: /static/socialisation/page_31_4.jpg
   :align: center

.. note:: If you want to be able to Select layer that are not
   checked, there is an option in the InaSAFE options window that can
   be turned off. We will go through the option menu later in the training.

17. :guilabel:`Click` Run

.. image:: /static/socialisation/inasafe_print.jpg
   :align: center

In this scenario approximately 796 buildings could be effected out of 13,
629 buildings.

Due to the provincial BPBD work in OpenStreetMap they have mapped all
important building (and then sum).

Important buildings are defined as:

* Clinic
* Fire Stations
* Government
* Hospitals
* Place of Worship
* Police
* Schools
* Sports Centres

A different set of Actions have been identified to relate to structures.

Assume affected in above 1 meter of water
Source of the Hazard and Population Datasets


18. :guilabel:`Click` |project_name| Print, save accordingly

Optional - Change the threshold to 0.8
......................................

19. Check that |project_name| has the following in the drop-down boxes

* a flood similar to the 2007 Jakarta event
* buildings
* Be Flooded

20. :guilabel:`Click` on the impact function tool (pencil) and change 1.0 to
    0.8)

21. Run |project_name|

22. Print and save accordingly

Basic Aggregation - Optional
----------------------------

23. :guilabel:`Click` Add vector button .. image:: /static/socialisation/

24. Navigate to the data folder and :guilabel:`Select` |project_name|
    projects/data/district_osm_jakarta.shp

.. image:: /static/socialisation/page_33.jpg
   :align: center

25. :guilabel:`Click` Open

26. :guilabel:`Click` once on the district of Jakarta Layer

.. image:: /static/socialisation/page_33_2.jpg
   :align: center

27. :guilabel:`Click` on the drop down menu for ´Aggregation results by´ and
    :guilabel:`Select` Subdistrict of Jakarta

.. image:: /static/socialisation/page_33_3.jpg
   :align: center

28. Change the threshold back to 1.0 (refer point 7)

29. Run |project_name| again

30. :guilabel:`Click` |project_name| Print, save accordingly

Keywords Editor
---------------

In the next chapter we will explore the keyword editor for the hazard and
exposure layers.

However the Keyword editor for postprocessing is slightly different. You are
able to :guilabel:`Select` an attribute to provide the percentage of females
per aggregation area. If there is no such layer |project_name| defaults at
50% or 0.5.

If you would like more detail please ask at the end of the session

.. image:: /static/socialisation/aggregation_keyword.png
   :align: center

31. Keywords Editor window will pop up, press OK

32. Scroll down the bottom of the results, you will see disaggregation of
the population data and demographics by district.

33. :guilabel:`Click` |project_name| Print, save accordingly

.. image:: /static/socialisation/page_34.jpg
   :align: center
