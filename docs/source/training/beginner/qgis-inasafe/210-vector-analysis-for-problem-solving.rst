.. image:: /static/training/beginner/qgis-inasafe/image7.*

..  _vector-analysis-for-problem-solving:

Module 10: Vector Analysis for Problem Solving
==============================================

**Learning Objectives**

- Understand GIS process
- Identify addressable problems
- Understand data needs
- Start a QGIS project
- Analyse problems
- Identify hazard zones
- Look for important roads
- Look for medical facilities
- Buffer roads & medical facilities
- Analyse overlapped areas

The power of GIS is its ability to help us analyse data. Vector data can be
analysed to reveal how different features interact with each other. In this
module, we’ll work through the GIS process, attempting to solve a problem, and
as we proceed, we will learn about various analysis tools that QGIS provides.

1. The GIS process
------------------

Before we start, it will be useful to give a brief overview of a process that
can be used to solve any GIS problem. The steps are simple:

    1) State the problem
    2) Get the data
    3) Analyse the problem
    4) Present the results

2. Problem
----------

Let’s start off by deciding on a problem to solve. Imagine that you’re
a disaster manager, and you need to provide the best locations to place refugees
(IDPs) in villages surrounding Mount Merapi when it erupts. You’ve come up with
the following criteria for these locations:

    1) The area should be a dry field or farm in the districts Ngemplak, Turi or
       Pakem.
    2) The area must be outside of Merapi Eruption Disaster Prone Region III.
    3) Access to the site should be easy, so it will not be more than 300
       metres from a main road.
    4) The site should be close to health facilities.
    5) The land area should be between 50000-150000 m².

3. Data
-------

To answer these questions, we’re going to need the following data:

    1) Landuse in Sleman regency
    2) Streets in Sleman
    3) Location of health facilities
    4) KRB Merapi (Merapi Eruption Disaster Prone Region - this is the
       same data that we learned how to georeference in the previous module)

.. note:: For this exercise the data has been provided already, but in a real
   scenario you may need to find providers for the datasets in question. In
   Indonesia, the National Land Agency and BNPB Bappeda are good sources for the
   types of data you will need, and OpenStreetMap can be used as a source for
   roads and infrastructure.

4. Start a project
------------------

Now that we know what we want to do, let’s start doing it!

1. Start a new QGIS project.

.. image:: /static/training/beginner/qgis-inasafe/image206.*
   :align: center

2. Start adding the layers we will use. In the :file:`Sleman/Merapi` folder,
   add the layers :file:`jalan_sleman_49S`, :file:`tempat_penting_Sleman_49S`,
   :file:`KRB3_49S` and :file:`vegetasi_49S`. Your Layers panel should look 
   like this:

.. image:: /static/training/beginner/qgis-inasafe/image207.*
   :align: center

.. note::  Most of the layers are pretty self-explanatory, but what are KRB3,
   KRB2, and KRB1? These layers show areas of impact when Merapi erupts. KRB3 is
   the area of worst impact, KRB2 is medium, and KRB1 has little impact. In
   this scenario we want to find locations that are not within KRB3.

The data we are working with now is similar to that from previous modules, but
now it is in a Projected Coordinate System. The previous data was saved in
WGS84 - this meant that the coordinates of our features were stored in degrees,
which aren’t very good for measuring size or distance. By using a projected
system our coordinates are in metres, which is important for analysis, because
we can easily measure distances between and around features.

3. Rename the layers by right-clicking on them and selecting :guilabel:`Rename`.

4. Give them the new, simpler names :guilabel:`jalan`, :guilabel:`lokasi_penting`,
   :guilabel:`KRB III` and :guilabel:`vegetasi`.

5. Save your project as :kbd:`merapi_analisis.qgs`.

6. In your operating system’s file manager, create a
   new folder under :file:`qgis/Sleman/Merapi` and call it
   :file:`evakuasi_bencana`.

This is where you’ll save the datasets that we will create during our anaysis.

Now that we’ve got the data, let’s analyse the problem!

5. Analysing the problem: farms and dry fields
----------------------------------------------

The first criterion we’re facing is that the land must be a farm or dry field,
and it must be in one of three areas. So let’s tell QGIS to only show us the
farms and dry fields that are, in fact, in these sub-districts!

7. Right-click on the :guilabel:`vegetasi` layer in the Layers panel.

8. Click :guilabel:`Filter...` This opens the Query Builder dialog.

.. image:: /static/training/beginner/qgis-inasafe/image208.*
   :align: center

9. Scroll down in the Fields list on the left of this dialog until
   you see the field :guilabel:`kec`. Click on it once.

10. Click the :guilabel:`All` button underneath the Values list:

.. image:: /static/training/beginner/qgis-inasafe/image209.*
   :align: center

Next we are going to build a query. A query is a statement that allows us to 
show only the data that we want from a layer. In this case, we want to instruct 
QGIS to only show us farms and dry fields which have a sub-district value equal to
Ngemplak, Turi, or Pakem.

11. Double-click :guilabel:`kec` in the Fields list.

12. Click the :guilabel:`=` button (under Operators).

.. image:: /static/training/beginner/qgis-inasafe/image210.*
   :align: center

13. Double-click the value :guilabel:`Ngemplak` in the Values list.

14. Click :guilabel:`OR`.

15. Repeat these steps twice more, using the values :guilabel:`Turi` and 
    :guilabel:`Pakem` instead of :guilabel:`Ngemplak`. The query should 
    look like this:

.. image:: /static/training/beginner/qgis-inasafe/image211.*
   :align: center

16. Click :guilabel:`AND`.

17. Now highlight :guilabel:`guna_lahan` in the Fields list,
    and click the :guilabel:`All` button to load the values.

18. Double-click :guilabel:`guna_lahan`. Then click the :guilabel:`=` button.
    Then double-click the value :guilabel:`KEBUN`.

19. Click :guilabel:`OR`.

20. Repeat the previous step but instead of :guilabel:`KEBUN` use 
    :guilabel:`TEGALAN`. Your query should look like this:

.. image:: /static/training/beginner/qgis-inasafe/image212.*
   :align: center

The idea is that query will filter the data layer so that it will only show us
features that we want that is, farms and dry fields in Pakem, Turi, and
Ngemplak.

21. We need to add one more thing to our query: parentheses.
    Without these, our query won’t work quite right.
    Add two pairs of parentheses on each side of the word AND, like so:

.. image:: /static/training/beginner/qgis-inasafe/image213.*
   :align: center

22. Click :guilabel:`OK`. The :guilabel:`vegetasi` layer has far fewer features 
    now.

.. image:: /static/training/beginner/qgis-inasafe/image214.*
   :align: center

Well done!  We’ve applied our first criteria to begin solving the problem!

6. Danger zone
--------------

Our next criteria is that our chosen location should be outside of the danger
zone, which is defined by the layer :guilabel:`KRB III`. For this we can use 
the Spatial Query tool.

23. Go to :menuselection:`Vector ‣ Spatial Query ‣ Spatial Query`.

.. image:: /static/training/beginner/qgis-inasafe/image215.*
   :align: center

24. Under :guilabel:`Select source features from` choose :guilabel:`vegetasi`.
    In the next box choose :guilabel:`Is disjoint`. The third box should be set
    to :guilabel:`KRB III`. The Spatial Query window should look like this:

.. image:: /static/training/beginner/qgis-inasafe/image216.*
   :align: center

25. Click :guilabel:`Apply`. Then click :guilabel:`Close`
    once the selection has been applied.

.. image:: /static/training/beginner/qgis-inasafe/image217.*
   :align: center

Now the vegetasi layer looks like the image below. Notice that all the features
have been selected that fall outside the KRB III area.

.. image:: /static/training/beginner/qgis-inasafe/image218.*
   :align: center

The next steps of our analysis will be easier if we save this selection as a
separate layer.

26. Right-click on the :guilabel:`vegetasi` layer and
    click :guilabel:`Save Selection As...`

.. image:: /static/training/beginner/qgis-inasafe/image219.*
   :align: center

27. Next to the :guilabel:`Save as` field in the dialog that appears,
    click the :guilabel:`Browse` button.

28. Save the layer under :guilabel:`evakuasi_bencana` as :file:`kebun_tegalan.shp`.

29. Check the box labelled :guilabel:`Add saved file to map` in the
    :guilabel:`Save vector layer as...` dialog.

.. image:: /static/training/beginner/qgis-inasafe/image220.*
   :align: center

30. Click :guilabel:`OK`. QGIS will tell you that the export has been
    completed.

31. Click :guilabel:`OK`.

32. :guilabel:`Right-click` on the old vegetation layer and remove it.
    You should have these layers remaining:

.. image:: /static/training/beginner/qgis-inasafe/image221.*
   :align: center

7. Finding important roads
--------------------------

We have a problem with our roads layer, similar to that of our vegetation layer.
Our roads layer has too many roads! We only want to use main roads for our
analysis, so that we can meet the criteria that our location is within 300
metres of a major road. Once again, we will use the Query Builder.

33. Right-click on the :guilabel:`jalan` layer and click :guilabel:`Query...`

34. Build a query for the roads layer, like you did above for the vegetation layer
    You want only primary and secondary roads,
    so you need to build this query:

*"TYPE" = 'primary' OR "TYPE" = 'secondary'*

35. You can use the approach that we learned above, or you can simply
    type this command into the query box. But be careful that you type it
    correctly!

.. image:: /static/training/beginner/qgis-inasafe/image222.*
   :align: center

8. Looking for health facilities
---------------------------------

36. Using the same approach, build a query for the :guilabel:`lokasi_penting` 
    layer as shown:
    
*"Fungsi" = 'Kesehatan'*

9. Buffering Roads
------------------

Okay, we’ve refined our data a bit so that it shows us the features we are
interested in analysing. Remember that according to our criteria our land area
should be within 300 metres of a main road and close to a health facility. QGIS
allows us to calculate distances from any vector object, and we will use this
functionality to help us reach a solution.

37. Make sure that only the :guilabel:`jalan` and :guilabel:`kebun_tegalan` 
    layers are visible,
    to simplify the map while you’re working.

.. image:: /static/training/beginner/qgis-inasafe/image223.*
   :align: center

38. Go to :menuselection:`Vector ‣ Geoprocessing Tools ‣ Buffer(s)`.

.. image:: /static/training/beginner/qgis-inasafe/image224.*
   :align: center

39. In the first dropdown box select :guilabel:`jalan`.

40. Enter :kbd:`300` next to :guilabel:`Buffer distance`.

41. Check the box next to :guilabel:`Dissolve buffer results.`

42. Click :guilabel:`Browse` and type :kbd:`buffer_jalan_300m.shp` for the
    filename.

.. image:: /static/training/beginner/qgis-inasafe/image225.*
   :align: center

.. note:: We input the buffer distance in metres. Good thing we used
   projected data!

43. Click :guilabel:`OK`. QGIS will create a buffer around the streets that
    extends 300 metres.

44. When you are asked to add the new layer to the TOC, click :guilabel:`Yes`
    (“TOC” stands for “Table of Contents”, by which it means the list of 
    Layers).

.. image:: /static/training/beginner/qgis-inasafe/image226.*
   :align: center

45. Close the Buffer dialog and see your new layer:

.. image:: /static/training/beginner/qgis-inasafe/image227.*
   :align: center

.. note:: Those big fat lines are actually areas that are within
   300 metres of primary and secondary roads.

10. Buffering health facilities
-------------------------------

46. Now try it yourself! Using the same approach, create a new buffer layer
    around your health facilities. The buffer should be 2.5 km in radius.

47. Don’t forget to check the box :guilabel:`Dissolve buffer results` so
    every overlapping buffer will become one feature. Then save the new layer in
    the same directory as :file:`buffer_fas_kesehatan_2.5km.shp`. Your resulting 
    map will look something like this:

.. image:: /static/training/beginner/qgis-inasafe/image228.*
   :align: center

.. note:: Remember that the buffer distance is in metres. Keep this in mind
   when you want to create a 2,5 km buffer!

11. Overlapping areas
---------------------

Now we can see areas where a main road is 300 metres away and where there is a
health facility within 2.5 km. But we only want the areas where both of these
criteria are satisfied at once!  To do that we will use the Intersect tool.

48. Go to :menuselection:`Vector ‣ Geoprocessing Tools ‣ Intersect`.

.. image:: /static/training/beginner/qgis-inasafe/image229.*
   :align: center

49. Enter :guilabel:`buffer_fas_kesehatan_2.5km` and 
    :guilabel:`buffer_jalan_300m` as the two input layers.
    Name the output shapefile :kbd:`intersect_buffer_jalan_kesehatan.shp`.

.. image:: /static/training/beginner/qgis-inasafe/image230.*
   :align: center

50. Click :guilabel:`OK` and add the layer to the project when prompted.

If we hide the original layers, we can see that our new layers shows us
the areas where they intersect. These are the areas where both of
these criteria are satisfied.

.. image:: /static/training/beginner/qgis-inasafe/image231.*
   :align: center

12. Select farms and dry fields
-------------------------------

Now we have the layer :guilabel:`kebun_tegalan`, which satisfies two of our 
criteria, and the layer :guilabel:`intersect_buffer_jalan_kesehatan.shp`, which 
satisfies two other criteria. We need to know where they overlap!

51. Go to :menuselection:`Vector ‣ Research Tools ‣ Select by location`.
    A dialog will appear.

.. image:: /static/training/beginner/qgis-inasafe/image232.*
   :align: center

52. Set it up like this:

.. image:: /static/training/beginner/qgis-inasafe/image233.*
   :align: center

53. Click :guilabel:`OK` and you’ll see the results are selected (they are 
    yellow).

.. image:: /static/training/beginner/qgis-inasafe/image234.*
   :align: center

Let’s save this selection as a new layer.

54. Right-click on the :guilabel:`kebun_tegalan` layer in the Layers panel.

55. Click :guilabel:`Save Selection As`....

56. Name the new file :kbd:`kebun_tegalan_lokasi_terpilih.shp` and
    check the box next to :guilabel:`Add saved file to map`.

.. image:: /static/training/beginner/qgis-inasafe/image235.*
   :align: center

If we hide all the other layers, we can see the resulting layer:

.. image:: /static/training/beginner/qgis-inasafe/image236.*
   :align: center

13. Select land areas of the appropriate size
---------------------------------------------

Hooray!  We have now found land areas that meet four of our five criteria. The
only remaining criteria is the size of the land. We need to make sure that our
possible locations are between 50000-150000 m².

57. Open the attribute table for the :guilabel:`kebun_tegalan_lokasi_terpilih`
    layer. Notice that there is a column named :guilabel:`luas_ha`. This is the
    size of the area in hectares. We could use this field to answer our question,
    but let’s add another column that contains the size of the area in
    square metres.

58. Select the :guilabel:`kebun_tegalan_lokasi_terpilih` layer and open its
    attribute table:

.. image:: /static/training/beginner/qgis-inasafe/image237.*
   :align: center

59. Enter editing mode by clicking this button:

.. image:: /static/training/beginner/qgis-inasafe/image238.*
   :align: center

60. Click the :guilabel:`Start the field calculator` button (located in the 
    Attribute Table window).

.. image:: /static/training/beginner/qgis-inasafe/image239.*
   :align: center

61. Check the box next to :guilabel:`Create a new field`. In the box type
    :kbd:`luas_m2`.

.. image:: /static/training/beginner/qgis-inasafe/image240.*
   :align: center

62. Change :guilabel:`Output field type` to :guilabel:`Decimal number (real)`.
    Then click on :guilabel:`Geometry` and double-click :guilabel:`$area`.

.. image:: /static/training/beginner/qgis-inasafe/image241.*
   :align: center

63. Click :guilabel:`OK`.

You should now see a new column on your attribute table, named :kbd:`luas_m2`.
And QGIS has filled it in for us with square metres!

.. image:: /static/training/beginner/qgis-inasafe/image242.*
   :align: center

64. Click the edit mode button again, and save your edits.

.. image:: /static/training/beginner/qgis-inasafe/image243.*
   :align: center

65. Close the attribute table. Now we can just do a simple query.

66. Right-click on the :guilabel:`kebun_tegalan_lokasi_terpilih` layer and
    click :guilabel:`Query...`

67. Enter the following:

*"luas_m2" >= 50000 AND "luas_m2" <= 150000*

.. image:: /static/training/beginner/qgis-inasafe/image244.*
   :align: center

68. Click :guilabel:`OK`.

.. image:: /static/training/beginner/qgis-inasafe/image245.*
   :align: center

That’s it!  We have eight pieces of land that meet ALL of our criteria.
Any of these pieces of land might be suitable for a location to place refugees.

69. Right-click the :guilabel:`kebun_tegalan_terpilih` layer and click 
    :guilabel:`Save As`. Name the file :file:`refugees_location.shp`.


:ref:`Go to next module --> <using-map-composer>` 

