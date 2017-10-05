LowOrder Beam Integration
==========================

.. py:function:: beamIntegration('LowOrder', intTag, N, *secTags, *locs, **wts)
   :noindex:

   This option is a generalization of the Fixed Location and User Defined integration approaches and is useful for moving load analysis. The locations of the integration points are userdefined, while a selected number of weights are specified and the remaining weights are computed by the method of undetermined coefficients.
      
   .. math::

      \sum_{i=1}^{N_f}x^{j-1}_{fi}w_{fi} = \frac{1}{j}-\sum_{i=1}^{N_c}x^{j-1}_{ci}w_{ci}

   Note that Fixed Location integration is recovered when :math:`N_c` is zero.

   Places N integration points along the element, which are defined in the list locations on the natural domain [0, 1]. The force-deformation response at each integration point is defined by the section tags stored in the list secTags. Both the locations and secTags lists should be of length N. The weights at user-selected integration points are specified (on [0, 1]) in the weights list, which can be of length Nc equals 0 up to N. These specified weights are assigned to the first Nc entries in the locations and secTags lists, respectively. The order of accuracy for Low Order integration is N-Nc-1. 
   

   :param int intTag: tag for the integration
   :param int N: the number of integration points
   :param secTags: N tags of sections 
   :type secTags: list[int]
   :param locs: N locations of integration points on [0,1]
   :type locs: list[float]
   :param wts: N weights of integration points
   :type wts: list[float]

.. note::

   :math:`N_c` is determined from the length of the weights list. Accordingly, FixedLocation integration is recovered when weights is an empty list and UserDefined integration is recovered when the weights and locations lists are of equal length.
