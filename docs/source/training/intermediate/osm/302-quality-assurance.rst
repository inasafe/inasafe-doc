.. image:: /static/training/intermediate/osm/image6.*


Module 2: Quality Assurance
===========================

**Learning Objectives**

- Use validation tools in JOSM
- Use online validation tools

Contributing to OpenStreetMap is easy to learn, but difficult to master.
Everybody makes mistakes, but the system works because even when one person does
something the “wrong” way, there are always other mappers ready to help and fix
errors.  As you map more and more, it will continue to get easier, and you will
learn the “proper” way to do things.  In this chapter we will take a look at the
JOSM validation tool, which is an automated tool to search for errors and
warnings in your data.  We will also take a look at one of the online validation
tools, which can aid us further in identifying mistakes on OpenStreetMap.

**1. Errors and Warnings**

Sometimes when you go to upload your edits you get a pop-up window like this:

.. image:: /static/training/intermediate/osm/image55.*
   :align: center

This is JOSM’s way of telling you that there is suspicious data and that you
might want to review the errors and warnings before uploading to OSM.

JOSM comes with a tool that does an automated analysis of possible mistakes.
This is useful for finding errors that you may have overlooked. When you run the
validation tool, it will return two lists of problems:

- **Errors:**  These are important to fix, and therefore usually you should not
  ignore these. Examples of errors include duplicated objects or overlapping
  lines and polygons.
- **Warnings:**  These are problems that are important to fix, but in some cases,
  they are tolerable.

One thing to note is that if you download a large area of the map and run the
validation tool, you may get a very long list of errors and warnings.  This is
because the validation tool works on the whole map-- not only the changes that
you have made.  So you may see mistakes that other mappers have made, and you
can fix them, or ignore them.  But the validation tool gives you the opportunity
to look at the mistakes one by one.

**2. Using the Validation Tool**

Let’s see how to use the validation tool:

- In JOSM, download a section of the map. If you don’t see the 
  :guilabel:`Validation Results` window in the right panel, click on the blue 
  checkmark on the left to show it.

.. image:: /static/training/intermediate/osm/image56.* 
   :align: center

- Ensure that nothing on the map is selected.  If you run the validation tool
  with anything selected, it will only validate what you have selected, and not
  the whole map. Hover your mouse in the validation window and click
  :guilabel:`Validation`

.. image:: /static/training/intermediate/osm/image57.*
   :align: center
 
- The map will change and any warnings will be circled in yellow, errors in red.
  In the :guilabel:`Validation Results` window you will see a list of warnings 
  and errors, if there are any.
 	
.. image:: /static/training/intermediate/osm/image58.*
   :align: center

- Errors should almost always be fixed.  You can zoom to an error, by right
  clicking on it in the window and selecting :guilabel:`Zoom to Problem`. Then 
  you can fix the mistake manually. Some errors can be automatically fixed, 
  such as "Duplicated nodes” errors.  You can click on the folder for these 
  types of errors and click the :guilabel:`Fix` button in the window. Many 
  errors, however, need to be corrected manually.

.. image:: /static/training/intermediate/osm/image59.*
   :align: center
 
- Usually there are many more warnings than errors.  By giving you a warning,
  JOSM is telling you that it is probably a mistake, but not always.  So you
  will need to use your judgement to see if it is an error or not.

- If you select a warning from the list and decide that it is not a problem,
  click :guilabel:`Ignore` and it will be removed from the list. 
- You can re-run the validation tool at any time by clicking 
  :guilabel:`Validation`

**3. Using The Tasking Manager**

HOT Tasking Manager, a tool that mappers can use to sort an area into a grid,
and work together to map an area in an organized way. Aside from being more
organized, the tasking manager is also one way to avoid conflicts, because it is
impossible for more than one person editing the same area.

One consistent challenge is coordinating field and/or remote workers to map an
area together.  To help address this, HOT has developed an OpenStreetMap Tasking
Tool to make it easier for administrators to define the areas of mapping
interest and to delegate workers.  The idea behind this tool is that if there is
an area, let’s say a city, that we want to map, and we have some people mapping
on the ground, and some people mapping remotely using satellite imagery, this
tool will allow us to create a grid of the entire area.  Collaborators can
select blocks in the grid that they plan to map, and when they finish, they can
mark that area as complete.  In this way a team of many people can coordinate to
map the entire grid.

To see how the tasking manager works, let’s take a closer look.

- Open your Internet browser and go to tasks.hotosm.org. You will see a page
  like this:

.. image:: /static/training/intermediate/osm/image60.*
   :align: center
 
- Click :guilabel:`Log in using your OpenStreetMap account` Here you are
  agreeing to allow this application some access to your OpenStreetMap account.
  Click :guilabel:`Save Changes`.

.. image:: /static/training/intermediate/osm/image61.*
   :align: center
  
- Now you will see the current list of projects.  These are different places
  that people are coordinating to map.

.. image:: /static/training/intermediate/osm/image62.*
   :align: center
 
- Click on one of the projects to see more information about it.

.. image:: /static/training/intermediate/osm/image63.*
   :align: center
 
- This page shows you everything you need to know about the project.  On the
  left side of the page is a description of the mapping project and how it is
  being organized.  You can click on the different tabs to get more information.
  On the right side is a grid showing the area to be mapped.  Red grid squares
  have been completed, green squares have been completed and checked by another
  person, and the remaining squares still need to be mapped or are being worked
  on.  By clicking on the “Workflow” tab, you can get information about how
  collaborators are meant to help map.  By clicking on :guilabel:`Task` you can
  take a grid square to work on yourself.

.. image:: /static/training/intermediate/osm/image64.*
   :align: center

- Here you see a view of the square that you have offered to map.  You can
  automatically open the area up for editing with JOSM, Potlatch 2, or create a
  Walking Paper. If you plan to edit with JOSM, you need to enable a JOSM plugin
  before you will be able to launch the application from the Tasking Manager.
  To do this, open JOSM and go the :menuselection:`Preferences` menu. Click on 
  the  :guilabel:`Remote Settings` tab and check the box next to
  :guilabel:`Enable remote control`.  Restart JOSM.

.. image:: /static/training/intermediate/osm/image65.*
   :align: center
           
- Go back to the Tasking Manager and choose JOSM.  If you have JOSM open and you
  correctly enabled the remote control, the grid area of the map you selected 
  will automatically be loaded into JOSM.
- You may now edit the area using the instructions provided in the project 
  information.  When you are finished, you can return to the tasking manager 
  website and add comments about your changes. Click :guilabel:`Mark task as done`
  to let other collaborators know that you have finished this grid square. 
  If you were unable to complete the task, click :guilabel:`Unlock it` to make 
  it available again for other mappers.

.. image:: /static/training/intermediate/osm/image66.*
   :align: center
 
- If you are wondering what happens when you finish an area, the grid square
  will turn red on the map to indicate that is done.  Someone else will then
  look at your work to make sure it is good, and if they agree that you’ve
  completed the square well, the grid square will turn green, meaning it is
  complete!


**4. Editing Tips**

**Ways that are not closed**: usually a line that does not form a polygon.  
Common examples are buildings where the first node does not meet the last node.

.. image:: /static/training/intermediate/osm/image67.*
   :align: center
 
To fix this, select both nodes and go to :menuselection:`Tools ‣ Merge Nodes` 
to connect them.

**Crossing Buildings (Overlapping Buildings)**: buildings that overlap each other.
 
.. image:: /static/training/intermediate/osm/image68.*
   :align: center

To fix this, move the nodes of one of the buildings outside of the other building.

**Untagged Nodes or Ways**: If someone draws a point or a line but forgets to 
give it any tags, then it is useless, because it doesn’t mean anything.

.. image:: /static/training/intermediate/osm/image69.*
   :align: center
 
To fix this, apply tags to the object to identify it, or delete it if it is a 
mistake.

**End node near another way**: If a line ends very close to another line but 
does not connect, this raises a warning.  Many times this warning is not 
important, but it helps to find road intersections that are supposed to connect 
but do not.

.. image:: /static/training/intermediate/osm/image70.*
   :align: center
 
**Crossing ways**: Lines that cross other lines without being connected will 
raise warnings.  Many times this is not a problem, because the crossing ways 
are intentional - such as in the case of bridges, or streets and rivers that 
cross landuse polygons.  It is sometimes helpful, however to find errors.

.. image:: /static/training/intermediate/osm/image71.*
   :align: center
 
OpenStreetMap depends on people correcting and editing mistakes.  Editing and 
validating data is important for improving maps.  If you do not have time to get 
in the field with a GPS or trace imagery, validating objects and attribute data 
is a good way to contribute.

**5. Presets Standardization**

OpenStreetMap allows the users to give as much informations as they can to their
map. These informations can be attached to every objects that they mapped using 
presets menu that is available in OSM editor. Many times we found inconsistency 
in some objects information. That’s why we should make a presets standardisation. 

The presets standardization purposes are:

1. Assuring data consistency and stability
2. Easier data search and analysis
3. As a standard in giving information using presets
4. As a benchmark if we want to make improvements or data validation
5. Maximizing the use of Internal Presets that are available in JOSM
6. Maximizing data visualisation on OpenStreetMap website 

With this preset standardisation, hopefully all OSM users are willing to use 
this preset when they edit their maps. One of the benefit if we use the internal 
preset that is available in JOSM is the visualisation will show up on 
OpenStreetMap website. You can find the list of these standard presets **here** 

**6. KeepRight**

- The Keep Right website is another useful validation tool for OpenStreetMap.  
  Open your web browser and head to http://keepright.at.
- You can switch the site into Indonesian by choosing :guilabel:`id` from the 
  dropdown box in the in the upper right.

.. image:: /static/training/intermediate/osm/image72.*
   :align: center
 
- Click on “Pengecekan data untuk Asia” to check the OSM data in Asia.  This 
  will open up a slippy map with errors displayed on it.  You can navigate to 
  your area of interest by using the zoom and pan functions.

.. image:: /static/training/intermediate/osm/image73.*
   :align: center

- The types of errors are listed on the left of the map.  You can get more 
  details about each error by clicking on the icons which hover above the map.

.. image:: /static/training/intermediate/osm/image74.*
   :align: center
 
- In order to fix one of the errors, you can click on the links to edit in 
  either JOSM or Potlatch.  Note that to edit in JOSM you must have the 
  JOSM Remote Control enabled.

The Keep Right website is a great way to keep an eye on your area of interest 
and fix and errors that may exist in the OSM data.
 