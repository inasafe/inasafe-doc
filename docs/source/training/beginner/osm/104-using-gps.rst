.. image:: /static/training/beginner/osm/image33.*


Module 4: Using GPS
===================

**Learning Objectives**

- Understanding what is GPS and types of GPS
- Turn on GPS
- Setting GPS
- Understanding the factor that affected GPS accuracy
- Understanding about track and waypoints
- Collect data using GPS
- Copy GPS data (track dan waypoint) to computer
- Open waypoint and track on JOSM
- Upload GPS track in JOSM
- Editing based on GPS data on JOSM

In this module we will learn step by step how to download and install JOSM,
the Java OpenStreetMap editor. We will change some of the settings in JOSM
to make it easier to use. Then we will open a sample map and learn some of
the basic operations of the software. Remember in Module 1 when we asked you
to draw a map of your town or village? We will conclude this module by
drawing your map again, this time digitally. After this you should have a
good understanding of how to draw maps in JOSM.

**1. What is GPS?**

A GPS is like a mobile phone, except that instead of receiving radio signals
from telephone companies, it receives signals from satellites that are going
around the Earth. By receiving these signals from the satellites,
a GPS is able to calculate your exact location on the planet.  It records
this location in coordinates, which are two long numbers.  One number tells
you how far East or West you are - this is called **longitude**.  The second
number tells you how far North or South you are - this is called **latitude**.
Every place on Earth has unique geographic coordinates.

For example: -8.639298 Latitude, 116.311607 Longitude is a location in
Lombok, Indonesia.

.. image:: /static/training/beginner/osm/image34.*
   :align: center
   *Google Earth software, showing coordinates of a place in Lombok, Indonesia.*

.. image:: /static/training/beginner/osm/image35.*
   :align: center
   *Garmin eTrex Vista HCx*

**2. Turn on the GPS**

- Before you turn on your GPS, go outside where you have a clear view of the
  sky.  Because the GPS determines your location by receiving signals from
  satellites, **it won’t work indoors**.
- On the right side of your GPS, press and hold the :guilabel:`Power` button.  
  The GPS will start, and it will show you the Satellites page.  You should see
  something like the image below.  Your GPS is looking for satellite signals.
  When it has connected to three or more satellites, it will have your location.

.. image:: /static/training/beginner/osm/image36.*
   :align: center

- Once your location is determined, the :guilabel:`Satellite` screen will 
  disappear and you will see the :guilabel:`Main Menu`.

.. image:: /static/training/beginner/osm/image37.*
   :align: center

**3. GPS Setting**

*3.1. GPS mode settings*

- Access the :guilabel:`Setup` menu on the :guilabel:`Main Menu` by using the 
  :guilabel:`Page` button. Then go to the :guilabel:`System`.

.. image:: /static/training/beginner/osm/image38.*
   :align: center

.. image:: /static/training/beginner/osm/image39.*
   :align: center

- In the :guilabel:`System` menu you can find some of the settings are as 
  follows:

a) GPS: regulate how the GPS sensor work. Choose the "Normal" option. The
   device captures only the signals from the GPS satellites. But your
   position accuracy sometimes less accurate (about 10-30 meters).
b) WAAS/EGNOS. WAAS stands for Wide Area Augmentation System,
   while EGNOS stands for Euro Geostationary Navigation Overlay Service.
   There are generally provided by the GPS accuracy is 15 meters. WAAS /
   EGNOS is a system satellites and ground stations that provide GPS signal
   corrections, giving you a better position accuracy (to less than 3
   meters). You should choose the mode WAAS / EGNOS by selecting "Enabled"
   to get better accuracy, but with the consequence you have to prepare a
   backup battery.

.. image:: /static/training/beginner/osm/image40.*

c) Battery Type: To optimize power usage, should be adapted to the type of
   battery you use (default: Alkaline).
d) Text Language: You can choose language you want to use.

.. image:: /static/training/beginner/osm/image41.*

*3.2. Unit Settings*

Access the menu Setup > Units. In this menu, you can manage want to display
units. For examples, in meter, feet, and other. You can also manage position
format (decimal degree, decimal minutes degree, second minutes degree),
datum (standard WGS 84) and projection (standard WGS 84).

.. image:: /static/training/beginner/osm/image42.*

.. image:: /static/training/beginner/osm/image43.*

*3.3. Times Settings*
Access the menu  Setup > Time. You can manage time format (12 hours or 24
hours) and your time zone.

.. image:: /static/training/beginner/osm/image44.*

.. image:: /static/training/beginner/osm/image45.*

*3.4. Page Settings*

Access the menu Setup > Page Sequences. You remember about function Pages
button ? You can manage pages function often your use,
so you do not a lot of pressing a button to access the page function. You
can press the Page button several times to page you want access the function
. You can add page function with select Add Page then select function such
as: Tracks (to see details of your trip), Map (to view maps),
Satellite (to view the status satellite, position, and accuracy).

 .. image:: /static/training/beginner/osm/image46.*

.. image:: /static/training/beginner/osm/image47.*

*3.5. Tracks*

Access Tracks menu. Do you remember the track function? Tracks can record
your track ride, it is very useful for mapping the road. In the menu there
are a few settings such as:

- Track Log:

a) “On” - track record, track trail will be visible on the map. Make sure
   the setting is selected before you start mapping.
b) “Off” - stop recording the track, should you choose this setting every
   time you finish mapping.

.. image:: /static/training/beginner/osm/image48.*

- Then, still in the Track menu, select "Setup".

.. image:: /static/training/beginner/osm/image49.*

- “Wrap When Full”: Put a check in this option. GPS device can save
  automatic your track, after out of memory.
- Record Method:

a) “Distance” – track recording every certain distance range
b) “Time” – track recording every time range
c) “Auto” – track recording automatic (should be choose this setting)

- Interval:

This setting decide how often the GPS will record your track ride. Often you
record your track make produce a line of track is smooth and tidy but will
drain the battery faster. If least often, recording infrequently,
the line produced track will appear broken.

a) “Most often” – track recording at any time as often as possible
b) “More often” – track recording done as often as possible
c) “Normal” – track recording at normal
d) “Less often” – track recording not at any time (below normally)
e) “Least often” – track recording infrequently

- Color: You can change display line color on track maps.

.. image:: /static/training/beginner/osm/image50.*


**4. Navigate the GPS**

- The GPS has different screens and menus that allow you to do different
  things.  To switch between screens, press the button marked “X”,
  just above the power button on the right side of the device.  This button
  also serves to go back.  If you press something by mistake and would like
  to cancel or go back, press the “X” button.
- By pressing the X button, you should be able to flip through different
  screens that will look something like this:

.. image:: /static/training/beginner/osm/image51.*

.. image:: /static/training/beginner/osm/image52.*

.. image:: /static/training/beginner/osm/image53.*

.. image:: /static/training/beginner/osm/image54.*


- If you return to the Satellites page, you can see that you are connected
  to three or more satellites.  In the upper left corner are your coordinates,
  your latitude and longitude.
- Flip to the Map page, and you can see a map of where you are.  If you have
  added OSM maps to your GPS, you may see roads and places.  Otherwise,
  the map may look quite blank. Zoom in and out by pressing the up and down
  arrow buttons on the left side of the GPS.

**5. Tracks and Waypoints**

Your GPS records two kinds of information that are useful for creating maps
or saving the coordinates of a place.  First, it allows you to save your
location in the memory of the GPS.  When you save a location,
the coordinates will be saved with a name.  For example,
your first saved point will be named 001, the second 002,
and so on.  When you save a point, you can write down the number on a piece
of paper, along with a note about what it is, any any attribute or
indicators you would like to know.  Saved locations on your GPS are called
waypoints.

Second, your GPS can save what are called tracks. While a waypoint only
saves a single location, a track will save a series of locations wherever
you move.  For example, the track will record your location every one
second, or every one meter, and the result will be a series of dots that
show the path of where you have been.  Tracks are useful for mapping objects
that are represented by lines or shapes, such as the course of a road,
or the shape of a field.

.. image:: /static/training/beginner/osm/image55.*

.. note:: A GPS can record a single point as well as a path of where you
          travel. Here the points are numbered in the order they are recorded.
          The path or “track” is shown in green line and the “waypoint” is
          shown in red.

**6. Save Your Location**

- To save your current location as a waypoint, click the “X” button until
  your reach the Main Menu.  Using the joystick, move it so that “Mark” is
  highlighted on the screen.  Push the joystick button down to open the “Save
  Waypoint” page.

 .. image:: /static/training/beginner/osm/image56.*

.. image:: /static/training/beginner/osm/image57.*

- You can see on this page some information about the waypoint that you are
  saving.  First is the name.  If this is your first waypoint,
  it probably reads “001”.  This is the number you should record on paper
  along with the information you want to collect with this object.  Next you
  will see the time and date when the point is recorded.  Below that are the
  coordinates, followed by the altitude.
- Use the joystick to move to the “OK” button at the bottom of the screen.
  Press the joystick button down to save this point.  Be sure to write down
  the number of the point, along with what the place is and any other
  information you want to record about the place in your notebook.
- Press the “X” button to go to the map page.  You should now see your point
  on the map.

**7. Turn on the Track Log**

- Now that we have learned how to save points, let’s learn how to turn the
  track log on and off.  When the track log is turned on,
  it will automatically record your path.  It’s good practice to turn on the
  log when you begin mapping, and turn it off when you are finished.  You
  will then be able to look at the track on a computer and see the path that
  you mapped.  If you would like to map the course of a road,
  it is a good idea to save a waypoint at the beginning and end of the road,
  writing in your notebook the name and type of the road,
  and any other important information about the road.
- To turn on the track log, click the “X” button until your reach the page
  that says Track Log.

.. image:: /static/training/beginner/osm/image58.*

- If you would like to empty the track log to delete earlier recordings,
  use the joystick to select “Clear”, and press the joystick down.  The bar at
  the top should read “0%”.
- To turn on the log, move the joystick to highlight “On”,
  and press the joystick down.  The track log is now recording your path.
- Under the “Set up” option, you also can set time or distance intervals to
  track.  Time intervals instruct your GPS to record your location at given
  intervals.  If you have a memory card in your GPS, it is good practice to
  set this to 1 second, meaning that every second your location will be added
  to the track log.  This may be useful when detailed surveys are needed.
- Press the “X” button to go to the map page.  As you move you will see your
  track shown as a series of dots.

**8. Copy Waypoints and Tracks to the Computer**

*8.1. Attach GPS to the Computer*

- When you are finished mapping with the GPS you will want to copy the
  points and tracks to your computer so that you can open them in JOSM.
  First, turn off the track log on your GPS, by going to the track page and
  selecting “Off”.
- Attach the GPS to your computer with the cable.  One end should plug into
  your computer’s USB port, and the other goes into the back of the GPS,
  beneath the rubber flap at the top.  The GPS should be turned on to copy
  the points and tracks.

*8.2. Install GPS Drivers*

- You may need to install GPS drivers on your computer.  Open your training
  folder and find software/USBDrivers_23.exe.  Double-click it and install.
- If you don’t have this file, you can download it.  Open your internet
  browser and go to: `http://www8.garmin.com/support/download_details
  .jsp?id=591 <http://www8.garmin.com/support/download_details.jsp?id=591>`_

- Click “Download” to get the installation file.  Locate it on your
  computer, and double-click to install.

*8.3. Get the GPSBabel Setup Program*

- GPSBabel is a program that allows us to copy data from the GPS.  It is
  saved as GPSBabel-1.4.2-Setup in the software/ folder.
- If you don’t have GPSbabel already, open your web browser and go to
  `www.gpsbabel.org <http://www.gpsbabel.org>`_

- Click “Downloads” at the top of the page.
- Scroll down the page.  If your computer uses Windows,
  you want to download the installation file for Windows.  Click
  GPSBabel-1.4.2-Setup.exe.  The file will be downloaded to your computer.

*8.4. Install GPSBabel*

- Locate the GPSBabel setup file on your computer.  Double-click it to
  install.
- Click “Next”.
- Click “I accept” and “Next”.
- Continue clicking “Next” until the program installs.
- When the program has finished installing, click “Finish” to start GPSBabel.

*8.5. Copy Tracks and Waypoints*

- Click in the circle next to the word “Device” at the top of the window.

.. image:: /static/training/beginner/osm/image59.*

- In the dropdown menu labelled “Format”, select “Garmin serial/USB protocol”
- Go down to the middle of the window, under Output.  In the dropdown menu
  labelled “Format”, select “GPX XML”:

.. image:: /static/training/beginner/osm/image60.*

- Click “File Name” and type a name for your saved file.  It should be
  something that describes the data, such as the date and the location.  For
  example, jakarta-07-07-2011.
- Make sure your GPS is connected to the computer and turned on.
- Click “Apply” in the bottom right corner of the window.
- If all goes well you should see a bar move across the screen,
  indicating that the data is being retrieved from the GPS.  When it is
  finished, your points and track will be saved in the file that you selected.

*8.6. Open in JOSM*

- Now open JOSM.  On the top menu, click “File” and then click “Open...”
- Find and select the file that you created with GPSBabel.  Click “Open”.
- You should now see your points and tracks loaded into JOSM.

.. image:: /static/training/beginner/osm/image61.*

**9. Upload GPS data in JOSM**

Adding GPS tracks and waypoints to the OSM server is very useful for many
reasons / goals. (If you don’t want your GPX data is seen by others,
you don’t need to read this section. You just show your GPX Data on JOSM
locally on your computer). First of all, it should be understood that the
tracks GPS is the most helpful way to collecting data and georeference
(provides geographic/spatial references) objects in the OSM. Upload GPX
tracks to the server allows you to share more information. Other people who
don’t have access, who can’t reach the location or because of the
limitations of GPS, they can still obtain information of data without the
need to stay / settle on that location and do not need to rent a GPS.

The easiest way to upload GPS tracks is to download the plugin "DirectUpload":

- Open JOSM and Click Edit - Preference - Plugin box.
- Type directupload on the “Search” box, give the check mark, then click OK.

.. image:: /static/training/beginner/osm/image62.*

- Restart JOSM.
- Open your GPX file on JOSM.
- Click “Tools” menu and then click submenu “Upload Traces”

.. image:: /static/training/beginner/osm/image63.*

- Describe your GPX file, write multiple tags, and visibility. On visibility
  option, you can chose “private”, “public”, “trackable”, or “identifiable”:

1. Private: tracks will not appear on the public track list. Trackpoints are
   accessible at different times through the GPS APIs public without time
   stamp.
2. Public: your tracks will be visible to the public (general) on your GPS
   tracks and GPS tracks on the public list. Other users can still download
   your tracks from the public track list and their time making a point
   contained in it. However, the data does not appear in the API reference on
   the page of your tracks.
3. Trackable: tracks will not appear on the track list public,
   but trackpoints will remain accessible via the public API and its GPS time
   taking its points. Other users can still download trackpoints but it will
   not be referenced with you.
4. Identifiable: Your tracks will be visible to the public (general) on your
   GPS tracks and public GPS tracks list. Other users can download your tracks
   and connect with your username. Making time points on the track can also
   be accessed through the public API GPS.

.. image:: /static/training/beginner/osm/image64.*

- Click <<Upload Trace>>. If requested to enter a username and password,
  you can enter the username and password of the account OpenStreetMap and
  check the "save user and password" then click “Authenticate”.

**10. Edit GPS Data using JOSM**
After you successfully open and upload the GPS data, you must enter the GPS
data as the field result into OSM server. The following way:

- Open a file gpx results of your field data back using JOSM.
- Click File - Download from OSM, You don’t have to re-draw the box to
  download because JOSM been reading your region according to the GPS layer
  automatically. Click “Download”.

.. image:: /static/training/beginner/osm/image65.*

- After downloading the data successfully and appears in JOSM layer,
  you can edit the OSM Data (Data Layer) is based on the GPS field data. To
  make it easier to add data, you can add Bing Satellite imagery. You can
  draw an uncharted street (a line) with the following results of the
  existing record GPS tracks.

.. image:: /static/training/beginner/osm/image66.*

- After you have finished editing OSM data, don’t forget to upload the data
  to the OSM, click File - Upload Data.
