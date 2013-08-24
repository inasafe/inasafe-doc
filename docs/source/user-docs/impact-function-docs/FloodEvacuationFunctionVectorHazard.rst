Flood Evacuation Function Vector Hazard
=======================================

Overview
--------

**Unique Identifier**: 
Flood Evacuation Function Vector Hazard

**Author**: 
AIFDR

**Rating**: 
4

**Title**: 
Need evacuation

**Synopsis**: 
To assess the impacts of (flood or tsunami) inundation in vector format on population.

**Actions**: 
Provide details about how many people would likely need to be evacuated, where they are located and what resources would be required to support them.

**Hazard Input**: 
A hazard vector layer which has attribute affected the value is either 1 or 0

**Exposure Input**: 
An exposure raster layer where each cell represent population count.

**Output**: 
Vector layer contains population affected and the minimum needs based on evacuation percentage.

Details
-------

The population subject to inundation is determined whether in an area which affected or not. You can also set an evacuation percentage to calculate how many percent of the total population affected to be evacuated. This number will be used to estimate needs based on BNPB Perka 7/2008 minimum bantuan.

Docstring
----------

Impact function for vector flood evacuation

    :author AIFDR
    :rating 4

    :param requires category=='hazard' and                     subcategory in ['flood', 'tsunami'] and                     layertype=='vector'

    :param requires category=='exposure' and                     subcategory=='population' and                     layertype=='raster'
    