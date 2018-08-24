.. include:: sub.txt

==============
 NormDispIncr
==============

.. function:: test('NormDispIncr', tol,iter,pFlag=0,nType=2)
   :noindex:

   Create a NormUnbalance test, which uses the norm of the left hand side solution vector of the matrix equation to determine if convergence has been reached.

   ======================   =============================================================
   ``tol`` |float|          Tolerance criteria used to check for convergence.
   ``iter`` |int|           Max number of iterations to check
   ``pFlag`` |int|          Print flag (optional):

                            * 0 print nothing.
		            * 1 print information on norms each time ``test()`` is invoked.
			    * 2 print information on norms and number of iterations at end of successful test.
			    * 4 at each step it will print the norms and also the :math:`\Delta U` and :math:`R(U)` vectors.
			    * 5 if it fails to converge at end of ``numIter`` it will print an error message **but return a successfull test**.

   ``nType`` |int|          Type of norm, (0 = max-norm, 1 = 1-norm, 2 = 2-norm). (optional)
   ======================   =============================================================

   When using the Lagrange method to enforce the constraints, the Lagrange multipliers appear in the solution vector.
