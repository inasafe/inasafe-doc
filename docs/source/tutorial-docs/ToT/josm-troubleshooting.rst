Java OpenStreetMap Editor Troubleshooting
==========================================

Basic Competency
----------------
After studying this chapter, participants will be able to:

1. Understand common technical problems and error messages in JOSM
2. Solving common technical problems in JOSM

When you edit or add data into OpenStreetMap (OSM) through JOSM editor, sometimes you will see these error messages that causing JOSM do not work properly. Here we list some error messages or warning often appear in JOSM, and how to solve them.

1. API error
2. JOSM compatibility for Windows 8
3. Troubleshoot in Remote Control JOSM
4. Uploading data with limited internet connection
5. Plugin do not downloaded and installed properly
6. Projection system do not compatible to OSM data
7. Failed downloading “Bing Aerial Attribution”
8. Internal server error

A. API Error
-------------
.. image:: /static/tutorial/ToT/4_apierror.png
	:align: center
**Problem:**

When you are trying to download OSM data, sometimes this error message (see the picture above) appear. This problem occurs because JOSM could not connect to OSM  server.

**Solution:**

Make sure you have connected to the internet. If you are not connected yet to the internet, please connect it immediately. But, if you have connected to the internet, but still having the same problem, follow the steps as follows :

1. Close JOSM, then go to this directory on your computer:
   **“C:\Users\(username komputer Anda)\AppData\Roaming\JOSM”**
2. You will find these two files :  **“preferences.xml” and “prefrences.xml_backup”**
.. image:: /static/tutorial/ToT/4_preferences.png
	:align: center

3. Move those files to other directory, but make sure to right click on your mouse first and then select **“Cut”**. Store those files in a convenient location in mind (e.g. “Documents”) by right click on your mouse and then select **“Paste”**.
4. Run JOSM. Re-download OSM data. But, perhaps you aware that some settings (for example the plugins setting) are missing. Close your JOSM now.
5. Find your **“preferences.xml”** and **“preferences.xml_backup”** that had been moved, then copy those files.
6.  Open this folder : **“C:\Users\(username komputer Anda)\AppData\Roaming\JOSM”**
7. Right click on your mouse and select **“Paste”**. If other warning appear, select **“Yes”**.
8. Run JOSM.

B. JOSM compatibility for Windows 8
------------------------------------
**Problem:**

For Windows 8 Operating System user, after you install JOSM, you  have to set the JOSM compatibility in order your JOSM work properly.

**Solution:**

The following are the steps to set JOSM compatibility for Windows 8:

1. Right click on JOSM shortcut at your desktop, then select **“Properties”**
.. image:: /static/tutorial/ToT/4_windows8.png
	:align: center

2. You will see “Proprties” window. Click on **“Compatibility”** tab, and check on **“Run this program in compatibility mode for :”**, select **“Windows XP (Service Pack 3)”** or **“Windows 7”**. Finally, check on **“Run this program as an administrator”** also, and then click **OK.**
.. image:: /static/tutorial/ToT/4_josmproperties.png
	:align: center
	
C. Troubleshoot in Remote Control JOSM
--------------------------------------

**Problem:**

Some websites such as KeepRight and Tasking Manager using Remote Control feature in JOSM. Unfortunately, remote control feature sometimes do not work properly, thus JOSM do not respond the request from  KeepRight or Tasking Manager site.
.. image:: /static/tutorial/ToT/4_osmtasking.png
	:align: center

OSM Tasking Manager using Remote Control feature in JOSM 
to connect the area you had choosen in Tasking Manager to JOSM software.

When this problem occurs, no warning or error message appear either in JOSM or your internet browser. In essence, you click an area on Tasking Manager but JOSM do not give any response, it means that there’s a trouble with your “Remote control” feature.

**Solution:**

1. Open JOSM, then click on **Edit** > **Preferences**. Go on tab **Remote Control**, make sure you have check the **“Enable Remote Control”** check box. Restart JOSM.
.. image:: /static/tutorial/ToT/4_preferences2.png
	:align: center

2. Make sure you have run JOSM before you click on ‘JOSM’ button on Tasking Manager or  KeepRight site. If JOSM still not working properly, try to use another internet browser such as Google Chrome, Firefox, or Opera
3. If you have work with another browser but remote control still not working properly, it means that **there is a problem on your localhost**.
4. Open your **“Preference”** Window, go on to Remote Control setting, then note your  **port number** where the remote control works. Commonly, the default setting for your localhost remote control is 8111.
.. image:: /static/tutorial/ToT/4_remotecontrol.png
	:align: center
5. Click on **‘Start’** menu, then select **‘Control Panel’**
.. image:: /static/tutorial/ToT/4_controlpanel.png
	:align: center
6. Click on **‘System and Security’**
.. image:: /static/tutorial/ToT/4_systemsecurity.png
	:align: center
7. Click on **‘Windows Firewall’**
.. image:: /static/tutorial/ToT/4_firewall.png
	:align: center
8. Click on **‘Advanced Setting’**
.. image:: /static/tutorial/ToT/4_advance.png
	:align: center
9. You should see a new window as follow. Click on **‘Inbound Rules’** at the left side, and then click on **‘New Rule’** at the right side.
.. image:: /static/tutorial/ToT/4_newrule.png
	:align: center
10. A new window will appear as shown below. For **‘Rule Type’** choose **‘Port’**, then click on  **‘Next’**.
.. image:: /static/tutorial/ToT/4_ruletype.png
	:align: center
11. Select **‘TCP’**, and choose **‘Specific local ports’**. Fill in the appropriate port number as what defined in the Remote Control setting (the default is: 8111, your port number may be different). Finally, click on **‘Next’** button
.. image:: /static/tutorial/ToT/4_tcp.png
	:align: center
12. Next setting is **Action Setting**. Select **‘Allow the connection’**, then click on **‘Next’** button
.. image:: /static/tutorial/ToT/4_connection.png
	:align: center
13. Next setting is **Profile setting**. Make sure you have check all of the check box on the right side (**Domain, Private, dan Public**). Then click on **‘Next’** button.
.. image:: /static/tutorial/ToT/4_profile.png
	:align: center
14 Finally, you just need to give a name for your setting. Give a name that is easy to remember. And for the **‘Description’** box, you  can leave it blank. Click on **‘Finish’** then restart your computer.
.. image:: /static/tutorial/ToT/4_finish.png
	:align: center
	
D. Uploading data with limited internet connection
--------------------------------------------------
**Problem :**

If your internet connection is slow, but you want to upload your edits on OSM data, some problem may be occurs. The most common problem when you upload OSM data in a big size is some data will be uploaded repeatedly. Thus, when you see the object in JOSM, the object (line and polygon) looks thick (see the picture below).
.. image:: /static/tutorial/ToT/4_poligon.png
	:align: center

So, if you have slow internet connection, to prevent error during upload, try to upload your data periodically such as every 10 - 15 objects or every 5 -10 minutes. The longer you postpone to upload your edits, the bigger data will be accumulated, thus the upload process will take longer time and you may have conflict with other user. 

**Solution :**

If you are already edit a lot of objects, you can split your upload process into some sections, thus  it need less internet connection bandwith.
Here are the steps to split the upload process :

1. Once you upload OSM data by click on “Uplaod” icon, you will see the window below. Click on **‘Advanced Configuration’**
.. image:: /static/tutorial/ToT/4_advance2.png
	:align: center

2. Choose **‘Upload data in chunks of objects’** option. Here, you can define the number of objects you want to upload for each upload process. For example, you want to upload 5000 object, and previously you have define to upload every 1000 object, thus the upload process will be divided into 5 times and each upload process JOSM will upload 1000 objects. Don’t forget to click on **‘Upload Changes’** after you change the setting. By split upload into some sections, upload process will be lighter and faster, even in a slow internet connection.
.. image:: /static/tutorial/ToT/4_chunk.png
	:align: center

**Note :** You do not need to return to this window every time you want to split your upload process into some sections. Once you set it and upload your data, JOSM automatically will save this setting for the next upload process. You can easily change the number of object you want to upload for each upload process through this setting.

E. Plugin not downloaded and installed properly
-----------------------------------------------

.. image:: /static/tutorial/ToT/4_tot_1.png
   :align: center
   
**Problem :**

This problem occurs because the plugin failed to be downloaded or not downloaded completely (for example, because of the internet connection suddenly cut off in the middle of the download process). 


**Solution :**

Alternative 1
 
Download the plugin again when the internet connection stable. However, the previous plugin that you have download before (but didn’t download completely) must be removed first. Here are the steps to remove the plugin :

1. Open this folder **“C:\Users\SamsungOke\AppData\Roaming”** (Note : “SamsungOke” is the name of your laptop). Actually there is a faster way to open this folder by click on **“Start”** menu at the bottom left corner of your laptop, then type  **“%AppData%”**

.. image:: /static/tutorial/ToT/4_tot_2.png
   :align: center

It will show you a name of a folder called **"Roaming"**. Select (left click) on the name (“Roaming”). Then, the **"Roaming"** folder will be opened, as shown below :

.. image:: /static/tutorial/ToT/4_tot_3.png
   :align: center
   
2. Once the **“Roaming”** folder is open, find a folder called **JOSM**. Open JOSM folder (Attention ! This folder is not located in “C:\Program Files”). Here is the content of the folder:

.. image:: /static/tutorial/ToT/4_tot_4.png
   :align: center

After you open the JOSM folder, find **“plugin”** folder and open it, then remove the plugin that failed to be downloaded previous. In this example, you failed to download “building_tools” plugin. So, just delete “building _tools” plugin file .

.. image:: /static/tutorial/ToT/4_tot_5.png
   :align: center

3. After you remove that file, re-download and install the plugin when the internet connection was stable. 

Alternative 2

However, if the internet connection is not stable or weak connections (so the download becomes very long), you can install the plugin in offline (without the download plugin from the internet). However, to use this way, one of your friend must have already successfully download and install this plugin. Here’s how to learn more :

1. Copy the plugin you want from your friends who have managed to download and install the plugin. Where are the plugins? That is at the folder  “Roaming” as describes in alternative 1.
**“C:\Users\samsung\AppData\Roaming\JOSM”**
It will opened the folder JOSM, and then go to the **plugin** folder. In the plugin folder, you wil see several folders that are installed on your JOSM. 

.. image:: /static/tutorial/ToT/4_tot_6.png
   :align: center

Once the plugin folder (picture above) on your friend’s computer open, copy the plugin you need. Save to your flash. 

**Note :**

* If the plugin does not have the extra folder, you can simply copy the file extension **.jar (Executable Jar File).** Example, for plugin “building tools”, You can simply copy one file is **“building_tools.jar”**.

.. image:: /static/tutorial/ToT/4_tot_7.png
   :align: center

* If you need plugins have additionals folder, you need copy the folder anyway. Example for the “ImportImage” plugin, you need copy the two files are file **“ImportImagePlugin.jar”** and the **”ImportImagePlugin”** folder.

.. image:: /static/tutorial/ToT/4_tot_8.png
   :align: center

2. Open your flash, find the plugin file that you have copied, then **“Paste”** the plugin on your computer. Where have to paste these plugin? That is the folder where the plugins should be installed (this folder is the same folder where the plugin is copied), namely :

**“C:\Users\samsung\AppData\Roaming\JOSM\plugins”**

.. image:: /static/tutorial/ToT/4_tot_9.png
   :align: center

3. The process that you just do not yet enable / install the plugin, you still have to install the plugin. How :

* Open your JOSM, and then go to **“Preference”**  (cick this icon image:: /static/tutorial/ToT/4_tot_10.png or click menu **“Edit”** > **“Preferences"**)
* Go to the tab **“Plugin”** image:: /static/tutorial/ToT/4_tot_11.png , and type the name of plugin you just copy. Now you should be able to see the plugin in the plugin list.
* Tick at the check box beside the name of the plugin. 

.. image:: /static/tutorial/ToT/4_tot_12.png
   :align: center

Then click OK, Installation should instantly work and the following message box will appear.

* Don’t forget Restart your JOSM

F. Projection system do not compatible with OSM data 
----------------------------------------------------

.. image:: /static/tutorial/ToT/4_tot_13.png
   :align: center

**Problem :**

When you download the OSM data, sometimes the OSM data can not appear, but instead appear as above. This is because the projection system is not defined on JOSM proper projection system. The recommended projection system are  (i) **Mercator**, or (ii) **WGSGeographic84**. Why? Because basically OpenStreetMap is covering the whole world, then the projection system used is a global projection, which can cover the entire region of the world. If it appear like the picture above, please check the coordinate system defined in your JOSM. How :

* Open your **JOSM**, then go to **“Preference”** (click this icon image:: /static/tutorial/ToT/4_tot_10.png  or click menu **“Edit”** > **“Preferences”**)
* Select the tab for 3 from the top, with a picture image:: /static/tutorial/ToT/4_tot_15.png. Then select the leftmost tab “Map Projection”. Once the page **“Map Projection”** is open, Look in “Projection method”. In the following example, the system-defined projection is “Belgian Lambert 1972”. Projection system is not the proper projection system to appear the OSM data. That’s why the OSM data can not open and appeared properly.

.. image:: /static/tutorial/ToT/4_tot_16.png
   :align: center

**Solution :**

To fix this problem, you should change the projection system on JOSM with proper projection system, namely  (i) Mercator atau (ii) WGSGeographic84. How :

* Open your **JOSM**, then go to **“Preference”**  (click this icon image:: /static/tutorial/ToT/4_tot_10.png or click menu **“Edit”** > **“Preferences”**)
* Select the tab for 3 from the top, with a picture image:: /static/tutorial/ToT/4_tot_15.png. Then select the leftmost tab **“Map Projection”**. Once the page “Map Projection” is open, look in the “Projection method”. In the following example, the defined projection system is “Belgian Lambert 1972”. Replace the projection system, Gantilah sistem proyeksi tersebut, a (i) **Mercator** or (ii) **WGSGeographic84**.

.. image:: /static/tutorial/ToT/4_tot_17.png
   :align: center

* Note : You can also replace the projection system to UTM. However, you should know what is right in the zone region you download it. If you wrong on the defining zones, the same problem (the OSM data not appear in JOSM) will occur.
* After you have defined the correct projection system, click OK then download OSM data back.

G. Failed to download “Bing Aerial Attribution”
------------------------------------------------
.. image:: /static/tutorial/ToT/4_bing.png
	:align: center
**Problem :**

To use the imagery from “Bing” (**Bing satellite**), first of all JOSM should download “Bing aerial attributions” (“Bing aerial attributions” is a file contains basic information about the Bing imagery). The download process may have problem/failed because an internet connection. JOSM will display an error message like **“Error loading Bing attributions”** at the bottom right corner (see picture above). Here is a part from “Bing aerial attributions”.
.. image:: /static/tutorial/ToT/4_bing2.png
	:align: center

If the downloaded file fails, then an error message **“Error loading Bing attributions”** will appear at the bottom right corner of JOSM. 

**Solutions :**

* Solution for solve this problem same like solution to solve the problem “API Error” (see problem no.1)

H. Internal Server Error
------------------------
.. image:: /static/tutorial/ToT/4_ise.png
	:align: center
**Problems :**

When you downloading data from OSM server or uploading data to the OSM server, JOSM tries to build a connection with the OSM server that has been configured on “Preferences” in JOSM. However, sometimes problems occur in the OSM server. If the OSM server is having trouble, then JOSM will display an error message like picture above.

**Solutions :**

Problem like these are temporary problems (only happens at certain times). Because an error on the OSM server, then there is nothing you can do to fix it. Wait a moment, and try to download or upload data OSM again. 

I. Glossary 
------------
:JOSM: This tool can help you in the process of mapping to gather an object information in OpenStreetMap.

:API: Stands for Application Programming Interface, a set of function that basic services ready to be executed by entities external programming. 

:Server: A computer system which provide types of certain services within a computer network. 

:Plugin: In computing, a plug-in (or plugin) is a set of software components that adds specific capabilities for the greater software application. If supported, plug-in allow to change the application function.

:Keep Right: One of website that automatically detects errors or warnings in OpenStreetMap data. It is usually used to quality assurance in the OpenStreetMap data. 

:Tasking Manager: Mapping tool designed and built for the humanitarian OpenStreetMap team  collaborative mapping. 

:Remote Control: Setting in JOSM which allows allows to connect to the data (maps) are stored in a server on the Internet. With the Remote Control, the JOSM can receive a map of the WFS and WMS, for example from the site Keep Right or Tasking Manager.

:Localhost: Delivering the web browser on a HTTP server that is installed on the local computer.

:Sistem Proyeksi: A way of presenting the business of a form that has a certain dimension to another dimension.

:Port: Mechanism that allows a computer to support multiple sessions and connections with other computers in the network program.

:TCP: Transmission Control Protocol (TCP) is a protocol in the transport layer (be it in the seven layers of the OSI reference model or models DARPA) connection-oriented (connection-oriented) and reliable (reliable).

