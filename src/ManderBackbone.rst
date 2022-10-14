.. include:: sub.txt

==================
ManderBackbone
==================

.. function:: hystereticBackbone('Mander', backboneTag, fc, epsc, E)
   :noindex:

   The backbone function :math:`F(x)` is developed by Mander, Priestly, and Park (1988) and defined as 
   
   .. math::

      F(x) = -f_c\frac{sr}{r-1+s^r}

      s = x / \epsilon_c

      r = \frac{E}{E-f_c/\epsilon_c}

   ===================================   ===========================================================================
   ``backboneTag`` |int|                 integer tag identifying the backbone function.
   ``fc`` |float|                        parameter :math:`f_c`.
   ``epsc`` |float|                      parameter :math:`\epsilon_c`.
   ``E`` |float|                         parameter :math:`E`.
   ===================================   ===========================================================================

