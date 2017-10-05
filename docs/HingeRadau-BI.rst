HingeRadau Beam Integration
===========================

.. py:function:: beamIntegration('HingeRadau', intTag, secTagI,lpI,secTagJ,lpJ,secTagE)
   :noindex:

   Modified two-point Gauss-Radau integration over each hinge region places an integration point at the element ends and at 8/3 the hinge length inside the element. This approach represents linear curvature distributions exactly and the characteristic length for softening plastic hinges is equal to the assumed plastic hinge length.

   The plastic hinge length at end I (J) is equal to lpI (lpJ) and the associated forcedeformation response is defined by the section with tag secTagI (secTagJ). The forcedeformation response of the element interior is defined by the section with tag secTagE. Typically, the interior section is linear-elastic, but this is not necessary.

   :param int intTag: tag for the integration
   :param int segTagI: tag of section I
   :param int lpI: plastic hinge length at end I
   :param int segTagJ: tag of section J
   :param int lpJ: plastic hinge length at end J
   :param int secTagE: tag for section E
