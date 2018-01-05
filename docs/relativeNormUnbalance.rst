include:: sub.txt

==============================================================
 relativeNormUnbalance 
==============================================================

.. class:: relativeNormUnbalance(tol,iter,pFlag=0,nType=2)

   Create a RelativeNormUnbalance test, which uses the relative norm of the right hand side of the matrix equation to determine if convergence has been reached. A subclass of :class:`test`.

   See :class:`normUnbalance` for parameters.

   * When using the Penalty method additional large forces to enforce the penalty functions exist on the right hand side, making convergence using this test usually impossible (even though solution might have converged).

::

   relativeNormUnbalance(tol=1.0e-10, iter=10)



