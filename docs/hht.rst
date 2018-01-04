.. include:: sub.txt

hht -- Time Integration with the Hilber-Hughes-Taylor
======================================================

.. class:: hht(alpha,gamma=1.5-alpha,beta=(2-alpha)^2/4)

   Create a Hilber-Hughes-Taylor (HHT) integrator. This is an implicit method that allows for energy dissipation and second order accuracy (which is not possible with the regular :class:`newmark` object). Depending on choices of input parameters, the method can be unconditionally stable. A subclass of :class:`integrator`.

   ========================   =============================================================
   ``alpha`` |float|          :math:`\alpha` factor.
   ``gamma`` |float|          :math:`\gamma` factor. (optional)
   ``beta`` |float|           :math:`\beta` factor. (optional)
   ========================   =============================================================

   #. Like :class:`newmark` and all the implicit schemes, the unconditional stability of this method applies to linear problems. There are no results showing stability of this method over the wide range of nonlinear problems that potentially exist. Experience indicates that the time step for implicit schemes in nonlinear situations can be much greater than those for explicit schemes.
   #. :math:`\alpha` = 1.0 corresponds to the :class:`newmark` method.
   #. :math:`\alpha` should be between 0.67 and 1.0. The smaller the :math:`\alpha` the greater the numerical damping.
   #. :math:`\gamma` and :math:`\beta` are optional. The default values ensure the method is second order accurate and unconditionally stable when :math:`\alpha` is :math:`\tfrac{2}{3} <= \alpha <= 1.0`. The defaults are:
   
      :math:`\beta = \frac{(2 - \alpha)^2}{4}`
	 
      and
	    
      :math:`\gamma = \frac{3}{2} - \alpha`

   ::

      hht(alpha=0.9)
