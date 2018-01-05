.. include:: sub.txt

========================================
 newtonCotes 
========================================

.. class:: newtonCotes(sec,N)

   Create a Newton-Cotes :class:`beamIntegration` object.
   Newton-Cotes places integration points uniformly along the element, including a point at
   each end of the element.

   Places ``N`` Newton-Cotes integration points along the element. The weights for the uniformly
   spaced integration points are tabulated in references on numerical analysis. The force deformation
   response at each integration point is defined by the ``sec``.
   The order of accuracy for Gauss-Radau integration is N-1.

   Arguments and examples see :class:`lobatto`.


   * attributes

     #. :attr:`beamIntegration.tag`

   * methods

     #. :meth:`beamIntegration.__str__`



