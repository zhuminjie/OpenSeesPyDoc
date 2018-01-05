.. include:: sub.txt

===========================================================
 fixedLocationBeamIntegration 
===========================================================

.. class:: fixedLocationBeamIntegration(secs,locs)

   Create a FixedLocation :class:`beamIntegration` object.
   This option allows user-specified locations of the integration points. The associated integration
   weights are computed by the method of undetermined coefficients (Vandermonde
   system)

   .. math::

      \sum^N_{i=1}x_i^{j-1}w_i = \int_0^1x^{j-1}dx = \frac{1}{j},\qquad (j=1,...,N)

   Note that :class:`newtonCotes` integration is recovered when the integration point locations are
   equally spaced.

   ========================   =============================================================
   ``secs`` |list|            A list previous-defined |section| objects.
   ``locs`` |listf|           Locations of integration points along the element.
   ========================   =============================================================

   * attributes

     #. :attr:`beamIntegration.tag`

   * methods

     #. :meth:`beamIntegration.__str__`


   Places ``N`` integration points along the element, whose locations are defined in ``locs``.
   on the natural domain [0, 1]. The force-deformation response at each integration
   point is defined by the ``secs``. Both the ``locs`` and ``secs``
   should be of length ``N``. The order of accuracy for Fixed Location integration is N-1.

   ::

      bi = fixedLocationBeamIntegration(secs=[sec1,sec2,sec2,sec2,sec1],
                                        locs=[0.0,0.2,0.5,0.8,1.0])



