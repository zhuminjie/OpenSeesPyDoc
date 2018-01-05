.. include:: sub.txt

========================================
 energyIncr 
========================================

.. class:: energyIncr(tol,iter,pFlag=0,nType=2)

   Create a EnergyIncr test, which uses the dot product of the solution vector and norm of the right hand side of the matrix equation to determine if convergence has been reached. A subclass of :class:`test`.

   See :class:`normUnbalance` for parameters.

   * When using the Penalty method additional large forces to enforce the penalty functions exist on the right hand side, making convergence using this test usually impossible (even though solution might have converged).
   * When using the Lagrange method to enforce the constraints, the Lagrange multipliers appear in the solution vector.

::

   energyIncr(tol=1.0e-8, iter=10)



