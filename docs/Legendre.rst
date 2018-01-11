.. include:: sub.txt

==============================================
 legendre  class
==============================================

.. class:: legendre(sec,N)

   Create a Gauss-Legendre :class:`beamIntegration` object.
   Gauss-Legendre integration is more accurate than Gauss-Lobatto; however, it is not common
   in force-based elements because there are no integration points at the element ends.


   Places ``N`` Gauss-Legendre integration points along the element. The location and weight
   of each integration point are tabulated in references on numerical analysis.
   The force deformation response at each integration point is defined by the ``sec``.
   The order of accuracy for Gauss-Legendre integration is 2N-1.

   Arguments and examples see :class:`lobatto`.


   * attributes

     #. :attr:`beamIntegration.tag`

   * methods

     #. :meth:`beamIntegration.__str__`





