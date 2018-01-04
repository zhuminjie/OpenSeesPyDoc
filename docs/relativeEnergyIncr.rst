.. include:: sub.txt

=========================================================
 relativeEnergyIncr -- Relative increment of energy test
=========================================================

.. class:: relativeEnergyIncr(tol,iter,pFlag=0,nType=2)

   Create a RelativeEnergyIncr test, which uses the relative dot product of the solution vector and norm of the right hand side of the matrix equation to determine if convergence has been reached. A subclass of :class:`test`.

   See :class:`normUnbalance` for parameters.

::

   relativeEnergyIncr(tol=1.0e-10, iter=10)
