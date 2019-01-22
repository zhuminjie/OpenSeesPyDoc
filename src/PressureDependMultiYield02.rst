.. include:: sub.txt

============================
 PressureDependMultiYield02
============================

.. function:: nDMaterial('PressureDependMultiYield02', matTag, nd, rho, refShearModul, refBulkModul, frictionAng, peakShearStra, refPress, pressDependCoe, PTAng, contrac[0], contrac[2], dilat[0], dilat[2], noYieldSurf=20.0, *yieldSurf=[], contrac[1]=5.0, dilat[1]=3.0, *liquefac=[1.0,0.0],e=0.6, *params=[0.9, 0.02, 0.7, 101.0], c=0.1)
   :noindex:

   PressureDependMultiYield02 material is modified from PressureDependMultiYield material, with:

   #. additional parameters (``contrac[2]`` and ``dilat[2]``) to account for :math:`K_{\sigma}` effect,
   #. a parameter to account for the influence of previous dilation history on subsequent contraction phase (``contrac[1]``), and
   #. modified logic related to permanent shear strain accumulation (``liquefac[0]`` and ``liquefac[1]``).

   ================================   ================================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``contrac[2]`` |float|             A non-negative constant reflecting :math:`K_\sigma` effect.
   ``dilat[2]`` |float|               A non-negative constant reflecting :math:`K_\sigma` effect.
   ``contrac[1]`` |float|             A non-negative constant reflecting dilation history on contraction tendency.
   ``liquefac[0]`` |float|            Damage parameter to define accumulated permanent
                                      shear strain as a function of dilation
				      history. (Redefined and different from
				      PressureDependMultiYield material).
   ``liquefac[1]`` |float|            Damage parameter to define biased accumulation of
                                      permanent shear strain as a function of load reversal
				      history. (Redefined and different from
				      PressureDependMultiYield material).
   ``c`` |float|                      Numerical constant (default value = 0.1 kPa)
   ================================   ================================================================================



See also `notes <http://opensees.berkeley.edu/wiki/index.php/PressureDependMultiYield02_Material>`_
