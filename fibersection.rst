.. include:: sub.txt

===============
 Fiber Section
===============

.. function:: section('Fiber', secTag, '-GJ', GJ=0.0)
   :noindex:

   This commnand allows the user to construct a FiberSection object. Each FiberSection object is composed of Fibers, with each fiber containing a UniaxialMaterial, an area and a location (y,z).

   ================================   ===========================================================================
   ``secTag`` |int|                   unique section tag
   ``GJ`` |float|                     linear-elastic torsional stiffness assigned
                                      to the section (optional)
   ================================   ===========================================================================

.. function:: section('FiberThermal', secTag, '-GJ', GJ=0.0)
   :noindex:

   This command create a FiberSectionThermal object.



.. note::


   #. The commands below should be called after the section command to generate all the fibers in the section.
   #. The patch and layer commands can be used to generate multiple fibers in a single command.


.. toctree::
   :maxdepth: 2
   :caption: Commands to generate all fibers

   fiber
   patch
   layer
