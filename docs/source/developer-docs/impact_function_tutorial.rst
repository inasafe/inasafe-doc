.. _impact_function_tutorial:

Impact Function Tutorial
========================

This is a simple tutorial for writing of |project_name| impact functions.

.. note:: This is an old text that needs to be verified, but it may be helpful
   and can serve as a starting point for additional documentation.

Introduction
------------

|project_name| contains a plugin system that allows complex impact functions
to be implemented in Python (http://www.python.org) whilst (ideally)
minimizing the need to understand all the complexity of the handling the
hazard and exposure layers. Features of the impact function system are:

* Auto registration of new impact functions after restart
* Derivation of more complex impact functions from simpler ones
* Auto hiding for impact functions that aren't appropriate (depending on the
  requirements)
* Allow for additional functionality to be added easily
* Provide up-to-date documentation on impact functions functionality

Writing a Simple Raster impact function:
----------------------------------------

This section provides a beginners tutorial on writing a simple earthquake
impact function from scratch. You will need to be familiar with the basics of
Python to be able to write and debug impact functions - if you are new to
Python the standard Python tutorial is a great place to start
see http://docs.python.org/tutorial/.

For this impact function we want to calculate a simple impact by using the
following function of the severity of hazard (i.e. the amount of ground shaking
- H) by the exposure (i.e. the number of people in that area - P). e.g.::

    Impact  = 10 ** (a * H - b) * P

    where
          H: Raster layer of MMI ground shaking
          P: Raster layer of population data on the same grid as H
          a,b: Parameters that were tuned from real world data

Defining the impact class
.........................

As the first step we need to define the impact function class.::

    class SimpleImpactEarthquakeFunction(FunctionProvider)

Every impact function must be subclassed from FunctionProvider. This is the
method of registration for the impact function and allows the |project_name|
Plugin Manager to know what impact functions are available.

Impact Parameters
.................

Each impact function needs to be used in the correct context. Using a flood
impact function for earthquakes will likely yield misleading results at best!
As such plugins may have a variety of conditions that need to be met before
they can be run. Such conditions may include:

* The type of hazard
* The type of exposure
* The form of the layer data (raster or vector)
* The measure or unit type of a layer
* Any other meta data defined in the layer

In the future impact functions may also support filtering by:
* The geographic location
* The available layer meta data

|project_name| will try to show users only those impact functions that can be
validly run.

These parameters required to run the impact function, and indeed all specific
parameters, are defined in the doc string of the class::

     class SimpleImpactEarthquakeFunction(FunctionProvider):
        """Simple impact function for earthquakes

        :author Allen
        :rating 1
        :param requires category=='hazard' and \
                subcategory=='earthquake' and \
                layer_type=='raster' and \
		unit=='MMI'
        :param requires category=='exposure' and \
                subcategory=='population' and \
                layer_type=='raster'
        """

	title = tr('Test Simple Earthquake impact function')

	parameters = OrderedDict([('a', 0.97429), ('b', 11.037)])


This tells |project_name| that this impact function requires at a minimum
inputs of:

* category of 'hazard', with a layer subcategory of 'earthquake' and it must
  be a layerType of 'Raster'
* category of 'exposure', with a layer subcategory of 'earthquake' and it must
  be a layerType of 'Raster'

title: tag specifies the title of the impact function as displayed in the InaSAFE user interface.

parameters: dictionary of parameters that can be configured from the user interface.  In this case two parameters a and b with their default values. 


The `require` expression can be any arbitrary python expression that can be
evaluated.

.. note::
    1. Lines can be broken using the line continuation character '\\' at the
       end of a line.
    2. If any one of the conditions is not met the plugin will not be visible
       from the impact selection box.

The calculation function
........................

Each impact function must then define a `run` method which contains the
execution code::

    def run(self, input):

The parameters are passed in as a dictionary. It is up to the framework to
populate the dictionary correctly in this case with keys containing relevant
data for the exposure and hazard.::

    def run(self, layers)

        """Risk plugin for earthquake fatalities

        Input
          layers: List of layers expected to contain
              H: Raster layer of MMI ground shaking
              P: Raster layer of population data on the same grid as H
        """

        # Identify input layers
        intensity = layers[0]
        population = layers[1]

        # Extract data
        H = intensity.get_data(nan=0)
        P = population.get_data(nan=0)

	# Parameters
	a = self.parameters['a']
        b = self.parameters['b']

        # Calculate impact
        F = 10 ** (a * H - b) * P

        # Create new layer and return
        R = Raster(F,
                   projection=population.get_projection(),
                   geotransform=population.get_geotransform(),
                   keywords={'impact_summary': ''})
        return R



At the end of the function the calculated impact layer R is returned. This
return layer in our example is a Raster layer. The correct projection for this
layer is ensured by passing the input layer projections.


Installing the impact function
..............................

The whole impact function file will now read::

    
    from safe.common.utilities import OrderedDict
    from safe.impact_functions.core import (
        FunctionProvider,
        get_hazard_layer,
        get_exposure_layer)

    from safe.storage.raster import Raster
    from safe.common.utilities import (
        ugettext as tr)

    class SimpleImpactEarthquakeFunction(FunctionProvider):
        """Simple plugin for earthquake damage

        :author Allen
        :rating 1
        :param requires category=='hazard' and \
                        subcategory=='earthquake' and \
                        layertype=='raster
        :param requires category=='exposure' and \
                        subcategory=='population' and \
                        layertype=='raster'
        """

        title = tr('Test Simple Earthquake impact function')

        parameters = OrderedDict([('a', 0.97429), ('b', 11.037)])

        def run(self, layers):

            """Risk plugin for earthquake fatalities

            Input
              layers: List of layers expected to contain
                  H: Raster layer of MMI ground shaking
                  P: Raster layer of population data on the same grid as H
            """

            # Extract input layers
            intensity = get_hazard_layer(layers)
            population = get_exposure_layer(layers)

            # Extract data
            H = intensity.get_data(nan=0)
            P = population.get_data(nan=0, scaling=True)

            a = self.parameters['a']
            b = self.parameters['b']

            # Calculate impact
            F = 10 ** (a * H - b) * P

            # Create new layer and return
            R = Raster(F,
                       projection=population.get_projection(),
                       geotransform=population.get_geotransform(),
                       keywords={'impact_summary': ''})

            return R

    

Save this as SimpleImpactEarthquakeFunction.py into into the following
directory::

    [root |project_name| dir]/safe/impact_functions/earthquake

Then start QGis and activate |project_name|.

Testing the plugin
..................

Load the following data

* Earthquake ground shaking
* Glp10ag (Population for Indonesia)
* You can also use the qgis project indonesia_earthquake_scenarios inside the insasfe data directory
  
Using the indonesia_earthquake_scenarios

* Select an earth quake layer and the population data
* Your new function should be available for execution.
