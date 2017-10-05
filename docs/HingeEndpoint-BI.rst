HingeEndpoint Beam Integration
==============================

.. py:function:: beamIntegration('HingeEndpoint', intTag, secTagI,lpI,secTagJ,lpJ,secTagE)
   :noindex:

   Endpoint integration over each hinge region moves the integration points to the element ends; however, there is a large integration error for linear curvature distributions along the element.


   The plastic hinge length at end I (J) is equal to lpI (lpJ) and the associated forcedeformation response is defined by the section with tag secTagI (secTagJ). The forcedeformation response of the element interior is defined by the section with tag secTagE. Typically, the interior section is linear-elastic, but this is not necessary.

   :param int intTag: tag for the integration
   :param int segTagI: tag of section I
   :param int lpI: plastic hinge length at end I
   :param int segTagJ: tag of section J
   :param int lpJ: plastic hinge length at end J
   :param int secTagE: tag for section E
