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
To assess the impacts of categorized hazard in raster format on structure/building raster layer.

**Actions**: 
Provide details about how many building would likely need to be affected for each category.

**Hazard Input**: 
A hazard raster layer where each cell represents the category of the hazard. There should be 3 categories: 1, 2, and 3.

**Exposure Input**: 
Vector polygon layer which can be extracted from OSM where each polygon represents the footprint of a building.

**Output**: 
Map of structure exposed to high category and a table with number of structure in each category

Details
-------

This function will calculate how many buildings will be affected per each category for all categories in the hazard layer. Currently there should be 3 categories in the hazard layer. After that it will show the result and the total of buildings that will be affected for the hazard given.

Doc String
----------

Impact plugin for categorising hazard impact on building data

    :author ESSC
    :rating 3
    :param requires category=='hazard' and                     unit=='categorised' and                     layertype=='raster'

    :param requires category=='exposure' and                     subcategory=='structure' and                     layertype=='vector'
    