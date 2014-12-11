Volcano Building Impact
=======================

Overview
--------

**Unique Identifier**: 
Volcano Building Impact

**Author**: 
AIFDR

**Rating**: 
4

**Title**: 
Be affected

**Synopsis**: 
To assess the impacts of volcano eruption on buildings

**Actions**: 
Provide details about how many buildings would likely be affected within each hazard zones

**Hazard Input**: 
A hazard vector layer can be polygon or point. If polygon, it must have "KRB" attribute and the values for it are "Kawasan Rawan Bencana I", "Kawasan Rawan Bencana II", or "Kawasan Rawan Bencana III." If you want to see the name of the volcano in the result, you must add the "NAME" attribute for point data or "GUNUNG" attribute for polygon data.

**Exposure Input**: 
Vector polygon layer extracted from OSM where each polygon represents the footprint of a building

**Output**: 
Vector layer containing buildings exposed to volcanic hazard zones for each Kawasan Rawan Bencana or radius

Details
-------

No documentation found

Doc String
----------

Risk plugin for volcano building impact

    :author AIFDR
    :rating 4
    :param requires category=='hazard' and                     subcategory in ['volcano'] and                     layertype=='vector'

    :param requires category=='exposure' and                     subcategory=='structure' and                     layertype=='vector'
    