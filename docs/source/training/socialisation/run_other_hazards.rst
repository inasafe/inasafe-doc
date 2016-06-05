.. image:: /static/training/socialisation/inasafe_logo.*

.. _run_other_hazards:

Other Hazards
=============

Introduction
------------

|project_name| was designed to predict the result of a disaster by giving us the potential impact on buildings, populations and roads based on specific scenarios.
From previous exercises, we have learned how to use Basic and Intermediate |project_name| functionality.
We also learned about using tools in |project_name| such as define keywords, configure minimum needs and area analysis,
using aggregation as well as many others.

In previous exercises, we used the "flooding in Jakarta" scenario and related data to learn |project_name| functionality.
In addition to floods, |project_name| impact analyses can be run for many hazard types including earthquakes, tsunamis and volcanos.
In this exercise, we will explore and learn to run other hazard scenarios in |project_name| using |project_name| dock and |project_name| Function Centric Wizard.
Last but not least, we will also use the Generic Impact Function.

Learning objectives:
--------------------

To improve the participant’s understanding of how to use |project_name| to run impact analyses for hazards other than floods.
By the end of this exercise, participants will be able to:

- Run |project_name| with other hazards such as Earthquakes, Tsunamis and Volcanos;

- Be able to read metadata and assign keywords to hazard data;

- Be able to use the |project_name| dock and the |project_name| Function Centric Wizard; and

- Be able to use the Generic Impact Function and understand how to use it to work with their own data.

Data for This Exercise:
-----------------------

The data used for this exercise is the same as that used in previous exercises. The data can be downloaded from |project_name| `Training Data Packages <http://data.inasafe.org/TrainingDataPackages/>`__
Once the data has been downloaded, we will use the following QGIS project file and spatial data:

- Padang.qgs

- Maumere.qgs

- Sinabung_Hazard_Map_2015_WGS84.shp

- Sinabung_buildings_WGS84.shp

- NGK_Landslide_Vulnerability_WGS84.shp

- NGK_Buildings_WGS84.shp

- NT_Population_WGS84.tiff

1. Run |project_name| for Earthquake
------------------------------------

1.1 Run |project_name| for Building
...................................

a. Open Project
^^^^^^^^^^^^^^^

Indonesia’s location on the edges of the Pacific, Eurasian, and Australian tectonic plates makes it not only a site of numerous volcanoes but also frequent earthquakes.
The hazard layer we are going to use for this example has been provided by Badan Geologi and AIFDR, Australian Government and describes the shaking or Modified Mercalli Intensity (MMI) Scale.

This particular scenario is a modelled version of the 2009 Padang earthquake. Please open QGIS project file :file:`Padang.qgs` from the :file:`InSAFE Training Data > West Sumatera` folder. Once opened, you will see the below :

.. image:: /static/training/socialisation/other_hazard_01.*
   :align: center

In the |project_name| dock, note that the |project_name| form is still empty. It means that your hazard and exposure data does not yet have keywords assigned.
Therefore, you must first define keywords for each dataset in the project.

To define keywords, please click on the :guilabel:`Keywords Creation Wizard` icon and follow the instructions provided. 
You can refer back to the :ref:`Run Intermediate InaSAFE <run_intermediate_inasafe>` module for step-by-step instructions.
Once you have finished defining keywords for each layer, your |project_name| form should look like this :

.. image:: /static/training/socialisation/other_hazard_03.*
   :align: center

b. Run |project_name|
^^^^^^^^^^^^^^^^^^^^^

Once your |project_name| dock appears the same as the above image, you are ready to run an earthquake analysis on buildings.
It poses the question “In the event of an **Earthquake in Padang 2009**", how many **buildings** might **be affected?**.
Click :guilabel:`Run` on the bottom right corner in your |project_name| Dock. If everything was set up correctly, you should get a result in the dock area after a few seconds, and a new map layer should be added to the map.
The new layer is named **Estimated Buildings Affected**.

.. image:: /static/training/socialisation/other_hazard_04.*
   :align: center


c. Interpret the Results
^^^^^^^^^^^^^^^^^^^^^^^^

Let’s take a look at the new data layer generated from |project_name|.

- Zoom in to any area in the Map Canvas

- There will be three new different colours generated from |project_name| (yellow, orange, and red).

- The red buildings are located in highly affected areas which have MMI Values greater than 8 MMI. The orange buildings are located in medium affected areas which have MMI between 6 to 8 MMI while the yellow buildings are considered located in areas with low impact which have MMI Values of less than 6 MMI.

- Click :guilabel:`Estimated buildings affected` in the layer list to select it, click the :guilabel:`Identify Feature` tool, and then click on building to view attributes of the building.

.. note:: Default Threshold  for Earthquake are 6 MMI for Low Threshold, 7 MMI for Medium and 8 MMI for high threshold. You can change the threshold of MMI Value for each affected area before run |project_name|. Please click Options In your |project_name| Dock. This configuration will make your result different with Run |project_name| using default threshold.

.. image:: /static/training/socialisation/other_hazard_06.*
   :align: center

In the |project_name| panel we now see the impact summary. Details are explained below.

.. image:: /static/training/socialisation/other_hazard_05.*
   :align: center

- **Hazard Category:** divides the results into several categories based on the threshold set in the hazard analysis. In this impact summary, |project_name| divides the impact buildings into three categories based on MMI.

- **Building type:** divides the exposed buildings into several categories based on the building type attribute for each building. In this impact summary, |project_name| breaks down the results into a more detailed report by looking at each type of the building.

- **Action checklist:** designed to make disaster managers think about what they need to do/discuss when planning for a similar event in the future.

- **Notes and assumptions:** provides details about the input data and any limitations or assumptions in the analysis or report summary. In this example, it explains why buildings are said to be inundated, wet and dry.

- **Detailed aggregation categorical report:** statistical breakdown of the number of results. This example shows the count of important infrastructure. When you choose to use an aggregation layer with your analysis (we will do this later) this table will show the number of buildings by aggregation boundary.

- **Hazard details:** explanation of where the hazard data come from

- **Exposure detail:** explanation of where the exposure come from

1.2 Run |project_name| for Population
.....................................

We are now ready to run our second |project_name| analysis using earthquake data in Padang. We will be working with the same earthquake data again, but this time looking at the number of impacted people in a specific area.
If you finished defining keywords, these data should have keywords assigned so you will be ready to run |project_name|.

In QGIS, turn off the **Buildings** and **estimated buildings affected** (the layers generated from |project_name| analysis and turn ON the population layer).
Because we want to look at the number people who might be killed or displaced in a specific area, we also need to turn ON **the Village** layer in QGIS. 
This layer will be used as an aggregation layer that can show us the result for each administrative area. 
If you forget the steps needed to define a layer as an aggregation, please refer to the :ref:`Run Intermediate InaSAFE. <run_intermediate_inasafe>`

Confirm that the |project_name| panel on the right side is set to query how many people might die or be displaced :

- Earthquake in Padang 2009

- People

- Die or be displaced according Pager mode

- Village

.. note::This particular impact function was developed in Italy in November 2013 during a code sprint.

Your |project_name| form should appear like the below screenshoot:

.. image:: /static/training/socialisation/other_hazard_07.*
   :align: center

a. Run |project_name|
^^^^^^^^^^^^^^^^^^^^^

If everything is setup correctly, the |project_name| dock should show that you are ready to run a flood analysis on population.
It poses the question “In the event of an **Earthquake in Padang (2009)**, how many **people** might **die or be displaced according to the Pager Model**?” 
In this analysis we still use Shakemap data which has values from 6 – 8 MMI. If you want to see the minimum relief needs that should be provided based on the result, you can click :guilabel:`Options` and select :guilabel:`Minimum Needs`.

You can refer to the `Run Basic InaSAFE <http://docs.inasafe.org/en/training/socialisation/run_basic_inasafe.html/>`__ to learn more about the basis of default minimum needs in |project_name|
or if you want edit an item or add new minimum needs, you can refer to the `Minimum Needs Configuration manuals <http://docs.inasafe.org/en/user-docs/application-help/minimum_needs.html#minimum-needs>`__.
After everything is setup accordingly, click :guilabel:`Run` to process the new scenario.

b. Interpret The Result
^^^^^^^^^^^^^^^^^^^^^^^

If everything was set up correctly, you should get a result in the dock area after a few  seconds, and a new map layer should be added to the map.
The new impact layer will be called Estimated displaced population per cell. Let’s explore the result again to help you better understand its meaning :

- Turn off the **Estimated building affected** layer and drag the Estimated displaced population per cell above Earthquake in Padang 2009.

- Zoom in to the area you choose.

- Select Estimated displaced population per cell in the layer list and use the :guilabel:`Identify Feature` tool again to select a pixel (square) in the map canvas.

- In the screenshot below, clicking on one of the brown pixels displays a value of 98.94451, which means there are approximately 98 people in this one pixel (square) whom might die or be displaced.

.. image:: /static/training/socialisation/other_hazard_08.*
   :align: center

In the |project_name| panel we now see the impact summary. The details are explained below.

.. image:: /static/training/socialisation/other_hazard_09.*
   :align: center

- **Population needing evacuation:** |project_name| estimates the number of affected people in the analysis area. It is assumed that all of these people will need to be evacuated.

- **Needs per week:** are calculated numbers of food, water and other products needed by evacuated people on a weekly basis.

- **Action checklist:** designed to make disaster managers think about what they need to do/discuss when planning for a similar event in the future.

- **Notes and assumptions:** provides details about the input data and any limitations or assumptions in the analysis or report summary. In this example, it explains the total number of people in the analysis area and the source of minimum needs.

- **Detailed gender and age report:** provides a breakdown of the number of affected people by age (youth, adults and elderly) and gender based on the default world population demographics and calculates the minimum needs for women’s hygiene and pregnant women. If you using aggregation layer, the result will be broken down based on administrative area.

.. image:: /static/training/socialisation/other_hazard_10.*
   :align: center

2. Run |project_name| for Tsunami
---------------------------------

The 1992 Flores earthquake occurred on December 12, 1992 on the island of Flores in Indonesia. With a magnitude of 7.8, it was the largest and also the deadliest earthquake in 1992.
This earthquake triggered another hazard in that area a tsunami in Maumere, Flores.

Next, we will run another scenario in |project_name| using Tsunami Hazard Model.
It is a modelled version of a Magnitude 8.1 earthquake generating a tsunami which impacts Maumere.

2.1 Open Project
.................

Please open the QGIS project file :file:`Maumere.qgs` from the :file:`InaSAFE Training Data
> Maumere` folder. Once opened, the project should appear similar to the screenshot below:

.. image:: /static/training/socialisation/other_hazard_11.*
   :align: center

You will see in the |project_name| dock that keywords for each layer have not yet been defined. As before, we use the :guilabel:`Keyword Creation Wizard` icon to define keyword. For detailed steps, please reference the :ref:`Run Intermediate InaSAFE. <run_intermediate_inasafe>` module

2.2 Run |project_name|
......................

Once you have finished defining keywords for each layer, your |project_name| form should look like this :

.. image:: /static/training/socialisation/other_hazard_12.*
   :align: center

In this scenario we will use Buildings as an exposure and Village Boundary as an aggregation layer. Once your |project_name| form appears the same as the above screenshoot,
click :guilabel:`Run` at the bottom right corner in your |project_name| dock.

2.3 Interpret the Result
........................

If everything was set up correctly, you should get a result in the dock area after a few  seconds, and a new map layer should be added to the map.
The new impact layer will be called Estimated buildings affected.
Let’s explore the result again to help you understand more.

- Zoom in to any area you choose

- Here we have zoomed in to a location in Maumere. There will be five new different colours generated from |project_name| (green, yellow, orange, blood orange, and red).

- The red buildings are situated in area where the depth of tsunami inundation is more than 8 metres; the blood orange buildings are situated in area where the depth of tsunami inundation is between 3.1 and 8 metres; the orange buildings are situated in area where the depth of tsunami inundation is 1.3 and 3.0 metres; the yellow buildings are situated in area where the depth of tsunami inundation is between 0.1 and 1 metres; and the green building considered unaffected as they are situated in water less than the threshold of 0.1 metre.

.. image:: /static/training/socialisation/other_hazard_13.*
   :align: center

- Click **Estimated building affected** in the layer list to select it and click :guilabel:`Identify Feature` tool and then click on building to know what attribute of the building.

.. image:: /static/training/socialisation/other_hazard_14.*
   :align: center

Here we clicked on one of the brown pixels and find that there is a value of depth 0.929329631. This means that the building is located in an affected area which is predicted to be flooded with 92 cm of water.

In the |project_name| panel we now see the impact summary. Detalils are explained below.

.. image:: /static/training/socialisation/other_hazard_15.*
   :align: center

- **Hazard Category**: divides the results into several categories based on the threshold set in the hazard analysis. In this impact summary, |project_name| divides the impact buildings into three categories: number of building inundated (affected by water deeper than the analysis threshold), number of wet building (affected by tsunami's impact but not flooded as deep as the analysis threshold), and number of dry buildings (not affected by any tsunami impact)

- **Building type**: divides the exposed buildings into several categories based on the building type attribute for each building.

- **Action checklist**: designed to make disaster managers think about what they need to do/discuss when planning for a similar event in the future.

- **Notes and assumptions**: provides details about the input data and any limitations or assumptions in the analysis or report summary. In this example, it explains why building are predicted to be inundated, wet and dry.

- **Detailed building type report**: statistical breakdown of the results. This example shows the count of important infrastructure. When you choose to use an aggregation layer with your analysis (we will do this later) this table will show the number of buildings by aggregation boundary.

.. image:: /static/training/socialisation/other_hazard_16.*
   :align: center

- **Hazard details**: explanation of where the hazard data come from

- **Exposure detail**: explanation of where the exposure come from

The results show the buildings that will be affected by tsunami starting from 1 metre. What if the disaster manager decides that buildings in 80 cm of water are also considered inundated? You can change the water depth threshold to see the result, refer to the `Run Basic InaSAFE <http://docs.inasafe.org/en/training/socialisation/run_basic_inasafe.html/>`__ module.

..note:: InaSAFE Tsunami Impact Function is very similar with Flood, but due to the force of tsunami waves, the maximum depth of water that would affect people and infrastructure is shallower.

3. Run |project_name| for Volcano
---------------------------------

Indonesia has many volcanoes, and most of them are still active today. In fact, one of the most frequent disasters in Indonesia is volcano eruptions. There are 129 active volcanoes across the country,
and it is valuable to know how many people and how much infrastructure is within a certain perimeter of the vent.

|project_name| also has an impact function for volcano eruption scenarios. This function can run some type of
hazard data. For detail information about the |project_name| volcano hazard function, please look at the `Hazard Data Section <http://docs.inasafe.org/en/training/socialisation/datasets.html/>`__ 

In this section we will be using the Sinabung volcano hazard from the National Disaster Management Agency (BNPB) as
hazard data and building from OpenStreetMap as exposure data. For this run, we will using
Impact Function Centric Wizard (IFCW). For more information about IFCW you can refer to 
`Key concepts in disaster management planning with InaSAFE <http://docs.inasafe.org/en/training/socialisation/inasafe_concepts.html>`__ 

3.1 Open Project
................

Please open a new QGIS project in order to use IFCW to run this project.
You new QGIS project should look like this:

.. image:: /static/training/socialisation/other_hazard_17.*
   :align: center

3.2 Run |project_name|
......................

To use the **Impact Function Centric Wizard**, please click :guilabel:`Impact Fuction Centric Wizard` icon.

.. image:: /static/training/socialisation/other_hazard_18.*
   :align: center

After clicking that icon, you will see the following dialogue box appear:

.. image:: /static/training/socialisation/other_hazard_19.*
   :align: center

In the box above, there are some fields that help us select the scenario to use.
Green fields mean those scenarios are available and ready to run in |project_name|. Grey fields means those scenarios are not available in |project_name| at the moment.

Because we want to run Volcano with building in this session, please click :guilabel:`Field Volcano and Structure`. The resulting dialogue box appears like this:

.. image:: /static/training/socialisation/other_hazard_20.*
   :align: center

You can click :guilabel:`Next` and follow the instructions in the IFCW box.

Hazard Data that we want to use for this scenario can be found in
:file:`InaSAFE Training Data > Sinabung > Hazard Data` folder.
Please select :file:`Sinabung_Hazard_Map_2015_WGS84.shp` . Building Exposure data can be found in :file:`InSAFE Training Data > Sinabung > Exposure Data` folder.
Please select :file:`Sinabung_buildings_WGS84.shp` .

..note:: The differences between Volcano and Volcanic Ash can be seen in
  `Hazard Data Section <http://docs.inasafe.org/en/training/socialisation/datasets.html/>`_ and for detail explanation
  about type of data you can be found in
  `Key concepts in disaster management planning with |project_name| <http://docs.inasafe.org/en/training/socialisation/inasafe_concepts.html/>`_.

If you have followed the instruction in IFCW box, before running |project_name| you should see the final form below:

.. image:: /static/training/socialisation/other_hazard_21.*
   :align: center

If your IFCW box looks like the screenshot above, click :guilabel:`Run` and wait for analysis processing until a result box appears.

.. image:: /static/training/socialisation/other_hazard_22.*
   :align: center

3.3 Interpret the Result
........................

Once you have finished running the analysis, you will see the result has new layer named
“Buildings Affected by each Hazard Zone” . This layer will show you which buildings are affected for each hazard zone.
There will be three new colours of building generated from |project_name| (green, orange, and red).

The blood orange buildings mean these buildings are located in a Low Risk Zone (Risk Zone 1), the red buildings mean these buildings are located in an Intermediate Risk Zone (Risk Zone 2) and dark red buildings are considered situated in a High Risk Zone (Risk Zone 3) of Sinabung Volcano.

.. image:: /static/training/socialisation/other_hazard_23.*
   :align: center

In the |project_name| result box, we now see the impact summary. It is very similar to the |project_name| Dock. Details are explained below.

.. image:: /static/training/socialisation/other_hazard_24.*
   :align: center


- **Hazard Category**: divides the results into several categories based on the threshold set in the hazard analysis. In this impact summary, |project_name| divides the impacted buildings into three categories for each hazard zone of Sinabung Volcano.

- **Building type**: divides the exposed buildings into several categories based on the building type attribute for each building.

- **Action checklist**: designed to make disaster managers think about what they need to do/discuss when planning for a similar event in the future.

- **Notes and assumptions**: provides details about the input data and any limitations or assumptions in the analysis or report summary. In this example, it explains why buildings are predicted to be inundated, wet, or dry.

- **Detailed building type report**: statistical breakdown of the number of results. This example shows the count of important infrastructure. When you choose to use an aggregation layer with your analysis (we will do this later) this table will show the number of buildings by aggregation boundary.

You have now run |project_name| for a volcano scenario using the Impact Function Centric Wizard (IFCW).
Quite different than the |project_name| Dock, this tool is designed to help a user run |project_name| more easily without needing to open all the required data one by one in QGIS. IFCW provides precise guidance and detail about
what actions should be taken step by step until the scenario is ready to run. This tool is very useful, especially for |project_name| user who are less familiar with QGIS and Spatial Data.

4. Generic Impact Function in |project_name|
---------------------------------------------

|project_name| can run analyses for multiple hazards, using scenarios that we set up based on
data availability. These scenarios include five types of hazards : floods, earthquakes, volcanos,
volcanic ash and tsunamis. What if our hazard scenario is not included in this list (for example, a land slide or drought). To solve this problem, |project_name| provides a tool called the **Generic Impact Function** that can run analyses for any hazard not available via a specific Scenario Impact Function.

4.1 Open Project
.................

Next, we will explore this tool using a landslide hazard in Nagekeo, East Nusa Tenggara with building and population data
for each scenario. Please open the QGIS project file :file:`Nagekeo.qgs` from 
the :file:`InSAFE Training Data > Nagekeo` folder. Once opened, the project should look like the screenshot below:

.. image:: /static/training/socialisation/other_hazard_25.*
   :align: center

In the |project_name| dock, the |project_name| form still appears empty. This means that your hazard and
exposure data lacks keywords. Before proceeding, you should define keywords for each dataset in this project.

To define a keyword, please click on the :guilabel:`Keywords Creation Wizard` icon

.. image:: /static/training/socialisation/other_hazard_02.*
   :align: center

and follow the instructions. You can refer to the :ref:`Run Intermediate InaSAFE. <run_intermediate_inasafe>` if you need additional assistance.
Once you finish defining keyword for each layer, your |project_name| form should appear like the below screenshot:

.. image:: /static/training/socialisation/other_hazard_35.*
   :align: center

4.2 Run |project_name| for Building
...................................

a. Run |project_name|
^^^^^^^^^^^^^^^^^^^^^

Your |project_name| Dock now poses the question “In the event of **Landslide Hazard Zone**,how many **buildings** might **be affected**?" 
Click :guilabel:`Run` on the bottom right corner in your |project_name| Dock.
If everything was set up correctly, you should get a result in the dock area after a few seconds, and a new map layer should be added to the map. The new layer will be named “Buildings Affected by each hazard zone”.

.. image:: /static/training/socialisation/other_hazard_26.*
   :align: center

.. image:: /static/training/socialisation/other_hazard_27.*
   :align: center

b. Interpret The Result
^^^^^^^^^^^^^^^^^^^^^^^

Let’s take a look at the new data layer generated from |project_name|:

- Zoom in to an area in the Map Canvas

- There will be three new colours generated from |project_name| (red, green, blue and purple).

- The red buildings are located in a high vulnerability zone, the orange buildings are located in moderate vulnerability zone, green buildings are located in a Low Landslide Vulnerability Zone.

- Click building affected in the layer list to select it. Next, click the :guilabel:`Identify Feature` tool and then click on a building to view attributes of the building.

.. image:: /static/training/socialisation/other_hazard_28.*
   :align: center

In the |project_name| panel we now see the impact summary. Details are explained below.

.. image:: /static/training/socialisation/other_hazard_29.*
   :align: center

- **Hazard Category**: divides the results into three categories based on the hazard data classification area. In this impact summary, |project_name| divides the impacted buildings into High, Moderate, and Low Landslide vulnerability zone.

- **Building type**: divides the exposed buildings into several categories based on the building type attribute for each building. In this impact summary, |project_name| breaks down the results into a more detailed report by looking at each type of the building.

- **Action checklist**: designed to make disaster managers think about what they need to do/discuss when planning for a similar event in the future.

- **Notes and assumptions**: provides details about the input data and any limitations or assumptions in the analysis or report summary.

- **Detailed aggregation categorical report**: statistical breakdown of the number of results. This example shows a count of important infrastructure. When you choose to use an aggregation layer with your analysis (we will do this on population) this table will show the number of buildings grouped by aggregation boundary.

- **Hazard details**: explanation of where the hazard data come from

- **Exposure detail**: explanation of where the exposure come from

4.3 Run |project_name| for Population
.....................................

a. Run |project_name|
^^^^^^^^^^^^^^^^^^^^^

Turn off the Buildings Affected by each hazard zone (the layers generated from |project_name| analysis and
turn ON the **People** layer. Because we want to look at the number of people who might die or be displaced in
a specific area, we also need to turn ON the **Village** layer in QGIS. This layer will be used as an aggregation layer that
can show us results grouped by administrative boundary.

If you forget the steps to define and aggregation layer, refer to the :ref:`Run Intermediate InaSAFE. <run_intermediate_inasafe>` section.
Edit the question form in the |project_name| Dock so that it appears similar to the below screenshot:

.. image:: /static/training/socialisation/other_hazard_30.*
   :align: center

Next, click :guilabel:`Run` to start the analysis.

b. Interpret the Result
^^^^^^^^^^^^^^^^^^^^^^^

If everything was set up correctly, you should get a result in the dock area after a few  seconds,
and a new map layer should be added to the map. The new impact layer will be called **People Impacted by Each Hazard Zone**.
Let’s explore the result again to help you understand more.

- Zoom in to any area.

- Select People Impacted by Each Hazard Zone in the layer list and use the :guilabel:`Identify Feature` tool again to select a pixel (square) in the map canvas.

Here we clicked on one of the yellow pixels and see a value of 220.283, which means
there are approximately 220 people in this one pixel (square) who might be impacted.

.. image:: /static/training/socialisation/other_hazard_31.*
   :align: center

.. image:: /static/training/socialisation/other_hazard_32.*
   :align: center   

In the |project_name| panel we now see the impact summary. The details are explained below.

.. image:: /static/training/socialisation/other_hazard_33.*
   :align: center

- **Population needing evacuation**: |project_name| estimates the number of affected people in the analysis area. It is assumed that all of these people will need to be evacuated.

- **Needs per week**: are calculated numbers of food, water and other products that are needed by evacuated people on a weekly basis.

- **Action checklist**: designed to make disaster managers think about what they need to do/discuss when planning for a similar event in the future.

- **Notes and assumptions**: provides details about the input data and any limitations or assumptions in the analysis or report summary. In this example, it explains the total number of people in the analysis area and the source of minimum needs.

- **Detailed gender and age report**: provides a breakdown of the number of affected people by age (youth, adults and elderly) and gender based on the default world population demographics and calculates the minimum needs for women’s hygiene and pregnant women. If you using aggregation layer, the result will break down the result based on administrative boundaries.

.. image:: /static/training/socialisation/other_hazard_34.*
   :align: center

.. note:: In the result of |project_name|, Action Checklist and Notes might be unrelated with hazard that we runned.
   For instance, if we run drought hazard the action checklist might be has some topics such as how many building closed, or people die or displaced. Those topics not really related with drought. 

Summary
-------

Congratulation! You have now learned to use most of |project_name|'s functionality. You can run analyses for specific hazard using tools such as
the Impact Function Centric Wizard (IFCW) and the Generic Impact Function which will make using |project_name| easier.

Now, to become an expert user of |project_name|, try utilizing all those tools that you explored in this module using your own scenarios and data, and practice interpreting the results.