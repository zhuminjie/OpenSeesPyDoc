.. include:: sub.txt

=======================================================
 userDefinedBeamIntegration 
=======================================================

.. class:: userDefinedBeamIntegration(secs,locs,wts)

   Create a UserDefined :class:`beamIntegration` object.
   This option allows user-specified locations and weights of the integration points.

   ========================   =============================================================
   ``secs`` |list|            A list previous-defined |section| objects.
   ``locs`` |listf|           Locations of integration points along the element.
   ``wts`` |listf|            weights of integration points.
   ========================   =============================================================

   * attributes

     #. :attr:`beamIntegration.tag`

   * methods

     #. :meth:`beamIntegration.__str__`



   ::

      locs = [0.1, 0.3, 0.5, 0.7, 0.9]
      wts = [0.2, 0.15, 0.3, 0.15, 0.2]
      secs = [sec1, sec2, sec2, sec2, sec1]
      bi = userDefinedBeamIntegration(secs=secs, locs=locs, wts=wts)

   Places ``N`` integration points along the element, which are defined in ``locs``
   on the natural domain [0, 1]. The weight of each integration point is
   defined in the ``wts`` also on the [0, 1] domain.
   The force-deformation response at each integration point
   is defined by the ``secs``. The ``locs``, ``wts``, and ``secs``
   should be of length ``N``. In general, there is no accuracy for this approach
   to numerical integration.



