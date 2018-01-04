.. include:: sub.txt

======================================
 hingeRadau -- HingeRadau Integration
======================================

.. class:: hingeRadau(secI,lpI,secJ,lpJ,secE)

   Create a HingeRadau :class:`beamIntegration` object.
   Two-point Gauss-Radau integration over each hinge region places an integration point at
   the element ends and at 2/3 the hinge length inside the element. This approach represents
   linear curvature distributions exactly; however, the characteristic length for softening plastic
   hinges is not equal to the assumed palstic hinge length.

   Arguments and examples see :class:`hingeMidpoint`.


   * attributes

     #. :attr:`beamIntegration.tag`

   * methods

     #. :meth:`beamIntegration.__str__`
