.. include:: sub.txt

============================================
 hingeRadauTwo -- HingeRadauTwo Integration
============================================

.. class:: hingeRadauTwo(secI,lpI,secJ,lpJ,secE)

   Create a HingeRadauTwo :class:`beamIntegration` object.
   Modified two-point Gauss-Radau integration over each hinge region places an integration
   point at the element ends and at 8/3 the hinge length inside the element. This approach
   represents linear curvature distributions exactly and the characteristic length for softening
   plastic hinges is equal to the assumed plastic hinge length.

   Arguments and examples see :class:`hingeMidpoint`.

   * attributes

     #. :attr:`beamIntegration.tag`

   * methods

     #. :meth:`beamIntegration.__str__`
