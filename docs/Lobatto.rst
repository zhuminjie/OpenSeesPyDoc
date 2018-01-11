.. include:: sub.txt

============================================
 lobatto  class
============================================

.. class:: lobatto(sec,N)

   Create a Gauss-Lobatto :class:`beamIntegration` object.
   Gauss-Lobatto integration is the most common approach for evaluating the response of
   :class:`forceBeamColumn` (`Neuenhofer and Filippou 1997`_) because it places an integration point at each end of the element, where bending moments are largest in the absence of interior element loads.

   ========================   =============================================================
   ``sec`` |section|          A previous-defined |section| object.
   ``N`` |int|                Number of integration points along the element.
   ========================   =============================================================

   * attributes

     #. :attr:`beamIntegration.tag`

   * methods

     #. :meth:`beamIntegration.__str__`


   Places ``N`` Gauss-Lobatto integration points along the element. The location and weight of
   each integration point are tabulated in references on numerical analysis.
   The force deformation response at each integration point is defined by
   the ``sec`` The order of accuracy for Gauss-Lobatto integration is 2N-3.

   ::

      bi = lobatto(sec=sec, N=5)




