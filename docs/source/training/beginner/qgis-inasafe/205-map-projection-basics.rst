.. image:: /static/training/beginner/qgis-inasafe/image6.*


Module 5: Map Projection Basics
===============================

**Learning Objectives**

- Understand Coordinate Reference Systems (CRS)
- Identify the CRS of a vector dataset
- Perform reprojection “on the fly”
- Save dataset with a different CRS
- Making its own projection

We’ve talked a little bit about Coordinate Reference Systems (CRSs) previously,
but haven’t covered it in depth.  In this chapter, we’ll look more at what a CRS
means practically, and how it affects our work in QGIS.


**1. Coordinate Reference System (CRS)**

The CRS that all the data as well as the map itself are in right now is called
WGS84. This is a very common Geographic Coordinate System (GCS) for representing
data. But there’s a problem, as we will see.

- Open the project :file:`world.qgs`, located in the :file:`qgis/ folder`
- Zoom in to Indonesia by using the Zoom In tool.

.. image:: /static/training/beginner/qgis-inasafe/image54.*
   :align: center

- Setting the scale in the Scale field, which is in the Status Bar along the
  bottom of the screen. While over Indonesia, set this value to 1:20000000 (one
  to twenty million).

.. image:: /static/training/beginner/qgis-inasafe/image55.*
   :align: center

- Now pan around the map while keeping an eye on the Scale field.

Notice the scale changing? That’s because you’re moving away from the one point
that you zoomed into at 1:20000000, which was at the center of your screen. All
around that point, the scale is different.

To understand why, think about a globe of the Earth. It has lines running along
it from North to South. These longitude lines are far apart at the equator, but
they meet at the poles.  In a GCS, you’re working on this sphere, but your
screen is flat. When you try to represent the sphere of the earth on a flat
surface, it becomes distorted, as if you took an orange peel and tried to
flatten it.  What this means on a map is that the longitude lines stay equally
far apart from each other, even at the poles (where they are supposed to meet).
This means that, as you travel away from the equator on your map, the scale of
the objects that you see gets larger and larger. What this means for us,
practically, is that there is no constant scale on our map!

To solve this, we’ll use a Projected Coordinate System (PCS) instead.  A PCS
“projects” or converts the data in a way that makes allowance for the scale
change and corrects it.  Therefore, to keep the scale constant, we should
reproject our data to use a PCS.

*Projection is the act of taking coordinates on a sphere (like the earth), and manipulating them so that they can be displayed on a flat surface.*

**2. “On the Fly” Reprojection**

Every QGIS project has a CRS, and each of the data layers have a CRS too.  Often
these are the same.  Your project may be in WGS84, and the layers too.  But
sometimes you will add a layer that is not in the same CRS as the project, and
you need QGIS to convert it so that it can be displayed along with the rest of
the data.  The term that we use for this is reprojecting “on the fly.”

- To enable “on the fly” projection, click on the :guilabel:`CRS Status` button
  in the Status Bar along the bottom of the QGIS window:

.. image:: /static/training/beginner/qgis-inasafe/image56.*
   :align: center

- In the dialog that appears, check the box next to
  :guilabel:`Enable ‘on the fly’ CRS transformation`.

.. image:: /static/training/beginner/qgis-inasafe/image57.*
   :align: center

- Type the word global into the Filter field. One CRS (NSIDC EASE-Grid Global)
  will appear in the list below.

.. image:: /static/training/beginner/qgis-inasafe/image58.*
   :align: center

- Click on it to select it, then click :guilabel:`OK`.
- Notice how the shape of Indonesia changes. All projections work by changing
  the apparent shapes of objects on Earth.
- Zoom in to a scale of 1:20000000 again, as before.
- Pan around the map.
- Notice how the scale stays the same!

“On the fly” reprojection is useful for combining datasets that are in different
“CRSes.

- Deactivate :guilabel:`“on the fly” reprojection` again, by unchecking the box
  next to Enable ‘on the fly’ CRS transformation.
- Now let’s add another vector layer, located in
  :file:`qgis/peta_dunia/Indonesia.shp`.

What do you notice? The layer isn’t visible! But that’s easy to fix, right?

- Right-click on the **layer** in the Layers list.
- Select :menuselection:`Zoom to Layer Extent`.

OK, so now we see Indonesia... but where is the rest of the world?

It turns out that we can zoom between these two layers, but we can’t ever see
them at the same time. That’s because their Coordinate Reference Systems are so
different. The continents layer is in degrees, but the Indonesia layer is in
meters.  In other words, one feature in the continents layer might be 8.5
degrees away from the equator, but the same feature in the Indonesia layer might
be 900000 meters away from the equator.

8.5 degrees and 900000 meters is about the same distance, but QGIS doesn’t know
that!  One of our layers must be reprojected to match the other layer. To
correct this:

- Switch :guilabel:`Enable ‘on the fly’ CRS transformation` on again as before.
- :guilabel:`Zoom to the layer extents` of the Indonesia dataset.

Now, because they’re made to project in the same CRS, the two datasets fit
perfectly:

.. image:: /static/training/beginner/qgis-inasafe/image59.*
   :align: center

When combining data from different sources, it’s important to remember that they
might not be in the same CRS. “On the fly” reprojection helps you to display
them together.


**3. Saving a Dataset to Another CRS**

It’s great that QGIS can reproject layers on the fly so that we can work with
them in the same project.  But this requires more time for our computer to
reproject the layers, and can slow down our work.  For this, or for other
reasons, we might want to be able to reproject a dataset, and save it with the
new projection.

Let’s reproject the Indonesia layer so that it is in the same CRS as the
project.  To do this, we will need to export the data to a new file using a new
projection.

- Right-click on the :guilabel:`Indonesia` layer in the Layers list.
- Select :guilabel:`Save As...` in the menu that appears. You will be shown the
  **Save vector layer as...** dialog.
- Click on the :guilabel:`Browse` button next to the :guilabel:`Save as field`.
- Navigate to :file:`qgis/peta_dunia/` and specify the name of the new layer as
  :kbd:` Indonesia_terproyeksi.shp`.
- Leave the Encoding unchanged.
- Change the value of the Layer CRS dropdown to **Project CRS**.
- Check the box next to :guilabel:`Add saved file to map`.
- The **Save vector layer as...** dialog now looks like this:

.. image:: /static/training/beginner/qgis-inasafe/image60.*
   :align: center

- Click :guilabel:`OK` and after a minute, you should be presented with:

.. image:: /static/training/beginner/qgis-inasafe/image61.*
   :align: center

- Click :guilabel:`OK`.

- Now your new layer, **Indonesia_terproyeksi**, will be shown in the layers
  panel.  If you turn off “on the fly” reprojection, this layer will still be
  shown correctly, because it has been reprojected into the same CRS as the
  project (and the continents layer).


**4. Creating Your Own Projection**

There are many more projections than just those included in QGIS by default. You
can even create your own projections.  Let’s see how this works.

- Start a new map.
- Load the vector layer :file:`oceans.shp` located in :file:`qgis/peta_dunia/`.
- Go to :menuselection:`Settings ‣ Custom CRS...` and you’ll see this dialog:

.. image:: /static/training/beginner/qgis-inasafe/image62.*
   :align: center

- We will create a projection known as Van der Grinten I.  This interesting
  projection represents the Earth on a circular field instead of a rectangular
  field, as most projections do.
- Enter :kbd:`Van der Grinten I` in the Name field.
- In the Parameters field, use the following string:

+proj=vandg +lon_0=0 +x_0=0 +y_0=0 +R_A +a=6371000 +b=6371000 +units=m +no_defs

.. image:: /static/training/beginner/qgis-inasafe/image63.*
   :align: center

- Click the :guilabel:`Save` button:

.. image:: /static/training/beginner/qgis-inasafe/image64.*
   :align: center

- Click :guilabel:`OK`.
- Enable “on the fly” reprojection.

.. image:: /static/training/beginner/qgis-inasafe/image65.*
   :align: center

- Search for your newly defined projection by typing it into the Filter box:

.. image:: /static/training/beginner/qgis-inasafe/image66.*
   :align: center

- You should see it appear in the box at the bottom.  Select it, and click
  :guilabel:`OK`.
- Once you’ve applied the new projection, the map will be reprojected like this:

.. image:: /static/training/beginner/qgis-inasafe/image67.*
   :align: center
