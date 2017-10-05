Lobatto Beam Integration
========================

.. py:function:: beamIntegration('Lobatto', intTag, secTag, N)
   :noindex:

   Gauss-Lobatto integration is the most common approach for evaluating the response of forcebased elements, because it places an integration point at each end of the element, where bending moments are largest in the absence of interior element loads. Places N Gauss-Lobatto integration points along the element. The location and weight of each integration point are tabulated in references on numerical analysis. The forcedeformation response at each integration point is defined by the section with tag secTag. The order of accuracy for Gauss-Lobatto integration is 2N-3.

   :param int intTag: tag for the integration
   :param int secTag: tag for the section using the integration
   :param int N: the number of integration points

