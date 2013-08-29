Categorised Hazard Population Impact Function
=============================================

Overview
--------

**Unique Identifier**: 
Categorised Hazard Population Impact Function

**Author**: 
AIFDR

**Rating**: 
2

**Title**: 
Be impacted

**Synopsis**: 
To assess the impacts of categorized hazards in raster format on population raster layer.

**Actions**: 
Provide details about how many people would likely need to be impacted for each category.

**Hazard Input**: 
A hazard raster layer where each cell represents the category of the hazard. There should be 3 categories: 1, 2, and 3.

**Exposure Input**: 
An exposure raster layer where each cell represent population count.

**Output**: 
Map of population exposed to high category and a table with number of people in each category

**Limitation**: 
The number of categories is three.

Details
-------

This function will calculate how many people will be impacted per each category for all categories in the hazard layer. Currently there should be 3 categories in the hazard layer. After that it will show the result and the total amount of people that will be impacted for the hazard given.

Docstring
----------

Plugin for impact of population as derived by categorised hazard

    :author AIFDR
    :rating 2
    :param requires category=='hazard' and                     unit=='normalised' and                     layertype=='raster'

    :param requires category=='exposure' and                     subcategory=='population' and                     layertype=='raster'
    