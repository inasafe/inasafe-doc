Using Orbview3 Imagery in JOSM
==============================

Basic Competition
-----------------

After studying this chapter, the participants will be able to: 
-	Understanding of satellite imagery Orbview3 both in its use and license. 
-	Downloading satellite imagery Orbview3 through the USGS 
-	Running JOSM software with additional memory 
-	Digitizing satellite imagery Orbview3 in JOSM with the ImportImage plugin

A. Downloading Imagery Orbview3 from USGS
-----------------------------------------

When you digitize a region by using JOSM, problems frequently arise that satellite imagery (Bing) are not clear, covered with clouds even some area don’t have detailed satellite imagery. These problems can be solved by using a plugin in JOSM is “ImportImagePlugin”, with these plugin you can open imagery obtained from other sources and used for digitizing. One of the imagery that can be used is Orbview Imagery that can be downloaded for free in <http://earthexplorer.usgs.gov/>`_.

.. image:: /static/tutorial/ToT/2_tot_1.png
   :align: center

Orbview 3 has a spatial resolution of 1 meter (panchromatic) and 4 meter (multispectral), orbiting at an altitude of 470 km, the resolution temporal is 3 days and were able to record the data of 2,100 km2.
A steps to download the Orbviewimagery :

1.	Visit the website <http://earthexplorer.usgs.gov/>`_ , requirement to download the imagery must have an account at the USGS, if you don’t have an account you can click “Register”

.. image:: /static/tutorial/ToT/2_tot_2.png
   :align: center

2.	There is some information should be filled in the register window is Login, User Affiliation, Address, and Confirmation. In the login window, you are prompted to enter a username and password that will be used to login when using the USGS. 

.. image:: /static/tutorial/ToT/2_tot_3.png
   :align: center

3.	Next you need to fill out some relating to your purpose using the imagery derived from USGS. The field box is long enough, you don’t have worry about this, just fill your needs, and the USGS just want to know the downloaded imagery is used for what purposes.
 
.. image:: /static/tutorial/ToT/2_tot_4.png
   :align: center
 
4.	The address box contains information about you that must be completed. When it is complete can click continue and wait for the registration process. At this step you have successfully created an account in USGS. 

.. image:: /static/tutorial/ToT/2_tot_5.png
   :align: center

5.	After login with your account, you can begin the process of downloading imagery in an area you want. In the below window, will display satellite maps, you can select the area you want to downloaded to pan and zoom in/zoom out until the area you want can be found. For example, you want to download a region Sorong, Papua Barat. The next step you have to draw a box around the area you want downloaded.
6.	When an error occurs in the area you choose, you can click “clear kriteria”. Clear criteria function to remove the area you have chosen, so you can start to choose the area you want. How to draw a box with the left click one by one to form a polygon. Then click “Data Sets” (located in the bottom left box).

.. image:: /static/tutorial/ToT/2_tot_6.png
   :align: center 

7.	In the window will appear some a imagery list can download, select OrbView 3 and click Results. 
 
.. image:: /static/tutorial/ToT/2_tot_7.png
   :align: center
 
8.	The result is aOrbView 3 imagery that will appear in the left column, you can choose which one you want to download or entirely. 

.. image:: /static/tutorial/ToT/2_tot_8.png
   :align: center

In the left column there are several menus to description on the OrbView 3 imagery, namely:
.. image:: /static/tutorial/ToT/2_tot_9.png
   :align: left		   				= show footprint to determine the coverage area of the imagery will be downloaded

.. image:: /static/tutorial/ToT/2_tot_10.png
   :align: left   					= show browse overlay is one part of the show footprint 

.. image:: /static/tutorial/ToT/2_tot_11.png
   :align: left   					= show metadata and browse to display the data from the imagery will be downloaded 

.. image:: /static/tutorial/ToT/2_tot_12.png
   :align: left					   = download option to download the imagery you want to use

9.	When you have to select one imageryor all imagery you want to download, a command will appear where you must select which one of the data that will be used like as the image below, you can select the fourth line.

.. image:: /static/tutorial/ToT/2_tot_13.png
   :align: center

10.	Then you can save the imagery data and the result in the form .rar, if the extracted result consists of 3 files, the format as shown below. 
 
.. image:: /static/tutorial/ToT/2_tot_14.png
   :align: center
 
B. Add Memory in JOSM
---------------------

Often when we *ImportImage* plugin to display the OrbView imagery, will appear warning like this, 

.. image:: /static/tutorial/ToT/2_tot_15.png
   :align: center

The display that appears due to insufficient memory in JOSM 

Look like this because the memory allocated for JOSM only 494 MB so that to carry out the command displaying images, JOSM don’t have enough memory. It is certainly will be difficult for us to use satellite imagery that we’ve had. But this can be solved with some enough complicated techniques.   

1.	Find a file named “josm-tested.jar” in program files >josm> josm-latest.jar / josm-tested.jar. On some computers might be the name could be “josm-latest.jar”

.. image:: /static/tutorial/ToT/2_tot_16.png
   :align: center	 
The given file is a file box to be created shortcut 

2.   Create a new file with a text editor (Notepad or Notepad++), then copy the contents of text below into your notepad:

:samp: java -jar -Xmx1g josm-tested.jar

3.  Then click File > Save As. Save the notepad file in the folder Program Files > JOSM with the ALL FILES  format and then give it a name with the suffix “.bat” for example “run-josm-more-memory.bat” (without quotation marks) or can change Save As Type to Batch File (*.bat, *.cmd *.nt).

.. image:: /static/tutorial/ToT/2_tot_17.png
   :align: center	

4.  Now copy a file that you created as a shortcut (right click > create shortcut), then save on the Desktop.

.. image:: /static/tutorial/ToT/2_tot_18.png
   :align: center

5.  If you want to run JOSM with larger memory, you can double click in the shortcut you created. It will be come out a command prompt window. Wait a moment, JOSM will run with larger memory and you can open larger the OrbView 3 satellite imagery by utilizing aImportmage plugin.

.. image:: /static/tutorial/ToT/2_tot_19.png
   :align: center
 
Display indicating that you have successfully executed JOSM with larger memory allocation


C. Using  the“ImportImage” Plugin in JOSM
-----------------------------------------

Important thing to do before using the OrbView imagery in JOSM that adds memory (you can see the steps of additional memory in tutorial).After you download from USGS, and get Orbview imagery file in format .rar, to open the imagery in JOSM you need to download the “ImportImage” plugin. Steps to be carried out, is:

- Open JOSM, then click Edit – Preferences – box Plugin (power jack icon) – ImportImagePlugin, click Ok and Restart JOSM.

.. image:: /static/tutorial/ToT/2_tot_20.png
   :align: center

- After JOSM open again, before you add imagery to JOSM first you have to setting coordinate in UTM projection which is same with the imagery. You can do it with click Edit – Preferences – PilihKotak Presets (di bawahgambar globe) – Map projection – Ok – and you don’t have to restart your JOSM again.

If you don’t know the coordinate of the imagery that you download, you can see it in Quantum GIS with open it in JPG format and right click on the image then click Properties and the coordinate information will shown.
 
.. image:: /static/tutorial/ToT/2_tot_21.png
   :align: center
 
- Once the image is properly projected, you can now open the image in JOSM.  Click File ? Import Image and open the file you recently downloaded.  You should find three files in the extracted folder (.rar).  You want to chose the .jpg. 

.. image:: /static/tutorial/ToT/2_tot_22.png

- Wait until the image opens in JOSM. OrbView imagery is panchromatic, so it is black and white like image below.  Roads, rivers, vegetation and buildings can still be seen

.. image:: /static/tutorial/ToT/2_tot_23.png

- Everytime you want to add information or digitize in JOSM, you must always remember to “Download From OSM”,  it is very useful as a layer to know what data that have been digitize on OpenStreetMap with other users.Hopefully, with the new imagery you will be able to digitize uncharted territory or improve existing data.

.. image:: /static/tutorial/ToT/2_tot_24.png

- After you add and edit data from imagery on OSM layer you can upload that changes with click File – Upload Data.

D. Summary
-----------

Congratulations! You should now be able to add satellite imagery using the ¨ImportImage¨ plugin.  In this guide we used free images from Orbview 3, but  the plugin can allow any other  public domain imagery.

### Final Reminders:
- You cannot import commercial satellite imagery, such as Google Earth Imagery, to OpenstreetMap.  If you work with satellite imagery please read the terms and conditions beforehand. It is not legal to copy commercial or other maps onto OpenstreetMap.
- Satellite images must have coordinate files or coordinate information. Be sure to know the coordinates of the satellite imagery (map projection) you are using and adjust your settings in JOSM.
- If you wish to return to using Bing Imagery, make sure the map projection settings are returned to **Mercator WGS 84**.

F. Appendix
------------

:Panchromatic imagery: Constructed from multiple images captured by sensors which have different wavelengths. image photo made using visible spectrum from red to violet color with wavelengths from 0.4 to 0.7 microns.
:Sattelite imagery:	is of the Earth surface description recorded by the sensor (camera) on a satellite orbiting the earth pengideraan far, in the form of image (image) digitally.
:A command prompt: dos command contained in the Windows OS that can allow a user to navigate the windows, both online and offline
:Dataset: Numbers of the data sets
:Digitization process: rawing features in a spatial map into digital format via an application example in JOSM
:Footprint: To determine the coverage area of the image to be downloaded
:ImportImage: in JOSM Plugin A plugin that allows you to open and import an image of an image (. Jpeg) into JOSM so have a coordinate system.
:JOSM: tool that can help you in the process of mapping objects to gather information on OpenStreetMap.
:Coordinate: Shows the location coordinates of a point on the Earth based on latitude and longitude.
:Layer: a visual representation of geographic data sets in a digital map environment. Conceptually, layers or strata is a geographic reality in a particular area, and is more or less equivalent to a legend item on a paper map.
:Metadata: Data that contains spatial information, containing information regarding the characteristics of the data and plays an important role in the mechanism of data exchange. Through the metadata information is expected to interpret the data user data together, when users see immediate spatial data
:Multispectral image: the recording by using more than one channel / band / wavelength.
:OrbView: An image that has a temporal resolution of 3 days, orbiting at an altitude of 470 km. These satellites can record data covering 2,100 km2 every minute of it.
:Overlay: objects that overlap with each other object in the map
:Plugin: a plug-in (or plugin) is a set of software components that adds specific capabilities to software applications greater. If supported, plug-in allows to change the function of the application
:The transfer of data: a projection topography of the earth's surface to the top of a flat surface.
:Projection mercator: geographically offending cylinder on a meridian earth called the central meridian.
:Resolution: image quality of the lens that is expressed with the maximum number of lines in each millimeter that still can be separated by the image.
:Spatial resolution: the smallest object size that can still be distinguished and recognized by the image. The smaller objects that can be recorded, the better the spatial resolution.
:Temporal resolution: ability of the sensor to re-record the same object.The faster a sensor to re-record the same object, the better the temporal resolution.
:USGS: Stands USGS United States Geological Survey (U.S. Geological Survey). USGS scientists are studying the landscape particularly the United States in the field of natural resources, and disasters that threaten it. The organization has four major science disciplines, namely biology, geography, geology, and water.
:UTM projection: which has mercator which have special properties, has transvere  a width of 6 degrees and the units are meters.
:WGS 84: World Geodetic System is a standard coordinate used in mapping, geodesy and navigation, has units of degrees, minutes, and seconds.
