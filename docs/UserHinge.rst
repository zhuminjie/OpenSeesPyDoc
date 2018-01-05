.. include:: sub.txt

============================================
 userHinge 
============================================

.. class:: userHinge(secE,secsL,locsL,wtsL,secsR,locsR,wtsR)

   Create a UserHinge :class:`beamIntegration` object.

   ========================   ============================================================================
   ``secE`` |section|         A previous-defined |section| objects for non-hinge area.
   ``secsL`` |list|           A list of previous-defined |section| objects for left hinge area.
   ``locsL`` |listf|          A list of locations of integration points for left hinge area.
   ``wtsL`` |listf|           A list of weights of integration points for left hinge area.
   ``secsR`` |list|           A list of previous-defined |section| objects for right hinge area.
   ``locsR`` |listf|          A list of locations of integration points for right hinge area.
   ``wtsR`` |listf|           A list of weights of integration points for right hinge area.
   ========================   ============================================================================

   * attributes

     #. :attr:`beamIntegration.tag`

   * methods

     #. :meth:`beamIntegration.__str__`


   ::

      bi = userHinge(secE=secE,
                     secsL=[sec1,sec2], locsL=[0.1,0.2], wtsL=[0.5,0.5],
                     secsR=[sec3,sec4], locsR=[0.8,0.9], wtsR=[0.5,0.5])



