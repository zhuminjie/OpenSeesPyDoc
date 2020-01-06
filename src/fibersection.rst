.. include:: sub.txt

===============
 Fiber Section
===============

.. function:: section('Fiber', secTag, '-GJ', GJ)
   :noindex:

   This commnand allows the user to construct a FiberSection object. Each FiberSection object is composed of Fibers, with each fiber containing a UniaxialMaterial, an area and a location (y,z). The dofs for 2D section are ``[P, Mz]``,
   for 3D are ``[P,Mz,My,T]``.

   ================================   ===========================================================================
   ``secTag`` |int|                   unique section tag
   ``GJ`` |float|                     linear-elastic torsional stiffness assigned
                                      to the section
   ================================   ===========================================================================

.. function:: section('Fiber', secTag, '-torsion', matTag)
   :noindex:

   This commnand allows the user to construct a FiberSection object. Each FiberSection object is composed of Fibers, with each fiber containing a UniaxialMaterial, an area and a location (y,z). The dofs for 2D section are ``[P, Mz]``,
   for 3D are ``[P,Mz,My,T]``.

   ================================   ===========================================================================
   ``secTag`` |int|                   unique section tag
   ``matTag`` |int|                   uniaxialMaterial tag assigned to the section
                                      for torsional response (can be nonlinear)
   ================================   ===========================================================================

.. function:: section('FiberThermal', secTag, '-GJ', GJ=0.0)
   :noindex:

   This command create a FiberSectionThermal object.
   The dofs for 2D section are ``[P, Mz]``,
   for 3D are ``[P,Mz,My]``.


.. note::


   #. The commands below should be called after the section command to generate all the fibers in the section.
   #. The patch and layer commands can be used to generate multiple fibers in a single command.


.. toctree::
   :maxdepth: 2
   :caption: Commands to generate all fibers

   fiber
   patch
   layer
