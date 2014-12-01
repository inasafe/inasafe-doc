.. image:: /static/training/intermediate/qgis-inasafe/image7.*

..  _calculating-damages-and-losses:

Module 5: Calculating Damages and Losses
========================================

**Learning Objectives**

- Understand the definition of damages, losses and their calculation based 
  on community exposure data
- Understand damage and losses assessment values based on BNPB and BPBD
- Make a damage and losses map
- Calculate damage area
- Manipulate attribute data of affected features to obtain damage values for
  each object
- Manipulate attribute data of affected features to obtain loss values for
  each object
- Group attribute data for administrative areas (hamlet, village,
  subdistrict)
- Join attribute data for administrative areas (hamlet, village,
  subdistrict)
- Present damage and loss values using charts

A **Damage and Loss Assessment (DaLA)** is usually created after a
disaster.
The standard DaLA methodology was developed by the UN Economic Commission for
Latin America and the Caribbean (UN-ECLAC) in 1972,
and has evolved with various international organisations since.
Simply, it is a methodology for approximating damage and losses due to a
disaster, basing calculations on a country’s economy and individual
livelihoods to define the needs for recovery and reconstruction.

A Damage and Loss Assessment includes the following:

- Damage calculated as the replacement value of totally or partially destroyed
  physical assets
- Losses in the flows of economy that arise from the temporary absence of the
  damaged assets
- The resultant impact on post-disaster macroeconomic performance, with special
  reference to economic growth/GDP, the balance of payments and fiscal situation
  of the government.

In this module we will learn how to calculate some of the basic data used in a
DaLA, and use various QGIS functions to design a thematic map that shows
damage and loss.

1. BPBD damage assessment guide
-------------------------------

The BPBD has created a guide for damage and loss assessment for Indonesia,
which defines varying degrees of damage and the economic impact of individual
elements.
Parts of this definition are shown here:

.. image:: /static/training/intermediate/qgis-inasafe/image83.*
   :align: center

Notice that there are several elements at work here. First,
damage to different types of infrastructure is “valued” differently.
To put losses into monetary terms, the loss of a bridge has a loss value as
does the loss of a public building or a private home.
Then, depending on whether a feature suffers heavy, medium or low damage,
a multiplier is applied to determine the value of the loss.

By adding up all of the damage it is possible to assess the total damages
caused by a disaster.
In the remainder of this module, we will calculate the value of the losses in
our Sirahan project, and see how we can display them graphically using our
map, based on the damage suffered in each hamlet.

2. Damage and losses assessment map
-----------------------------------

We will create a damage and loss assessment map using our data from Sirahan
village that we have been working with throughout this unit.

1. Open QGIS and make sure that the following layers are loaded into your project:

  - area_terdampak_Sirahan
  - Jalan_Sirahan
  - Sungai_Sirahan
  - Batas_Desa_Sirahan
  - Bangunan_Sirahan

.. image:: /static/training/intermediate/qgis-inasafe/image84.*
   :align: center

We will assume that all the buildings in the :guilabel:`area_terdampak_Sirahan` 
layer (hazard zone) suffered heavy damage from the disaster.
Let’s create a spatial query to filter out these buildings.

2. Go to :menuselection:`Vector ‣ Spatial Query ‣ Spatial Query` and enter the
   fields like this:

.. image:: /static/training/intermediate/qgis-inasafe/image85.*
   :align: center

We now have a group of buildings selected which we are assuming will suffer
heavy damages. According to the BNPB Guide, we can assess the loss of heavily 
damaged buildings at a rate of 1.8 million Rp. per square metre, and the 
multiplier factor is 70%. Our formula for calculating losses is:

  *Total Building area x Loss Value per m² x Multiplier factor*

Therefore we want to calculate:

  *Total Building Area x 1.8 million Rp. x 70%*

in order to get a calculation of the value of total losses.

We will use the Intersect Geoprocessing tool so that we can combine
attributes from our district layer with the selection of buildings we have
just made.

3. Go to :menuselection:`Vector ‣ Geoprocessing Tools ‣ Intersect` and fill in
   the fields as follows:

.. image:: /static/training/intermediate/qgis-inasafe/image86.*
   :align: center

4. Save the result as :kbd:`Bangunan_Terdampak`.

5. Hide the original buildings layer so that your map looks like this:

.. image:: /static/training/intermediate/qgis-inasafe/image87.*
   :align: center

6. Run Intersect again, this time with the new :guilabel:`Bangunan_Terdampak` 
   layer and the :guilabel:`Batas_Desa_Sirahan` layer, so that the attribute 
   table will include the DUSUN attribute. Name the new layer 
   :kbd:`bangunan_terdampak_perdusun.shp`.

.. image:: /static/training/intermediate/qgis-inasafe/image88.*
   :align: center

3. Calculating damage area
--------------------------

7. On the attribute table of :guilabel:`bangunan_terdampak_perdusun`, 
   click the :guilabel:`Toggle Editing` button.

.. image:: /static/training/intermediate/qgis-inasafe/image89.*
   :align: center

8. Click the :guilabel:`New Column` button.

.. image:: /static/training/intermediate/qgis-inasafe/image90.*
   :align: center

9. Create a new column named :kbd:`Damage` of type decimal number:

.. image:: /static/training/intermediate/qgis-inasafe/image91.*
   :align: center

10. To calculate the damaged area of affected buildings we will use the field
    calculator to determine the number of square metres in each building 
    feature. Click on :guilabel:`Field Calculator`.

.. image:: /static/training/intermediate/qgis-inasafe/image92.*
   :align: center

11. Check the box next to :guilabel:`Update existing field` and select
    :guilabel:`Damage_Area` in the drop-down box.

12. Find :guilabel:`$area` under :guilabel:`Geometry` in the function list
    and double-click on it, so that it appears in the Expression box at the
    bottom. It should look like this:

.. image:: /static/training/intermediate/qgis-inasafe/image93.*
   :align: center

13. Click :guilabel:`OK`. You will see that the column is filled in with the area, 
    in square metres, of the buildings.

.. image:: /static/training/intermediate/qgis-inasafe/image94.*
   :align: center

14. Click the :guilabel:`Toggle Editing` button and be sure to save your edits.

4. Calculating damages using the Group Stats plugin
---------------------------------------------------

We will be using a QGIS plugin called Group Stats in order to calculate damages
by each hamlet within Sirahan.
You must be connected to the internet to install this plugin.

15. Go to :menuselection:`Plugins ‣ Manage and Install Plugins`.

16. Go to the :guilabel:`Get more` tab. Type :kbd:`group stats`. When you find the 
    plugin, select it and click :guilabel:`Install`.

.. image:: /static/training/intermediate/qgis-inasafe/image95.*
   :align: center

17. Once it is installed, you will find Group Stats on your Toolbar. Click it.
    
.. image:: /static/training/intermediate/qgis-inasafe/image96.*
   :align: center

The Group Stats window will appear.

18. To calculate building damages per hamlet, select 
    :guilabel:`bangunan_terdampak_perdusun`
    in the drop-down box under :guilabel:`layers`.

19. Find :guilabel:`Dusun` in the list of fields. Drag and drop it 
    to :guilabel:`Rows`.

20. Find :guilabel:`Damage` and :guilabel:`sum` in the list of fields. Drag and
    drop them to :guilabel:`Value`.

21. Click :guilabel:`Calculate`. The results should look like this:

.. image:: /static/training/intermediate/qgis-inasafe/image97.*
   :align: center

22. Go to :menuselection:`Data ‣ Save all to CSV files` and save it as 
    :kbd:`BNG_Damages`.

5. Calculating losses
---------------------

We’ve calculated the damaged area and we’ve created a table with damage
data for various hamlets in Sirahan.
Now let’s implement our losses formula in the same way.

23. Go back to the attribute table for :guilabel:`bangunan_terdampak_perdusun` 
    and add a new column named :kbd:`Losses`.

.. image:: /static/training/intermediate/qgis-inasafe/image98.*
   :align: center

24. Open the :guilabel:`Field Calculator`.

25. Check the box next to :guilabel:`Update existing field` and choose 
    :guilabel:`Losses` in the function list.

26. At the bottom in the Expression box, enter the following formula:

  *“Damage” * 1800000 * 0.7*

.. image:: /static/training/intermediate/qgis-inasafe/image99.*
   :align: center

Your new column is now filled with information calculated from this formula,
which assesses the value of losses in Rp for each individual building.

27. Save the layer and end the editing session.

6. Calculating losses using the Group Stats plugin
--------------------------------------------------

Now let’s calculate losses per hamlet using the Group Stats again.

28. Open the Group Stats window.

29. Select :guilabel:`bangunan_terdampak_perdusun`
    in the drop-down box under :guilabel:`layers`.

30. Click :guilabel:`Clear` to start a new analysis.

31. Find :guilabel:`Dusun` in the list of fields. Drag and drop it 
    to :guilabel:`Rows`.

32. Find :guilabel:`Losses` and :guilabel:`sum` in the list of fields. Drag and
    drop them to :guilabel:`Value`.

33. Click :guilabel:`Calculate`. The new table shows the losses in each hamlet:

.. image:: /static/training/intermediate/qgis-inasafe/image100.*
   :align: center

34. Go to :menuselection:`Data ‣ Save all to CSV files` and save it as 
    :kbd:`BNG_Losses`.

7. Joining data
---------------

Now we will join the tables that we created to our 
:guilabel:`Batas_Desa_Sirahan` attribute
table and then use them to add new columns to the file.

35. Add the files :file:`BNG_Damages` and :file:`BNG_Losses` into QGIS, using
    :guilabel:`Add vector layer`. Make sure you set the file type as CSV in
    the dialog so that CSV files appear.

.. image:: /static/training/intermediate/qgis-inasafe/image101.*
   :align: center

36. The new files will appear in your Layers panel but not on your map,
    because they are not geographic data files, but rather tables.

.. image:: /static/training/intermediate/qgis-inasafe/image102.*
   :align: center

37. Now we will perform an operation to join the layer 
    :guilabel:`Batas_Desa_Sirahan` with
    :guilabel:`BNG_Damage`. Right-click on the :guilabel:`Batas_Desa_Sirahan` 
    layer and open the Properties window.

38. Go to the Joins tab:

.. image:: /static/training/intermediate/qgis-inasafe/image103.*
   :align: center

39. Click the plus sign and fill in the following fields:

  - Join layer: BNG_Damages
  - Join field: DUSUN
  - Target field: DUSUN

.. image:: /static/training/intermediate/qgis-inasafe/image104.*
   :align: center

40. Click :guilabel:`OK`.

41. Click the plus sign again and fill in the following fields:

  - Join layer : BNG_Losses
  - Join field: DUSUN
  - Target field : DUSUN

42. Click :guilabel:`OK`.

43. Close the Properties window. Open the attribute table for 
    :guilabel:`Batas_Desa_Sirahan`.
    The BNG_Damages and BNG_Losses columns 
    are now attached based on the hamlet.

.. image:: /static/training/intermediate/qgis-inasafe/image105.*
   :align: center

44. Note that the BNG_Damages and BNG_Losses columns are not permanently 
    attached, but rather joined together with our file in the computer
    memory. We should save it as a new layer. Close the attribute table.
    Right-click the :guilabel:`Batas_Desa_Sirahan` layer
    and click :guilabel:`Save as`. Name the new layer 
    :kbd:`analisis_dala_Sirahan.shp`.

45. We need to convert the BNG_Damages and BNG_Losses column in our new layer 
    to real numbers. Open the attribute table for 
    :guilabel:`analisis_dala_Sirahan`. 
    Click the :guilabel:`Toggle editing` button and open the Field Calculator. 

46. This time, we will create a new field. 
    Enter as the new field name :kbd:`Damages`, with the output field type
    as :guilabel:`Decimal number (real)`. 
    Enter :kbd:`20` as the field width and the precision as :kbd:`10`. Under 
    the function list double-click :guilabel:`BNG_Damage`.
    The window should look like this:

.. image:: /static/training/intermediate/qgis-inasafe/image106.*
   :align: center

47. Click :guilabel:`OK`.

48. Now, we will create another new field for Losses. Enter as the new field 
    name :kbd:`Losses`, with the output field type
    as :guilabel:`Decimal number (real)`. 
    Enter :kbd:`20` as the field width and the precision as :kbd:`10`. Under 
    the function list double-click :guilabel:`BNG_Losses`.
    Click :guilabel:`OK`.

49. Exit editing mode and save your changes.


8. Creating a chart
-------------------

We will conclude by representing these damage and loss values as a chart in QGIS.

50. Open the the Properties window for :guilabel:`analisis_dala_Sirahan`. Go 
    to the :guilabel:`Diagram` tab.

51. Check the box next to :guilabel:`Display diagrams`

52. Make sure :guilabel:`Pie chart` is selected in the drop-down box.

53. Under :guilabel:`Available attributes`, select :guilabel:`Damages` 
    and click the plus(+) button.

54. You can change the colour by double-clicking the colour under 
    :guilabel:`Assigned attributes`. The settings should look like this:

.. image:: /static/training/intermediate/qgis-inasafe/image107.*
   :align: center

55. Go to the :guilabel:`Size` tab.

56. Disable the fixed value, and then click :guilabel:`Find Maximum Value`.
    Change the scale value to :guilabel:`Area`.

.. image:: /static/training/intermediate/qgis-inasafe/image108.*
   :align: center

57. You may change the value next to :guilabel:`Size` also if you feel the 
    diagram is too big.

The resulting map will look like this:

.. image:: /static/training/intermediate/qgis-inasafe/image109.*
   :align: center

The size of each bubble represents the loss values in each hamlet. The bigger 
the size, the heavier the losses. Creating a map with this sort of chart can 
be an effective way to communicate the impact of a disaster. Now you can lay 
out your map, and then create another map showing Losses.

