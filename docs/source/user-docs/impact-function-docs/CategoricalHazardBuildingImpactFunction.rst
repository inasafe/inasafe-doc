Categorical Hazard Building Impact Function
===========================================

Overview
--------

**Unique Identifier**: 
Categorical Hazard Building Impact Function

**Author**: 
ESSC

**Rating**: 
3

**Title**: 
Be impacted by each category

**Synopsis**: 
To assess the impacts of categorised hazard in raster format on structure/building raster layer

**Actions**: 
Provide details about how many buildings would likely need to be affected for each category

**Hazard Input**: 
A hazard raster layer where each cell represents the category of the hazard. There should be three categories: 1, 2 and 3

**Exposure Input**: 
Vector polygon layer which can be extracted from OSM where each polygon represents the footprint of a building

**Output**: 
Map of structure exposed to high category and a table with number of structures in each category

Details
-------

This function calculates how many buildings will be affected per each category for all categories in the hazard layer. Currently there should be three categories in the hazard layer. After running it shows the results and the total buildings that will be affected for the given hazard.

Doc String
----------

Impact plugin for categorising hazard impact on building data

    :author ESSC
    :rating 3
    :param requires category=='hazard' and                     unit=='categorised' and                     layertype=='raster'

    :param requires category=='exposure' and                     subcategory=='structure' and                     layertype=='vector'
    