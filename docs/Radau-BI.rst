Radau Beam Integration
========================

.. py:function:: beamIntegration('Radau', intTag, secTag, N)
   :noindex:

   Gauss-Radau integration is not common in force-based elements because it places an integration point at only one end of the element; however, it forms the basis for optimal plastic hinge integration methods. Places N Gauss-Radau integration points along the element with a point constrained to be at ndI. The location and weight of each integration point are tabulated in references on numerical analysis. The force-deformation response at each integration point is defined by the section with tag secTag. The order of accuracy for Gauss-Radau integration is 2N-2.

   :param int intTag: tag for the integration
   :param int secTag: tag for the section using the integration
   :param int N: the number of integration points

