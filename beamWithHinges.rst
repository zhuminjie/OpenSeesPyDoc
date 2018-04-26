.. include:: sub.txt

========================
Beam With Hinges Element
========================

This command is used to construct a forceBeamColumn element object, which is based on the non-iterative (or iterative) flexibility formulation. The locations and weights of the element integration points are based on so-called plastic hinge integration, which allows the user to specify plastic hinge lenghts at the element ends. Two-point Gauss integration is used on the element interior while two-point Gauss-Radau integration is applied over lengths of 4LpI and 4LpJ at the element ends, viz. "modified Gauss-Radau plastic hinge integration". A total of six integration points are used in the element state determination (two for each hinge and two for the interior).

Users may be familiar with the beamWithHinges command format (see below); however, the format shown here allows for the simple but important case of using a material nonlinear section model on the element interior. The previous beamWithHinges command constrained the user to an elastic interior, which often led to unconservative estimates of the element resisting force when plasticity spread beyond the plastic hinge regions in to the element interior.

The advantages of this new format over the previous beamWithHinges command are

* Plasticity can spread beyond the plastic hinge regions
* Hinges can form on the element interior, e.g., due to distributed member loads

.. note::

   Use following :func:`beamIntegration`:

   * ``'HingeRadau'``
   * ``'HingeRadauTwo'``
   * ``'HingeMidpoint'``
   * ``'HingeEndpoint'``

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Beam_With_Hinges_Element>`_
