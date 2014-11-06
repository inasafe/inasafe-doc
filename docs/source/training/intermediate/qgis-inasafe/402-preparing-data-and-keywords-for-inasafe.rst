.. image:: /static/training/intermediate/qgis-inasafe/image7.*

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

Now you you know your way around QGIS and |project_name|, let’s go further.
In this module, we will see how to prepare our own data so that it can be
processed in |project_name|.
Much of what we cover in this module you’ve already done, though we
will go over some of it in greater detail.
We’ll be using the project created in this module throughout the rest of the
unit, so be sure to save it along the way!

1. InaSAFE inputs
-----------------

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
parameters through the keyword editor correctly.

.. image:: /static/training/intermediate/qgis-inasafe/image27.*
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

.. image:: /static/training/intermediate/qgis-inasafe/image28.*
  :align: center

2. If you are a new user, create an account.
   If you already have an account already, sign in.

The HOT Export website allows you to choose an area and create a data extract
from that area.
Then you can download the data in a variety of formats that are easily read
by QGIS.

3. In the upper right corner, click :guilabel:`New Job`

4. Give the job a name, such as :kbd:`Desa Sirahan`.

5. Zoom in on the map until you can see the village Sirahan, which is just
   north-west of Yogyakarta.

6. Click :guilabel:`Select Area` and then draw a box around Sirahan village.

.. image:: /static/training/intermediate/qgis-inasafe/image29.*
   :align: center

The page should look somethings like this:

.. image:: /static/training/intermediate/qgis-inasafe/image30.*
   :align: center

7. Click the :guilabel:`Create Job` button.

You will be asked to define a presets file.
This is like the presets that you added to JOSM in the previous unit,
except here, they define the attributes that the HOT export server will 
provide.

8. Choose :guilabel:`preset file-INASAFE`.

.. image:: /static/training/intermediate/qgis-inasafe/image31.*
   :align: center

9. Click the :guilabel:`Save` button and take a few breaths!

It may take a few minutes for the data extraction job to process.
When it is finished, the page will change and you will see a list of files
you can download like this:

.. image:: /static/training/intermediate/qgis-inasafe/image32.*
   :align: center

10. Click on :guilabel:`ESRI Shapefile` to download shapefiles, and once you have
    it, extract (unzip) the archive on your computer.
    It should create a directory named :file:`extract.shp`.

3. Load data
------------

11. We will use this OSM data as our exposure data.
    Open a new QGIS project and add all of the shapefiles that you downloaded
    as vector layers.
    You should have four layers:

.. image:: /static/training/intermediate/qgis-inasafe/image33.*
   :align: center

For reasons that will become clear later, we need to change the map projection
from the default OSM projection (WGS 84) to WGS 84 / UTM 49S.
In other words, we need a CRS that uses metres, not degrees.

12. Right-click on the :guilabel:`planet_osm_polygon` layer and click 
    :guilabel:`Save as`.

13. Click :guilabel:`Browse` and navigate to a place where you would like to 
    put the new shapefile.
    Name the file :kbd:`Bangunan_Sirahan` and click :guilabel:`Save`.

14. Next to CRS, click :guilabel:`Browse`.

15. In the filter box, type :kbd:`UTM zone 49S`, as shown below:

.. image:: /static/training/intermediate/qgis-inasafe/image34.*
  :align: center

16. Select the CRS :guilabel:`WGS 84 / UTM zone 49S` and click :guilabel:`OK`.

The :guilabel:`Save vector layer as...` dialog will look like this:

.. image:: /static/training/intermediate/qgis-inasafe/image35.*
   :align: center

This is the layer that we will be using as our exposure data.
You can remove the other OSM layers, or if you would like them to
remain visible, go to :menuselection:`Settings ‣ Project Properties` and
enable “on the fly” transformation.

4. Adding keywords
------------------

Since we’ll be using this buildings layer as our exposure, we need to set the
keywords so that |project_name| knows what the layer contains.
If you remember from Unit 2, this is done with the keywords editor.

17. Select the :guilabel:`Bangunan_Sirahan` layer and click the
    :guilabel:`Keyword Editor` button on the |project_name| toolbar.

.. image:: /static/training/intermediate/qgis-inasafe/image36.*
   :align: center

18. Adjust the settings so that the keyword editor looks similar to the
    following:
    Most likely you will only need to change the subcategory field to
    :guilabel:`structure`.

.. image:: /static/training/intermediate/qgis-inasafe/image37.*
   :align: center

19. Now we will do something new by adding advanced keywords.
    Click on the :guilabel:`Advanced` tab.

20. You can add keywords manually using the advanced editor.
    Manually add a keyword so that the value of :guilabel:`datatype` 
    is :kbd:`osm`.
    It should look like this:

.. image:: /static/training/intermediate/qgis-inasafe/image40.*
   :align: center

21. Click :guilabel:`Add to list`.

22. Click :guilabel:`OK`.
    You should see the layer appropriately loaded in the |project_name| panel.

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

23. Click :guilabel:`Add Vector Layer...` and add 
    :file:`area_terdampak_Sirahan.shp` in
    the :file:`qgis/Sirahan` directory.

.. image:: /static/training/intermediate/qgis-inasafe/image41.*
   :align: center

You can see that this layer is already known to |project_name|,
so presumably it has keywords already set.

24. Select the layer and open the keywords editor.
    Notice that the subcategory is set to :guilabel:`flood [wet/dry]`.

.. image:: /static/training/intermediate/qgis-inasafe/image42.*
   :align: center

25. Because of the way that |project_name| calculates this function,
    we need to make sure that this exposure layer has a column in the attribute
    table that |project_name| expects, named "AFFECTED".

26. Click OK and then open the attribute table for the 
    :guilabel:`area_terdampak_Sirahan` layer.

.. image:: /static/training/intermediate/qgis-inasafe/image43.*
   :align: center

We need to add some data to this layer so that QGIS can run the flood
function correctly.
When QGIS runs the flood function, it checks every feature in the hazard
layer to make sure that it is in fact a flood prone area.
Hence, each feature must have an attribute named "AFFECTED".
First, let’s add the new column to our layer.

27. In the attribute table, click the :guilabel:`Toggle Editing` button.

.. image:: /static/training/intermediate/qgis-inasafe/image44.*
   :align: center

28. Click the :guilabel:`New Column` button.

.. image:: /static/training/intermediate/qgis-inasafe/image45.*
   :align: center

29. Type :kbd:`affected` as the name and select :guilabel:`Text(string)` for 
    :guilabel:`Type`.
    Give :kbd:`10` for the width.

.. image:: /static/training/intermediate/qgis-inasafe/image46.*
   :align: center

30. Click :guilabel:`OK`.

31. Now select each value in the column “affected” and type “1”, instead of NULL.

.. image:: /static/training/intermediate/qgis-inasafe/image47.*
   :align: center

32. Click :guilabel:`Save Edits` and then :guilabel:`Toggle Editing` to stop the
    editing process.

.. image:: /static/training/intermediate/qgis-inasafe/image48.*
   :align: center

6. Run InaSAFE
--------------

Everything is prepared now - our layers are loaded, the keywords are set, and
we’ve ensured that they layers have the data that |project_name| expects.
Time to click :guilabel:`Run`!

.. image:: /static/training/intermediate/qgis-inasafe/image49.*
   :align: center

The results should looks something like this:

.. image:: /static/training/intermediate/qgis-inasafe/image50.*
   :align: center

Save your project!
We’ll be using it in the upcoming modules...

We’ve run a few scenarios, but what is next?
In the next modules we will use our QGIS skills to find the best evacuation
routes for people to use in the case of the flood disaster,
as well as examining appropriate places for IDP camps.


:ref:`Go to next module --> <determining-idp-camp-location>`