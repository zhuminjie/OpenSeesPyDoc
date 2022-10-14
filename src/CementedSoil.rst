.. include:: sub.txt

======================
CementedSoil
======================

.. function:: hystereticBackbone('CementedSoil', backboneTag, pM, pU, Kpy, z, b)
   :noindex:

   The Evans and Duncan (1982) SILT model can be found `here <http://www.findapile.com/p-y-curves/p-y-curves-models>`_

   The backbone function is defined in this `manual <https://ntrl.ntis.gov/NTRL/dashboard/searchResults/titleDetail/PB94108305.xhtml`_ in page 348

   ===================================   ===========================================================================
   ``backboneTag`` |int|                 integer tag identifying the backbone function.
   ``pM`` |float|                        soil resistance at point M in figure below
   ``pU`` |float|                        Evans and Duncan (1982) proposed a procedure for 
                                         developing p-y curves and deciding pU, the ultimate 
                                         soil resistance, in silty soils, which also defines the point U
   ``Kpy`` |float|                       The initial modulus of subgrade reaction defines
                                         the initial straight line between O and K in figure below
   ``z`` |float|                         the depth below ground surface to p-y curve.
   ``b`` |float|                         diameter (width) of the pile.
   ===================================   ===========================================================================


There are no available recommendations on developing p-y curves for soil with cohesion and friction angle that are generally accepted. Generally, in design, the soil is classified in only two different types: cohesive or cohesionless. In the practice, this simplification leads to a significantly conservative design in the case of cemented soil or silt, which always neglects the soil resistance from the cohesion component (Juirnarongrit et al. 2005). 

.. image:: _static/CementedSoil.png

The initial straight line (EQ. 21) is defined as 

.. math::
  p = K_{py} z y

the parabolic portion (EQ. 14) is defined as 

.. math::
  p = Cy^{1/n}



where 

.. math::
  C = \frac{p_{M}}{y^{1/n}_M}

  n=\frac{p_M}{my_M}

  m=\frac{p_U-pM}{y_U-y_M}

The point :math:`K` is defined at :math:`y_K = (C/(K_{py}z))^{n/(n-1)}` and
:math:`p_K = y_KK_{py}`.

The point :math:`M` is defined at :math:`y_M = b/60` and :math:`p_M`.

The point :math:`U` is defined at :math:`y_U = 3b/80` and :math:`p_U`.