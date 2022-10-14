.. include:: sub.txt

======================
ReeseStiffClayAboveWS
======================

.. function:: hystereticBackbone('ReeseStiffClayAboveWS', backboneTag, pu, y50)
   :noindex:

   The backbone function is defined in this `manual <https://ntrl.ntis.gov/NTRL/dashboard/searchResults/titleDetail/PB94108305.xhtml`_ in page 328

   ===================================   ===========================================================================
   ``backboneTag`` |int|                 integer tag identifying the backbone function.
   ``pu`` |float|                        see below
   ``y50`` |float|                       see below
   ===================================   ===========================================================================


.. image:: _static/ReeseStiffClayBelowWS.png


pu
-----

Obtain values for undrained shear strength :math:`c`, soil unit
weight :math:`\gamma`, and pile diameter :math:`b`.
Also obtain the values
of :math:`\varepsilon_{50}` from stress-strain curves.
If no stress-strain
curves are available, use a value from :math:`\varepsilon_{50} of 0.010 or
0.005 as given in the following table, the larger value being more
conservative.

.. list-table:: Consistency of Clay
   :header-rows: 1

   * - Consistency of Clay
     - :math:`\varepsilon_{50}
   * - Soft
     - 0.020
   * - Medium
     - 0.010
   * - Stiff
     - 0.005

Compute the ultimate soil resistance per unit length of shaft, :math:`p_u`, using the smaller of the values given by the following equations

.. math::

  p_u = (3 + \frac{\gamma'}{c}x+\frac{J}{b}x)cb
  p_u = 9cb



y50
----

Compute the deflection, :math:`y_{50}` at one-half the ultimate
soil resistance from the following equation

.. math::

  y_{50} = 2.5\varepsilon_{50}b


