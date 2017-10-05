UserHinge Beam Integration
===========================

.. py:function:: beamIntegration('UserHinge', intTag, secTagE, npL, *secTagLs, *ptLs, *wtLs, npR, *secTagRs, *ptRs, *wtRs)
   :noindex:

   :param int intTag: tag for the integration
   :param int segTagE: tag of section E
   :param int npL: number of integration points for secTagLs
   :param secTagLs: tags for L sections
   :type secTagLs: list[int]
   :param ptLs: locations for L sections
   :type ptLs: list[float]
   :param wtLs: weights for L sections
   :type wtLs: list[float]
   :param int npR: number of integration points for secTagRs
   :param secTagRs: tags for R sections
   :type secTagRs: list[int]
   :param ptRs: locations for R sections
   :type ptRs: list[float]
   :param wtRs: weights for R sections
   :type wtRs: list[float]
