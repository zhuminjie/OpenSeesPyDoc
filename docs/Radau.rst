.. include:: sub.txt

============================================
 radau  class
============================================

.. class:: radau(sec,N)

   Create a Gauss-Radau :class:`beamIntegration` object.
   Gauss-Radau integration is not common in force-based elements because it places an integration point at only one end of the element; however, it forms the basis for optimal plastic
   hinge integration methods.

   Places ``N`` Gauss-Radau integration points along the element with a point constrained to be at ndI. The location and weight of each integration point are tabulated in references on
   numerical analysis. The force-deformation response at each integration point is defined
   by the ``sec``. The order of accuracy for Gauss-Radau integration is 2N-2.

   Arguments and examples see :class:`lobatto`.

   * attributes

     #. :attr:`beamIntegration.tag`

   * methods

     #. :meth:`beamIntegration.__str__`




