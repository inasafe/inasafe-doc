.. image:: /static/training/intermediate/osm/image6.*


Module 3: Dealing With Conflicts
================================

**Learning Objectives**

- Identify Conflicts
- Understand Why Conflicts Happen
- Solve Conflicts

**Introduction**

Sometimes you are working in JOSM and when you upload all of your beautiful edits you get a nasty message complaining about a conflict.

.. image:: /static/training/intermediate/osm/image75.*
 

What happened is that you downloaded a bunch of data, which included a point which we will call Node A.  Then while you were editing, somebody else also downloaded Node A, changed it, and saved the changes back on OpenStreetMap.  Now when you try to upload your version of Node A, it is different from the one saved on OSM.  Therefore JOSM doesn’t know which version of Node A should be saved.

**1. Conflicts**
Sometimes, JOSM is able to figure out what to do with conflicts on its own, and it will give you a message like this:
 
.. image:: /static/training/intermediate/osm/image76.*

This means that JOSM has automatically decided that items in your local dataset will not be uploaded to main server because they have already been deleted by another user.  

In some conflicts, however, there is no easy action for JOSM to take and so it leaves the decision up to the user to determine what the best course of action is.  This means it is up to you to resolve the conflicts.

.. image:: /static/training/intermediate/osm/image77.*

*This tells you to look at all of your conflicts in Layer 1 in the Dialog List box.* 


.. image:: /static/training/intermediate/osm/image78.*

*This window provides you with a warning as to whether you are likely to experience a conflict with your edits.  If you check on the server you will be able to fix the editing issues that would arise.*

.. image:: /static/training/intermediate/osm/image79.*
 
*This warning tells you that JOSM failed to delete a node due to it still being referenced in a way.  In order to remedy this, the user has to go back into JOSM and resolve the conflict before uploading the data.* 

**2. Conflict Resolution**

The process of resolving a conflict is quite simple, although it can appear quite confusing at first in JOSM.  Basically, for every conflict JOSM will present you with two choices - your version of an object and the one that is on the server.  You need to choose whether to keep your version, or whether the new version on the server should remain.

You might think, “of course my version is going to be better!”  And maybe you’re right.  But think back to our example at the start of this chapter.  Perhaps while you were busy editing, another mapper added a lot of information to one of the nodes in your data set.  If you choose your version over their version, you will lose all of that valuable information that they added.  Hence you should consider keeping their version, or merging it with your own.

- When you get a conflict window pop-up, it is best to choose the button “Synchronize ... only.”  You may need to do this for more than one object, but it is best to resolve conflicts one at a time. 

.. image:: /static/training/intermediate/osm/image80.*

- Once you click this button, you will get a pop-up window that details your conflict.  The error message may look complicated, but it is rather simple.  You will know what type of conflict you have by the symbol  

.. image:: /static/training/intermediate/osm/image81.* 

in the top tab.  The conflict in this example refers to the properties, such as the location and existence of the object.  This is why the coordinates and deleted state are listed.  

Types of Conflict:

- Properties:  Object has been moved (coordinates) or deleted
- Tags:  Tags do not match
- Nodes:  There is a differences in the list of nodes in two ways  
- Members:  There is a difference in the list of members in a relation

.. image:: /static/training/intermediate/osm/image82.* 

Conflicts only appear with two different edits at a time.  If there are three or more conflicts, then a chain of conflicts will pop-up.  Therefore you have to choose or merge with only two conflicts at a time.  You can choose your version, the other version or, at times, merge the two.  

- In this example you do not have the option of merging.    Click on the first column, or My version if you believe that your edits are correct.  Click on Their version if you think that the other edits are better.  

.. image:: /static/training/intermediate/osm/image83.*
 

- Once you have selected which version you think is best, then click “Apply Resolution.”  A few more windows will pop up and you will be on your way toward being able to upload your edits.  
- Do some more editing.  Then click ‘Upload’.  You will get a pop-up that says:

.. image:: /static/training/intermediate/osm/image84.*
 
- On your Windows menu you have a Conflict List Dialog  
  
.. image:: /static/training/intermediate/osm/image85.*
 
This window displays a list of conflicts.  The total number of unresolved conflicts is shown in the header. You can select or resolve a conflict by clicking on it.  This is useful when you have many conflicts to deal with. 

.. image:: /static/training/intermediate/osm/image86.*
  
- You cannot upload your changes until this list is empty.  

**3. Ways to Avoid Conflicts**

**Upload Frequently**

To minimize the chance and number of conflicts it is important to upload your edits regularly.  Conflicts appear more frequently for those who tend to save the area they are working on in their local server and wait a while to upload it.  It is best to download the area you are working on, edit it and then immediately upload it.  The longer the time between downloading data and uploading changes to that data, the more likely it is that someone has edited something in the meantime.

**Edit in the Area You Download**

Editing in the specific area you have downloaded minimizes conflict risk.  Make sure you do not edit outside of the area that you have downloaded.  You can easily see which areas outside your download area in JOSM, because the background is made up of diagonal lines instead of being solid black.

.. image:: /static/training/intermediate/osm/image87.*
 