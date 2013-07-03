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

When you digitize a region by using JOSM, problems frequently arise that satellite imagery (Bing) are not clear, covered with clouds even some area don’t have detailed satellite imagery. These problems can be solved by using a plugin in JOSM is “ImportImagePlugin”, with these plugin you can open imagery obtained from other sources and used for digitizing. One of the imagery that can be used is Orbview Imagery that can be downloaded for free in http://earthexplorer.usgs.gov/.
 

Orbview 3 has a spatial resolution of 1 meter (panchromatic) and 4 meter (multispectral), orbiting at an altitude of 470 km, the resolution temporal is 3 days and were able to record the data of 2,100 km2.
A steps to download the Orbviewimagery :

1.	Visit the website http://earthexplorer.usgs.gov/ , requirement to download the imagery must have an account at the USGS, if you don’t have an account you can click “Register”
 

2.	There is some information should be filled in the register window is Login, User Affiliation, Address, and Confirmation. In the login window, you are prompted to enter a username and password that will be used to login when using the USGS. 

 

3.	Next you need to fill out some relating to your purpose using the imagery derived from USGS. The field box is long enough, you don’t have worry about this, just fill your needs, and the USGS just want to know the downloaded imagery is used for what purposes.
 

4.	The address box contains information about you that must be completed. When it is complete can click continue and wait for the registration process. At this step you have successfully created an account in USGS. 
 

5.	After login with your account, you can begin the process of downloading imagery in an area you want. In the below window, will display satellite maps, you can select the area you want to downloaded to pan and zoom in/zoom out until the area you want can be found. For example, you want to download a region Sorong, Papua Barat. The next step you have to draw a box around the area you want downloaded.
6.	When an error occurs in the area you choose, you can click “clear kriteria”. Clear criteria function to remove the area you have chosen, so you can start to choose the area you want. How to draw a box with the left click one by one to form a polygon. Then click “Data Sets” (located in the bottom left box).

 

7.	In the window will appear some a imagery list can download, select OrbView 3 and click Results. 
 

8.	The result is aOrbView 3 imagery that will appear in the left column, you can choose which one you want to download or entirely. 

 

In the left column there are several menus to description on the OrbView 3 imagery, namely:
   = show footprint to determine the coverage area of the imagery will be downloaded
   = show browse overlay is one part of the show footprint 
   = show metadata and browse to display the data from the imagery will be downloaded 
   = download option to download the imagery you want to use

9.	When you have to select one imageryor all imagery you want to download, a command will appear where you must select which one of the data that will be used like as the image below, you can select the fourth line.

 

10.	Then you can save the imagery data and the result in the form .rar, if the extracted result consists of 3 files, the format as shown below. 
 

B. Add Memory in JOSM
---------------------

Often when we *ImportImage* plugin to display the OrbView imagery, will appear warning like this, 


The display that appears due to insufficient memory in JOSM 

Look like this because the memory allocated for JOSM only 494 MB so that to carry out the command displaying images, JOSM don’t have enough memory. It is certainly will be difficult for us to use satellite imagery that we’ve had. But this can be solved with some enough complicated techniques.   

1.	Find a file named “josm-tested.jar” in program files >josm> josm-latest.jar / josm-tested.jar. On some computers might be the name could be “josm-latest.jar”
	 
The given file is a file box to be created shortcut 

2.   Create a new file with a text editor (Notepad or Notepad++), then copy the contents of text below into your notepad:

java -jar -Xmx1g josm-tested.jar

3.  Then click File > Save As. Save the notepad file in the folder Program Files > JOSM with the ALL FILES  format and then give it a name with the suffix “.bat” for example “run-josm-more-memory.bat” (without quotation marks) or can change Save As Type to Batch File (*.bat, *.cmd *.nt).

 	

4.  Now copy a file that you created as a shortcut (right click > create shortcut), then save on the Desktop.
 

5.  If you want to run JOSM with larger memory, you can double click in the shortcut you created. It will be come out a command prompt window. Wait a moment, JOSM will run with larger memory and you can open larger the OrbView 3 satellite imagery by utilizing aImportmage plugin.

 
Display indicating that you have successfully executed JOSM with larger memory allocation


C. Using  the“ImportImage” Plugin in JOSM
-----------------------------------------

Important thing to do before using the OrbView imagery in JOSM that adds memory (you can see the steps of additional memory in tutorial).After you download from USGS, and get Orbview imagery file in format .rar, to open the imagery in JOSM you need to download the “ImportImage” plugin. Steps to be carried out, is:

- Open JOSM, then click Edit – Preferences – box Plugin (power jack icon) – ImportImagePlugin, click Ok and Restart JOSM.

 

- After JOSM open again, before you add imagery to JOSM first you have to setting coordinate in UTM projection which is same with the imagery. You can do it with click Edit – Preferences – PilihKotak Presets (di bawahgambar globe) – Map projection – Ok – and you don’t have to restart your JOSM again.

If you don’t know the coordinate of the imagery that you download, you can see it in Quantum GIS with open it in JPG format and right click on the image then click Properties and the coordinate information will shown.
 

- Once the image is properly projected, you can now open the image in JOSM.  Click File ? Import Image and open the file you recently downloaded.  You should find three files in the extracted folder (.rar).  You want to chose the .jpg. 


 

- Wait until the image opens in JOSM. OrbView imagery is panchromatic, so it is black and white like image below.  Roads, rivers, vegetation and buildings can still be seen
 

- Everytime you want to add information or digitize in JOSM, you must always remember to “Download From OSM”,  it is very useful as a layer to know what data that have been digitize on OpenStreetMap with other users.Hopefully, with the new imagery you will be able to digitize uncharted territory or improve existing data .

 

- After you add and edit data from imagery on OSM layer you can upload that changes with click File – Upload Data.

D. Summary
-----------

Congratulations! You should now be able to add satellite imagery using the ¨ImportImage¨ plugin.  In this guide we used free images from Orbview 3, but  the plugin can allow any other  public domain imagery.

### Final Reminders:
- You cannot import commercial satellite imagery, such as Google Earth Imagery, to OpenstreetMap.  If you work with satellite imagery please read the terms and conditions beforehand. It is not legal to copy commercial or other maps onto OpenstreetMap.
- Satellite images must have coordinate files or coordinate information. Be sure to know the coordinates of the satellite imagery (map projection) you are using and adjust your settings in JOSM.
- If you wish to return to using Bing Imagery, make sure the map projection settings are returned to **Mercator WGS 84**.
