.. include:: sub.txt

======================
ReeseStiffClayBelowWS
======================

.. function:: hystereticBackbone('ReeseStiffClayBelowWS', backboneTag, Esi, y50, As, Pc)
   :noindex:

   The backbone function is defined in this `manual <https://ntrl.ntis.gov/NTRL/dashboard/searchResults/titleDetail/PB94108305.xhtml`_ in page 328

   ===================================   ===========================================================================
   ``backboneTag`` |int|                 integer tag identifying the backbone function.
   ``Esi`` |float|                       see below
   ``y50`` |float|                       see below
   ``As`` |float|                        see below
   ``Pc`` |float|                        see below
   ===================================   ===========================================================================


.. image:: _static/ReeseStiffClayBelowWS.png


Esi
-----

:math:`Esi = k_sx` 

where ks is the k value for static load selected from the 
following table

The average shear strength should be computed from the shear strength of the soil to a depth of 5 pile diameters.
It should be defined as half the total maximum principal stress difference in an unconsolidated undrained triaxial
test.

.. list-table:: Average Undrained Shear Strength (ton/ft^2)
   :widths: 25 25 50
   :header-rows: 1

   * - 
     - 0.5 - 1
     - 1 - 2
     - 2 - 4
   * - :math:`k_s`` (Static) :math:`lb/in^3`
     - 500
     - 1000
     - 2000

y50
----

:math:`y_{50} = \varepsilon_{50} b`

Use an appropriate value of :math:`\varepsilon_{50}` from results of
laboratory tests or, in the absence of laboratory tests,
from the following table.

.. list-table:: Average Undrained Shear Strength (ton/ft^2)
   :widths: 25 25 50
   :header-rows: 1

   * - 
     - 0.5 - 1
     - 1 - 2
     - 2 - 4
   * - :math:`\varepsilon_{50}`` (Static) :math:`in/in`
     - 0.007
     - 0.005
     - 0.004


As
---

Choose the appropriate value of As from the following figure for the particular nondimensional depth.

.. image:: _static/Figure3.7.png


Pc
----

Compute the ultimate soil resistance per unit length of
pile, using the smaller of the values given by the
equations below

..math:
  p_{ct} = 2c_ab+\gamma'bx+2.83c_ax

  p_{cd} = 11cb

where 

1. Obtain values for undrained soil shear strength :math:`c`, soil
submerged unit weight :math:`\gamma'`, and pile diameter :math:`b`
2. Compute the average undrained soil shear strength :math:`c_a`
over the depth :math:`x`.