.. image:: /static/training/intermediate/osm/image6.*

..  _using-private-data-store:

Module 5: Using the Separate Data Store
=======================================

**Learning Objectives**

- Understand the functions of the Separate Data Store (SDS)
- Understand what data should be kept publicly and what should be private
- Install SDS plugin in JOSM
- Use SDS presets
- Use SDS plugin for selecting public and private data
- Access online datastore

OpenStreetMap data is open and available to anyone who would like to access it.
However, there may be times when you want to use OSM to collect data,
but you would like to keep some attributes stored in a private database.
For this purpose, HOT has developed an tool for JOSM known as the
Separate Data Store.
The SDS allows you to create maps and add data into JOSM the same as always,
but when you upload your edits, public data will be saved to the
OpenStreetMap database, and private data will be saved separately to your 
private data server.

.. image:: /static/training/intermediate/osm/image104.*
   :align: center

--------------

*How the SDS Plugin works with JOSM*

Data uploaded to the private HOT Datastore is only accessible to people who
have an account at datastore.hotosm.org.
This chapter is designed for people who already have an account and desire to
store private geospatial information, such as household income,
personal health care data, or the location of gold mines.

..Note:: If you do not have a HOT Datastore account or if you want to set up
         your own private datastore server please contact us
         (team.id[at]hotosm.org).

--------------

1. Installing the SDS plugin
----------------------------

This plug-in allows private data to be diverted into the private data
store, rather than being saved in the OSM database.
A recent version of JOSM is required for the SDS plugin to run.
(If you do not have a recent version of JOSM, download and install it from
http://josm.openstreetmap.de/.).

1. Open the preferences menu in JOSM and go to the plugins tab.

.. image:: /static/training/intermediate/osm/image105.*
   :align: center

2. Click :guilabel:`Download List` to ensure that all available plugins are
   listed.

3. In the search box, type :kbd:`sds`.

.. image:: /static/training/intermediate/osm/image106.*
   :align: center

4. Check the box next to the plugin to activate it. Click :guilabel:`OK`
   to download and install. You will need to restart JOSM.

2. Using the plugin
-------------------

Editing the map works just the same as before.
The only difference is that when you upload changes,
some tags will be automatically saved on the private datastore,
and the rest will be saved directly onto OpenStreetMap.

5. After installing the plugin, the first time you download data you will be
   asked for your HOT datastore username and password.

.. image:: /static/training/intermediate/osm/image108.*
   :align: center

- In order to use the plugin, you need to enter your username and password.
  To save them, check the box next to :guilabel:`Save user and password`.
- The private datastore is now working.
  When you upload changes, the usual tags will be saved to OSM,
  and special private tags will be saved to the datastore.

**3. How It Works**

How does the plugin know which data you want to store on OpenStreetMap and
which data you want to store publicly?
Quite simply, it knows because of the tags.
Normal tags go to OpenStreetMap, as always, but you can use new tags with a
special prefix that will be sent to the private datastore.
By default, any tag that begins with the prefix **“hot:”** will go to the
private datastore.
If you open the Preferences menu you will see a new tab on the bottom for SDS
plugin options:

.. image:: /static/training/intermediate/osm/image109.*
   :align: center

There are some basic settings here.
By default the server URL is set to the HOT datastore, and your username and
password can be saved here as well.
The line labelled **“SDS tag prefix” **contains the prefix that will cause
tags to be saved on the private datastore.
By default it is **“hot:”**

When you create or edit an object on the map, you can apply tags like this:

.. image:: /static/training/intermediate/osm/image110.*
   :align: center

In this case, the first two tags will be saved on OSM.
The third tag, because it has the prefix **hot:** will be saved on the
private datastore.

You will most likely collaborate with others when using the private datastore,
so you will have a standard list of tags to use for the specific data your are
collecting.
These tags can then be made into a presets menu, which will provide an
easy-to-use form for adding both public and private data.

**4. Access the Datastore Online**

Just like `openstreetmap.org <http://openstreetmap.org>`_ , you can access the
online datastore directly, by visiting http://sds.openstreetmap.or.id and
logging in with your username and password.

.. image:: /static/training/intermediate/osm/image111.*
   :align: center

*4.1 Private Data Store Users*

There is 2 types of Data Store users.
They are Admin who can add new projects or users onto SDS and Personal are
regular users who joined on some project that using SDS.

This is the screenshot :

.. image:: /static/training/intermediate/osm/image112.*
   :align: center

*4.2 Figure of Using Private Data Store and JOSM*

.. image:: /static/training/intermediate/osm/image113.*
   :align: center

*4.3 Editing Data Store Online*

You can edit your data in SDS online. These are the steps :

- Open this site http://sds.openstreetmap.or.id
- Username : team.id.personal@hotosm.org   (Personal)
- Password : osmidpersonal
- Click :guilabel:`tag search`

.. image:: /static/training/intermediate/osm/image114.*
   :align: center

- Add 'String' which is a name when we saved the sds tag and click search

.. image:: /static/training/intermediate/osm/image115.*
   :align: center

- You only can edit the objects attribute that has saved in JOSM but if you
  want to delete objects you must to use JOSM.

.. image:: /static/training/intermediate/osm/image116.*
   :align: center

- Click :guilabel:`Save Tags`

*4.4 Add data on Data Store Online*

You can directly add your data on Data Store. These are the steps :

- Click Map Search and Load OSM Geometries

.. image:: /static/training/intermediate/osm/image117.*
   :align: center

.. image:: /static/training/intermediate/osm/image118.*
   :align: center

- After that add/edit information about object that chosen by you

.. image:: /static/training/intermediate/osm/image119.*
   :align: center

- After you finish click Save tags

.. image:: /static/training/intermediate/osm/image120.*
   :align: center

.. image:: /static/training/intermediate/osm/image121.*
   :align: center

*4.5 Add and Edit User on Private Data Store*

- Open this site : http://sds.openstreetmap.or.id
- Username : team.id@hotosm.org  (admin)
- Password : osmidceria
- Click :guilabel:`user administration`

.. image:: /static/training/intermediate/osm/image122.*
   :align: center

- Click :guilabel:`Add New User`

.. image:: /static/training/intermediate/osm/image123.*
   :align: center

.. image:: /static/training/intermediate/osm/image124.*
   :align: center

- Click :guilabel:`Save` if you finished

*Edit Users*

- Click :guilabel:`user administration`

.. image:: /static/training/intermediate/osm/image125.*
   :align: center

- Click "Eye Symbol" in the left box

.. image:: /static/training/intermediate/osm/image126.*

- Click :guilabel:`Edit User`

.. image:: /static/training/intermediate/osm/image127.*
   :align: center

*4.6 Add Project on Private Data Store*

- Click :guilabel:`Project`
- Click :guilabel:`Create New Project`

.. image:: /static/training/intermediate/osm/image128.*
   :align: center

- Next you have to write Tag Fields Definition in JavaScript Object Notation
  (JSON) language.
  You have to translate Extensible Mark-up Language (XML) language at Preset
  that you want to use into JSON language.
- Let's see the difference between XML Preset and JSON

XML

.. image:: /static/training/intermediate/osm/image129.*
   :align: center

JSON

.. image:: /static/training/intermediate/osm/image130.*
   :align: center

1. If your preset use ELEMENT COMBO, MULTISELECT or CHECK KEY it must
   converted with format:

::

 {"type":"select","tag":"YOUR KEY","en":"YOUR COLUMN TABLE NAME","option":["VALUES 1","VALUES 2", "SO ON.."]},

Example (first is XML, second is JSON)

.. image:: /static/training/intermediate/osm/image131.*
   :align: center

2. If your preset use ELEMENT TEXT, it must converted with format:

::

 {"type":"text","tag":"YOUR KEY","en":" YOUR COLUMN TABLE NAME"},

Example (first is XML, second is JSON)

.. image:: /static/training/intermediate/osm/image132.*
   :align: center

- Write your tag definition into JSON language at the available row of Tag
  Field Definition (JSON)

.. image:: /static/training/intermediate/osm/image33.*
   :align: center

- Click :guilabel:`Create Project` if your finish
- You can upload your presets in your project to the row of
  :guilabel:`Preset File`
- If you click :guilabel:`Project` on right corner, you can see your Project.
  Click :guilabel:`View Table` to see the data.
  If there is any ERROR, it possibly there is mistake at your JSON tag
  definition!
  If it doesn't you will see a table like this :

.. image:: /static/training/intermediate/osm/image134.*
   :align: center

- You also can download the table in the CSV format or Excel format.

**5.General Questions**

*How to save our data?*

To save your private data the steps are similar like upload your changes to
OSM.
Remember to always use right prefix (in this case is :hot) with your private
tag to make sure that they will be saved on your private database and would
not be published.

*How much users can use the same account? How if I would like to add users?*

There is no limit for users account. At the moment users access organized by
HOT.

*How much data that I can save in my private server?*

A lot of Data

*Is there any easy way to search certain private data?*

When you login to the datastore.hotosm.org you will have a choice to do some
tag search.
This is possible to you to search certain tag.


:ref:`Go to next module --> <editing-wiki-osm>`