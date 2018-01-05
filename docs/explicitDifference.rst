.. include:: sub.txt

explicitDifference 
==========================================================================

.. class:: explicitDifference()

   Create a ExplicitDifference integrator. A subclass of :class:`integrator`.

   #. When using Rayleigh damping, the damping ratio of high vibration modes is overrated, and the critical time step size will be much smaller. Hence Modal damping is more suitable for this method.
   #. There should be no zero element on the diagonal of the mass matrix when using this method.
   #. Diagonal solver should be used when lumped mass matrix is used because the equations are uncoupled.
   #. For stability, :math:`\Delta t \leq \left(\sqrt{\zeta^2+1}-\zeta\right)\frac{2}{\omega}`

   ::

      explicitDifference()



