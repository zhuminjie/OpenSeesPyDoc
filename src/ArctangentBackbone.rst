.. include:: sub.txt

==================
ArctangentBackbone
==================

.. function:: hystereticBackbone('Arctangent', backboneTag, K1, gamma, alpha)
   :noindex:

   The backbone function :math:`F(x)` is developed by Ranzo and Petrangeli (1998) and defined as 
   
   .. math::

      F(x) = K_1atan(K_2x)

      K_2 = tan(\alpha)/\gamma

   ===================================   ===========================================================================
   ``backboneTag`` |int|                 integer tag identifying the backbone function.
   ``K1`` |float|                        parameter :math:`K_1`.
   ``gamma`` |float|                     parameter :math:`\gamma`.
   ``alpha`` |float|                     parameter :math:`\alpha`.
   ===================================   ===========================================================================

