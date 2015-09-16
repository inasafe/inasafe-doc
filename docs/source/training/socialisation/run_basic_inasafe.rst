.. _run_basic_inasafe:

.. image:: /static/training/socialisation/inasafe_logo.*

Run Basic |project_name|
========================

Introduction
-------------

In this exercise we will work through an example scenario where we show
how the different data elements used by |project_name| are combined in order to
analyse the potential impact of a flood in Jakarta on both the buildings
and the population.

After we have run the |project_name| analysis we will print the map and
analysis report as pdf and review the results. We will also learn how to
change the flood threshold and take a look at the default settings for
minimum needs. We will also learn how to save our work.

Learning objective
-------------------

To develop the participant’s basic understanding of the |project_name| workflow
and application of |project_name| in the Disaster Management sector. By the end
of this exercise; participants will:

-  Be able to run a flood analysis using |project_name| - on buildings

-  Be able to run a flood analysis using |project_name| - on population

-  understand the flood impact default settings;

-  understand the impact summary report;

-  be able to change the analysis threshold and run a new scenario; and

-  Be able to generate a PDF map from the results of an analysis

-  be able to save their work to share with others.

Data for this exercise
----------------------

The data for this exercise are available in **Run Basic InaSAFE v3.2 zip**
which can be downloaded from `InaSAFE Training
Data <http://data.inasafe.org/TrainingDataPackages/>`__ Packages . We will use the following
QGIS project file and spatial data:

1. DKI_Jakarta_Basic.qgs

2. Jakarta_Flood_HKV_WGS84

3. Jakarta_Buildings_WGS84

4. Java_Population

Exercise
--------

1. Open QGIS Project
.....................

Before we started to run |project_name| analysis, we must open QGIS project.
Please open QGIS project file :file:`DKI_Jakarta.qgs` from the :file:`InSAFE
Training Data > DKI Jakarta` folder. The project looks something like
this:

.. image:: /static/training/socialisation/run_basic_00.*
   :align: center


As you can see from the picture above, you will presented with several
data in Jakarta from building, java population, raster and vector flood
hazard.

You will see that the project has three layers loaded:

-  Buildings: these are exposure data. We will use these to assess the
   flood impact on buildings.

-  Flood: this is the hazard model. We will use this to determine the
   depth of water.

-  Population: this is a population raster. We will use it to determine
   the number of people exposed to the flood.

More detailed information about the data used in this exercise can be
found in (datasets.rst). The table below provides a brief summary about
the source of the data.

+------------------------------+---------------+---------------------------------------------------------------------------------+
| **Data**                     | **Source**    | **Description**                                                                 |
+==============================+===============+=================================================================================+
| Buildings                    | OpenStreetMap | Most of the important buildings in Jakarta                                      |
|                              |               | have been mapped through the collaboration                                      |
|                              |               | of BPBD DKI Jakarta, OpenStreetMap and                                          |
|                              |               | the Australian Government. `See more at...                                      |
|                              |               | <http://inasafe.org/en/training/socialisation/functionality_datasets.html>`__   |
+------------------------------+---------------+---------------------------------------------------------------------------------+
| Java_population_WGS84        | AsiaPop       | High resolution, modelled data for human population distributions.              |
|                              |               | `See more at...                                                                 |
|                              |               | <http://inasafe.org/en/training/socialisation/functionality_datasets.html>`__   |
+------------------------------+---------------+---------------------------------------------------------------------------------+
| a Flood similiar to 2007     | HKV           |                                                                                 |
| Jakarta Event                |               | The flood model was created by scientists/engineers in coordination with        |
|                              |               | DKI Jakarta Public Works based on the 2007 flood conditions. `See more at...    |
|                              |               | <http://inasafe.org/en/training/socialisation/functionality_datasets.html>`__   |
+------------------------------+---------------+---------------------------------------------------------------------------------+

Let's move into the next section where we will run our first |project_name|
analysis using these data. We will be working with the flood hazard
model to look at the number of affected buildings. These data already
have keywords assigned so we are ready to run the analysis.

2. Run |project_name| Analysis for Building
............................................

Take a look at the |project_name| dock on the right side of QGIS. The |project_name|
dock should show that you are ready to run a flood analysis on
buildings. It poses the question “In the event of **a flood similar to the 2007 Jakarta event**, how many **buildings** might **be flooded**?”
In this analysis we will use the default flood depth threshold of 1.0
metre. Later on we will learn how to change the threshold.

a. Run |project_name| Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /static/training/socialisation/run_basic_01.*
   :align: center

Click :guilabel:`Run` in the lower right corner of the |project_name| panel to start
the analysis process. If everything was set up correctly, you should get
a result in the dock area after a few seconds, and a new map layer
should be added to the map.

.. image:: /static/training/socialisation/run_basic_02.*
   :align: center

b. Interpret The Result
^^^^^^^^^^^^^^^^^^^^^^^

The new impact layer will be generated and called **Estimated buildings
affected**. Let’s take a look for a while for the new data layer
generated from |project_name|.

-  Zoom in to some area in Map Canvas

-  Here we have zoomed in to a location showing two rivers going through
   the middle of Jakarta. There will be three new different colours
   generated from |project_name| (green, orange, and red).

.. image:: /static/training/socialisation/run_basic_03.*
   :align: center

.. note:: If you didn't see these colours, you might need to turn off the data layer above the *Estimated building affected* layer.

-  The red buildings are situated in water greater than one metre, the
   orange buildings are situated in water between zero and one
   metre, while the green buildings are considered unaffected as
   they are situated in water less than the threshold of one metre.

-  Click :guilabel:`Estimated building affected` in the layer list to select
   it and click :guilabel:`Identify Feature` tool and then click on building
   to know what attribute of the building.

.. image:: /static/training/socialisation/run_basic_04.*
   :align: center

In the |project_name| panel we now see the impact summary. The details of are
explained below.

.. image:: /static/training/socialisation/run_basic_05.*
   :align: center

-  **Hazard Category**: divides the results into several categories
   based on the threshold set in the hazard analysis. In this impact
   summary, |project_name| divides the impact buildings into three
   category: number of building inundated (building affected by
   water deeper than the analysis threshold), number of wet building
   (building affected by flood water but not as deep as the analysis
   threshold), and number of dry building (building that are not
   affected by any flood water)

-  **Building type:** divides the exposed buildings into several
   categories based on the building type attribute for each
   building. In this impact summary, |project_name| breaks down the results
   into a more detailed report by looking at each type of the
   building, for example the number of inundated hospitals and the
   total number of hospital in analysis area.

-  **Action checklist:** designed to make disaster managers think about
   what they need to do/discuss when planning for a similar event in
   the future.

-  **Note:** provides details about the input data and any limitations
   or assumptions in the analysis or report summary. In this
   example, it explains why building are said to be inundated, wet
   and dry.

-  **Detailed building type report:** statistical breakdown of the
   number of results. In this example is the number of important
   infrastructure. When you choose to use an aggregation layer with
   your analysis (we will do this later) this table will show the
   number of buildings by aggregation boundary.

-  **Hazard details:** explanation where the hazard data come from

-  **Exposure detail:** explanation where the exposure come from

The results show the buildings that will be affected by flood water 1m deep.
But what if the disaster manager decides that buildings in 80cm of water are also flooded?
In order to assess this new scenario, we need to change the water depth threshold
at which buildings are considered to be inundated.
With |project_name| it is easy to run a new scenario, all you need to do is
change the **Thresholds [m]** in the Options tab to 0.8 and run the scenario again.
We will do this next.

c. Changing threshold
^^^^^^^^^^^^^^^^^^^^^

In the Jakarta flood scenario we are running; the threshold refers to
the depth of water that a disaster manager decides is the boundary
between buildings being flooded (affected) and buildings not being
affected.

.. note:: You only can change the threshold mostly for Raster Hazard Type. Default threshold for this hazard is 1m or 100cm.

If you want to open |project_name| question panel again,
click on :guilabel:`Show question form` at the top of the |project_name| panel.
You will see the |project_name| question panel again and you can click the :guilabel:`Options` button
next to :guilabel:`be flooded`.

.. image:: /static/training/socialisation/run_basic_06.*
   :align: center

It will open the |project_name| impact function configuration.

.. image:: /static/training/socialisation/run_basic_07.*
   :align: center

Here you can change the threshold of the flood according to your need,
in this example we change it to 0.8m. After you change the threshold to 0.8,
click :guilabel:`OK` to close the dialog and then run the analysis again to see
the change in the results.

When the function completes, take a look at the impact summary in the
|project_name| panel. How do the results compare to the first analysis results?
The result should be different to the first analysis because
in the first analysis |project_name| buildings are said to be inundated if the **flood level exceeds 1.0m**
and now we have changed the flood level to **0.8m**,
this means that building are said to be inundated when the **flood level exceed 0.8m**.
This means that more building will be defined as inundated with the lower flood threshold value
because a greater area of Jakarta is flooded at this depth.

.. note:: ask your tutor to explain if you do not understand this.

This completes our first |project_name| analysis using the flood hazard model to look at the number of affected buildings. 

3. Run |project_name| for population
....................................

We are now ready to run our second |project_name| analysis using the flood
hazard data for Jakarta. We will be working with the flood hazard model
again, but this time to look at the number of impacted people. These
data already have keywords assigned so we will be ready to run the
analysis as soon as we have turned on the relevant data layers.

In the QGIS, turn OFF the **Buildings** and **estimated building affected**
(the layers generated from |project_name| analysis and turn ON **Java_Population_WGS84** layer.

Confirm that the |project_name| panel on the right side is set to query how many people might need evacuation:

- A flood similar to the 2007 Jakarta event

- People

- Need evacuation

.. image:: /static/training/socialisation/run_basic_08.*
   :align: center

a. Run |project_name| Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If everything is setup correctly, the |project_name| dock should show that you
are ready to run a flood analysis on population. It poses the question
“In the event of **a flood similar to the 2007 Jakarta event**, how many
**people** might **need evacuation**?” In this analysis we will use the
default flood depth threshold of 1.0 metre to find out how many people
are in 1 metre of water. After everything is setup accordingly click
:guilabel:`Run` to process the new scenario.

.. note:: Notice that if you click on the drop-down list on "How Many **People**,
          the **building** option is not available. This is because **building**
          is not checked in the Layers panel.

b. Interpret The Results
^^^^^^^^^^^^^^^^^^^^^^^^

If everything was set up correctly, you should get a result in the dock
area after a few seconds, and a new map layer should be added to the
map. The new impact layer will be called **population which need evacuation**.
Let’s explore the result again to make you understand more about the |project_name| result.

1. Turn Off **Estimated building affected** layer and drag the
   **population which need evacuation** above **a flood similar to 2007 Jakarta event**

2. Zoom in the area you choose

3. Select **population which need evacuation** in the layer list and
   use :guilabel:`Identify Feature` tool again to select a pixel (square) in
   the map canvas.

4. Here we clicked on one of the light green pixels and find that there
   is a value of 80.75106, which means there are approximately 80
   people in this one pixel (square) needed to evacuate because of
   the flood.

.. image:: /static/training/socialisation/run_basic_09.*
   :align: center

In the |project_name| panel we now see the impact summary. The details of are
explained below.

.. image:: /static/training/socialisation/run_basic_10.*
   :align: center

- **Population needing evacuation:** |project_name| estimates the number of
  affected people in the analysis area. It is assumed that all of these
  people will need to be evacuated.

- **Needs per week:** are calculation numbers of food, water and other
  products that needed by evacuated people. These needs should be provided
  weekly.

- **Action checklist:** designed to make disaster managers think about
  what they need to do/discuss when planning for a similar event in the future.

- **Notes:** provides details about the input data and any limitations or
  assumptions in the analysis or report summary. In this example, it
  explains the total people in the analysis area and the source of minimum needs.

- **Detailed gender and age report:** provides a breakdown of the number
  of affected people by age (youth, adults and elderly) and gender based
  on the default world population demographics and calculates the minimum
  needs for women’s hygiene and pregnant women.

- **Detailed minimum needs report:** provides a breakdown of the number
  minimum needs for evacuated people which based on **PERKA No 7/2008**.
  This minimum need consist of rice, drinking water, clean water, family
  kits and toilet and provided weekly.

.. image:: /static/training/socialisation/run_basic_11.*
   :align: center

c. Understand defaults minimum needs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The |project_name| impact summary for flood impact on people includes details
for the amount of drinking water, rice, clean water, and family kits and
for the number of toilets that should provide for displaced persons each
week. The minimum needs in the Jakarta flood impact assessment are based
on **Head of Indonesia National Disaster Management Agency, BNPB,
regulation, PERKA No 7/2008 guideline procedure for fulfillment of basic
needs in Disaster Response.** According to the following default
formula:

- 400g rice per person per day (2.8kg per week)

- 2.5l drinking water per person per day (17.5l per week)

- 15l clean water per person per day (105l per week)

- one family kit per family per week (assumes five people per family which is not specified in perka)

- 20 people per toilet

As described above, the impact summary and minimum needs calculation is
based on the default world population demographics (which assumes a
ratio of x:y female to male and x% youth, y% adult and z% elderly).

You may like to refer to local population statics (for example -
`Population of DKI Jakarta <http://sp2010.bps.go.id/index.php/site/tabel?tid=336&wid=3100000000>`__)
to change these defaults for your analysis area,
similarly if you have other regulation for minimum needs,
you can change in the Impact Function Configuration in Minimum Needs Tab
or if you want to create your own minimum needs,
you can use minimum needs configuration (see more at Minimum Needs Configuration manuals).

.. image:: /static/training/socialisation/run_basic_14.*
   :align: center

4. Print and Save your |project_name| Results
.............................................

We can also print the analysis results; the impact map and the impact summary,
as two separate pdf files. To print |project_name| result:

1. Click :guilabel:`Print` at the bottom of the |project_name| panel.

2. A window will pop up as shown below.

.. image:: /static/training/socialisation/run_basic_12.*
   :align: center

- **Area to print**: leave this set to the default **analysis extent**.

- **Template to use**: leave this set to the **default portrait - a3**.

For more information about printing, click :guilabel:`Help` in the print window.

3. Click :guilabel:`Open PDF`.

4. Navigate to where you would like to save the PDF. By default,
   the filename is related to the scenario
   (in this case it will say Buildings_inundated)
   but you can name the file name by yourself,
   for example :file:`Jakartaflood_building_1m`.
   In this case adding 1m to the file name reminds us that
   in this flood impact scenario our threshold flood depth was 1 metre.
   Click :guilabel:`Save`.

Two PDFs will be generated, one shows a map with the impact layer and
the other has tables from the impact summary. Take a look at the result.

.. image:: /static/training/socialisation/run_basic_13.*
   :align: center

We are now already have the impact result in pdf files, but what if we
want to keep the impact result in shapefile? Is the impact result
shapefile automatically stored?

The |project_name| impact result layer is saved in temporary folder, this means
that it will automatically deleted if you restart your computer, unless
you save your QGIS project. If you want to keep your |project_name| results (so
you can refer to them again or share them with others), you need to
manually save the |project_name| impact layer |project_name| as new layer in same
directory as your project.

1. Right click on your |project_name| analysis result, for example **estimated building affected** or **population which need evacuation**
   and click :guilabel:`Save As...`

2. A new window will appear. Click :guilabel:`Browse…` and name your new layer
   and click :guilabel:`Save` and then click :guilabel:`OK`.

If you want to save your current project you can save it by clicking on
:menuselection:`Project > Save As...` to save your current project. It’s better to
not overwrite the training project so you can exercise again later.

Summary
-------

In this exercise you have learned how to run a basic |project_name| analysis
using an existing QGIS project file and what the minimum component that
must be there to run |project_name| properly. Those components are hazard and
exposure data. In this exercise, you have run an |project_name| impact
assessment for a flood scenario in Jakarta using two types of exposure
data. The hazard data you used was a modelled flood raster and the
exposure data were buildings and population. These analyses produced
impact layers and impact summaries for affected buildings and impacted
people.

You have also learned how to modify the analysis options through the
Impact Function configuration, how to print |project_name| results in PDF
format, understand what minimum needs is and how to save both your
impact layers and your QGIS project file.

In the next section you will learn more about how to run |project_name| in more
detail. In that module you will learn how to use more |project_name| tools such
as Agreggation options, OSM Downloader, Minimum Needs Configuration,
etc.