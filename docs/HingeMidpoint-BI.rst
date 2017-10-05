HingeMidpoint Beam Integration
==============================


.. py:function:: beamIntegration('HingeMidpoint', intTag, secTagI,lpI,secTagJ,lpJ,secTagE)
   :noindex:

   Midpoint integration over each hinge region is the most accurate one-point integration rule; however, it does not place integration points at the element ends and there is a small integration error for linear curvature distributions along the element.

   The plastic hinge length at end I (J) is equal to lpI (lpJ) and the associated forcedeformation response is defined by the section with tag secTagI (secTagJ). The forcedeformation response of the element interior is defined by the section with tag secTagE. Typically, the interior section is linear-elastic, but this is not necessary.

   :param int intTag: tag for the integration
   :param int segTagI: tag of section I
   :param int lpI: plastic hinge length at end I
   :param int segTagJ: tag of section J
   :param int lpJ: plastic hinge length at end J
   :param int secTagE: tag for section E
