.. image:: /static/training/beginner/qgis-inasafe/image6.*

Module 10: Vector Analysis for Problem Solving
==============================================

**Learning Objectives**

- Explaining GIS processes
- Identifying problems
- Explaining data needed
- Starting a project
- Analyzing problems
- Identifying hazard zone
- Looking for Important Roads
- Looking for Medical Facilities
- Buffering Roads
- Buffering Medical Facilities
- Analyzing Overlapped Areas
- Choosing Farms and Moors

The power of GIS is its ability to help us analyze data.  Vector data can be
analyzed to reveal how different features interact with each other.  In this
chapter, we’ll work through the GIS process, attempting to solve a problem, and
as we proceed, we will learn about various analysis tools that QGIS provides.

**1. The GIS Process**

Before we start, it would be useful to give a brief overview of a process that
can be used to solve any GIS problem.  The steps are simple:

    1) State the Problem
    2) Get the Data
    3) Analyze the Problem
    4) Present the Results

**2. The Problem**

Let’s start off the process by deciding on a problem to solve.  Let’s say you’re
a disaster manager, and you need to provide the best locations to place refugees
(IDPs) in villages surrounding Mount Merapi when it erupts. You’ve come up with
the following criteria for these locations:

1) The area should be a dry field or farm in the districts **Ngemplak, Turi or
Pakem**.
2) The area must be outside of Merapi Eruption Disaster Prone Region
III.
3) Access to the site should be easy, so it will not be more than 300
meters from a main roads.
4) The site should be close to health facilities.
5) The land area should be between 50000-150000 m².

**3. The Data**

To answer these questions, we’re going to need the following data:

1) Landuse in Sleman regency
2) Streets in Sleman
3) Location of health
   facilities
4) KRB Merapi (Merapi Eruption Disaster Prone Region - this is the
   same data that we learned how to georeference in the previous chapter)

.. note:: For this exercise the data has been provided already, but in a real
   scenario you may need to find providers for the datasets in question.  In
   Indonesia, the National Land Agency and BNPB Bappeda are good sources for the
   types of data you will need, and OpenStreetMap can be used as a source for
   roads and infrastructure.

**4. Start a Project**

So now that we know what we want to do, let’s start doing it!

- Start a new QGIS project.

.. image:: /static/training/beginner/qgis-inasafe/image208.*
   :align: center

- Start adding the layers we will use.  In the :file:`../Sleman/Merapi` folder,
  add the layers **jalan_sleman_49S**,  **tempat_penting_Sleman_49S**,
  **KRB3_49S** and **vegetasi_49S**.  Your Layers list should look like this:

.. image:: /static/training/beginner/qgis-inasafe/image209.*
   :align: center

.. note::  Most of the layers are pretty self-explanatory, but what are KRB3,
   KRB2, and KRB1? These layers show areas of impact when Merapi erupts. KRB3 is
   the area of worst impact, KRB2 is medium, and KRB1 has little impact.  In
   this scenario we want to find locations that are not within KRB3.

The data we are working with now is similar to that from previous chapters, but
now it is in a Projected Coordinate System.  The previous data was saved in
WGS84 - this meant that the coordinates of our features were stored in degrees,
which aren’t very good for measuring size or distance.  By using a projected
system our coordinates are in meters, which is important for analysis, because
we can easily measure distances between and around features.

- :guilabel:`Rename` the layers by right-clicking on them and selecting the
  Rename option.
- :guilabel:`Give them the new`, simpler names **jalan**,
  **lokasi_penting**,**KRB III** and **vegetasi**.
- :guilabel:`Save` your map as :kbd:`merapi_analisis.qgs`.
- In your operating system’s file manager, create a
  new folder under :file:`../qgis/Sleman/Merapi` and call it
  **evakuasi_bencana**.

This is where you’ll save the datasets that we will create during our anaysis.

Now that we’ve got the data, let’s analyze the problem!

**5. Analyzing the Problem: Farms and Dry Fields**

The first criterion we’re facing is that the land must be a farm or dry field,
and it must be in one of three areas.  So let’s tell QGIS to only show us the
farms and dry fields that are, in fact, in these sub-districts!

- :guilabel:`Right-click` on the **vegetasi** layer in the Layers list.
- :guilabel:`Select` the option **Query**.... This opens the Query Builder
  dialog.
- :guilabel:`Scroll down` in the Fields list on the left of this dialog until
  you see the field **kec**.
- Click on it once.
- Click the :guilabel:`All` button underneath the Values list:

.. image:: /static/training/beginner/qgis-inasafe/image210.*
   :align: center

We are going to build a query.  A query is a statement that allows us to show
only the data that we want from a layer.  In this case, we want to instruct QGIS
to only show us farms and dry fields which have a sub-district value equal to
Ngemplak, Turi, or Pakem.

- :guilabel:`Double-click` the word kec in the **Fields list**.
- :guilabel:`Click` the = button (under Operators).

.. image:: /static/training/beginner/qgis-inasafe/image211.*
   :align: center

- :guilabel:`Double-click` the value Ngemplak in the Values list.
- Click :guilabel:`OR`.
- Repeat these steps twice more, using the values Turi and Pakem
  instead of Ngemplak. The query should look like this:

.. image:: /static/training/beginner/qgis-inasafe/image212.*
   :align: center

- Click :guilabel:`AND`.
- :guilabel:`Now highlight` **guna_lahan** in the Fields list,
  and click the “All” button to load the values.
- :guilabel:`Double-click` **guna_lahan**.  Then click the = button.
  Then double-click the value **KEBUN**.
- Click :guilabel:`OR`.
- Repeat the previous step but instead of KEBUN use TEGALAN.
  Your query should look like this:

.. image:: /static/training/beginner/qgis-inasafe/image213.*
   :align: center

- The idea is that query will filter the data layer so that it will only show us
  features that we want that is, farms and dry fields in Pakem, Turi, and
  Ngemplak.
  But we need to add one thing to our query: parentheses.
  Without these, our query won’t work quite right.
  We need to add two pair of parentheses on each side of the word AND, like so:

.. image:: /static/training/beginner/qgis-inasafe/image214.*
   :align: center

- Click :guilabel:`OK`. Our **vegetasi** layer has far fewer features now.

.. image:: /static/training/beginner/qgis-inasafe/image215.*
   :align: center

.. note:: Well done!  We’ve applied our first criteria to begin solving the
   problem!

**6. The Danger Zone**

Our next criteria is that our chosen location should be outside of the danger
zone, which is defined by the layer **KRB III**.  For this we can use the Spatial
Query tool.

- Go to :menuselection:`Vector ‣ Spatial Query ‣ Spatial Query`.
- Under :guilabel:`Select source features from` choose **vegetasi**.
  In the next box choose :guilabel:`Is disjoint`  The third box should be set
  to **KRB III**.  The Spatial Query window should look like this:

.. image:: /static/training/beginner/qgis-inasafe/image216.*
   :align: center

- Click :guilabel:`Apply`  Then click :guilabel:`Close`
  once the selection has been applied.

Now the vegetasi layer looks like the image below.  Notice that all the features
have been selected that fall outside the KRB III area.

.. image:: /static/training/beginner/qgis-inasafe/image217.*
   :align: center

The next steps of our analysis will be easier if we save this selection as a
separate layer.

- :guilabel:`Right-click` on the **vegetasi layer** and
  click :guilabel:`Save As`....
- Next to the Save as field in the dialog that appears,
  click the :guilabel:`Browse` button.
- :guilabel:`Save` the layer under **evakuasi_bencana**, as kebun_tegalan.shp
- :guilabel:`Check` the Add saved file to map box in the
  **Save vector layer as**... dialog.
- Click :guilabel:`OK`. It will tell you that Export to vector file has been
  completed.
- Click :guilabel:`OK`.
- :guilabel:`Right-click` on the old vegetation layer and remove it.
  You should have these layers remaining:

.. image:: /static/training/beginner/qgis-inasafe/image218.*
   :align: center

**7. Finding Important Roads**

We have a problem with our roads layer, similar to that of our vegetation layer.
Our roads layer has too many roads!  We only want to use main roads for our
analysis, so that we can meet the criteria that our location is within 300
meters of a major road.  Once again, we will use the Query Builder.

- :guilabel:`Right-click` on the **jalan** layer and click :guilabel:`Query`...
- Build a query for the roads layer, like you did above for the vegetation layer
  You want only the **types primary and secondary**,
  so you need to build this query:

*"TYPE" = 'primary' OR "TYPE" = 'secondary'*

- You can use the approach that we learned above, or you can simply
  type this command into the query box.  But be careful that you type it
  correctly!

.. image:: /static/training/beginner/qgis-inasafe/image219.*
   :align: center

**8.  Looking for Health Facilities**

- Using the same approach, build a query for the lokasi_penting layer as shown:
  *"Fungsi" = 'Kesehatan'*

**9. Buffering Roads**

Okay, we’ve refined our data a bit so that it shows us the features we are
interested in analyzing. Remember that according to our criteria our land area
should be within 300 meters of a main road and close to a health facility. QGIS
allows us to calculate distances from any vector object, and we will use this
functionality to help us reach a solution.

- Make sure that only the **jalan** and **kebun_tegalan** layers are visible,
  to simplify the map while you’re working.
- Go to :menuselection:`Vector ‣ Geoprocessing Tools ‣ Buffer(s)`.

.. image:: /static/training/beginner/qgis-inasafe/image220.*
   :align: center

- In the first dropdown box :guilabel:`choose` **jala**
- :guilabel:`Enter` “300” next to Buffer distance.
- Check the box next to :guilabel:`Dissolve buffer results.`
- Click :guilabel:`Browse` and type :kbd:`buffer_jalan_300m.shp` for the
  filename.

.. image:: /static/training/beginner/qgis-inasafe/image221.*
   :align: center

.. note:: that we input the buffer distance in meters. Good thing we used
   projected data!

- Click :guilabel:`OK`.  QGIS will create a buffer around the streets that
  extends 300 meters.
- When you are asked to add the new layer to the TOC, click :guilabel:`Yes`
  (“TOC” stands for “Table of Contents”, by which it means the Layers list)

.. image:: /static/training/beginner/qgis-inasafe/image222.*
   :align: center

- :guilabel:`Close` the Buffer dialog and witness your new layer:

.. image:: /static/training/beginner/qgis-inasafe/image223.*
   :align: center

.. note:: Interesting!  Those big fat lines are actually areas that are within
   300 meters of primary and secondary roads.

**10. Buffering Health Facilities**

- Now try it yourself!  Using the same approach, create a new buffer layer
  around your health facilities.  The buffer should be 2.5 km in radius,
  and save the new layer in the same directory as
  **buffer_fas_kesehatan_2.5km.shp**.  Your resulting map will
  look something like this:

.. image:: /static/training/beginner/qgis-inasafe/image224.*
   :align: center

.. note:: Remember that the buffer distance is in meters. Keep this in mind
   when you want to create a 2,5 km buffer!

**11.  Overlapping Areas**

Now we can see areas where a main road is 300 meters away and where there is a
health facility within 2.5 km.  But we only want the areas where both of these
criteria are satisfied at once!  To do that we will use the Intersect tool.

- Go to :menuselection:`Vector ‣ Geoprocessing Tools ‣ Intersect`.
- :guilabel:`Enter` **buffer_fas_kesehatan_2.5km** and **buffer_jalan_300m**
  as the two input layers.
  Name the output shapefile :kbd:`intersect_buffer_jalan_kesehatan.shp`

.. image:: /static/training/beginner/qgis-inasafe/image225.*
   :align: center

- Click :guilabel:`OK` and add the layer to the Layers list when prompted.
- If we hide the original layers, we can see that our new layers shows us
  the areas where they intersect.  These are the areas where both of
  these criteria are satisfied.

.. image:: /static/training/beginner/qgis-inasafe/image226.*
   :align: center

**12. Select Farms and Dry Fields**

Now we have the layer **kebun_tegalan**, which satisfies two of our criteria,
and the layer **intersect_buffer_jalan_kesehatan.shp** which satisfied two other
criteria.  We need to know where they overlap!

- Go to :menuselection:`Vector ‣ Research Tools ‣ Select by location`.
  A dialog will appear.
- Set it up like this:

.. image:: /static/training/beginner/qgis-inasafe/image227.*
   :align: center

- Click :guilabel:`OK` and you’ll see the results are selected (they are yellow)

.. image:: /static/training/beginner/qgis-inasafe/image228.*
   :align: center

Let’s save this selection as a new layer.

- :guilabel:`Right-click` on the **kebun_tegalan layer** in the Layers list.
- Select :guilabel:`Save Selection As`....
- :guilabel:`Name` the new file :kbd:`kebun_tegalan_lokasi_terpilih.shp` and
  check the box next to :guilabel:`Add saved file to map`.  If we hide all the
  other layers, we can see the resulting layer:

.. image:: /static/training/beginner/qgis-inasafe/image229.*
   :align: center

**13. Select Land Areas of the Appropriate Size**

Hooray!  We have now found land areas that meet four of our five criteria.  The
only remaining criteria is the size of the land.  We need to make sure that our
possible locations are between 50000-150000 m².

- :guilabel:`Open the attribute table` for the **kebun_tegalan_lokasi_terpilih**
  layer.  You’ll notice that there is a column named *luas_ha*.  This is the
  size of the area in hectares.  We could use this field to answer our question,
  but let’s add another column that contains the size of the area in
  square meters.

- :guilabel:`Select` the **kebun_tegalan_lokasi_terpilih** layer and
  enter edit mode:

.. image:: /static/training/beginner/qgis-inasafe/image230.*
   :align: center

- :guilabel:`Start the field calculator` (located in the Attribute Table window)

.. image:: /static/training/beginner/qgis-inasafe/image231.*
   :align: center

- :guilabel:`Check the box` next to **Create a new field**.  In the box type
  “luas_m2.”

.. image:: /static/training/beginner/qgis-inasafe/image232.*
   :align: center

- :guilabel:`Click on` **Geometry** and then :guilabel:`double-click` **$area**

.. image:: /static/training/beginner/qgis-inasafe/image233.*
   :align: center

- Click :guilabel:`OK`.
- You should now see a new column on your attribute table, named :kbd:`luas_m2`.
  And QGIS has filled it in for us with square meters!
- Click the edit mode button again, and save your edits.

.. image:: /static/training/beginner/qgis-inasafe/image234.*
   :align: center

- Now we can just do a simple query.
- :guilabel:`Right-click` on the **kebun_tegalan_lokasi_terpilih** layer and
  click :guilabel:`Query`...
- Enter the following:

*"luas_m2" >= 50000 AND "luas_m2" <= 150000*

.. image:: /static/training/beginner/qgis-inasafe/image235.*
   :align: center

- Click :guilabel:`OK`.

.. image:: /static/training/beginner/qgis-inasafe/image236.*
   :align: center

That’s it!  We have eight pieces of land that meet ALL of our criteria.
Any of these pieces of land might be suitable for a location to place refugees.


 

