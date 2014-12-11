Categorical Hazard Population Impact Function
=============================================

Overview
--------

**Unique Identifier**: 
Categorical Hazard Population Impact Function

**Author**: 
ESSC

**Rating**: 
3

**Title**: 
Be affected by each hazard category

**Synopsis**: 
To assess the impacts of categorised hazards in raster format on population raster layer

**Actions**: 
Provide details about how many people would likely need to be impacted for each category

**Hazard Input**: 
A hazard raster layer where each cell represents the category of the hazard. There should be three categories: 1, 2 and 3

**Exposure Input**: 
An exposure raster layer where each cell represents population count

**Output**: 
Map of population exposed to high category and a table with number of people in each category

**Limitation**: 
The number of categories is three

Details
-------

This function calculates how many people will be impacted per each category for all categories in the hazard layer. Currently there should be three categories in the hazard layer. After that it will show the result and the total amount of people that will be impacted for the hazard given.

Doc String
----------

Plugin for impact of population as derived by categorised hazard

    :author ESSC
    :rating 3
    :param requires category=='hazard' and                     unit=='categorised' and                     layertype=='raster'

    :param requires category=='exposure' and                     subcategory=='population' and                     layertype=='raster'
    