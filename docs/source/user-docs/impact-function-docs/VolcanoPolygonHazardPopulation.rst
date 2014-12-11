Volcano Polygon Hazard Population
=================================

Overview
--------

**Unique Identifier**: 
Volcano Polygon Hazard Population

**Author**: 
AIFDR

**Rating**: 
4

**Title**: 
Need evacuation

**Synopsis**: 
To assess the impacts of volcano eruption on population

**Actions**: 
Provide details about the population likely affected by each hazard zone

**Hazard Input**: 
A hazard vector layer can be polygon or point. If polygon, it must have "KRB" attribute and the valuefor it are "Kawasan Rawan Bencana I", "Kawasan Rawan Bencana II", or "Kawasan Rawan Bencana III." If you want to see the name of the volcano in the result, you must add the "NAME" attribute for point data or "GUNUNG" attribute for polygon data.

**Exposure Input**: 
An exposure raster layer where each cell represents population count

**Output**: 
Vector layer contains people affected and the minimum needs based on the number of people affected.

Details
-------

No documentation found

Doc String
----------

Impact function for volcano hazard zones impact on population

    :author AIFDR
    :rating 4
    :param requires category=='hazard' and                     subcategory in ['volcano'] and                     layertype=='vector'

    :param requires category=='exposure' and                     subcategory=='population' and                     layertype=='raster'
    