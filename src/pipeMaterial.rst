.. include:: sub.txt

==================
Pipe Material
==================

.. function:: uniaxialMaterial('Pipe', matTag, nt, T1, E1, xnu1, alpT1, <T2, E2, xnu2, alpT2, ... >)
   :noindex:

   The pipe material should be used with :doc:`pipe` for pipes.
   The material is defined with `nt` temperature points, each of which defines a set of parameters.
   The actual material properties are interpolated based on the average temperature of the element.

   ===================================   =================================================================================================================================================================================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``nt`` |float|                        the number of temperature points for the material. If two or more points
  are provided, the expected range of average temperatures in the element must be covered.
   ``T1`` |float|                        the temperature for point 1
   ``E1`` |float|                        the Young's modulus for point 1
   ``xnu1`` |float|                      the Poisson's ratio for point 1
   ``alpT1`` |float|                     the thermal expansion coefficient for point 1
   ===================================   =================================================================================================================================================================================================================================
