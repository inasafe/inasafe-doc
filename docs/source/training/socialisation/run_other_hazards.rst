.. _run_other_hazards:

.. image:: /static/training/socialisation/inasafe_logo.*

Other Hazards
=============

Introduction
------------

|project_name| was designed to give us result of disaster impact both for building, population and road based on specific scenario.
From previous exercise, we have learned about Basic |project_name| and also Intermediate |project_name|.
We also learn about using tools in |project_name| such as define keywords, configure minimum needs and area analysis,
using aggregation and many more.

In previous exercise, we using Flood in Jakarta as a data and scenario to learn those things.
However, |project_name| can be runned not only flood but many disasters such as earthquake, tsunami and volcano.
Therefore,in this exercise we will explore and learn to run other hazard scenario in |project_name| using |project_name| dock and |project_name| Function Centric Wizard.
Last but not least, we also using Generic Impact Function in |project_name|.

Learning objectives:
--------------------

To improve participant’s understanding of how to use |project_name| to run impact analysis for hazards other than flood.
By the end of this exercise, participants will be able to:

- Run |project_name| with other hazards such as Earthquake, Tsunami and Volcano;

- Be able to read metadata and assign keywords to hazard data;

- Be able to use the |project_name| dock and the |project_name| Function Centric Wizard; and

- Be able to use the Generic Impact Function and understand how to use it to work with their own data.

Data for This Exercise:
-----------------------

The data for same with that we use in previous exercise. The data can be downloaded from |project_name| Training Data Packages. 
If you already have it, we will use the following QGIS project file and spatial data:

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

This particular scenario is a modelled version of the 2009 Padang earthquake. Please open QGIS project file :file:`Padang.qgs` from the :file:`InSAFE Training Data > West Sumatera` folder. The project looks something like this:

.. image:: /static/training/socialisation/other_hazard_01.*
   :align: center

You will see in |project_name| dock, |project_name| form still empty. It means that your data both hazard and exposure data does not have keyword yet.
Therefore, you have to define keyword first for each data in this project.

To define keyword, please click on :guilabel:`Keywords Creation Wizard` icon and follow the further instruction. 
You can refer back to `Run Intermediate InaSAFE <http://docs.inasafe.org/en/training/socialisation/run_intermediate_inasafe.html/>`__.
If you finished define keywords for each layer, your |project_name| form should look like this :

.. image:: /static/training/socialisation/other_hazard_03.*
   :align: center

b. Run |project_name|
^^^^^^^^^^^^^^^^^^^^^

If your |project_name| dock already have same look with image above, it means that you are ready to run a earthquake analysis on buildings.
It poses the question “In the event of **Earthquake in Padang 2009**", how many **buildings** might **be affected**.
Click :guilabel:`Run` on the bottom right corner in your |project_name| Dock. If everything was set up correctly, you should get a result in the dock area after a few seconds, and a new map layer should be added to the map.
It named **Estimated Buildings Affected**.

.. image:: /static/training/socialisation/other_hazard_04.*
   :align: center

.. image:: /static/training/socialisation/other_hazard_05.*
   :align: center

c. Interpret The Result
^^^^^^^^^^^^^^^^^^^^^^^

Let’s take a look for a while for the new data layer generated from |project_name|.

- Zoom in to some area in Map Canvas

- There will be three new different colours generated from |project_name| (yellow, orange, and red).

- The red buildings are located in high affected area which has MMI Value greater than 8 MMI, the orange buildings are located in medium affected area which has MMI greater between 6 until 8 MMI while the yellow buildings are considered located in low affected area which has MMI Value less than 6 MMI.

- Click :guilabel:`Estimated building affected` in the layer list to select it and click :guilabel:`Identify Feature` tool and then click on building to know what attribute of the building.

.. note:: Default Threshold  for Earthquake are 6 MMI for Low Threshold, 7 MMI for Medium and 8 MMI for high threshold. You can change the threshold of MMI Value for each affected area before run |project_name|. Please click Options In your |project_name| Dock. This configuration will make your result different with Run |project_name| using default threshold.

.. image:: /static/training/socialisation/other_hazard_06.*
   :align: center

In the |project_name| panel we now see the impact summary. The details of are explained below.

.. image:: /static/training/socialisation/other_hazard_05.*
   :align: center

- **Hazard Category:** divides the results into several categories based on the threshold set in the hazard analysis. In this impact summary, |project_name| divides the impact buildings into three category: number of building affected (building affected by MMI Values threshold)

- **Building type:** divides the exposed buildings into several categories based on the building type attribute for each building. In this impact summary, |project_name| breaks down the results into a more detailed report by looking at each type of the building.

- **Action checklist:** designed to make disaster managers think about what they need to do/discuss when planning for a similar event in the future.

- **Note:** provides details about the input data and any limitations or assumptions in the analysis or report summary. In this example, it explains why building are said to be inundated, wet and dry.

- **Detailed aggregation categorical report:** statistical breakdown of the number of results. In this example is the number of important infrastructure. When you choose to use an aggregation layer with your analysis (we will do this later) this table will show the number of buildings by aggregation boundary.

- **Hazard details:** explanation where the hazard data come from

- **Exposure detail:** explanation where the exposure come from

1.2 Run |project_name| for Population
.....................................

We are now ready to run our second |project_name| analysis using earthquake data in Padang. We will be working with same earthquake data again, but this time to look at the number of impacted people in specific area.
If you finished define keywords, these data should already have keywords assigned so you will be ready to run the |project_name|.

In the QGIS, turn off the **Buildings** and **estimated building affected** (the layers generated from |project_name| analysis and turn ON population layer).
Because we want to look number people who might be die or displaced in specific area, we also need to turn ON **Village** layer in QGIS. 
This layer will be used as an aggregation layer that can show us the result by administrative boundary. 
If you forget the steps how to define a layer as an aggregation, you can see in `Run Intermediate InaSAFE <http://docs.inasafe.org/en/training/socialisation/run_intermediate_inasafe.html/>`__

Confirm that the |project_name| panel on the right side is set to query how many people might die or displaced :

- Earthquake in Padang 2009

- Population

- Die or be displaced according Pager mode

- Village

.. note::This particular impact function was developed in Italy in November 2013 during a code sprint

Your |project_name| form should looking like this :

.. image:: /static/training/socialisation/other_hazard_07.*
   :align: center

a. Run |project_name|
^^^^^^^^^^^^^^^^^^^^^

If everything is setup correctly, the |project_name| dock should show that you are ready to run a flood analysis on population.
It poses the question “In the event of **Earthquake in Padang 2009**, how many **people** might **die or be displaced according Pager Model**?” 
In this analysis we still use Shakemap data which has values from 6 – 8 MMI. If you want to see minimum needs that should be provided based on the result, you can click :guilabel:`Options` and select :guilabel:`Minimum Needs`.

You can see `Run Basic InaSAFE <http://docs.inasafe.org/en/training/socialisation/run_basic_inasafe.html/>`__ to know basis of default minimum needs in |project_name|
or If you want edit item or add new minimum needs , you can refer to `Minimum Needs Configuration manuals <http://docs.inasafe.org/en/user-docs/application-help/minimum_needs.html#minimum-needs>`__.
After everything is setup accordingly click :guilabel:`Run` to process the new scenario.

b. Interpret The Result
^^^^^^^^^^^^^^^^^^^^^^^

If everything was set up correctly, you should get a result in the dock area after a few  seconds, and a new map layer should be added to the map.
The new impact layer will be called Estimated displaced population per cell. Let’s explore the result again to make you understand more about the |project_name| result.

- Turn Off **Estimated building affected** layer and drag the Estimated displaced population per cell above Earthquake in Padang 2009

- Zoom in the area you choose

- Select Estimated displaced population per cell in the layer list and use :guilabel:`Identify Feature` tool again to select a pixel (square) in the map canvas.

- Here we clicked on one of the red maroon pixels and find that there is a value of 98.94451, which means there are approximately 98 people in this one pixel (square) whom might be die or be displaced.

.. image:: /static/training/socialisation/other_hazard_08.*
   :align: center

In the |project_name| panel we now see the impact summary. The details of are explained below.

.. image:: /static/training/socialisation/other_hazard_09.*
   :align: center

- **Population needing evacuation:** |project_name| estimates the number of affected people in the analysis area. It is assumed that all of these people will need to be evacuated.

- **Needs per week:** are calculated numbers of food, water and other products that needed by evacuated people. These needs should be provided weekly.

- **Action checklist:** designed to make disaster managers think about what they need to do/discuss when planning for a similar event in the future.

- **Notes:** provides details about the input data and any limitations or assumptions in the analysis or report summary. In this example, it explains the total people in the analysis area and the source of minimum needs.

- **Detailed gender and age report:** provides a breakdown of the number of affected people by age (youth, adults and elderly) and gender based on the default world population demographics and calculates the minimum needs for women’s hygiene and pregnant women. If you using aggregation layer, the result will break down the number of result based on administrative boundary.

.. image:: /static/training/socialisation/other_hazard_10.*
   :align: center

2. Run |project_name| for Tsunami
---------------------------------

The 1992 Flores earthquake occurred on December 12, 1992 on the island of Flores in Indonesia. With a magnitude of 7.8, it was the largest and also the deadliest earthquake in 1992.
This earthquake triggered another hazard in that area. That hazard was Tsunami in Maumere, Flores.

Now, we will run another scenario in |project_name| using Tsunami Hazard Model.
It is a modelled version of a Magnitude 8.1 earthquake generating a tsunami which impacts Maumere.

2.1 Open Project
.................

Please open QGIS project file :file:`Maumere.qgs` from the :file:`InaSAFE Training Data
> Maumere` folder. The project looks something like this:

.. image:: /static/training/socialisation/other_hazard_11.*
   :align: center

You will see in |project_name| dock the keywords for each layers does not define yet. As we did it before, we using :guilabel:`Impact Function Centric Wizard` icon to define keyword. You can see detail steps in `Run Intermediate InaSAFE <http://docs.inasafe.org/en/training/socialisation/run_intermediate_inasafe.html/>`__

2.2 Run |project_name|
......................

If you finished define keywords for each layer, your |project_name| form should look like this :

.. image:: /static/training/socialisation/other_hazard_12.*
   :align: center

In this scenario we will using buildings as an exposure and village boundary as an aggregation layer. If your |project_name| form already same with picture above,
you can click :guilabel:`Run` at the bottom right corner in your |project_name| dock.

2.3 Interpret the Result
........................

If everything was set up correctly, you should get a result in the dock area after a few  seconds, and a new map layer should be added to the map.
The new impact layer will be called Estimated buildings affected.
Let’s explore the result again to make you understand more about the |project_name| result.

- Zoom in the area you choose

- Here we have zoomed in to a location showing two rivers going through the middle of Jakarta. There will be three new different colours generated from |project_name| (green, orange, and red).

- The red buildings are situated in water greater than one metre, the orange buildings are situated in water between zero and one metre, while the green buildings are considered unaffected as they are situated in water less than the threshold of one metre.

.. image:: /static/training/socialisation/other_hazard_13.*
   :align: center

-  Click **Estimated building affected** in the layer list to select it and click :guilabel:`Identify Feature` tool and then click on building to know what attribute of the building.

.. image:: /static/training/socialisation/other_hazard_14.*
   :align: center

Here we clicked on one of the red maroon pixels and find that there is a value of depth 0.929329631 which means that building located in affected area which has 92 cm of water depth.

In the |project_name| panel we now see the impact summary. The details of are explained below.

.. image:: /static/training/socialisation/other_hazard_15.*
   :align: center

- **Hazard Category**: divides the results into several categories based on the threshold set in the hazard analysis. In this impact summary, |project_name| divides the impact buildings into three category: number of building inundated (building affected by water deep than the analysis threshold), number of wet building (building affected by tsunami impact but not as deep as the analysis threshold), and number of dry building (building that are not affected by any tsunami impact)

- **Building type**: divides the exposed buildings into several categories based on the building type attribute for each building. In this impact summary, |project_name| breaks down the results into a more detailed report by looking at each type of the building.

- **Action checklist**: designed to make disaster managers think about what they need to do/discuss when planning for a similar event in the future.

- **Note**: provides details about the input data and any limitations or assumptions in the analysis or report summary. In this example, it explains why building are said to inundated, wet and dry.

- **Detailed building type report**: statistical breakdown of the number of results. In this example is the number of important infrastructure. When you choose to use an aggregation layer with your analysis (we will do this later) this table will show the number of buildings by aggregation boundary.

.. image:: /static/training/socialisation/other_hazard_16.*
   :align: center

- **Hazard details**: explanation where the hazard data come from

- **Exposure detail**: explanation where the exposure come from

The results show the buildings that will be affected by flood water 1 m deep. But what if the disaster manager decides that buildings in 80 cm of water are also flooded? You can change the water depth threshold. 
To see the steps to change water depth threshold, you can refer back to `Run Basic InaSAFE <http://docs.inasafe.org/en/training/socialisation/run_basic_inasafe.html/>`__

3. Run |project_name| for Volcano
---------------------------------

Indonesia has many volcanoes which most of them still active until now. There are 129 active volcanoes in Indonesia,
and it is valuable to know how many people and how much infrastructure is within a certain perimeter of the vent.
Moreover, one of the most frequent disaster in Indonesia is volcano eruption.

|project_name| also has impact function that can run Volcano based on specific scenario. This function can run some type of
hazard data. For detail information about|project_name| volcano hazard, please look at `Hazard Data Section <http://docs.inasafe.org/en/training/socialisation/datasets.html/>`__ 

In this section we will be using Sinabung volcano hazard from National Disaster Management Agency (BNPB) as
hazard data and building from OpenStreetMap as exposure data. For this run, we will using
|project_name| Impact Function Centric Wizard (IFCW). For more information about IFCW you can refer to 
`Key concepts in disaster management planning with InaSAFE <http://docs.inasafe.org/en/training/socialisation/inasafe_concepts.html>`__ 

3.1 Open Project
................

Please open New QGIS project. We open new project in QGIS because we want to use IFCW to run this project.
You new QGIS project should look like this :

.. image:: /static/training/socialisation/other_hazard_17.*
   :align: center

3.2 Run |project_name|
......................

To use Impact Function Centric Wizard, please click at |project_name| Impact Fuction Centric Wizard icon

.. image:: /static/training/socialisation/other_hazard_18.*
   :align: center

After click that icon, you will see box shows up like this:

.. image:: /static/training/socialisation/other_hazard_19.*
   :align: center

In that box, there are some fields that show us which scenario that we want to use. Green fields mean
those scenario available and ready to run in |project_name| and the grey fields means those scenario not available
in |project_name| at the moment.

Because we want to run Volcano with building in this session, please click Field Volcano and Structure,
your box should be like this :

.. image:: /static/training/socialisation/other_hazard_20.*
   :align: center

You can click Next and Follow the further instruction in the IFCW box.

Hazard Data that we want to use for this scenario can be found in
:file:`InaSAFE Training Data > Sinabung > Hazard Data` folder
and please select :file:`Sinabung_Hazard_Map_2015_WGS84.shp` .
For Building Exposure Data, you can find it in :file:`InSAFE Training Data > Sinabung > Exposure Data` folder
and please select :file:`Sinabung_buildings_WGS84.shp` .

..note:: The differences between Volcano and Volcanic Ash can be seen in
  `Hazard Data Section <http://docs.inasafe.org/en/training/socialisation/datasets.html/>`_ and for detail explanation
  about type of data you can be found in
  `Key concepts in disaster management planning with |project_name| <http://docs.inasafe.org/en/training/socialisation/inasafe_concepts.html/>`_.

If you have follow the instruction in IFCW box, before Run |project_name| you should see final form like this :

.. image:: /static/training/socialisation/other_hazard_21.*
   :align: center

If your IFCW looks like picture above, you can click Run and you wait for the analysis processing until
the result box shows up.

.. image:: /static/training/socialisation/other_hazard_22.*
   :align: center

3.3 Interpret The Result
........................

Once you finished run the analysis, You will see the result has new layer named
“Buildings Affected by each Hazard Zone” . This layer will show you which buildings affected for each hazard zone.
There will be three new different colours generated from |project_name| (green, orange, and red).

The red buildings mean these buildings located in Low Risk Zone (Risk Zone 1), the green buildings mean
these buildings located in Intermediate Risk Zone (Risk Zone 2) and blue buildings are considered situated in
High Risk Zone (Risk Zone 3) of Sinabung Volcano.

.. image:: /static/training/socialisation/other_hazard_23.*
   :align: center

In the |project_name| result box, we now see the impact summary. It is very similar with |project_name| Dock.
The details of are explained below.

.. image:: /static/training/socialisation/other_hazard_24.*
   :align: center

-  Hazard Category: divides the results into several categories based on the threshold set in the hazard analysis.
   In this impact summary, |project_name| divides the impact buildings into three category for each hazard zone of
   Sinabung Volcano

-  Building type: divides the exposed buildings into several categories based on the building type attribute for
   each building. In this impact summary, |project_name| breaks down the results into a more detailed report
   by looking at each type of the building.

-  Action checklist: designed to make disaster managers think about what they need to do/discuss when planning for
   a similar event in the future.

-  Note: provides details about the input data and any limitations or assumptions in the analysis or report summary.
   In this example, it explains why building are said to inundated, wet and dry.

-  Detailed building type report: statistical breakdown of the number of results. 
   In this example is the number of important infrastructure. When you choose to use an aggregation layer
   with your analysis (we will do this later) this table will show the number of buildings by aggregation boundary.

Now, you have run |project_name| for Volcano Scenario using Impact Function Centric Wizard (IFCW).
Quite different with |project_name| Dock, this tool designed to help us as a user to run |project_name| easier
without need to open all data that we need one by one in QGIS. IFCW will guide us precisely and detail about
what action we should done step by step until our scenario ready to be runned. This tool very usefull for us
especially for |project_name| user who not really familiar with QGIS and Spatial Data.

4. Generic Impact Function in |project_name|
---------------------------------------------

We all already know that |project_name| can run multi hazard using some scenarios that we can setting based on
our data availability. As we know, |project_name| can run 5 type of hazards which are flood, earthquake, volcano,
volcanic ash and tsunami. The problem is how if our hazard scenario can not be runned by |project_name| such as land slide or
drought. To solved that problem, |project_name| provide one tool that called Generic Impact Function that can run any hazard
which can not be run using specific Scenario Impact Function.

4.1 Open Project
.................

Now, we will try this tool using Landslide Hazard in Nagekeo, East Nusa Tenggara with building and population data
for each scenario. Please open QGIS project file :file:`Nagekeo.qgs` from 
the :file:`InSAFE Training Data > Nagekeo` folder. The project looks something like this:

.. image:: /static/training/socialisation/other_hazard_25.*
   :align: center

You will see in |project_name| dock, |project_name| form still empty. It means that your data both hazard and
exposure data does not have keyword yet. Therefore, you have to define keyword first for each data
in this project.

To define keyword, please click on Keywords Creation Wizard icon

.. image:: /static/training/socialisation/other_hazard_02.*
   :align: center

and follow the further instruction. You can refer back to `Run Intermediate InaSAFE <http://docs.inasafe.org/en/training/socialisation/run_intermediate_inasafe.html/>`__.
If you finished define keywords for each layer, your |project_name| form should look like this :

4.2 Run |project_name| for Building
...................................

a. Run |project_name|
^^^^^^^^^^^^^^^^^^^^^

Your |project_name| Dock should poses the question “In the event of Landslide Hazard Zone,
how many buildings might be affected. Click Run on the bottom right corner in your |project_name| Dock.
If everything was set up correctly, you should get a result in the dock area after a few seconds, and a new map layer
should be added to the map. It named “Buildings Affected by each hazard zone”.

.. image:: /static/training/socialisation/other_hazard_26.*
   :align: center

.. image:: /static/training/socialisation/other_hazard_27.*
   :align: center

b. Interpret The Result
^^^^^^^^^^^^^^^^^^^^^^^

Let’s take a look for a while for the new data layer generated from |project_name|.

-  Zoom in to some area in Map Canvas

-  There will be three new different colours generated from |project_name| (red, green, blue and red).

-  The red buildings are located in high vulnerability zone, the blue buildings are located in
   moderate vulnerability zone, green buildings are considered located in Low Landslide Vulnerability Zone and
   purple buildings not affected by landslide.

-  Click building affected in the layer list to select it and click Identify Feature tool and then click on
   building to know what attribute of the building.

.. image:: /static/training/socialisation/other_hazard_28.*
   :align: center

In the |project_name| panel we now see the impact summary. The details of are explained below.

.. image:: /static/training/socialisation/other_hazard_29.*
   :align: center

-  Hazard Category: divides the results into three categories based on the hazard data classification area.
   In this impact summary, |project_name| divides the impact buildings into High, Moderate, and
   Low Landslide vulnerability zone.

-  Building type: divides the exposed buildings into several categories based on the building type attribute
   for each building. In this impact summary, |project_name| breaks down the results into a more detailed report by
   looking at each type of the building.

-  Action checklist: designed to make disaster managers think about what they need to do/discuss when planning for
   a similar event in the future.

-  Note: provides details about the input data and any limitations or assumptions in the analysis or report summary.
   In this example, it explains why building are said to be inundated, wet and dry.

-  Detailed aggregation categorical report: statistical breakdown of the number of results. 
   In this example is the number of important infrastructure. When you choose to use an aggregation layer
   with your analysis (we will do this on population) this table will show the number of buildings by
   aggregation boundary.

-  Hazard details: explanation where the hazard data come from

-  Exposure detail: explanation where the exposure come from

4.3 Run |project_name| for Population
.....................................

a. Run |project_name|
^^^^^^^^^^^^^^^^^^^^^

Turn off the Buildings Buildings Affected by each hazard zone (the layers generated from |project_name| analysis and
turn ON :file:`PopulationSP_2010` layer. Because we want to look number people who might be die or displaced in
specific area, we also need to turn ON Village layer in QGIS. This layer will be used as an aggregation layer that
can show us the result by administrative boundary.

If you forget the steps how to define a layer as an aggregation, you can see in `Run Intermediate InaSAFE <http://docs.inasafe.org/en/training/socialisation/run_intermediate_inasafe.html/>`__.
You can edit the question form in |project_name| Dock, so it should looks like this :

.. image:: /static/training/socialisation/other_hazard_30.*
   :align: center

After that you can click Run to start the analysis.

b. Interpret The Result
^^^^^^^^^^^^^^^^^^^^^^^

If everything was set up correctly, you should get a result in the dock area after a few  seconds,
and a new map layer should be added to the map. The new impact layer will be called People Impacted by
Each Hazard Zone. Let’s explore the result again to make you understand more about the |project_name| result.

-  Zoom in the area you choose

-  Select People Impacted by Each Hazard Zone in the layer list and use Identify Feature tool again to select a pixel
   (square) in the map canvas.

Here we clicked on one of the red maroon pixels and find that there is a value of 220.283, which means
there are approximately 220 people in this one pixel (square) whom might be impacted.

.. image:: /static/training/socialisation/other_hazard_31.*
   :align: center

.. image:: /static/training/socialisation/other_hazard_32.*
   :align: center   

In the |project_name| panel we now see the impact summary. The details of are explained below.

.. image:: /static/training/socialisation/other_hazard_33.*
   :align: center

-  Population needing evacuation: |project_name| estimates the number of affected people in the analysis area.
   It is assumed that all of these people will need to be evacuated.

-  Needs per week: are calculated numbers of food, water and other products that needed by evacuated people.
   These needs should be provided weekly.

-  Action checklist: designed to make disaster managers think about what they need to do/discuss when planning for
   a similar event in the future.

-  Notes: provides details about the input data and any limitations or assumptions in the analysis or report summary.
   In this example, it explains the total people in the analysis area and the source of minimum needs.

-  Detailed gender and age report: provides a breakdown of the number of affected people by age
   (youth, adults and elderly) and gender based on the default world population demographics and
   calculates the minimum needs for women’s hygiene and pregnant women. If you using aggregation layer,
   the result will break down the number of result based on administrative boundary.

.. image:: /static/training/socialisation/other_hazard_34.*
   :align: center

.. note:: In the result of |project_name|, Action Checklist and Notes might be unrelated with hazard that we runned.
   For instance, if we run drought hazard the action checklist might be has some topics such as 
   how many building closed, or people die or displaced. Those topics not really related with drought. 

Summary
-------

Congratulation! You have learn most of |project_name| use. You can run specific hazard using specific tools such as
Impact Function Centric Wizard (IFCW) and Generic Impact Function which will help us as a user to using |project_name| easily.

Now, to make you more expert using |project_name|, try using all those tools that you have used before using your own data and find your own result using your own scenario.