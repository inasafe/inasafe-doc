.. image:: /static/training/beginner/osm/image67.*


Module 5: Field Papers
======================

**Learning Objectives**

- How to use Field Papers
- Make and print  Field Papers
- Add data to print using Field Papers
- Scan and upload Field Papers to Field Papers website
- Open Field Papers into JOSM

In this module we will see how we can record the coordinates of places
without a GPS.  We will use a tool called Field Papers,
which allows you to print a map of an area, draw on it and add notes,
and load the paper back into JOSM, where you can add your locations to
OpenStreetMap.

**1. Overview of Field Papers**

Before going into detail about Field Papers, let’s look at an overview of
how the process works:

**Step 1:**  Locate the area you want to map on the Field Papers website.
Print out a map of this area. You can choose to print the current map of
the area with OpenStreetMap, or you can choose to print aerial imagery,
if it is available in your area.

**Step 2:**  Use your printed map to survey the area. Add more places by
drawing them on the map. Draw lines for roads, shapes for buildings,
and so forth. Write notes about each location directly on the map,
or write numbers on the map that relate to numbers in your notebook,
where you can write more detailed information about each object.

.. image:: /static/training/beginner/osm/image68.*

**Step 3:**  Scan your paper into the computer.  If you do not have a
scanner, you can take a photograph of the paper, if your camera is able to
take high quality pictures.  Upload the image to the Field Papers website
(`http://fieldpapers.org/upload.php <http://fieldpapers.org/upload.php>`_
).

**Step 4:** In JOSM, load the Field Papers.  Use the objects you drew as a
reference to add them digitally into OpenStreetMap.

.. image:: /static/training/beginner/osm/image69.*


**2. How does Field Papers work?**

If you follow the Field Papers process described above,
you will be collecting accurate geographic coordinates of places with
nothing more than paper. How is this possible?

.. image:: /static/training/beginner/osm/image70.*

When you print a Field Papers, the paper comes with a square barcode on the
bottom of the page. This bar code allows Field Papers to determine the
exact location of the map that you are using to survey.  Later,
when you load the paper back into JOSM, all the objects that you drew will
be in shown in their actual locations, or at least quite close,
which is good enough for us.

Now let’s learn how to create and use Field Papers.

**3. Create and Print**

- Open your web browser - this may be Firefox, Chrome, Opera,
  or Internet Explorer.
- In the address bar at the top of the window, enter the following text and
  press Enter: `http://fieldpapers.org/ <http://fieldpapers.org>`_
- The website should look something like this:

.. image:: /static/training/beginner/osm/image71.*

- Click on “Make yourself an Atlas.”
- Enter a place where you would like to print out a map,
  and press Enter.  Here we will search for “jakarta.”

.. image:: /static/training/beginner/osm/image72.*

- Now you are presented with an interface where you can define the
  boundaries of your Field Papers.  The map that you see shows the area that
  you would like to print on paper.  You can print multiple pages,
  zoom in and out, and drag the papers to cover specific boundaries on the
  map.

.. image:: /static/training/beginner/osm/image73.*

- Click on the various buttons to see what each does.  Note that in our
  example, we are presented with a two page set of Field Papers.  To add or
  subtract a page, we can click on the + and - buttons on the map.

.. image:: /static/training/beginner/osm/image74.*

- We can expand or decrease the area of the papers by dragging the button in
  the lower right corner.

.. image:: /static/training/beginner/osm/image75.*

- You can move the paper by clicking and dragging the button in the upper
  left corner.

.. image:: /static/training/beginner/osm/image76.*

- You can adjust the paper orientation and type of map using the controls at
  the top

.. image:: /static/training/beginner/osm/image77.*


- When you’re finished, click “Next.”
- Next give your map a name, and if you want, you can add notes to be
  printed on the map, such as questions you want to remember to answer or
  specific places you want to identify.  After you fill out the form,
  click “Next.”
- Finally choose your layout.  You can indicate whether you want pages only
  for your maps, or if you want notes on the same page.  If you choose the
  notes option, then half of your page will be left for taking notes,
  and the other half will contain your map.

.. image:: /static/training/beginner/osm/image78.*

- It may take a few minutes to prepare your Field Papers.

.. image:: /static/training/beginner/osm/image79.*

- When your print is ready, scroll to the bottom and click “Download PDF.”
  The Field Papers should begin downloading.   If it loads in your browser,
  you may need to save it by going to File -> Save.
- When the download is finished, open the PDF file.  Connect your computer
  to a printer and print the page.  If everything goes well,
  you should now have your map printed on paper.

**4. Map with Field Papers**

- Take your Field Papers outside, and use it as a guide to walk and identify
  new places that are not on the map.
- Draw lines for roads, shapes for buildings, and so forth.  Write notes
  about each location directly on the map, or write numbers on the map that
  relate to numbers in your notebook, where you can write more detailed
  information about each object.
- When you are satisfied with your additions on the paper map,
  then you can add them digitally into OpenStreetMap.

**5. Scan and Upload**

- Field Papers are very useful for mapping with nothing more than paper,
  but they are not 100% magic.  We will still need to add our paper into JOSM,
  add our information digitally, and save our changes on OpenStreetMap.
- The first step is to scan your Field Papers into your computer.  You can
  do this by attaching a scanner to your computer, scanning the paper,
  and saving it as an image file.  If you don’t have a scanner,
  you can take a photography of the paper, but you should be carefully to
  take a very good photo.  Make sure that the paper is flat and your camera
  is directly in front of it.  Be sure to include the barcode in the image,
  as Field Papers will not work without it.  Here is an example of a
  scanned/photographed image:

.. image:: /static/training/beginner/osm/image68.*

- Once you have your Field Papers scanned and saved on the computer,
  open your web browser and return to
  `Field Papers website <http://fieldpapers.org/>`_ just as before.
- Click on the “Upload” tab at the top of the page.

 .. image:: /static/training/beginner/osm/image80.*

- Click “Choose File” and navigate to the file where you
  scanned/photographed your Field Papers.
- Click “Upload.”  It may take a few minutes for your paper to upload,
  depending on the speed of your internet connection.

.. image:: /static/training/beginner/osm/image81.*

- You’ll be able to add additional notes to your Field Papers,
  but we will skip this for now.  Click on “Finished.”

.. image:: /static/training/beginner/osm/image82.*

**6. Open in JOSM**

- When your scan have been processed, now you can add the results of your
  scan in JOSM and add your information to OpenStreetMap. To display Field
  Papers scan result in JOSM, you can use the fieldpapers plugin.
- Open JOSM and Click Edit - Preference
- Chose Plugin box

.. image:: /static/training/beginner/osm/image83.*

and type ‘fieldpapers’ on the “Search” box. After it was found,
put checks on the fieldpapers box - Click OK - then Restart your JOSM.

.. image:: /static/training/beginner/osm/image84.*

- Open your browser and open Field Papers website: http://fieldpapers.org

- Click Watch Menu - move your mouse to the bottom and click Snapshots until
  your browser page looks like this:

.. image:: /static/training/beginner/osm/image85.*

- Then select Field Papers according with the scans results that have been
  uploaded.
- If you've found an image that correspond to the scan results,
  click on the image until the url appear as shown below,
  copy the URL for example
  *http://fieldpapers.org/snapshot.php?id=67v87z5n#18/-5.15534/119.43913*
  and paste on Field Papers menu in JOSM.

.. image:: /static/training/beginner/osm/image86.*

- Open your JOSM and make sure there are Field Papers menu on the top of
  toolbar.
- Click Field Papers Menu - Click on the Scanned Map then paste the URL that
  we have copy of Field Papers site by pressing Ctrl + V on your keyboard.
- Click OK.

.. image:: /static/training/beginner/osm/image87.*

- Please wait a moments until Field Papers map appears on your JOSM layer.

.. image:: /static/training/beginner/osm/image88.*

- Currently you have Field Papers layers that can be used as a reference to
  add OSM data according to field result (survey) that has been done. It is
  important to remember to edit the data we need to download OSM data first
  by clicking File - Download from OSM. You don’t have to re-draw the box to
  download because JOSM been reading your region according to the Field
  Papers layer automatically. Then Click “Download” to download that area.

.. image:: /static/training/beginner/osm/image89.*

- Wait until the download is complete and the layer that contains OSM data
  appear as shown below.
- You can edit the OSM data according to the field results (survey).
- After editing all area are finished, don’t forget to upload the OSM data
  by clicking File and select Upload Data.

.. image:: /static/training/beginner/osm/image90.*

- Now you have finished adding OSM data according to field result (survey)
  that has been done.
