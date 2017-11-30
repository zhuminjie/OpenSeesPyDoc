.. include:: sub.txt

BeamIntegration Object
=======================

.. class:: beamIntegration

   A python :class:`beamIntegration` object
   is a wrapper to the OpenSees ``BeamIntegration`` object.

   A wide range of numerical integration options are available in OpenSees to represent distributed plasticity or non-prismatic section details in :ref:`Beam-Column Elements <Beam-Column-Elements>`, i.e., across the entire element domain [0, L].

   .. note::
   
      One cannot create an :class:`beamIntegration` object
      directly, but only through :ref:`beamIntegration-class-methods`.


Object attributes
-------------------

.. attribute:: beamIntegration.tag
      
   An object attribute (get) |int|.
   The :class:`beamIntegration` tag.

   ::

      print(bi.tag)

Object methods
---------------
#. :meth:`beamIntegration.__str__`

.. method:: beamIntegration.__str__()

   The string reprsentation of the :class:`beamIntegration`. Usually
   used in the |print| function.

   ::

      print(bi)

.. _beamIntegration-class-methods:

Class methods
---------------

* Integration Methods for Distributed Plasticity

  Distributed plasticity methods permit yielding at any integration point along the element
  length.

  #. :meth:`beamIntegration.Lobatto`
  #. :meth:`beamIntegration.Legendre`
  #. :meth:`beamIntegration.NewtonCotes`
  #. :meth:`beamIntegration.Radau`
  #. :meth:`beamIntegration.Trapezoidal`
  #. :meth:`beamIntegration.CompositeSimpson`
  #. :meth:`beamIntegration.UserDefined`
  #. :meth:`beamIntegration.FixedLocation`
  #. :meth:`beamIntegration.LowOrder`
  #. :meth:`beamIntegration.MidDistance`

* Plastic Hinge Integration Methods

  Plastic hinge integration methods confine material yielding to regions of the element of
  specified length while the remainder of the element is linear elastic. A summary of plastic
  hinge integration methods is found in (`Scott and Fenves 2006`_).

  #. :meth:`beamIntegration.UserHinge`
  #. :meth:`beamIntegration.HingeMidpoint`
  #. :meth:`beamIntegration.HingeRadau`
  #. :meth:`beamIntegration.HingeRadauTwo`
  #. :meth:`beamIntegration.HingeEndpoint`

.. classmethod:: beamIntegration.Lobatto(sec,N)

   Create a Gauss-Lobatto :class:`beamIntegration` object.
   Gauss-Lobatto integration is the most common approach for evaluating the response of
   :meth:`element.forceBeamColumn` (`Neuenhofer and Filippou 1997`_) because it places an integration point at each end of the element, where bending moments are largest in the absence of interior element loads.

   ========================   =============================================================
   ``sec`` |section|          A previous-defined |section| object.
   ``N`` |int|                Number of integration points along the element.
   ========================   =============================================================

   Places ``N`` Gauss-Lobatto integration points along the element. The location and weight of
   each integration point are tabulated in references on numerical analysis.
   The force deformation response at each integration point is defined by
   the ``sec`` The order of accuracy for Gauss-Lobatto integration is 2N-3.

   ::

      bi = beamIntegration.Lobatto(sec=sec, N=5)



.. classmethod:: beamIntegration.Legendre(sec,N)

   Create a Gauss-Legendre :class:`beamIntegration` object.
   Gauss-Legendre integration is more accurate than Gauss-Lobatto; however, it is not common
   in force-based elements because there are no integration points at the element ends.


   Places ``N`` Gauss-Legendre integration points along the element. The location and weight
   of each integration point are tabulated in references on numerical analysis.
   The force deformation response at each integration point is defined by the ``sec``.
   The order of accuracy for Gauss-Legendre integration is 2N-1.

   Arguments and examples see :meth:`beamIntegration.Lobatto`.


.. classmethod:: beamIntegration.NewtonCotes(sec,N)

   Create a Newton-Cotes :class:`beamIntegration` object.
   Newton-Cotes places integration points uniformly along the element, including a point at
   each end of the element.

   Places ``N`` Newton-Cotes integration points along the element. The weights for the uniformly
   spaced integration points are tabulated in references on numerical analysis. The force deformation
   response at each integration point is defined by the ``sec``.
   The order of accuracy for Gauss-Radau integration is N-1.

   Arguments and examples see :meth:`beamIntegration.Lobatto`.


.. classmethod:: beamIntegration.Radau(sec,N)

   Create a Gauss-Radau :class:`beamIntegration` object.
   Gauss-Radau integration is not common in force-based elements because it places an integration point at only one end of the element; however, it forms the basis for optimal plastic
   hinge integration methods.

   Places ``N`` Gauss-Radau integration points along the element with a point constrained to be at ndI. The location and weight of each integration point are tabulated in references on
   numerical analysis. The force-deformation response at each integration point is defined
   by the ``sec``. The order of accuracy for Gauss-Radau integration is 2N-2.

   Arguments and examples see :meth:`beamIntegration.Lobatto`.

.. classmethod:: beamIntegration.Trapezoidal(sec,N)

   Create a Trapezoidal :class:`beamIntegration` object.

   Arguments and examples see :meth:`beamIntegration.Lobatto`.

.. classmethod:: beamIntegration.CompositeSimpson(sec,N)

   Create a CompositeSimpson :class:`beamIntegration` object.

   Arguments and examples see :meth:`beamIntegration.Lobatto`.



.. classmethod:: beamIntegration.UserDefined(secs,locs,wts)

   Create a UserDefined :class:`beamIntegration` object.
   This option allows user-specified locations and weights of the integration points.

   ========================   =============================================================
   ``secs`` |list|            A list previous-defined |section| objects.
   ``locs`` |listf|           Locations of integration points along the element.
   ``wts`` |listf|            weights of integration points.
   ========================   =============================================================


   ::

      locs = [0.1, 0.3, 0.5, 0.7, 0.9]
      wts = [0.2, 0.15, 0.3, 0.15, 0.2]
      secs = [sec1, sec2, sec2, sec2, sec1]
      bi = beamIntegration.UserDefined(secs=secs, locs=locs, wts=wts)

   Places ``N`` integration points along the element, which are defined in ``locs``
   on the natural domain [0, 1]. The weight of each integration point is
   defined in the ``wts`` also on the [0, 1] domain.
   The force-deformation response at each integration point
   is defined by the ``secs``. The ``locs``, ``wts``, and ``secs``
   should be of length ``N``. In general, there is no accuracy for this approach
   to numerical integration.

.. classmethod:: beamIntegration.FixedLocation(secs,locs)

   Create a FixedLocation :class:`beamIntegration` object.
   This option allows user-specified locations of the integration points. The associated integration
   weights are computed by the method of undetermined coefficients (Vandermonde
   system)

   .. math::

      \sum^N_{i=1}x_i^{j-1}w_i = \int_0^1x^{j-1}dx = \frac{1}{j},\qquad (j=1,...,N)

   Note that :meth:`beamIntegration.NewtonCotes` integration is recovered when the integration point locations are
   equally spaced.

   ========================   =============================================================
   ``secs`` |list|            A list previous-defined |section| objects.
   ``locs`` |listf|           Locations of integration points along the element.
   ========================   =============================================================

   Places ``N`` integration points along the element, whose locations are defined in ``locs``.
   on the natural domain [0, 1]. The force-deformation response at each integration
   point is defined by the ``secs``. Both the ``locs`` and ``secs``
   should be of length ``N``. The order of accuracy for Fixed Location integration is N-1.

   ::

      bi = beamIntegration.FixedLocation(secs=[sec1,sec2,sec2,sec2,sec1],
                                         locs=[0.0,0.2,0.5,0.8,1.0])


.. classmethod:: beamIntegration.LowOrder(secs,locs,wts)

   Create a LowOrder :class:`beamIntegration` object.
   This option is a generalization of the :meth:`beamIntegration.FixedLocation` and :meth:`beamIntegration.UserDefined` integration approaches and is useful for moving load analysis (`Kidarsa, Scott and Higgins 2008`_). The locations of the integration points are user defined,
   while a selected number of weights are specified and the remaining weights are
   computed by the method of undetermined coefficients.

   .. math::

      \sum_{i=1}^{N_f}x_{fi}^{j-1}w_{fi}=\frac{1}{j}-\sum_{i=1}^{N_c}x_{ci}^{j-1}w_{ci}

   Note that :meth:`beamIntegration.FixedLocation` integration is recovered when ``Nc`` is zero.

   ========================   =============================================================
   ``secs`` |list|            A list previous-defined |section| objects.
   ``locs`` |listf|           Locations of integration points along the element.
   ``wts`` |listf|            weights of integration points.
   ========================   =============================================================


   ::

      locs = [0.0, 0.2, 0.5, 0.8, 1.0]
      wts = [0.2, 0.2]
      secs = [sec1, sec2, sec2, sec2, sec1]
      bi = beamIntegration.LowOrder(secs=secs, locs=locs, wts=wts)

   Places ``N`` integration points along the element, which are defined in ``locs``.
   on the natural domain [0, 1]. The force-deformation response at each integration point is
   defined by the ``secs``. Both the ``locs`` and ``secs``
   should be of length ``N``. The ``wts`` at user-selected integration
   points are specified on [0, 1],
   which can be of length ``Nc`` equals ``0`` up to ``N``. These specified weights
   are assigned to the first ``Nc`` entries in the ``locs`` and ``secs``, respectively. The
   order of accuracy for Low Order integration is N-Nc-1.

   .. note::

      ``Nc`` is determined from the length of the ``wts`` list. Accordingly,
      :meth:`beamIntegration.FixedLocation`
      integration is recovered when ``wts`` is an empty list and
      :meth:`beamIntegration.UserDefined` integration is
      recovered when the ``wts`` and ``locs`` lists are of equal length.



.. classmethod:: beamIntegration.MidDistance(secs,locs)

   Create a MidDistance :class:`beamIntegration` object.
   This option allows user-specified locations of the integration points. The associated integration weights are determined from the midpoints between adjacent integration point locations.
   :math:`w_i=(x_{i+1}-x_{i-1})/2` for :math:`i=2...N-1`, :math:`w_1=(x_1+x_2)/2`, and :math:`w_N=1-(x_{N-1}+x_N)/2`.

   ========================   =============================================================
   ``secs`` |list|            A list previous-defined |section| objects.
   ``locs`` |listf|           Locations of integration points along the element.
   ========================   =============================================================


   ::

      locs = [0.0, 0.2, 0.5, 0.8, 1.0]
      secs = [sec1, sec2, sec2, sec2, sec1]
      bi = beamIntegration.MidDistance(secs=secs, locs=locs)


   Places ``N`` integration points along the element, whose locations are defined
   in ``locs`` on the natural domain [0, 1].
   The force-deformation response at each integration
   point is defined by the ``secs``.
   Both the ``locs`` and ``secs`` should be of length N.
   This integration rule can only integrate constant
   functions exactly since the sum of the integration weights is one.

   For the ``locs`` shown above, the associated integration weights
   will be ``[0.15, 0.2, 0.3, 0.2, 0.15]``.

.. classmethod:: beamIntegration.UserHinge(secE,secsL,locsL,wtsL,secsR,locsR,wtsR)

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


   ::

      bi = beamIntegration.UserHinge(secE=secE,
                                     secsL=[sec1,sec2], locsL=[0.1,0.2], wtsL=[0.5,0.5],
                                     secsR=[sec3,sec4], locsR=[0.8,0.9], wtsR=[0.5,0.5])




.. classmethod:: beamIntegration.HingeMidpoint(secI,lpI,secJ,lpJ,secE)

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

   The plastic hinge length at end I (J) is equal to ``lpI`` (``lpJ``) and the associated force deformation response is defined by the ``secI` (``secJ``). The force deformation
   response of the element interior is defined by the ``secE``.
   Typically, the interior section is linear-elastic, but this is not necessary.


   ::

      bi = beamIntegration.HingeMidpoint(secI=sec1,lpI=0.1,secJ=sec2,lpJ=0.2,secE=sec3)


.. classmethod:: beamIntegration.HingeRadau(secI,lpI,secJ,lpJ,secE)

   Create a HingeRadau :class:`beamIntegration` object.
   Two-point Gauss-Radau integration over each hinge region places an integration point at
   the element ends and at 2/3 the hinge length inside the element. This approach represents
   linear curvature distributions exactly; however, the characteristic length for softening plastic
   hinges is not equal to the assumed palstic hinge length.

   Arguments and examples see :meth:`beamIntegration.HingeMidpoint`.

.. classmethod:: beamIntegration.HingeRadauTwo(secI,lpI,secJ,lpJ,secE)

   Create a HingeRadauTwo :class:`beamIntegration` object.
   Modified two-point Gauss-Radau integration over each hinge region places an integration
   point at the element ends and at 8/3 the hinge length inside the element. This approach
   represents linear curvature distributions exactly and the characteristic length for softening
   plastic hinges is equal to the assumed plastic hinge length.

   Arguments and examples see :meth:`beamIntegration.HingeMidpoint`.


.. classmethod:: beamIntegration.HingeEndpoint(secI,lpI,secJ,lpJ,secE)

   Create a HingeEndpoint :class:`beamIntegration` object.
   Endpoint integration over each hinge region moves the integration points to the element ends;
   however, there is a large integration error for linear curvature distributions along the element.

   Arguments and examples see :meth:`beamIntegration.HingeMidpoint`.

