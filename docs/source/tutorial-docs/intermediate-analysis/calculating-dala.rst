Calculating Damage and Losses
=============================

Learning Objectives
-------------------

- Able to explain the definition of damages, losses, and their calculation based on exposure data from OSM/community participation impacted by disasters
- Understand damage and loss assessment values from BNPB and BPBD
- Manipulate attributes of affected features to obtain damage and loss values for each object
- Group and join attribute data for each administration area (hamlet, village, subdistrict)
- Able to develop thematic maps of damages and losses for each administrative area
- Able to present damages and losses value using charts


Introduction
------------

**A Damage and Loss Assessment (DaLA)** is usually created after after a disaster.  The standard DaLA methodology was developed by the UN Economic Commission for Latin America and the Caribbean (UN-ECLAC) in 1972, and has evolved with various international organizations since.  Simply, it is a methodology for approximating damage and losses due to a disaster, basing calculations on a country's economy and individual livelihoods to define the needs for recovery and reconstruction.
A Damage and Loss Assessment includes the following:
- Damage calculated as the replacement value of totally or partially destroyed physical assets;
- Losses in the flows of  economy that arise from the temporary absence of the damaged assets;
- The resultant impact on post-disaster macroeconomic performance, with special reference to economic growth/GDP, the balance of payments and fiscal situation of the Government.[1]
 
In this chapter we will learn how to calculate some of the basic data used in a DaLA, and use various QGIS functions to design a thematic map that shows damage and loss.
 
1. BPBD Damage Assessment Guide
...............................
The BPBD has created a guide for damage and loss assessment for Indonesia, which defines varying degrees of damage and the economic impact of individual elements.  Parts of this definition are shown here:


These are the guidelines for **Damage & Loss Assessment**.

.. image:: /static/tutorial/intermediate-analysis/6_1.png
   :align: center

Notice that there are several elements at work here.  First, damage to different types of infrastructure is "valued" differently.  To put losses into monetary terms, a the loss of a bridge has a loss value as does the loss of a public building or a private home.  Then, depending on whether a feature suffers heavy, medium, or low damage, a multiplier is applied to determine the value of the loss.


By adding up all of the damage it is possible to assess the total damages caused by a disaster.  In the remainder of this chapter, we will calculate the value of the losses in our Sirahan project, and see how we can display them graphically using our map, based on the damage suffered in each hamlet.


2. Damage and Loss Assessment Map
..................................
We will create a Damage and Loss Assessment Map using our data from Sirahan Village that we have been working with throughout this unit.
- Open QGIS and make sure that the following layers are loaded into your project:
	- **area_terdampak_Sirahan**
	- **Jalan_Sirahan**
	- **Sungai_Sirahan**
	- **Batas_Desa_Sirahan**
	- **Bangunan_Sirahan**

.. image:: /static/tutorial/intermediate-analysis/6_2.png
   :align: center

We will assume that all the buildings in the **area_terdampak_Sirahan layer** (hazard zone) suffered heavy damage from the disaster.  Let's create a spatial query to filter out these buildings.
- Go to Vector ? Spatial Query ? Spatial Query and enter the fields like this:

.. image:: /static/tutorial/intermediate-analysis/6_3.png
   :align: center
   
- We now have a bunch of buildings selected which we are assuming will suffer heavy damages.  According to the BNPB Guide, we can assess the loss of heavily damaged buildings at a rate of 1.8million Rp. / square meter, and the multiplier factor is 70%.  Our formula for calculating losses is:
:samp: Total Building area x Loss Value per m² x Multiplier factor
- Therefore we want to calculate:
	:samp: Total Building Area x 1.8 million Rp. x 70%
    in order to get a calculation of the value of total losses.
- We will use the Intersect Geoprocessing tool so that we can combine attributes from our district layer with the selection of buildings we have just made.  Go to Vector ? Geoprocessing Tools ? Intersect and fill in the fields as follows:

.. image:: /static/tutorial/intermediate-analysis/6_4.png
   :align: center

- Save the result as **Bangunan_Terdampak_perDusun**.
- Hide the original buildings layer so that your map looks like this:

.. image:: /static/tutorial/intermediate-analysis/6_5.png
   :align: center

- Because we used the intersect tool our attribute table will include the DUSUN attribute.

.. image:: /static/tutorial/intermediate-analysis/6_6.png
   :align: center


3. Calculate Damage Area
........................
- On the attribute table of **Bangunan_Terdampak_perDusun**, click the "Toggle Editing" button.

.. image:: /static/tutorial/intermediate-analysis/6_7.png
   :align: center

- Then click the "New Column" button.

.. image:: /static/tutorial/intermediate-analysis/6_8.png
   :align: center

- Create a new column named "Damage" of type decimal number:

.. image:: /static/tutorial/intermediate-analysis/6_9.png
   :align: center

- To calculate the damaged area of affected buildings we will use the field calculator to determine the number of square meters in each building feature.  Click on "Field Calculator."

.. image:: /static/tutorial/intermediate-analysis/6_10.png
   :align: center

- Check the box next to "Update existing field" and select "Damage_Area" in the dropdown box.
- Find "$area" under Geometry in the function list and double-click on it, so that it appears in the Expression box at the bottom.  It should look like this:

.. image:: /static/tutorial/intermediate-analysis/6_11.png
   :align: center

- Click OK.  You will see that the column is filled in with the area, in square meters, of the buildings.

.. image:: /static/tutorial/intermediate-analysis/6_12.png
   :align: center

- Click the "Toggle Editing" button and be sure to save your edits.


4. Damages Group Stats
......................
We will be using a QGIS plugin called Group Stats in order to calculate damages by each hamlet within Sirahan.   You will need to be connected to the internet to install this plugin.
- Go to Plugins > Fetch Python Plugins.
- Type "group stats" and when you find the plugin, select it and click "Install."
- Once it is installed, go to Plugins > Group Stats > Group Stats

.. image:: /static/tutorial/intermediate-analysis/6_13.png
   :align: center

- In  'Choose vector layer' choose Bangunan_Terdampak_perDusun
- In  'Choose classification field' fill in 'DUSUN'
- In  'Choose field attributes' fill in 'Damage'.
- Click on "Calculate."  The results should look like this:

.. image:: /static/tutorial/intermediate-analysis/6_14.png
   :align: center

- Select all the rows by clicking on the top row, holding SHIFT, and clicking on the last row.
- Click "Save" and save it as **BNG_Damages**.


5. Calculate Losses
...................
Now we've calculated the damaged area and we've created a table with damage data for various hamlets in Sirahan.  Now let's implement our losses formula in the same way.
- Go back to the attribute table for **Bangunan_Terdampak_perDusun**  and add a new column named "Losses."

.. image:: /static/tutorial/intermediate-analysis/6_15.png
   :align: center

- Once again, open the Field Calculator.
- Check "Update existing field" and choose "Losses"
- At the bottom in the Expression box, enter the following formula:
:samp: "Damage" * 1800000 * 0.7

.. image:: /static/tutorial/intermediate-analysis/6_16.png
   :align: center

- Your new column is now filled with information calculated from this formula, which assesses the value of losses in Rp for each individual building.  Save the layer and end the editing session.


6. Losses Group Stats
.....................
Now let's calculate losses per hamlet using Group Stats again.
- In  'Choose vector layer' choose Bangunan_Terdampak_perDusun
- In 'Choose classification field' type in 'DUSUN'
- In 'Choose field attributes' fill in 'Losses'.
- Click "Calculate."  

.. image:: /static/tutorial/intermediate-analysis/6_17.png
   :align: center

- The new table shows the losses in each hamlet.
- Select all the rows in the table and click "Save". Save as BNG_Losses.

7. Join Data
............
Now we will join the tables that we created to our Batas_Desa_Sirahan attribute table and then use them to add new columns to the file.
- Add the files **BNG_Damages** and **BNG_Losses** into QGIS, using "Add vector layer"
 
.. image:: /static/tutorial/intermediate-analysis/6_18.png
   :align: center

- They will appear in your Layers list but not on your map, because they are not geographic data files, but rather tables.

.. image:: /static/tutorial/intermediate-analysis/6_19.png
   :align: center

- Now we will perform an operation to join the layer **Batas_Desa_Sirahan** with **BNG_Damage**. Right click on the **Batas_Desa_Sirahan** layer and go to Properties.
- Go to the Joins tab:

.. image:: /static/tutorial/intermediate-analysis/6_20.png
   :align: center

- Click the plus sign and fill in the following fields:
	- Join layer : BNG_Damages
	-  Join field: DUSUN
	- Target field : DUSUN
- Click OK.
- Open the Attribute Table for **Batas_Desa_Sirahan**.  You can see that the table we calculated with group stats is now attached to our attributes for each hamlet.
- Click toggle *editing* and choose Field *Calculator*.
- This time we will create a new field inside the field calculator.  Fill in the top of the window like this:

.. image:: /static/tutorial/intermediate-analysis/6_21.png
   :align: center
   
- Then in the expression box, enter
"Sum"

.. image:: /static/tutorial/intermediate-analysis/6_22.png
   :align: center

 
-  Click OK.  The *BNG_Dmg* column now contains the same value as column Sum in **BNG_Damage.csv**
- As the damage values for each hamlet have been obtained we can delete the join.  Right-click **Batas_Desa_Sirahan**, select properties, go to the Join tab, and click the minus button.

.. image:: /static/tutorial/intermediate-analysis/6_23.png
   :align: center

- Now click the plus button, but this time join **BNG_Losses** in the same way as before:
 
.. image:: /static/tutorial/intermediate-analysis/6_24.png
   :align: center

- Open the attribute table for **Batas_Desa_Sirahan**, click toggle editing and open the Field Calculator.  Fill in as follows:

.. image:: /static/tutorial/intermediate-analysis/6_25.png
   :align: center


- Click OK and save the layer.
- Now that we have calculated the loss value and saved it in a new column, we can remove the join.  Open the layer properties and click the minus button to remove the join with **BNG_Losses**. 
- The attribute table when you finish will look like this:

.. image:: /static/tutorial/intermediate-analysis/6_26.png
   :align: center


8. Create a Chart
.................
Now we will conclude by representing these damage and loss values as a chart in QGIS.
- Go the the properties for the **Batas_Desa_Sirahan** layer and go to the Overlay tab.
- Check the box next to "Display diagrams."
- Make sure "Pie chart" is selected in the dropdown.
- Choose BNG_Dmg next to "Attributes" and click Add.
- The following dropdown boxes should read "linearly scaling" and "BNG_Dmg."
- Click "Find Maximum Value."
- In the size box enter "500."

.. image:: /static/tutorial/intermediate-analysis/6_27.png
   :align: center

- The resulting map will look like this:

.. image:: /static/tutorial/intermediate-analysis/6_28.png
   :align: center


The size of each bubble represents the loss values in each hamlet. The bigger the size, the heavier the losses.  Creating a map with this sort of chart can be an effective way to communicate the impact of a disaster.




Summary
-------

In this chapter we have learned about methodology for evaluating losses, and we have learned how to calculate this in QGIS.  We also learned how to export tables, join them with shapefiles, and overlay charts on top of our map.


________________
[1] Source:https://www.gfdrr.org/gfdrr/Track-III-TA-Tools