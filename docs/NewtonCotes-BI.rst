NewtonCotes Beam Integration
============================

.. py:function:: beamIntegration('NewtonCotes', intTag, secTag, N)
   :noindex:

   Newton-Cotes places integration points uniformly along the element, including a point at each end of the element. Places N Newton-Cotes integration points along the element. The weights for the uniformly spaced integration points are tabulated in references on numerical analysis. The forcedeformation response at each integration point is defined by the section with tag secTag. The order of accuracy for Gauss-Radau integration is N-1.

   :param int intTag: tag for the integration
   :param int secTag: tag for the section using the integration
   :param int N: the number of integration points

