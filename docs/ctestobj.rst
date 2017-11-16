.. include:: sub.txt

Test Object
=======================

.. class:: test()

   A python :class:`test` object
   is a wrapper to the OpenSees ``ConvergenceTest`` object.

   .. note::
   
      One cannot create an :class:`test` object
      directly, but only through the :ref:`test-class-methods`.

      There is only one global :class:`test` object.
      Creating another :class:`test` object
      will automatically invalid the previous :class:`test` objects.

.. _test-class-methods:

Class methods
--------------

#. :meth:`test.NormUnbalance`
#. :meth:`test.NormDispIncr`
	       
.. classmethod:: test.NormUnbalance(tol,iter,pFlag=0,nType=2,maxincr=-1)

   Create a NormUnbalance :class:`test`, which uses the norm of the right hand side of the matrix equation to determine if convergence has been reached. What the right-hand-side of the matrix equation is depends on :class:`integrator` and :class:`constraints` handler chosen. Usually, though not always, it is equal to the unbalanced forces in the system. 

   ======================   =============================================================
   ``tol`` |float|          Tolerance criteria used to check for convergence.
   ``iter`` |int|           Max number of iterations to check before returning
		            failure condition.
   ``pFlag`` |int|          Print flag (optional):
		 
                            * 0 print nothing.
		            * 1 print information on norms each time ``test()`` is invoked.
			    * 2 print information on norms and number of iterations at end of successful test.
			    * 4 at each step it will print the norms and also the :math:`\Delta U` and :math:`R(U)` vectors.
			    * 5 if it fails to converge at end of ``numIter`` it will print an error message **but return a successfull test**.
			    
   ``nType`` |int|          Type of norm, (0 = max-norm, 1 = 1-norm, 2 = 2-norm). (optional)
   ``maxincr`` |int|        Maximum times of error increasing. (optional)
   ======================   =============================================================

   When using the Penalty method additional large forces to enforce the penalty functions exist on the right hand side, making convergence using this test usually impossible (even though solution might have converged).
   
.. classmethod:: test.NormDispIncr(tol,iter,pFlag=0,nType=2)

   Create a NormUnbalance :class:`test`, which uses the norm of the left hand side solution vector of the matrix equation to determine if convergence has been reached. What the solution vector of the matrix equation is depends on :class:`integrator` and :class:`constraints` handler chosen. Usually, though not always, it is equal to the displacement increments that are to be applied to the model.

   ======================   =============================================================
   ``tol`` |float|          Tolerance criteria used to check for convergence.
   ``iter`` |int|           Max number of iterations to check before returning
		            failure condition.
   ``pFlag`` |int|          Print flag (optional) (see :meth:`test.NormUnbalance`)
   ``nType`` |int|          Type of norm (optional) (see :meth:`test.NormUnbalance`)
   ======================   =============================================================

   When using the Lagrange method to enforce the constraints, the Lagrange multipliers appear in the solution vector.


Examples
----------

::

   test.NormUnbalance(tol=1.0e-8, iter=10, pFlag=4)


