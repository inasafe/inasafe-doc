from safe.impact_functions.core import (FunctionProvider,
                                        get_hazard_layer,
                                        get_exposure_layer,
                                        get_question)
from safe.storage.vector import Vector
from safe.common.tables import Table, TableRow
from safe.engine.interpolation import assign_hazard_values_to_exposure_data
from third_party.odict import OrderedDict


class EarthquakeBuildingImpactFunction1(FunctionProvider):
    """Earthquake impact on building data (tutorial)

    :param requires category=='hazard' and \
                    subcategory=='earthquake' and \
                    layertype=='raster'

    :param requires category=='exposure' and \
                    subcategory=='structure' and \
                    layertype=='vector'
    """

    target_field = 'Shake_cls'
    statistics_type = 'class_count'
    statistics_classes = [0, 1, 2, 3]
    title = 'Be affected'

    def run(self, layers):
        """Earthquake impact to buildings (e.g. from Open Street Map)
        """

        # Thresholds for mmi breakdown
        t0 = 6
        t1 = 7
        t2 = 8

        class_1 = 'Low'
        class_2 = 'Medium'
        class_3 = 'High'

        # Extract data
        H = get_hazard_layer(layers)    # Depth
        E = get_exposure_layer(layers)  # Building locations

        question = get_question(H.get_name(),
                                E.get_name(),
                                self)

        # Define attribute name for hazard levels
        hazard_attribute = 'mmi'

        # Interpolate hazard level to building locations
        I = assign_hazard_values_to_exposure_data(H, E,
                                             attribute_name=hazard_attribute)

        # Extract relevant exposure data
        #attribute_names = I.get_attribute_names()
        attributes = I.get_data()

        N = len(I)

        # Calculate building impact
        lo = 0
        me = 0
        hi = 0
        building_values = {}
        contents_values = {}
        for key in range(4):
            building_values[key] = 0
            contents_values[key] = 0

        for i in range(N):
            # Classify building according to shake level

            x = float(attributes[i][hazard_attribute])  # Interpolated MMI val
            if t0 <= x < t1:
                lo += 1
                cls = 1
            elif t1 <= x < t2:
                me += 1
                cls = 2
            elif t2 <= x:
                hi += 1
                cls = 3
            else:
                # Buildings not reported for MMI levels < t0
                cls = 0

            attributes[i][self.target_field] = cls

        # Generate simple impact report for unspecific buildings
        table_body = [question,
                      TableRow(['Hazard Level',
                                'Buildings Affected'],
                               header=True),
                      TableRow([class_1, lo]),
                      TableRow([class_2, me]),
                      TableRow([class_3, hi])]

        table_body.append(TableRow('Notes', header=True))
        table_body.append('High hazard is defined as shake levels greater '
                          'than %i on the MMI scale.' % t2)
        table_body.append('Medium hazard is defined as shake levels '
                          'between %i and %i on the MMI scale.'
                          % (t1, t2))
        table_body.append('Low hazard is defined as shake levels '
                          'between %i and %i on the MMI scale.'
                          % (t0, t1))

        impact_summary = Table(table_body).toNewlineFreeString()
        impact_table = impact_summary
        map_title = 'Buildings affected'

        # Create style
        style_classes = [dict(label=class_1, value=1,
                              colour='#ffff00', transparency=1),
                         dict(label=class_2, value=2,
                              colour='#ffaa00', transparency=1),
                         dict(label=class_3, value=3,
                              colour='#ff0000', transparency=1)]
        style_info = dict(target_field=self.target_field,
                          style_classes=style_classes,
                          style_type='categorizedSymbol')

        # Create vector layer and return
        V = Vector(data=attributes,
                   projection=I.get_projection(),
                   geometry=I.get_geometry(),
                   name='Estimated buildings affected',
                   keywords={'impact_summary': impact_summary,
                             'impact_table': impact_table,
                             'map_title': map_title,
                             'target_field': self.target_field,
                             'statistics_type': self.statistics_type,
                             'statistics_classes': self.statistics_classes},
                   style_info=style_info)

        return V
