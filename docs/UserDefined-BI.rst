UserDefined Beam Integration
============================

.. py:function:: beamIntegration('UserDefined', intTag, N, *secTags, *locs, **wts)
   :noindex:

   Places N integration points along the element, which are defined in the list locations on the natural domain [0, 1]. The weight of each integration point is defined in the list weights, also on the [0, 1] domain. The force-deformation response at each integration point is defined by the sections with tags stored in the list secTags. The locations, weights, and secTags lists should be of length N. In general, there is no accuracy for this approach to numerical integration.

   :param int intTag: tag for the integration
   :param int N: the number of integration points
   :param secTags: N tags of sections 
   :type secTags: list[int]
   :param locs: N locations of integration points on [0,1]
   :type locs: list[float]
   :param wts: N weights of integration points
   :type wts: list[float]

