.. include:: sub.txt

============================================
 hingeMidpoint 
============================================

.. class:: hingeMidpoint(secI,lpI,secJ,lpJ,secE)

   Create a HingeMidpoint :class:`beamIntegration` object.
   Midpoint integration over each hinge region is the most accurate one-point integration rule;
   however, it does not place integration points at the element ends and there is a small integration
   error for linear curvature distributions along the element.

   ========================   ============================================================================
   ``secI`` |section|         A previous-defined |section| object for hinge at I.
   ``lpI`` |float|            The plastic hinge length at I.
   ``secJ`` |section|         A previous-defined |section| object for hinge at J.
   ``lpJ`` |float|            The plastic hinge length at J.
   ``secE`` |section|         A previous-defined |section| object for the element interior.
   ========================   ============================================================================

   * attributes

     #. :attr:`beamIntegration.tag`

   * methods

     #. :meth:`beamIntegration.__str__`


   The plastic hinge length at end I (J) is equal to ``lpI`` (``lpJ``) and the associated force deformation response is defined by the ``secI` (``secJ``). The force deformation
   response of the element interior is defined by the ``secE``.
   Typically, the interior section is linear-elastic, but this is not necessary.


   ::

      bi = hingeMidpoint(secI=sec1,lpI=0.1,secJ=sec2,lpJ=0.2,secE=sec3)



