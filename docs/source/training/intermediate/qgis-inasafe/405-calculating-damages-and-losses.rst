.. image:: /static/training/intermediate/qgis-inasafe/image7.*

Module 5: Calculating Damages and Losses
========================================

**Learning Objectives**

- Explain the definition of damages, losses, and their calculation based on
  exposure data from OSM/community participation which is impacted by disasters
- Explain damage and losses assessment values based on BNPB and BPBD
- Making damage and losses map
- Calculate damage area
- Manipulate attributes data of affected features to obtain damage values for
  each object
- Manipulate attributes data of affected features to obtain losses values for
  each object
- Grouping attributes data for each administration area (hamlet, village,
  subdistrict)
- Join attribute data for each administration area (hamlet, village,
  subdistrict)
- Present damages and losses value using charts

**A Damage and Loss Assessment (DaLA)** is usually created after after a
disaster.
The standard DaLA methodology was developed by the UN Economic Commission for
Latin America and the Caribbean (UN-ECLAC) in 1972,
and has evolved with various international organizations since.
Simply, it is a methodology for approximating damage and losses due to a
disaster, basing calculations on a country’s economy and individual
livelihoods to define the needs for recovery and reconstruction.

A Damage and Loss Assessment includes the following:

- Damage calculated as the replacement value of totally or partially destroyed
  physical assets;
- Losses in the flows of  economy that arise from the temporary absence of the
  damaged assets;
- The resultant impact on post-disaster macroeconomic performance, with special
  reference to economic growth/GDP, the balance of payments and fiscal situation
  of the Government.

In this Module we will learn how to calculate some of the basic data used in a
DaLA, and use various QGIS functions to design a thematic map that shows
damage and loss.

**1. BPBD Damage Assessment Guide**

The BPBD has created a guide for damage and loss assessment for Indonesia,
which defines varying degrees of damage and the economic impact of individual
elements.
Parts of this definition are shown here:

These are the guidelines for **Damage & Loss Assessment.**

.. image:: /static/training/intermediate/qgis-inasafe/image83.*
   :align: center

Notice that there are several elements at work here.  First,
damage to different types of infrastructure is “valued” differently.
To put losses into monetary terms, a the loss of a bridge has a loss value as
does the loss of a public building or a private home.
Then, depending on whether a feature suffers heavy, medium, or low damage,
a multiplier is applied to determine the value of the loss.

By adding up all of the damage it is possible to assess the total damages
caused by a disaster.
In the remainder of this Module, we will calculate the value of the losses in
our Sirahan project, and see how we can display them graphically using our
map, based on the damage suffered in each hamlet.

**2. Damage and Losses Assessment Map**

We will create a Damage and Loss Assessment Map using our data from Sirahan
Village that we have been working with throughout this module.

- Open QGIS and make sure that the following layers are loaded into your project:
    - area_terdampak_Sirahan
    - Jalan_Sirahan
    - Sungai_Sirahan
    - Batas_Desa_Sirahan
    - Bangunan_Sirahan

.. image:: /static/training/intermediate/qgis-inasafe/image84.*
   :align: center

We will assume that all the buildings in the area_terdampak_Sirahan layer
(hazard zone) suffered heavy damage from the disaster.
Let’s create a spatial query to filter out these buildings.

- Go to :menuselection:`Vector > Spatial Query > Spatial Query` and enter the
  fields like this:

.. image:: /static/training/intermediate/qgis-inasafe/image85.*
   :align: center

- We now have a bunch of buildings selected which we are assuming will suffer
  heavy damages. According to the BNPB Guide, we can assess the loss of heavily 
  damaged buildings at a rate of 1.8million Rp. / square meter, and the 
  multiplier factor is 70%. Our formula for calculating losses is:

*Total Building area x Loss Value per m² x Multiplier factor*

- Therefore we want to calculate:

**Total Building Area x 1.8 million Rp. x 70%**

in order to get a calculation of the value of total losses.

- We will use the Intersect Geoprocessing tool so that we can combine
  attributes from our district layer with the selection of buildings we have
  just made.
- Go to :menuselection:`Vector > Geoprocessing Tools > Intersect` and fill in
  the fields as follows:

.. image:: /static/training/intermediate/qgis-inasafe/image86.*
   :align: center

- Save the result as Bangunan_Terdampak
- Hide the original buildings layer so that your map looks like this:

.. image:: /static/training/intermediate/qgis-inasafe/image87.*
   :align: center

- Then, we need to intersect bangunan_terdampak.shp layer with 
  Batas_Desa_Sirahan layer so our attribute table will include the DUSUN 
  attribute. Give the new layer name with bangunan_terdampak_perdusun.shp

.. image:: /static/training/intermediate/qgis-inasafe/image88.*
   :align: center

**3. Calculate Damage Area**

- On the attribute table of Bangunan_Terdampak_perDusun, click the
  :guilabel:`Toggle Editing` button.

.. image:: /static/training/intermediate/qgis-inasafe/image89.*
   :align: center

- Then click the :guilabel:`New Column` button.

.. image:: /static/training/intermediate/qgis-inasafe/image90.*
   :align: center

- Create a new column named :kbd:`Damage` of type decimal number:

.. image:: /static/training/intermediate/qgis-inasafe/image91.*
   :align: center

- To calculate the damaged area of affected buildings we will use the field
  calculator to determine the number of square meters in each building feature.
  Click on :guilabel:`Field Calculator`.

.. image:: /static/training/intermediate/qgis-inasafe/image92.*
   :align: center

- Check the box next to :guilabel:`Update existing field` and select
  “Damage_Area” in the dropdown box.
- Find :menuselection:`$area` under :guilabel:`Geometry` in the function list
  and double-click on it, so that it appears in the Expression box at the
  bottom. It should look like this:

.. image:: /static/training/intermediate/qgis-inasafe/image93.*
   :align: center

- Click :guilabel:`OK`. You will see that the column is filled in with the area, 
  in square meters, of the buildings.

.. image:: /static/training/intermediate/qgis-inasafe/image94.*
   :align: center

- Click the :guilabel:`Toggle Editing` button and be sure to save your edits.

**4. Calculate Damages Using “Group Stats” Plugin**

We will be using a QGIS plugin called Group Stats in order to calculate damages
by each hamlet within Sirahan.
You will need to be connected to the internet to install this plugin.

- Go to :menuselection:`Plugins > Manage and InstallPlugins`.
- Go to :guilabel:`Get more` tab, type :kbd:`group stats` and when you find the 
  plugin, select it and click :guilabel:`Install`.

.. image:: /static/training/intermediate/qgis-inasafe/image95.*
   :align: center

- Once it is installed, you will find Group Stats on your Toolbar. Click it.

.. image:: /static/training/intermediate/qgis-inasafe/image96.*


- Then, Group Stats window will shows up.
- To calculate building damages per hamlet, in :guilabel:`layers`, 
  select: Bangunan_Terdampak_perDusun
- Find "Dusun" on the field list, then drag and drop to :guilabel:`Rows`
- Find "Damage" and "sum" on the field list, then drag and drop to 
  :guilabel:`Value`
- Click on :guilabel:`Calculate`  The results should look like this:


.. image:: /static/training/intermediate/qgis-inasafe/image97.*
   :align: center

- Click :menuselection:`Data > Save all to CSV files` and save it as BNG_Damages.

**5. Calculate Losses**

Now we’ve calculated the damaged area and we’ve created a table with damage
data for various hamlets in Sirahan.
Now let’s implement our losses formula in the same way.

- Go back to the attribute table for Bangunan_Terdampak_perDusun and add a new
  column named "Losses."

.. image:: /static/training/intermediate/qgis-inasafe/image98.*
   :align: center

- Once again, open the :guilabel:`Field Calculator`.
- Check :guilabel:`Update existing field` and choose “Losses”
- At the bottom in the Expression box, enter the following formula:

*“Damage” * 1800000 * 0.7*

.. image:: /static/training/intermediate/qgis-inasafe/image99.*
   :align: center

- Your new column is now filled with information calculated from this formula,
  which assesses the value of losses in Rp for each individual building.
  Save the layer and end the editing session.

**6. Calculating Losses Using “Group Stats” Plugin**

Now let’s calculate losses per hamlet using Group Stats again.

- Open Group Stat window. Then select bangunan_terdampak_perdusun layer
- Click :guilabel:`Clear` to start new analysis
- Find DUSUN on the field list, then drag and drop to :guilabel:`Rows` 
- Find "Losses" and "sum" on the field list, then drag and drop to 
  :guilabel:`Values`
- Click :guilabel:`Calculate`

.. image:: /static/training/intermediate/qgis-inasafe/image100.*
   :align: center

- The new table shows the losses in each hamlet.
- Click :menuselection:`Data > Save all to CSV files`. Save as BNG_Losses

**7. Join Data**

Now we will join the tables that we created to our Batas_Desa_Sirahan attribute
table and then use them to add new columns to the file.

- Add the files BNG_Damages and BNG_Losses into QGIS, using
  :guilabel:`Add vector layer`. Make sure you click on file type as CSV,
  otherwise, the CSV file won't shows up.

.. image:: /static/training/intermediate/qgis-inasafe/image101.*
   :align: center

- They will appear in your Layers list but not on your map,
  because they are not geographic data files, but rather tables.

.. image:: /static/training/intermediate/qgis-inasafe/image102.*
   :align: center

- Now we will perform an operation to join the layer Batas_Desa_Sirahan with
  BNG_Damage. Right click on the Batas_Desa_Sirahan layer and go to Properties.
- Go to the Joins tab:

.. image:: /static/training/intermediate/qgis-inasafe/image103.*
   :align: center

- Click the plus sign and fill in the following fields:
    - Join layer : BNG_Damages
    - Join field: DUSUN
    - Target field : DUSUN

.. image:: /static/training/intermediate/qgis-inasafe/image104.*
   :align: center

- Click :guilabel:`OK`

- Click the plus sign again and fill in the following fields:
    - Join layer : BNG_Losses
    - Join field: DUSUN
    - Target field : DUSUN

- Click :guilabel:`OK`
- Close layer properties, now open the attribute tables for Batas_Desa_Sirahan 
  layer. You will see that BNG_Damages and BNG_Losses column now attached 
  based on its hamlet.

.. image:: /static/training/intermediate/qgis-inasafe/image105.*
   :align: center

- Remember that we won’t have BNG_Damages and BNG_Losses column permanently 
  because it’s being saved on our virtual memory. So, we need to save it as a 
  new layer. Close the attribute table, right-click Batas_Desa_Sirahan layer, 
  and click :guilabel:`Save as`. Give the new layer name 
  analisis_dala_Sirahan.shp
- We need to convert the BNG_Damages and BNG_Losses column on our new layer 
  as real number. To do this open attribute table for analisis_dala_Sirahan. 
  Click toggle editing mode and open Field Calculator. 
- This time, we will create a new field. 
  Enter the new field name: Damages, with output field as decimal number (real). 
  Field width 20 and Precision 10. Under Fields and Values, double click 
  BNG_Damage. Our setting now should look like this. 

.. image:: /static/training/intermediate/qgis-inasafe/image106.*
   :align: center


- Click :guilabel:`OK`.
- Now, we will create another new field for Losses. Enter the new field name: 
  Losses, with output field as decimal number (real). Field width 20 and 
  Precision 10. Under Fields and Values, double click BNG_Losses. Click 
  :guilabel:`OK`. 
- Exit editing mode and save your changes.


**8. Create a Chart**

Now we will conclude by representing these damage and loss values as a chart in QGIS.

- Go the the properties for the analisis_dala_Sirahan layer and go to the 
  :guilabel:`Diagram` tab.
- Check the box next to :guilabel:`Display diagrams`
- Make sure :guilabel:`Pie chart` is selected in the dropdown.
- On Available attributes, select "Damages" then click plus (+) sign
- You can change the color by double-clicking the color on the Assigned 
  attribute column. Our setting should look like this

.. image:: /static/training/intermediate/qgis-inasafe/image107.*
   :align: center


- Go to the size tab
- Disabled the fixed value, and then click :guilabel:`Find Maximum Value`
  Change the scale into Area.

.. image:: /static/training/intermediate/qgis-inasafe/image108.*
   :align: center

- You also can change the size for example 35 if you feel the diagram is too big.
- The resulting map will look like this:

.. image:: /static/training/intermediate/qgis-inasafe/image109.*
   :align: center

The size of each bubble represents the loss values in each hamlet. The bigger 
the size, the heavier the losses.  Creating a map with this sort of chart can 
be an effective way to communicate the impact of a disaster. Now you can layout 
your map, then try to create another map with diagram showing Losses.

In this Module we have learned about methodology for evaluating losses, and we 
have learned how to calculate this in QGIS.  We also learned how to export 
tables, join them with shapefiles, and overlay charts on top of our map.

