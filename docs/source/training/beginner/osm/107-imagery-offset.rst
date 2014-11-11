.. image:: /static/training/beginner/osm/image6.*

..  _imagery-offset:

Module 7: Imagery Offset
========================

**Learning Objectives**

- Understand the definition of imagery offset
- Understand components of imagery (resolution and georeference)
- Understand how imagery offset occurs
- Fix imagery offset

Using aerial imagery is the most widely used approach in making maps with
OpenStreetMap. Mappers typically use Bing or Mapbox satellite imagery as a 
background layer, or imagery from another provider. We have already
seen this in action. In this module we will learn a little bit more about
aerial imagery, and we will learn how to solve the one important problem of
using aerial photographs - imagery offset.


1. Components of imagery
------------------------

Aerial imagery is the term that we use to describe photographs that are
taken from the sky. These can be taken from airplanes, helicopters,
or even kites and balloons, but the most common source of imagery comes from
satellites orbiting the Earth.

In the :ref:`module on GPS<using-gps>` we learned about the dozens of satellites 
orbiting Earth which allow our GPS receivers to identify latitude and longitude.
In addition to these GPS satellites, there are also satellites which take
photos of the earth. These photos are then manipulated so that they can be
used in GIS (mapping) software. Bing Aerial Imagery is made up of satellite
photos.

Let's look at a couple of the components of aerial imagery - resolution and 
georeferencing.

1.1. Resolution
...............

All digital photographs are made up of pixels. If you zoom in very close on
a photograph, you will notice the the image starts to get blurry,
and eventually you’ll see that an image is made up of thousands of little
squares that are each a different colour. This is true whether the
photograph is taken with a handheld camera, a mobile phone
or a satellite orbiting Earth.

.. image:: /static/training/beginner/osm/image108.*
   :align: center

Resolution refers to the number of pixels wide by the number of pixels high
that an image is. More pixels means higher resolution,
which means that you are able to see greater detail in the photograph.
Resolution in handheld cameras is often measured in megapixels. The more
megapixels your camera is able to record, the higher the resolution of your
photos.

Aerial imagery works the same, except that we talk about resolution
differently. Measurement is important with aerial photographs - hence,
a pixel represents a certain measurable area on the surface of the Earth. We 
usually describe imagery as something like "two metre resolution imagery",
which means that one pixel in the image is equivalent to two metres on the 
ground. One metre resolution imagery would have a higher resolution than this,
and 50cm resolution would be higher still. This is generally the range of
imagery that is provided by Bing, though it varies between locations,
and in many places it is worse than two metres, at which point it becomes
difficult to identify objects in the image.

.. image:: /static/training/beginner/osm/image109.*
   :align: center

The higher the resolution of an aerial image, the easier it is to use in
making maps.

1.2. Georeferencing
...................

Every aerial image is georeferenced, meaning that it is manipulated so that
it can be shown in its correct location on the Earth. Georeferencing is a
relatively complex process, because images are flat and the Earth is round,
and the images need to be positioned and stretched so that the pixels are
accurately positioned on the planet.

The imagery available to us is already georeferenced, so it is not something
that we need to concern ourselves with too deeply. We can happily use imagery 
to help add to OSM, so long as we understand a little bit about the
imagery we are using, and so long as we are aware of one common pitfall -
imagery offset.


2. Imagery offset
-----------------

Imagery providers usually do a pretty good job of georeferencing their
imagery, but occasionally the images can be a little bit out of position. This
is particularly true in hilly or mountainous areas, where it can be difficult
to stretch a flat image over an area of the Earth with many contours. When
you load imagery in JOSM, it can sometimes be ten metres or more from its
true position. This is called imagery offset.

.. note:: Aerial imagery layers are composed of many photographs of the Earth's 
   surface that have been georeferenced and then stitched together. Imagery 
   providers cannot verify the accuracy of every photo, so some images may be 
   shifted from their actual positions. This might be a shift of a couple 
   metres, or in rare instances up to hundreds of metres. In mountainous areas, 
   imagery may be distorted non-linearly, which means that nearby parts of the
   same image may be shifted in many different directions.

Notice in the following image that two separate aerial photographs have been
georeferenced and merged together. Because georeferencing is not a perfect
process, the images do not line up perfectly with each other. Hence one,
or both, must be inaccurate.

.. image:: /static/training/beginner/osm/image110.*
   :align: center

We’ve learned about two major ways of making maps - one is by utilising
aerial imagery to identify features on the ground, and another is by using
GPS to record tracks and waypoints and then add them to OSM. The
advantage of aerial imagery is obvious. It enables you, the mapper,
to see the whole picture, to observe various details from the image,
consider your knowledge of the area, and easily trace roads, buildings
and areas. One key advantage of GPS however, is that it doesn’t suffer from
offset like imagery. A GPS will always provide you with a correct latitude
and longitude. The only exception is when the satellite signals are
interrupted by tall buildings or mountains, but in this case it is easy to
recognise the error. Observe the GPS trace in this image,
compared with the Bing aerial imagery layer beneath it:

.. image:: /static/training/beginner/osm/image111.*
   :align: center

Because of what we now know, it is clear that the GPS trace is likely to be
accurate, and the image beneath it is out of place.

So now we must ask, “if the imagery may be out of place,
how can we still use it and make accurate maps?”

3. Correcting imagery offset
----------------------------

The answer to the preceding question is that we can move the imagery so that
it aligns with things that we know are in the correct location,
such as GPS tracks. It is easy to correct imagery offset in JOSM.

The best references for adjusting imagery are GPS tracks that follow roads.
And the more GPS tracks that you have to reference, the more accurate you
will be able to align your imagery. Since OSM users often upload
their GPS tracks to the OSM database, we can download them and use them to
align our imagery.

1. In JOSM, click on the :guilabel:`Download` button.

2. Check the box next to :guilabel:`Raw GPS Data` near the top of the
   :guilabel:`Download` window. Select your area and click
   :guilabel:`Download`.

.. image:: /static/training/beginner/osm/image112.*
   :align: center

3. This will download an additional layer to JOSM containing GPS tracks.
   Depending on how many tracks have been uploaded by OSM users,
   you may see few tracks (or even no tracks):

.. image:: /static/training/beginner/osm/image113.*
   :align: center

4. Or, you may see many tracks:

.. image:: /static/training/beginner/osm/image114.*
   :align: center

5. Add an imagery layer (such as Bing Sat) to JOSM.

6. To adjust an imagery layer, click on the :guilabel:`Adjust imagery offset`
   button at the top of JOSM, and then click :guilabel:`New Offset`.

.. image:: /static/training/beginner/osm/image115.*
   :align: center

7. Ignoring the box that pops up, use your mouse to drag the imagery layer so
   that it aligns correctly with the GPS tracks. The GPS tracks should line
   up with the roads on the imagery as closely as possible. You will see the
   offset numbers in the box change.

.. image:: /static/training/beginner/osm/image116.*
   :align: center

8. If you like, you can save these offset settings by entering a bookmark
   name and then clicking :guilabel:`OK`. You can then automatically apply
   the same settings later by going to :menuselection:`Imagery ‣ Imagery offset`
   and clicking on your bookmark.

9. If you do not want to save the offset, simply click :guilabel:`OK` without
   entering a bookmark name.

What if there are no GPS tracks on OSM, and you don’t have a GPS?
Without GPS tracks, it is difficult to align imagery. If it is a relatively
empty area (not much mapping done), you might choose to simply use the
imagery as it is and correct the data later. It’s better to map an
area 20 or 30 metres offset than to not map it at all.

If you can positively identify the latitude and longitude of one object on
the ground, you can ensure the imagery is correctly placed by following
these steps:

10. First, identify the object whose position you know on the imagery.

11. Click on the latitude and longitude in the bottom left corner of JOSM.

.. image:: /static/training/beginner/osm/image117.*
   :align: center

12. In the dialog that opens, enter the latitude and longitude of the place
    that you know, and enter a small number for :guilabel:`Zoom`, about five 
    or 10.

.. image:: /static/training/beginner/osm/image118.*
   :align: center

13. This will zoom and centre the map to your longitude and latitude. Now you
    can move the imagery as you did previously so that the feature you know is
    centred at the correct position.

If, on the other hand, the area has already been extensively mapped,
then hopefully the previous mappers have drawn objects in their correct
locations. In this case, you can align the imagery to the OSM map,
but beware!  Other mappers may not be aware of imagery offset,
and they may have made mistakes when they mapped.

3.1. The imagery offset database
................................

Now you know how to watch out for and correct imagery offset,
but there is one major problem with this approach that we have overlooked
thus far. If every OSM user adjusts the imagery differently,
everybody will be mapping with slightly different backgrounds.

Imagine that you are mapping a small town, and you realise that Bing imagery
is offset by 15 metres to the north. So you adjust the imagery and then
use it to map the whole town accurately. But then somebody else wants to
add something to the map, so they download the data and load Bing imagery,
but they don’t know about the imagery offset you discovered!  They will
think that something is wrong and all of the objects in town are misplaced
by 15 metres, and they will start to move them, which is not correct!  This
can be disastrous for the town’s map data.

For this reason it is important that all users are aware of imagery offset,
and should always check for it before mapping an area. To help with this
problem, some smart people created a plugin that allows users to save offset
information in a database and share it with others. Let’s see how this works:

14. Open the :guilabel:`Preferences` menu in JOSM, and click on the
    :guilabel:`Plugins` tab.

.. image:: /static/training/beginner/osm/image119.*
   :align: center

15. Find the plugin named *imagery_offset_db* and check the box next to it.

.. image:: /static/training/beginner/osm/image120.*
   :align: center

16. Click :guilabel:`OK`. You will need to restart JOSM to finish the plugin
    installation.

In the same way that you are able to save offsets as bookmarks,
this plugin allows you to save offsets to a central database,
and to access the offsets that other users have created. Hence,
if one mapper creates an imagery offset in an area, other users can use the
exact same offset to map with.

When using aerial imagery layers, you should ALWAYS check for existing
offsets, and when you create your own offset, you should ALWAYS save it to
this database.

3.2. Add imagery offset from the database
.........................................

17. When you add an imagery layer, the new plugin will alert you that you
    should check the imagery database for an existing offset. You will see an
    icon with a red exclamation point on it at the top of JOSM, like this:

.. image:: /static/training/beginner/osm/image121.*
   :align: center

18. Click on the button and the plugin will communicate with the database to
    see if there are existing offsets in this area.

19. Here we have downloaded OSM data and GPS tracks in Kuta, Bali,
    Indonesia. In this case, we have found one existing offset. Click on it to
    apply to the map.

.. image:: /static/training/beginner/osm/image122.*
   :align: center

20. This causes the imagery layer to shift. However,
    when we add someone else’s offset like this, we should check that it is
    valid by comparing it to GPS tracks.

.. image:: /static/training/beginner/osm/image123.*
   :align: center

21. We can see that the imagery layer is in fact misaligned. We don’t want
    other users to use this offset, so we should mark it as incorrect in the
    database. Click on the :guilabel:`Offsets` button again (it won’t have a red
    exclamation mark anymore).

.. image:: /static/training/beginner/osm/image124.*
   :align: center

22. This time when the dialog opens, right-click on the offset and click
    :guilabel:`Deprecate Offset`.

.. image:: /static/training/beginner/osm/image125.*
   :align: center

23. Click :guilabel:`Yes` to confirm.

24. Enter a reason for deprecating this offset.

.. image:: /static/training/beginner/osm/image126.*
   :align: center

3.3. Add imagery offset to the database
.......................................

Now that we have marked this user’s offset as "deprecated", we should add an
improved offset to the database.

25. Click on the :guilabel:`Adjust imagery offset` button.
26. Adjust the imagery to match the GPS tracks. Click :guilabel:`OK` in the box.
27. Now go to :menuselection:`Offset ‣ Store Imagery Offset...`

.. image:: /static/training/beginner/osm/image127.*
   :align: center

28. Enter a description of the offset in the box that opens.

.. image:: /static/training/beginner/osm/image128.*
   :align: center

29. Click :guilabel:`OK`. Your offset will be saved to the database.

30. Now let’s hide the GPS layer and look at the OSM data against the
    correctly placed imagery.

.. image:: /static/training/beginner/osm/image129.*
   :align: center

Oh No!  Somebody mapped this area with misaligned imagery,
so the area is not correctly mapped. This will take some time to fix.

3.4. Imagery offset database website
....................................

For more information on the offset database,
you can visit the website at http://offsets.textual.ru/. This lists all the
offsets that have been uploaded to the database, and it also has a map
feature that visualises where the offsets are located, as you can see here:

.. image:: /static/training/beginner/osm/image130.*
   :align: center

One last thing to remember is that the imagery may not be offset the same
distance everywhere! This is especially true in regions where there are
lots of hills and mountains. So if the imagery seems to be offset
differently in different areas, you’ll need to move it again.


:ref:`Go to next module --> <getting-osm-data>`