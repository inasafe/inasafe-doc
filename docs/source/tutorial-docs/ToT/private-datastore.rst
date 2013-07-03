Using Private Data Store
========================


Basic Competency
-----------------
After studying this chapter, participants will be able to:

1. Understanding the function of SDS
2. Understanding the types of data that can be published and the data is private
3. Install the plug-in SDS into JOSM
4. Insert presets in SDS
5. Using the plug-in SDS in sorting general data and privacy
6. Accessing the online datastore
7. Creating private accounts datastore
8. Manage private data store as an admin
9. Creating a new project in a private data store

A. Introduction
---------------
OpenStreetMap data is open and available to anyone who would like to access it.  However, there may be times when you want to use OpenStreetMap to collect data, but you would like to keep some attributes stored in a private database.  For this, HOT has developed an additional tool for JOSM known as the SDS (Separate Data Store).

The SDS allows you to create maps and add data into JOSM the same as always, but when you upload your edits, public data will be saved to the OpenStreetMap database, and private data will be saved separately to the HOT Datastore.
.. image:: /static/tutorial/ToT/3_dataflow.png
	:align: center
How the SDS Plugin works with JOSM
----------------------------------
Data uploaded to the private HOT Datastore is only accessible to people who have an account at datastore.hotosm.org.  This chapter is designed for people who already have an account and desire to store private geospatial information, such as household income, personal health care data,  or the location of gold mines.  If you do not have a HOT Datastore account or if you want to set up your own private datastore server please contact Kate Chapman (k8chapman@gmail.com).


### 1.  Installing the SDS plugin
This plug-in allows private data to be streamlined into the private data store.  The newest version of JOSM is required for the SDS plugin to run.  (If you do not have a recent version of JOSM, download and install it from http://josm.openstreetmap.de/.  If you cannot install the latest version, go to the Appendix to see how you can install this plug-in by source).

* Open the preferences menu in JOSM and go to the plugins tab.
.. image:: /static/tutorial/ToT/3_plugin.png
	:align: center
* Click “Download List” to ensure that all available plugins are listed.
* In the search box, type “sds”.
.. image:: /static/tutorial/ToT/3_pluginbox.png
	:align: center

* Check the box next to the plugin to activate it.  You will need to restart JOSM.

* If JOSM is open, restart it.

If the steps above works fine / successful then you do not need to perform the steps described below. But if it does not work find the plugin "sds" in the Preferences menu, you have to perform manual steps in the install plugin sds, namely:

* Download the plugin sds in http://kunden.geofabrik.de/03df698c95134f04949eb67ac7ba2195/   website and click on sds.jar, then you are instructed to keep the plugin.

* Click the Start Menu and type "% APPDATA%" in the search box. Click the name of the folder "Roaming".
.. image:: /static/tutorial/ToT/3_roaming.png
	:align: center

* In the open window, double-click on "JOSM" to open the program file JOSM.
* Double-click the folder "plugins"
* Move sds.jar that have been downloaded to this folder
* If the JOSM is open you must be restart it first.

### 2.  Using the Plugin

Editing the map works just the same as before.  The only difference is that when you upload changes, some tags will be automatically saved on the private datastore, and the rest will be saved directly onto OpenStreetMap.

* After installing the plugin, the first time you download data you will be asked for your HOT datastore username and password.
.. image:: /static/tutorial/ToT/3_api.png
	:align: center


* In order to use the plugin, you need to enter your username and password.  To save them, check the box next to “Save user and password.”
* The private datastore is now working.  When you upload changes, the usual tags will be saved to OSM, and special private tags will be saved to the datastore.

### 3.  How SDS Plugins Works

How does the plugin know which data you want to store on OpenStreetMap and which data you want to store publicly?  Quite simply, it knows because of the tags.  Normal tags go to OpenStreetMap, as always, but you can use new tags with a special prefix that will be sent to the private datastore.  By default, any tag that begins with the prefix “hot:” will go to the private datastore.  If you open the Preferences menu you will see a new tab on the bottom for SDS plugin options:
.. image:: /static/tutorial/ToT/3_preferences.png
	:align: center


There are some basic settings here.  By default the server URL is set to the HOT datastore, and your username and password can be saved here as well.  The line labelled “SDS tag prefix” contains the prefix that will cause tags to be saved on the private datastore.  By default it is “hot:”

When you create or edit an object on the map, you can apply tags like this:
.. image:: /static/tutorial/ToT/3_attributebox.png
	:align: center


In this case, the first two tags will be saved on OSM.  The third tag, because it has the prefix hot: will be saved on the private datastore.

You will most likely collaborate with others when using the private datastore, so you will have a standard list of tags to use for the specific data your are collecting.  These tags can then be made into a presets menu, which will provide an easy-to-use form for adding both public and private data.

### 4. Access Datastore Online

You could access datastore online through http://bit.ly/sds-hot2 and login with your username and password.
.. image:: /static/tutorial/ToT/3_sds.png
	:align: center
	
#### 4.1 Private Data Store Users
There is 2 types of Data Store users. They are Admin who can add new projects or users onto SDS and Personal are regular users who joined on some project that using SDS. This is the screenshoot :
.. image:: /static/tutorial/ToT/3_datastoreuser.png
	:align: center

#### 4.2 Figure of Using Private Data Store and JOSM 
.. image:: /static/tutorial/ToT/3_datastorefigure.png
	:align: center

#### 4.3 Editing Data Store Online

You can edit your data in SDS online. These are the steps :

* Open this site http://bit.ly/sds-hot2
* Username : test@example.com (Personal)
* Password : osmosm123
* Clik tag search
.. image:: /static/tutorial/ToT/3_tagsearch.png
	:align: center

* Add ‘String’ which is a name when we saved the sds tag and click search
.. image:: /static/tutorial/ToT/3_string.png
	:align: center
* You only can edit the objects attribute that has saved in JOSM but if you want to delete objects you must to use JOSM.
* Click Save Tags
.. image:: /static/tutorial/ToT/3_saveobjects.png
	:align: center
	

#### 4.4 Add data on Data Store Online

You can directly add your data on Data Store. These are the steps :
.. image:: /static/tutorial/ToT/3_sds2.png
	:align: center
* Click Map Search and Load OSM Geometries
.. image:: /static/tutorial/ToT/3_mapsearch.png
	:align: center
* After that add/edit information about object that chosen by you
.. image:: /static/tutorial/ToT/3_mapsearch2.png
	:align: center
.. image:: /static/tutorial/ToT/3_mapsearch3.png
	:align: center
* After you finish click Save tags
.. image:: /static/tutorial/ToT/3_savetag.png
	:align: center


#### 4.5 Add and Edit User on Private Data Store

* Open this site : http://bit.ly/sds-hot2 
* Username : admin@example.com (admin)
* Password : osm
* Klik user administration
.. image:: /static/tutorial/ToT/3_useradministration.png
	:align: center
* Click Add New User
.. image:: /static/tutorial/ToT/3_newuser.png
	:align: center

* Click Save if you finish
.. image:: /static/tutorial/ToT/3_saveuser.png
	:align: center
	
Edit Users
* Click user administration
* Click “Eye Symbol” in the left box
* Click Edit User
.. image:: /static/tutorial/ToT/3_edituser.png
	:align: center
.. image:: /static/tutorial/ToT/3_edituser2.png
	:align: center
.. image:: /static/tutorial/ToT/3_edituser3.png
	:align: center	

       
#### 4.6 Add Project on Private Data Store

* Click Project
* Click Create New Project
.. image:: /static/tutorial/ToT/3_addproject.png
	:align: center
.. image:: /static/tutorial/ToT/3_addproject2.png
	:align: center
.. image:: /static/tutorial/ToT/3_addproject3.png
	:align: center


* Next you have to write **Tag Fields Definition** in JavaScript Object Notatioan (JSON) language. You have to translate Extensible Mark-up Language (XML) language at **Preset that you want to use into JSON language.** 
* Let’s see the difference between **XML Preset and JSON**
**XML**
.. image:: /static/tutorial/ToT/3_xml.png
	:align: center
       
**JSON**
.. image:: /static/tutorial/ToT/3_json.png
	:align: center

**NOTE:** 
1. If your preset use **ELEMENT COMBO, MULTISELECT or CHECK KEY** it must converted with format

{“type”:”select”,”tag”:”YOUR KEY”,”en”:”YOUR COLOUMN TABLE NAME”,”option”:[“VALUES 1”,”VALUES 2”, “DST..”]},

Example **(first is XML, second is JSON)**
.. image:: /static/tutorial/ToT/3_xmlandjson.png
	:align: center

2. If your preset use **ELEMENT TEXT**, it must converted with format

{“type”:”text”,”tag”:”YOUR KEY”,”en”:” YOUR COLOUMN TABLE NAME”},

Example (first is XML, second is JSON)
.. image:: /static/tutorial/ToT/3_xmlandjson2.png
	:align: center


Write your tag definition into JSON language at the available row of Tag Field Definition (JSON)
.. image:: /static/tutorial/ToT/3_tagjson.png
	:align: center

* You can upload your presets in your project to the row of **Preset File**
* Click **Create Project** if your finish
* If you click **Project** on right corner, you can see your Project. Click **View Table**  to see the data. If there is any ERROR, it possibly there is **mistake at your JSON tag definition!** If it doesn’t you will see a table like this :
.. image:: /static/tutorial/ToT/3_tagtable.png
	:align: center
* You also can download the table in the CSV format or Excel format.

B. General Questions
---------------------
***How to save our data?***

To save your private data the steps are similar like upload your changes to OSM. Remember to always use right prefix (in this case is :hot) with your private tag to make sure that they will be saved on your private database and would not be published.

***How much users can use the same account? How if I would like to add users?***

There is no limit for users account. At the moment users access organized by HOT

***How much data that I can save in my private server?***

A lot of Data

***Is there any easy way to search certain private data?***

When you login to the datastore.hotosm.org you will have a choice to do some tag search. This is possible to you to search certain tag.

C. Summary
-----------
In this chapter we learn about how to install SDS plugin and how to use it to save some specific data for private datastore. You have seen the website private datastore and see how to save some information separately. SDS is a great tool to your group to collect private information using OpenStreetMap. If you want to collect private information, call HOT and manage your data type which are want you save in private datastore.

D. Appendix

**Geometries** In OpenStreetMap, is drawing shapes on OpenStreetMap maps.

**JSON**  JavaScript Object Notation (JSON) is a text-based open standard designed for human in 
                 	 data exchange.

**Plugin** 	In computing, a plug-in (or plugin) is a set of software components that adds specific capabilities to software applications greater. If supported, plug-in allows to change the function of the application.

**Prefix**	 Prefix. Affixes are added at the beginning of a word.

**Private Datastore** 	personal data storage space that is different from the data of a general nature

**SDS** Separate Data Store. OpenStreetMap is a feature that allows you to separate the data can only be accessed by certain parties (private) from public data. To split the data to the storage space will be different from the general data
