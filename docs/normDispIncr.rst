.. include:: sub.txt

======================================================
 normDispIncr -- Increment of left hand unknowns test
======================================================

.. class:: normDispIncr(tol,iter,pFlag=0,nType=2)

   Create a NormUnbalance test, which uses the norm of the left hand side solution vector of the matrix equation to determine if convergence has been reached. A subclass of :class:`test`.

   See :class:`normUnbalance` for parameters.

   When using the Lagrange method to enforce the constraints, the Lagrange multipliers appear in the solution vector.

::

   normDispIncr(tol=1.0e-8, iter=10)
