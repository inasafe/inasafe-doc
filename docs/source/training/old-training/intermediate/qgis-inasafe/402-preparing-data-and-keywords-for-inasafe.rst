.. image:: /static/training/old-training/intermediate/qgis-inasafe/image7.*

..  _preparing-data-and-keywords-for-inasafe:

Module 2: Preparing Data and Keywords for |project_name|
========================================================

**Learning Objectives**

- Understand |project_name| inputs
- Get OSM data from the HOT export server
- Load data into |project_name|
- Add keywords
- Prepare the hazard layer
- Run |project_name|

Now that you know your way around QGIS and |project_name|, let’s go further.
In this module, we will see how to prepare our own data so that it can be
processed in |project_name|.
Much of what we cover in this module you’ve already done, though we
will go over some of it in greater detail.
We’ll be using the project created in this module throughout the rest of the
unit, so be sure to save it along the way!

1. |project_name| inputs
------------------------

Let’s review the types of data used by |project_name|.

**Hazards** are conditions, phenomenon, or human activity that potentially
cause victims and destruction to society and environment.
Frequently observed hazards are earthquakes, tsunamis, floods, landslides
and tornadoes.

When we are working in |project_name|, hazard data refers to a vector or raster
dataset that represents the level and magnitude of an event that can
potentially cause damages.
To be used for impact calculation in |project_name|, level and magnitude of
an event scenario must be mapped over the area of interest.
This means that hazard data must be geographic - it must have location.
We have already looked at hazard data for the 2007 Jakarta flood and the
Lembang earthquake.
These hazard layers were produced from scientific modelling conducted by
scientific organisations and government agencies.
These are typical sources for such hazard data, although in cases of flood
hazards such data may also be gathered from affected communities.

Generally, hazard data has the following characteristics:

- are at a particular location
- have a measured intensity (ie. the depth of a flood or the MMI of an
  earthquake)
- have a measured duration of impact (ie. hours or days after a flood)
- have a certain time frame (ie. in the case of a sea rise flood)

In this module, our hazard input will be a flood in the village of Sirahan, in
Magelang regency in Central Java.
The data for this flood comes from participatory mapping activities done by
community members as part of the REKOMPAK project.
The data is in the training folder :file:`qgis/Sirahan/`.

**Exposure** data refers to natural and man-made objects that may be
affected if a disaster scenario really happens.
In this module we will use building exposure data created in OpenStreetMap.

The |project_name| impact functions produce an output layer representing
potential damages or losses on the affected exposure layer.
This output layer will be created once the impact calculation process is
finished processing.
|project_name| has many impact functions available, which are listed through
the 'Impact Functions Doc' menu (see below).
The impact calculation will only be possible when users provide the hazard
and exposure layer datasets and, when necessary, users define the required
parameters through the keyword Wizard correctly.

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image27.*
   :align: center

**Aggregation** is used to reclassify the result of the impact calculation
according to a specific administrative boundary level.

**Keywords** define which category a dataset belongs to, whether hazard or
exposure.
They are also used to define specific parameters to be considered,
as we shall see.
After you calculate the impact of a scenario with |project_name|, what next?
Well, the impact calculation can be used to prepare a contingency plan.
That's why relevant questions and remarks are displayed in the Result section,
which may then be considered by disaster risk managers or planning managers.

2. Getting OSM data from HOT Exports
------------------------------------

In previous scenarios, we used example data provided in the training directory,
but to set up our scenario in the village of Sirahan, let’s access the
OSM data ourselves to use as our exposure layer.
We will use the OSM buildings to calculate how many buildings (and which)
will be inundated when a flood occurs similar to our hazard model.

We’ve worked with OSM data a lot already.
Now we will utilise a website where we can quickly and easily access the data
from OSM.

1. Open your web browser and navigate to http://export.hotosm.org.

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image28.*
  :align: center

2. If you are a new user, create an account.
   If you have an account already, sign in.

The HOT Export website allows you to choose an area and create a data extract
from that area.
Then you can download the data in a variety of formats that are easily read
by QGIS.

3. In the upper right corner, click :guilabel:`New Job`

4. Give the job a name, such as :kbd:`Desa Sirahan`.

5. Zoom in on the map until you can see the village Sirahan, which is just
   north-west of Yogyakarta.

6. Click :guilabel:`Select Area` and then draw a box around Sirahan village.

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image29.*
   :align: center

The page should look something like this:

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image30.*
   :align: center

7. Click the :guilabel:`Create Job` button.

You will be asked to define a presets file.
This is like the presets that you added to JOSM in the previous unit,
except here, they define the attributes that the HOT export server will 
provide.

8. Choose :guilabel:`preset file-INASAFE`.

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image31.*
   :align: center

9. Click the :guilabel:`Save` button and take a few breaths!

It may take a few minutes for the data extraction job to process.
When it is finished, the page will change and you will see a list of files
you can download like this:

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image32.*
   :align: center

10. Click on :guilabel:`ESRI Shapefile` to download shapefiles, and once you have
    it, extract (unzip) the archive on your computer.
    It should create a directory named :file:`extract.shp`.

3. Loading data
---------------

11. We will use this OSM data as our exposure data.
    Open a new QGIS project and add all of the shapefiles that you downloaded
    as vector layers.
    You should have four layers:

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image33.*
   :align: center

For reasons that will become clear later, we need to change the map projection
from the default OSM projection (WGS 84) to WGS 84 / UTM 49S.
In other words, we need a CRS that uses metres, not degrees.

12. Right-click on the :guilabel:`planet_osm_polygon` layer and click 
    :guilabel:`Save as`.

13. Click :guilabel:`Browse` and navigate to a place where you would like to 
    put the new shapefile.
    Name the file :kbd:`Bangunan_Sirahan` and click :guilabel:`Save`.

14. Next to CRS, click :guilabel:`CRS icon`.

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image33a.*
   :align: center

15. In the filter box, type :kbd:`UTM zone 49S`, as shown below:

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image34.*
  :align: center

16. Select the CRS :guilabel:`WGS 84 / UTM zone 49S` and click :guilabel:`OK`.

The :guilabel:`Save vector layer as...` dialog will look like this:

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image35.*
   :align: center

This is the layer that we will be using as our exposure data.
You can remove the other OSM layers, or if you would like them to
remain visible, go to :menuselection:`Settings ‣ Project Properties` and
enable 'on the fly' transformation.

4. Adding keywords
------------------

Since we’ll be using this buildings layer as our exposure, we need to set the
keywords so that |project_name| knows what the layer contains.
If you remember from Unit 2, this is done with the keywords Wizard.

17. Select the :guilabel:`Bangunan_Sirahan` layer and click the
    :guilabel:`Wizard` button on the |project_name| toolbar.

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image36.*
   :align: center

18. You will see a dialog box and select :guilabel:`exposure` and after that you
    can follow the steps in the dialog box.

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image37.*
   :align: center

19. Select unit information that you want to calculate in InaSAFE. For building
    data you can choose :guilabel:`building type` to group the result of the impact
    function. You need to make sure there is the building type attribute in your
    exposure data. Or if you do not have the building type attribute in your exposure
    data, you can select :guilabel:`building generic`.

20. You also need to select which attribute has building type values.  In
    this data please select :guilabel:`amenity` and in the last step you can
    give a title for your exposure data and click :guilabel:`Finish`

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image38.*
   :align: center

5. Preparing a hazard layer
---------------------------

The hazard data that we have used previously has come from government agencies
and scientific institutions.
This time, we will use data that came from community mapping activities,
that is, from community members on the ground.
The data was created as a paper map and later converted into digital
format.
The data has already been prepared, so we simply need to add it as our hazard
layer.

21. Click :guilabel:`Add Vector Layer...` and add 
    :file:`area_terdampak_Sirahan.shp` in
    the :file:`qgis/Sirahan/` directory.

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image41.*
   :align: center

You can see that this layer is already known to |project_name|,
so presumably it has keywords already set.

22. Before we define the keywords of this data and because of the way that
    |project_name| calculates this function, we need to make sure that this
    exposure layer has a column in the attribute table that |project_name|
    expects, named "AFFECTED".

23. Open the attribute table for the :guilabel:`area_terdampak_Sirahan` layer.

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image43.*
   :align: center

We need to add some data to this layer so that QGIS can run the flood
function correctly.
When QGIS runs the flood function, it checks every feature in the hazard
layer to make sure that it is in fact a flood prone area.
Hence, each feature must have an attribute named "AFFECTED".
First, let’s add the new column to our layer.

24. In the attribute table, click the :guilabel:`Toggle Editing` button.

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image44.*
   :align: center

25. Click the :guilabel:`New Column` button.

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image45.*
   :align: center

26. Type :kbd:`affected` as the name and select :guilabel:`Text(string)` for
    :guilabel:`Type`. Give :kbd:`10` for the width.

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image46.*
   :align: center

27. Click :guilabel:`OK`.

28. Now select each value in the column “affected” and type “1”, instead of NULL

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image47.*
   :align: center

29. Click :guilabel:`Save Edits` and then :guilabel:`Toggle Editing` to stop the
    editing process.

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image48.*
   :align: center

30. Select the layer and open the :guilabel:`Keyword Wizard` and select
    :guilabel:`Hazard` and follow the steps in the dialog box

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image42.*
   :align: center

31. In this hazard data we select :guilabel:`flood` as the hazard type because we
    assume that this is a flood hazard.

32. Select :guilabel:`wet/dry` as the subcategory for flood, and after that select the
    :guilabel:`wet/dry` attribute that represents the flood extent as wet/dry.

33. As the last step, you can give a title for your hazard data and click
    :guilabel:`Finish`

6. Running |project_name|
-------------------------

Everything is prepared now - our layers are loaded, the keywords are set, and
we’ve ensured that the layers have the data that |project_name| expects. Make
sure the question form in InaSAFE looks like this

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image49a.*
   :align: center

and then click :guilabel:`Run`!

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image49.*
   :align: center

The results should looks something like this:

.. image:: /static/training/old-training/intermediate/qgis-inasafe/image50.*
   :align: center

Save your project!
We’ll be using it in the upcoming modules...

We’ve run a few scenarios, but what is next?
In the next modules we will use our QGIS skills to find the best evacuation
routes for people to use in the case of the flood disaster,
as well as examining appropriate places for IDP camps.


:ref:`Go to next module --> <determining-idp-camp-location>`