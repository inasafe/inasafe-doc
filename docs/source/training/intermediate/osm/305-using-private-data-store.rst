.. image:: /static/training/intermediate/osm/image6.png


Module 5: Using Private Data Store
==================================

**Learning Objectives**

- Understand the functions of the SDS
- Understand what data should be kept publicly and what needs to be private
- Install SDS plugin in JOSM
- Use SDS presets
- Use SDS plugin for selecting public and private data
- Access online datastore

OpenStreetMap data is open and available to anyone who would like to access it.  However, there may be times when you want to use OpenStreetMap to collect data, but you would like to keep some attributes stored in a private database.  For this, HOT has developed an additional tool for JOSM known as the SDS (Separate Data Store).
The SDS allows you to create maps and add data into JOSM the same as always, but when you upload your edits, public data will be saved to the OpenStreetMap database, and private data will be saved separately to the HOT Datastore.

.. image:: /static/training/intermediate/osm/image104.png
 
*How the SDS Plugin works with JOSM*

Data uploaded to the private HOT Datastore is only accessible to people who have an account at datastore.hotosm.org.  This chapter is designed for people who already have an account and desire to store private geospatial information, such as household income, personal health care data,  or the location of gold mines.  If you do not have a HOT Datastore account or if you want to set up your own private datastore server please contact Kate Chapman (k8chapman[at]gmail.com).

**1. Installing the SDS plugin**

This plug-in allows private data to be streamlined into the private data store.  The newest version of JOSM is required for the SDS plugin to run.  (If you do not have a recent version of JOSM, download and install it from http://josm.openstreetmap.de/.  If you cannot install the latest version, go to the Appendix to see how you can install this plug-in by source).  

- Open the preferences menu in JOSM and go to the plugins tab.

.. image:: /static/training/intermediate/osm/image105.png
 
- Click “Download List” to ensure that all available plugins are listed.
- In the search box, type “sds”.

.. image:: /static/training/intermediate/osm/image106.png 

- Check the box next to the plugin to activate it.  You will need to restart JOSM.
- If JOSM is open, restart it.

**Installing SDS Plugin by Source**

If you are unable to find the “sds” plugin on the Preferences menu, you may need to install it manually as described here:

- Download the sds plugin by going to http://kunden.geofabrik.de/03df698c95134f04949eb67ac7ba2195/ and clicking on *sds.jar*
- Click on the Start Menu and type “%APPDATA%” into the search box.  Click on the folder named “Roaming.”

.. image:: /static/training/intermediate/osm/image107.png 
 
- In the window that opens, double-click on “JOSM” to open the JOSM program files.
- Double-click on the “plugins” folder to open it. Move the *sds.jar* file into this folder.

**2. Using the Plugin**

Editing the map works just the same as before.  The only difference is that when you upload changes, some tags will be automatically saved on the private datastore, and the rest will be saved directly onto OpenStreetMap.

- After installing the plugin, the first time you download data you will be asked for your HOT datastore username and password.

.. image:: /static/training/intermediate/osm/image108.png  

- In order to use the plugin, you need to enter your username and password.  To save them, check the box next to “Save user and password.”
- The private datastore is now working.  When you upload changes, the usual tags will be saved to OSM, and special private tags will be saved to the datastore.

**3. How It Works**

How does the plugin know which data you want to store on OpenStreetMap and which data you want to store publicly?  Quite simply, it knows because of the tags.  Normal tags go to OpenStreetMap, as always, but you can use new tags with a special prefix that will be sent to the private datastore.  By default, any tag that begins with the prefix **“hot:”** will go to the private datastore.  If you open the Preferences menu you will see a new tab on the bottom for SDS plugin options:

.. image:: /static/training/intermediate/osm/image109.png 

 

There are some basic settings here.  By default the server URL is set to the HOT datastore, and your username and password can be saved here as well.  The line labelled **“SDS tag prefix” **contains the prefix that will cause tags to be saved on the private datastore.  By default it is **“hot:”**

When you create or edit an object on the map, you can apply tags like this:

.. image:: /static/training/intermediate/osm/image110.png 
 

In this case, the first two tags will be saved on OSM.  The third tag, because it has the prefix **hot:** will be saved on the private datastore.

You will most likely collaborate with others when using the private datastore, so you will have a standard list of tags to use for the specific data your are collecting.  These tags can then be made into a presets menu, which will provide an easy-to-use form for adding both public and private data.

**4. Access the Datastore Online**

Just like `openstreetmap.org <http://openstreetmap.org>`_ , you can access the online datastore directly, by visiting http://sds.openstreetmap.or.id and logging in with your username and password.  

.. image:: /static/training/intermediate/osm/image111.png 
 
 
*4.1 Private Data Store Users*
There is 2 types of Data Store users. They are Admin who can add new projects or users onto SDS and Personal are regular users who joined on some project that using SDS. This is the screenshoot :

.. image:: /static/training/intermediate/osm/image112.png 
 
 
*4.2 Figure of Using Private Data Store and JOSM*

.. image:: /static/training/intermediate/osm/image113.png 
 
 
*4.3 Editing Data Store Online*

You can edit your data in SDS online. These are the steps :

- Open this site hhttp://sds.openstreetmap.or.id
- Username : team.id.personal@hotosm.org   (Personal)
- Password : osmidpersonal
- Clik tag search

.. image:: /static/training/intermediate/osm/image114.png 
 
- Add 'String' which is a name when we saved the sds tag and click search

.. image:: /static/training/intermediate/osm/image115.png 
 
- You only can edit the objects attribute that has saved in JOSM but if you want to delete objects you must to use JOSM.
 
.. image:: /static/training/intermediate/osm/image116.png 
 
- Click Save Tags

*4.4 Add data on Data Store Online*

You can directly add your data on Data Store. These are the steps :

- Click Map Search and Load OSM Geometries

.. image:: /static/training/intermediate/osm/image117.png 

.. image:: /static/training/intermediate/osm/image118.png 
 
- After that add/edit information about object that chosen by you

.. image:: /static/training/intermediate/osm/image119.png 
 
- After you finish click Save tags

.. image:: /static/training/intermediate/osm/image120.png 

.. image:: /static/training/intermediate/osm/image121.png 
 

*4.5 Add and Edit User on Private Data Store*
	
- Open this site : http://sds.openstreetmap.or.id
- Username : team.id@hotosm.org  (admin)
- Password : osmidceria
- Click user administration

.. image:: /static/training/intermediate/osm/image122.png 
 
- Click Add New User

.. image:: /static/training/intermediate/osm/image123.png 

.. image:: /static/training/intermediate/osm/image124.png 
 
- Click Save if you finished


*Edit Users*

- Click user administration

.. image:: /static/training/intermediate/osm/image125.png
 
- Click "Eye Symbol" in the left box

.. image:: /static/training/intermediate/osm/image126.png
 
- Click Edit User

.. image:: /static/training/intermediate/osm/image127.png 

*4.6 Add Project on Private Data Store*

- Click Project
- Click Create New Project

.. image:: /static/training/intermediate/osm/image128.png 
 
- Next you have to write Tag Fields Definition in JavaScript Object Notatioan (JSON) language. You have to translate Extensible Mark-up Language (XML) language at Preset that you want to use into JSON language.
- Let's see the difference between XML Preset and JSON

XML

.. image:: /static/training/intermediate/osm/image129.png 
       
JSON

.. image:: /static/training/intermediate/osm/image130.png 
 
NOTE:

1. If your preset use ELEMENT COMBO, MULTISELECT or CHECK KEY it must converted with format
{"type":"select","tag":"YOUR KEY","en":"YOUR COLOUMN TABLE NAME","option":["VALUES 1","VALUES 2", "DST.."]},

Example (first is XML, second is JSON)

.. image:: /static/training/intermediate/osm/image131.png 
 

2. If your preset use ELEMENT TEXT, it must converted with format

{"type":"text","tag":"YOUR KEY","en":" YOUR COLUMN TABLE NAME"},

Example (first is XML, second is JSON)

.. image:: /static/training/intermediate/osm/image132.png 
 
- Write your tag definition into JSON language at the available row of Tag Field Definition (JSON)

.. image:: /static/training/intermediate/osm/image33.png 
 
- Click Create Project if your finish
- You can upload your presets in your project to the row of Preset File
- If you click Project on right corner, you can see your Project. Click **View Table**  to see the data. If there is any ERROR, it possibly there is mistake at your JSON tag definition! If it doesn't you will see a table like this :

.. image:: /static/training/intermediate/osm/image134.png 

- You also can download the table in the CSV format or Excel format.

**5.General Questions**

*How to save our data?*

To save your private data the steps are similar like upload your changes to OSM. Remember to always use right prefix (in this case is :hot) with your private tag to make sure that they will be saved on your private database and would not be published.

*How much users can use the same account? How if I would like to add users?*

There is no limit for users account. At the moment users access organized by HOT

*How much data that I can save in my private server?*

A lot of Data

*Is there any easy way to search certain private data?*

When you login to the datastore.hotosm.org you will have a choice to do some tag search. This is possible to you to search certain tag.

