.. include:: sub.txt

==========================
 centralDifference  class
==========================

.. class:: centralDifference()

   Create a centralDifference integrator. A subclass of :class:`integrator`.

   #. The calculation of :math:`U_t + \Delta t`, is based on using the equilibrium equation at time t. For this reason the method is called an explicit integration method.
   #. If there is no rayleigh damping and the C matrix is 0, for a diagonal mass matrix a diagonal solver may and should be used.
   #. For stability, :math:`\frac{\Delta t}{T_n} < \frac{1}{\pi}`

   ::

      centralDifference()




