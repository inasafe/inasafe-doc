.. _faq:

Frequently Asked Questions
==========================
A short list of questions to assist course participants with the common
questions asked by new users when performing a natural disaster scenario
analysis with
QGIS and |project_name|.


1. *What are the important things that need to prepared before running |project_name|?*

   - To run |project_name| you need one hazard dataset and one exposure dataset.
   - The data must have keywords defined (current version) and it must be turned on.
   - There must be an overlap between the hazard and exposure layers.
   - `See more in |project_name| concepts .. <http://inasafe.org/en/training/socialisation/inasafe_concepts.html>`__


2. *Why are there is no active layers available in the |project_name| dock?*

   - Check that your data layers are turned on
   - Check that the layers have keywords defined.
   - If keywords are not defined or are not current, use the keywords wizard.


3. *The data has keywords defined, but it is not showing up in the dock as an option for |project_name| analysis?*

   - Check the keyword version is the same with the |project_name| version.
   - Use the keywords wizard to and update your keywords if necessary.
   - Check that the layer appears in the map and is turned on.


4. *The data has keywords and is showing up in the dock, but there is no option in the "might" list?*

   - The impact function for that data might not be available yet.
   - `See the list of available impact functions in |project_name| concepts .. <http://inasafe.org/en/training/socialisation/inasafe_concepts.html>`__


5. *Can InaSAFE summarise the impact summary results for different areas?*

   - Yes, you can use the aggregation feature in |project_name| to summarise the
     impact summary results for smaller areas such as administration districts.


6. *Why are there no options for population in the keyword for my vector population data?*

   - Make sure that your population data in in raster format
   - The current version of |project_name| only supports raster population data.
   - `See more in |project_name| concepts .. <http://inasafe.org/en/training/socialisation/inasafe_concepts.html>`__


7. *Can |project_name| be used to analyse hazard data besides flood, tsunami, earthquake and volcanic hazard?*

   - Yes it can. |project_name| has a Generic Hazard Impact Function that can
     be used to analyse other hazards as long as the data are classified.
   - Classified data will have values such as Low, Medium and High.


8. *Why is there some data that is not relevant showing on my pdf map when I print?*

   - Before you click the "Print" button, please turn off any layers you do not
     want to see on the map.
   - Rearrange the order of layers to make sure the important things are on top.


9. *Why are the impact results different in different parts of the impact report?*

   - In the general report the results are rounded.
   - In the detailed report the results may not be rounded as much.
   - |project_name| provides an estimate of the impact. Rounded numbers are good estimates.


10. *My hazard and exposure data have different projections, can I still run an |project_name| analysis on these data?*

    - Yes you can, but you need to enable on the fly projection.
    - In QGIS, activate OTF CRS Transformation
       - :menuselection:`Project > Project Properties > CRS`
       - checkbox in the :guilabel:`Enable 'on the fly' CRS transformation`.


11. *My flood polygon hazard data includes a flood depth. Why can't I run an analysis in |project_name| and set the threshold with these data?*

    - At this moment, users can only set a flood depth threshold for raster data.
    - If you would like to build a new impact function to work with different
      types of hazard data, please contact the developer team.

