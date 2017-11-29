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
      will automatically invalidate the previous :class:`test` objects.

.. _test-class-methods:

Class methods
--------------

#. :meth:`test.NormUnbalance`
#. :meth:`test.NormDispIncr`
#. :meth:`test.EnergyIncr`
#. :meth:`test.RelativeNormUnbalance`
#. :meth:`test.RelativeNormDispIncr`
#. :meth:`test.RelativeTotalNormDispIncr`
#. :meth:`test.RelativeEnergyIncr`
#. :meth:`test.FixedNumIter`
#. :meth:`test.NormDispAndUnbalance`
#. :meth:`test.NormDispOrUnbalance`
#. :meth:`test.PFEM`
	       
.. classmethod:: test.NormUnbalance(tol,iter,pFlag=0,nType=2,maxincr=-1)

   Create a NormUnbalance :class:`test`, which uses the norm of the right hand side of the matrix equation to determine if convergence has been reached. 

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
   ``maxincr`` |int|        Maximum times of error increasing. (optional)
   ======================   =============================================================

   When using the Penalty method additional large forces to enforce the penalty functions exist on the right hand side, making convergence using this test usually impossible (even though solution might have converged).

::

   test.NormUnbalance(tol=1.0e-8, iter=10, pFlag=4)

   
.. classmethod:: test.NormDispIncr(tol,iter,pFlag=0,nType=2)

   Create a NormUnbalance :class:`test`, which uses the norm of the left hand side solution vector of the matrix equation to determine if convergence has been reached.

   See :meth:`test.NormUnbalance` for parameters.

   When using the Lagrange method to enforce the constraints, the Lagrange multipliers appear in the solution vector.

::

   test.NormDispIncr(tol=1.0e-8, iter=10)

.. classmethod:: test.EnergyIncr(tol,iter,pFlag=0,nType=2)

   Create a EnergyIncr :class:`test`, which uses the dot product of the solution vector and norm of the right hand side of the matrix equation to determine if convergence has been reached.

   See :meth:`test.NormUnbalance` for parameters.

   * When using the Penalty method additional large forces to enforce the penalty functions exist on the right hand side, making convergence using this test usually impossible (even though solution might have converged).
   * When using the Lagrange method to enforce the constraints, the Lagrange multipliers appear in the solution vector.

::

   test.EnergyIncr(tol=1.0e-8, iter=10)

.. classmethod:: test.RelativeNormUnbalance(tol,iter,pFlag=0,nType=2)

   Create a RelativeNormUnbalance :class:`test`, which uses the relative norm of the right hand side of the matrix equation to determine if convergence has been reached.

   See :meth:`test.NormUnbalance` for parameters.

   * When using the Penalty method additional large forces to enforce the penalty functions exist on the right hand side, making convergence using this test usually impossible (even though solution might have converged).

::

   test.RelativeNormUnbalance(tol=1.0e-10, iter=10)

.. classmethod:: test.RelativeNormDispIncr(tol,iter,pFlag=0,nType=2)

   Create a RelativeNormDispIncr :class:`test`, which uses the relative of the solution vector of the matrix equation to determine if convergence has been reached. 

   See :meth:`test.NormUnbalance` for parameters.


::

   test.RelativeNormDispIncr(tol=1.0e-10, iter=10)

.. classmethod:: test.RelativeTotalNormDispIncr(tol,iter,pFlag=0,nType=2)

   Create a RelativeTotalNormDispIncr :class:`test`, which uses the ratio of the current norm to the total norm (the sum of all the norms since last convergence) of the solution vector.

   See :meth:`test.NormUnbalance` for parameters.

::

   test.RelativeTotalNormDispIncr(tol=1.0e-8, iter=10)

.. classmethod:: test.RelativeEnergyIncr(tol,iter,pFlag=0,nType=2)

   Create a RelativeEnergyIncr :class:`test`, which uses the relative dot product of the solution vector and norm of the right hand side of the matrix equation to determine if convergence has been reached.

   See :meth:`test.NormUnbalance` for parameters.

::

   test.RelativeEnergyIncr(tol=1.0e-10, iter=10)

.. classmethod:: test.FixedNumIter(iter,pFlag=0,nType=2)

   Create a FixedNumIter :class:`test`, that performs a fixed number of iterations without testing for convergence

   See :meth:`test.NormUnbalance` for parameters.

::

   test.FixedNumIter(iter=20)

.. classmethod:: test.NormDispAndUnbalance(tolIncr,tolR,iter,pFlag=0,nType=2,maxincr=-1)

   Create a NormDispAndUnbalance :class:`test`, which check if both
   :meth:`test.NorUnbalance` and :meth:`test.NormDispIncr` are converged.

   ======================   =============================================================
   ``tolIncr`` |float|      Tolerance for left hand solution increments
   ``tolIncr`` |float|      Tolerance for right hand residual
   ``iter`` |int|           Max number of iterations to check
   ``pFlag`` |int|          See :meth:`test.NormUnbalance` (optional)		    
   ``nType`` |int|          See :meth:`test.NormUnbalance` (optional)
   ``maxincr`` |int|        See :meth:`test.NormUnbalance` (optional)
   ======================   =============================================================

::

   test.NormDispAndUnbalance(tolIncr=1.0e-8, tolR=1.0e-6, iter=10)

.. classmethod:: test.NormDispOrUnbalance(tolIncr,tolR,iter,pFlag=0,nType=2,maxincr=-1)

   Create a NormDispOrUnbalance :class:`test`, which check if either
   :meth:`test.NorUnbalance` or :meth:`test.NormDispIncr` are converged.

   See :meth:`test.NormDispAndUnbalance` for parameters.


::

   test.NormDispAndUnbalance(tolIncr=1.0e-8, tolR=1.0e-6, iter=10)

.. classmethod:: test.PFEM(tolv,tolp,tolrv,tolrp,iter,maxincr,tolrelv=1e-15,tolrelp=1e-15,pFlag=0,nType=2)

   Create a PFEM :class:`test`, which check both increments and residual for
   velocities and pressures.

   ======================   =========================================================================
   ``tolv`` |float|         Tolerance for velocity increments
   ``tolp`` |float|         Tolerance for pressure increments
   ``tolrv`` |float|        Tolerance for velocity residual
   ``tolrp`` |float|        Tolerance for pressure residual
   ``maxincr`` |int|        Max times for error increasing
   ``iter`` |int|           Max number of iterations to check
   ``tolrv`` |float|        Tolerance for relative velocity increments (optional)
   ``tolrp`` |float|        Tolerance for relative pressure increments (optional)
   ``pFlag`` |int|          See :meth:`test.NormUnbalance` (optional)		    
   ``nType`` |int|          See :meth:`test.NormUnbalance` (optional)
   ======================   =========================================================================

   ::

      test.PFEM(tolv=1e-6, tolp=1e-6, tolrv=1e-6, tolrp=1e-6, iter=20, maxincr=3, pFlag=1)



