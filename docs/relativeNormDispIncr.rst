.. include:: sub.txt

=======================================================================
 relativeNormDispIncr -- Relative increment of left hand unknowns test
=======================================================================

.. class:: relativeNormDispIncr(tol,iter,pFlag=0,nType=2)

   Create a RelativeNormDispIncr test, which uses the relative of the solution vector of the matrix equation to determine if convergence has been reached.  A subclass of :class:`test`.

   See :class:`normUnbalance` for parameters.


::

   relativeNormDispIncr(tol=1.0e-10, iter=10)
