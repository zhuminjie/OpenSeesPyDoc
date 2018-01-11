.. include:: sub.txt

==================================================================
 relativeTotalNormDispIncr  class
==================================================================

.. class:: relativeTotalNormDispIncr(tol,iter,pFlag=0,nType=2)

   Create a RelativeTotalNormDispIncr test, which uses the ratio of the current norm to the total norm (the sum of all the norms since last convergence) of the solution vector. A subclass of :class:`test`.

   See :class:`normUnbalance` for parameters.

::

   relativeTotalNormDispIncr(tol=1.0e-8, iter=10)




