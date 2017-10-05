Legendre Beam Integration
=========================

.. py:function:: beamIntegration('Legendre', intTag, secTag, N)
   :noindex:

   Gauss-Legendre integration is more accurate than Gauss-Lobatto; however, it is not common in force-based elements because there are no integration points at the element ends. Places N Gauss-Legendre integration points along the element. The location and weight of each integration point are tabulated in references on numerical analysis. The forcedeformation response at each integration point is defined by the section with tag secTag. The order of accuracy for Gauss-Legendre integration is 2N-1.

   :param int intTag: tag for the integration
   :param int secTag: tag for the section using the integration
   :param int N: the number of integration points

