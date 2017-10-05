MidDistance Beam Integration
============================


.. py:function:: beamIntegration('MidDistance', intTag, N, *secTags, *locs)
   :noindex:

   This option allows user-specified locations of the integration points. The associated integration weights are determined from the midpoints between adjacent integration point locations. :math:`w_i = (x_i+1 − x_i−1)/2` for :math:`i = 2 . . . N-1, w_1 = (x_1 + x_2)/2`, and :math:`w_N = 1 − (x_N−1 + x_N )/2`.

   Places N integration points along the element, whose locations are defined in a list locations on the natural domain [0, 1]. The force-deformation response at each integration point is defined by the sections with tags stored in the list secTags. Both the locations and secTags lists should be of length N. This integration rule can only integrate constant functions exactly since the sum of the integration weights is one.

   :param int intTag: tag for the integration
   :param int N: the number of integration points
   :param secTags: N tags of sections 
   :type secTags: list[int]
   :param locs: N locations of integration points on [0,1]
   :type locs: list[float]
