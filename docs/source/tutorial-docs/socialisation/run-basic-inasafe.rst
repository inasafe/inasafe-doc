Run basic InaSAFE
=================

Introduction
------------

In this chapter you will run InaSAFE in Jakarta to determine the impact of a flood model on Jakarta’s population and buildings. 

1. Open Jakarta_floods.qgs - File/Open Project... ,

2. Click on “browse” navigate to *InaSAFE projects* and select *Jakarta_floods*, click open and then open again
 
  

People need evacuating
----------------------

3. As you can see the InaSAFE panel has the first three drop down menus filed in already

* a flood similar to the 2007 Jakarta event

* buildings

* Be Flooded

4. Click the arrow next to buildings, select people, it now should have:

* a flood similar to the 2007 Jakarta event

* people

* Need evacuating

.. note:: You can see that the Impact function below “Might” automatically changes depending on the layers added

5. Lets run this scenario first - Click Run at the bottom right hand corner of the InaSAFE panel

A new layer should appear in the layer panel called “Population which needs evacuating” and in the InaSAFE Panel, inside the main window you will see text and statistics, lets explore this further.
 
 
In this scenario there are 1,109,000 people that could be exposed to more than 1 meter of water, it is assumed that all of these people will need to evacuate their homes.

The Minimum needs, is calculated using the above evacuation number to estimate the amount of food, water and other products that the refugees will need to survive.

Action list: designed to make disaster managers think about what they need to do to prepare for the event.
 
.. note:: explains the total people in the map canvas, when evacuation is needed,  and source of the minimum needs assessment

Source of the Hazard and Population Datasets
 
Statistical breakdown of the number of females, and added minimum needs for women hygiene and pregnant women.
 
Statistical breakdown of Youth, Adults and Elderly.
 
 
 
 
Print Results
.............

6. Click the print button at the bottom the inasafe panel
 
7. Navigate to where you would like to save the pdf, click save

Two pdfs will be generated

.. note:: The result provides a map and a table of information about the impact.

**Help is needed to reconstruct the InaSAFE print output to be more benefical to disaster managers**

**If you get time during this course please proved us with your ideas on how the print map and table should look!**

Changing threshold
..................

What if the disaster manager has decided that actually anyone in more than 80cm of water should be evacuated?

8. Click the impact function editor button (the pencil icon next to “Need Evacuation”)
 
9. Type 0.8 next to Thresholds

10. Click OK

11. Click the Run button
 
12. How many people need to be evacuated

Answer__________________________
................................

13. Click InaSAFE Print, save as “ people in need of evacuation above 80cm”

14. Before moving onto buildings, lets turn some layers off. In your Layer panel you will now have 5 layers, we are going to uncheck everything but:

* a flood similar to the 2007 Jakarta event

* buildings
 

Buildings Affected
------------------

15. Check that buildings is in the drop down menu under “How Many”

16. Click on the arrow, as you can see you can not select people, as we have uncheck it in the layer panel

.. note:: If you want to be able to select layer that are not checked, there is an option in the InaSAFE options window that can be turned off - We will go through the option menu later in the training.

17. Click Run
 
In this scenario approximately 796 buildings could be effected out of 13,629 buildings.
 
Due to the provincial BPBD work in OpenStreetMap they have mapped all important building (and then sum).

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
 
 
18. Click InaSAFE Print, save accordingly

Optional - Change the threshold to 0.8
......................................

19. Check that InaSAFE has the following in the drop-down boxes

* a flood similar to the 2007 Jakarta event

* buildings

* Be Flooded

20. Click on the impact function tool (pencil) and change 1.0 to 0.8)

21. Run InaSAFE

22. Print and save accordingly

Basic Aggregation - Optional
----------------------------

23. Click Add vector button

24. Navigate to the data folder and select InaSAFE projects/data/district_osm_jakarta.shp

25. Click Open
 
26. Click once on the district of Jakarta Layer

27. Click on the drop down menu for “Aggregation results by” and select Subdistrict of Jakarta

28. Change the threshold back to 1.0 (refer point 7)

29. Run InaSAFE again

30. Click InaSAFE Print, save accordingly

31. Keywords Editor window will pop up, press OK

32. Scroll down the bottom of the results, you will see disaggregation of the population data and demographics by district.

33. Click InaSAFE Print, save accordingly
