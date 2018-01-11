.. include:: sub.txt

==================================================
 hingeEndpoint  class
==================================================

.. class:: hingeEndpoint(secI,lpI,secJ,lpJ,secE)

   Create a HingeEndpoint :class:`beamIntegration` object.
   Endpoint integration over each hinge region moves the integration points to the element ends;
   however, there is a large integration error for linear curvature distributions along the element.

   Arguments and examples see :class:`hingeMidpoint`.

   * attributes

     #. :attr:`beamIntegration.tag`

   * methods

     #. :meth:`beamIntegration.__str__`




