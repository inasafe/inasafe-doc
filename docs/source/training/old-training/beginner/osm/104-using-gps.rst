.. image:: /static/training/old-training/beginner/osm/image33.*
..  _using-gps:

Module 4: Using GPS
===================

**Learning Objectives**

- Understand GPS and the types of GPS                
- Turn on GPS                                                                                  
- Understand factors that affect GPS accuracy            
- Understand tracks and waypoints                        
- Collect data using GPS
- GPS settings
- Copy GPS data (tracks and waypoints) to computer    
- Open waypoints and tracks in JOSM                   
- Upload GPS tracks using JOSM                        
- Edit OSM based on GPS data in JOSM                 

In this module we see what a GPS does and how it works. We explore 
how to operate a GPS and how to use it to create maps. We will
explain how to operate the Garmin eTrex Vista HCx, a common GPS used for
mapping. There are many other models of GPS which do the same thing, so if you
are working with a different one, don’t worry - the principles remain the same.


1. What is GPS?
---------------

A GPS is like a mobile phone, except that instead of receiving radio signals
from telephone companies, it receives signals from satellites that are going
around the Earth. By receiving these signals from the satellites,
a GPS is able to calculate its exact location on the planet. It records
this location in coordinates, which are two long numbers. One number tells
you how far east or west you are - this is called **longitude**. The second
number tells you how far north or south you are - this is called **latitude**.
Every place on Earth has unique geographic coordinates.

For example: -8.639298 Latitude, 116.311607 Longitude is a location in
Lombok, Indonesia.

.. figure:: /static/training/old-training/beginner/osm/image34.*
   :align: center

   *Google Earth software, showing coordinates of a place in Lombok, Indonesia.*

.. figure:: /static/training/old-training/beginner/osm/image35.*
   :align: center
   :width: 200 pt

   *Garmin eTrex Vista HCx*

2. Turning on the GPS
---------------------

1. Before turning on your GPS, go outside where you have a clear view of the
   sky. Because the GPS determines your location by receiving signals from
   satellites, **it won’t work indoors**.

2. On the right side of the GPS, press and hold the :guilabel:`Power` button.
   The GPS will start, and it will show you the Satellites page. You 
   should see something like the image below. The GPS is looking for satellite signals.
   When it has connected to three or more satellites, it will have your location.

.. image:: /static/training/old-training/beginner/osm/image36.*
   :align: center
   :width: 225 pt

3. Once your location is determined, the Satellites page will
   disappear and you will see the Main Menu.

.. image:: /static/training/old-training/beginner/osm/image37.*
   :align: center
   :width: 225 pt

3. Navigating the GPS
---------------------

4. The GPS has different pages and menus that allow you to do different
   things. To switch between pages, press the button marked :kbd:`X`,
   just above the power button on the right side of the device. This button
   also serves to go back. If you press something by mistake and would like
   to cancel or go back, press the :kbd:`X` button.

5. By pressing the :kbd:`X` button, you should be able to flip through different
   screens that will look something like this:

.. image:: /static/training/old-training/beginner/osm/image51.*
   :align: center
   :width: 225 pt

.. image:: /static/training/old-training/beginner/osm/image52.*
   :align: center
   :width: 225 pt

.. image:: /static/training/old-training/beginner/osm/image53.*
   :align: center
   :width: 225 pt

.. image:: /static/training/old-training/beginner/osm/image54.*
   :align: center
   :width: 225 pt

6. Return to the Satellites page and see that you are
   connected to three or more satellites. In the upper left corner are your
   coordinates, your latitude and longitude.

7. Flip to the Map page, and you can see a map of where you are. If you have
   added OpenStreetMap maps to your GPS, you may see roads and places. 
   Otherwise, the map may look quite blank. Zoom in and out by pressing the 
   up and down arrow buttons on the left side of the GPS.

4. Tracks and waypoints
-----------------------

A GPS records two kinds of information that are useful for creating maps
or saving the coordinates of a place. First, it allows you to save your
location in the memory of the GPS. When you save a location,
the coordinates will be saved with a name. For example,
your first saved point will be named 001, the second 002,
and so on. When you save a point, you can write down the number on a piece
of paper, along with a note about what it is, and any attributes or
indicators you would like to collect. Saved locations on your GPS are called
waypoints.

Second, a GPS can save what are called tracks. While a waypoint only
saves a single location, a track will save a series of locations wherever
you move. For example, a track will record your location every one
second, or every one metre, and the result will be a series of dots that
show the path of where you have been. Tracks are useful for mapping objects
that are represented by lines or shapes, such as the course of a road
or the shape of a field.

.. image:: /static/training/old-training/beginner/osm/image55.*
   :align: center
   :width: 400 pt

.. note:: A GPS can record a single point as well as a path of where you
          travel. Here the points are numbered in the order they are recorded.
          The path or **track** is shown with a green line and the 
          **waypoints** are shown in red.

5. Saving Your location
-----------------------

8. To save your current location as a waypoint, click the :kbd:`X` button until
   your reach the Main Menu. Using the joystick, move it so that :guilabel:`Mark`
   is highlighted on the screen. Push the joystick button down to open the
   Save Waypoint page.

.. image:: /static/training/old-training/beginner/osm/image56.*
   :align: center
   :width: 225 pt

.. image:: /static/training/old-training/beginner/osm/image57.*
   :align: center
   :width: 225 pt

You can see on this page some information about the waypoint that you are
saving. First is the name. If this is your first waypoint,
it probably reads “001”. This is the number you should record on paper
along with the information you want to collect with this object. Next you
will see the time and date when the point is recorded. Below that are the
coordinates, followed by the altitude.

9. Use the joystick to move to the :guilabel:`OK` button at the bottom of the
   screen. Press the joystick button down to save this point. Be sure to write
   down the number of the point, along with what the place is and any other
   information you want to record about the place in your notebook.

10. Press the :kbd:`X` button to go to the Map page. You should now see your point
    on the map.

..  _turn-on-track-log:

6. Turning on the Track Log
---------------------------

Now that we have learned how to save points, let’s learn how to turn the
track log on and off. When the track log is turned on,
it will automatically record your path. It’s good practice to turn on the
log when you begin mapping, and turn it off when you are finished. You
will then be able to look at the track on a computer and see the path that
you mapped. If you would like to map the course of a road,
it is a good idea to save a waypoint at the beginning and end of the road,
writing in your notebook the name and type of the road,
and any other important information about the road.

11. Click the :kbd:`X` button until your reach the page
    that says Track Log.

.. image:: /static/training/old-training/beginner/osm/image58.*
   :align: center
   :width: 225 pt

12. To empty the track log (to delete earlier recordings),
    use the joystick to select :guilabel:`Clear`, and press the joystick down.
    The bar at the top should read “0%”.

13. To turn on the log, move the joystick to highlight :guilabel:`On`,
    and press the joystick down. The track log is now recording your path.

.. note:: Under :guilabel:`Setup`, you also can set time or distance
   intervals to track. Time intervals instruct your GPS to record your location
   at given intervals. If you have a memory card in your GPS, it is good
   practice to set this to one second, meaning that every second your location 
   will be added to the track log. This may be useful when detailed surveys are
   needed.

   See :ref:`GPS Settings <gps-settings-tracks>` for more information on setting 
   up the track log.

14. Press the :kbd:`X` button to go to the Map page. As you move you will see
    your track shown as a series of dots.

7. GPS settings
---------------

Here we demonstrate how to edit some of the core settings of the GPS
device. Use this as a reference to set up your GPS properly.

7.1. System settings
....................

15. Go to the Main Menu by using the :guilabel:`Page` button 
    (the :kbd:`X` button on the right side of the device). Use the joystick
    to click :guilabel:`Setup`, and then click on :guilabel:`System`.

.. image:: /static/training/old-training/beginner/osm/image38.*
   :align: center
   :width: 175 pt

.. image:: /static/training/old-training/beginner/osm/image39.*
   :align: center
   :width: 175 pt

Some of the settings that can be changed on the :guilabel:`System` menu 
are as follows:

- **GPS**: regulates how the GPS sensor works. Choose the :guilabel:`Normal`
  option. This tells the device to capture only signals from GPS satellites.
  The only drawback is that positional accuracy may sometimes be 
  less accurate (about 10-30 metres).

- **WAAS/EGNOS**: WAAS stands for Wide Area Augmentation System,
  while EGNOS stands for Euro Geostationary Navigation Overlay Service.
  WAAS/EGNOS is a system of satellites and ground stations that provide GPS 
  signal corrections, giving you a better position accuracy (to less than
  three metres). Ensure that it is :guilabel:`Enabled`. The drawback
  to this feature is that although it provides better accuracy, it will
  use the GPS battery more quickly.

.. image:: /static/training/old-training/beginner/osm/image40.*
   :align: center

- **Battery Type**: To optimise power usage, this should match the type of battery
  in the device. The default is Alkaline.

- **Text Language**: Choose the language for the device.

.. image:: /static/training/old-training/beginner/osm/image41.*
   :align: center
   :width: 175 pt

7.2. Unit settings
..................

16. From the Main Menu, go to :menuselection:`Setup ‣ Units`. Here the 
    type of measurement units can be set, such as metres, feet and more.
    The location unit format is also set here (decimal degrees, decimal 
    minutes degrees, second minutes degrees), datum (standard WGS 84) and 
    projection (standard WGS 84).

.. image:: /static/training/old-training/beginner/osm/image42.*
   :align: center
   :width: 175 pt

.. image:: /static/training/old-training/beginner/osm/image43.*
   :align: center
   :width: 175 pt

7.3. Time settings
..................

17. From the Main Menu, go to :menuselection:`Setup ‣ Time`. Here the time
    format is set (12 hours or 24 hours) as well as the time zone. It is good 
    to have the local time set, because all tracks and waypoints
    saved in the device are also saved with the current time.

.. image:: /static/training/old-training/beginner/osm/image44.*
   :align: center
   :width: 175 pt

.. image:: /static/training/old-training/beginner/osm/image45.*
   :align: center
   :width: 175 pt

7.4. Page settings
..................

Remember that when you press the :guilabel:`Page` button (the :kbd:`X`)
you are able to switch between different menus. By editing the page
settings, the pages, as well as their order, may be customised.

18. From the Main Menu, go to :menuselection:`Setup ‣ Page Sequence`.

19. Add a new page to the list by selecting :guilabel:`Add Page`. Then select
    a page such as: :guilabel:`Tracks` (to see details of your trip),
    :guilabel:`Map` (to view maps), or :guilabel:`Satellite` (to view the
    satellite status, position, and accuracy).

20. Click on one of the pages to move it around the list and change
    the order in which the pages flip.

.. image:: /static/training/old-training/beginner/osm/image46.*
   :align: center
   :width: 175 pt

.. image:: /static/training/old-training/beginner/osm/image47.*
   :align: center
   :width: 175 pt


..  _gps-settings-tracks:

7.5. Track settings
...................

Remember that :ref:`tracks <turn-on-track-log>` are a bread-crumb trail
recording your movement, which is useful for mapping roads. On the Track 
page there are several settings.

21. From the Track page, click :guilabel:`Setup`.

.. image:: /static/training/old-training/beginner/osm/image49.*
   :align: center
   :width: 175 pt

The settings are as follows:

- **Wrap When Full**: This option should be checked. It means that when the GPS 
  runs out of internal memory, it will start overwriting the oldest trackpoints
  to record new ones. It is a good idea to keep this checked, although typically
  you will be recording tracks to a memory card anyway, making this option
  unimportant.
  
- **Record Method**: There are several ways the GPS can record track points:

  - *Distance*: tracks a new point each time a certain distance has been covered
  - *Time*: tracks a new point when an amount of time has elapsed
  - *Auto*: automatically choose method (typically this should be selected)

- **Interval**: This setting indicates how often the GPS will record the track, 
  depending on the method selected in **Record Method**. Using a high setting 
  (collecting many points) here will result in tracks that are smooth and 
  detailed but will also drain the battery faster. If **Record Method** is set 
  to *Auto*, the **Interval** options will be as follows:

  - *Most often*
  - *More often*
  - *Normal*
  - *Less often*
  - *Least often*

If **Record Method** is set to *Distance* or *Time*, the options will allow
you to set a matching unit of measurement.

- **Color**: This setting is for defining the colour of the track line as 
  shown on the GPS map page.

.. image:: /static/training/old-training/beginner/osm/image50.*
   :align: center
   :width: 175 pt


8. Copying waypoints and tracks to the computer
-----------------------------------------------

8.1. Attaching GPS to the computer
..................................

When you are finished mapping with the GPS you will want to copy the
points and tracks to your computer so that you can open them in JOSM.
  
22. First, turn off the track log on your GPS by going to the Track page and
    selecting :guilabel:`Off`.

23. Attach the GPS to your computer with the cable. One end should plug into
    your computer’s USB port, and the other goes into the back of the GPS,
    beneath the rubber flap at the top. The GPS should be turned on to copy
    the points and tracks.


8.2. Installing GPS drivers
...........................

24. You may need to install GPS drivers on your computer. Open your training
    folder and find :file:`software/USBDrivers_23.exe`. Double-click it and 
    install.

25. If you don’t have this file, you can download it. Open your internet
    browser and go to: `http://www8.garmin.com/support/download_details
    .jsp?id=591 <http://www8.garmin.com/support/download_details.jsp?id=591>`_

26. Click :guilabel:`Download` to get the installation file. Locate it on your
    computer, and double-click to install.


8.3. Getting the GPSBabel setup program
.......................................

27. GPSBabel is a program that allows us to copy data from the GPS. It is
    saved as :file:`GPSBabel-1.5.1-Setup` in the :file:`software` folder (the
    exact version number may be different).

28. If you don’t have GPSbabel already, open your web browser and go to
    `www.gpsbabel.org <http://www.gpsbabel.org>`_.

29. Click :guilabel:`Downloads` at the top of the page.

30. Scroll down the page. If your computer uses Windows,
    you want to download the installation file for Windows. Click
    :file:`GPSBabel-1.5.1-Setup.exe`. The file will be downloaded to 
    your computer.


8.4. Installing GPSBabel
........................

31. Locate the GPSBabel setup file on your computer. Double-click it to install.

32. Click :guilabel:`Next`.

33. Click :guilabel:`I accept` and :guilabel:`Next`.

34. Continue clicking :guilabel:`Next` until the program installs.

35. When the program has finished installing, click :guilabel:`Finish` to start
    GPSBabel.


8.5. Copying Tracks and Waypoints
.................................

36. Click in the circle next to the word :guilabel:`Device` at the top of the
    window.

.. image:: /static/training/old-training/beginner/osm/image59.*
   :align: center
   :width: 400 pt

37. In the drop-down menu labelled :guilabel:`Format`, select
    :guilabel:`Garmin serial/USB protocol`

38. Go down to the middle of the window, under :guilabel:`Output`. In the 
    drop-down menu labelled :guilabel:`Format`, select :guilabel:`GPX XML`:

.. image:: /static/training/old-training/beginner/osm/image60.*
   :align: center
   :width: 300 pt

39. Click :guilabel:`File Name` and type a name for your saved file. It should be
    something that describes the data, such as the date and the location. For
    example: :file:`jakarta-07-07-2011`.

40. Make sure your GPS is connected to the computer and turned on.

41. Click :guilabel:`Apply` in the bottom right corner of the window.

42. If all goes well you should see a bar move across the screen,
    indicating that the data is being retrieved from the GPS. When it is
    finished, your points and track will be saved in the file that you selected.


8.6. Opening in JOSM
....................

43. Now open JOSM. Go to :menuselection:`File ‣ Open...`

44. Find and select the file that you created with GPSBabel. Click
    :guilabel:`Open`.

You should now see your points and tracks loaded into JOSM.

.. image:: /static/training/old-training/beginner/osm/image61.*
   :align: center


9. Uploading GPS data in JOSM
-----------------------------

.. note:: If you are not interested in sharing your tracks publicly on OSM, 
   feel free to skip this section.

Adding GPS tracks to the OSM server is useful because it enables other users
to see and use your tracks. For those who do not have a GPS or who can't
access a location, they are still able to benefit from your work and
help improve the map.

The easiest way to upload GPS tracks is to download the JOSM plugin
:guilabel:`DirectUpload`:

45. Open JOSM and go to :menuselection:`Edit ‣ Preferences`. Click the plugins 
    tab.

46. Type :kbd:`directupload` in the :guilabel:`Search` box. Check the box next
    to the plugin, and then click :guilabel:`OK`.

.. image:: /static/training/old-training/beginner/osm/image62.*
   :align: center
   :width: 300 pt

47. Restart JOSM.

48. Open your GPX file in JOSM.

49. Go to :menuselection:`Tools ‣ Upload Traces`

.. image:: /static/training/old-training/beginner/osm/image63.*
   :align: center

50. Add tags, a description, and choose an option for whom to make the track
    visible. Unless you have a reason for doing otherwise, choose
    :guilabel:`Public`.

.. image:: /static/training/old-training/beginner/osm/image64.*
   :align: center

51. Click :guilabel:`Upload Trace`. If requested to enter a username and password,
    enter the credentials of your OSM account and click
    :guilabel:`Authenticate`.



:ref:`Go to next module --> <field-papers>`
