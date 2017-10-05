FixedLocation Beam Integration
==============================


.. py:function:: beamIntegration('FixedLocation', intTag, N, *secTags, *locs)
   :noindex:

   This option allows user-specified locations of the integration points. The associated integration weights are computed by the method of undetermined coefficients (Vandermonde system). Note that Newton-Cotes integration is recovered when the integration point locations are equally spaced. Places N integration points along the element, whose locations are defined in a list locations on the natural domain [0, 1]. The force-deformation response at each integration point is defined by the sections with tags stored in the list secTags. Both the locations and secTags lists should be of length N. The order of accuracy for Fixed Location integration is N-1.

   :param int intTag: tag for the integration
   :param int N: the number of integration points
   :param secTags: N tags of sections 
   :type secTags: list[int]
   :param locs: N locations of integration points on [0,1]
   :type locs: list[float]
