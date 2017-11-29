.. include:: sub.txt

Algorithm Object
=======================

.. class:: algorithm()

   A python :class:`algorithm` object
   is a wrapper to the OpenSees ``Algorithm`` object.

   .. note::
   
      One cannot create an :class:`algorithm` object
      directly, but only through the :ref:`algorithm-class-methods`.

      There is only one global :class:`algorithm` object.
      Creating another :class:`algorithm` object
      will automatically invalidate the previous :class:`algorithm` objects.

.. _algorithm-class-methods:

Class methods
--------------

#. :meth:`algorithm.Linear`
#. :meth:`algorithm.Newton`
#. :meth:`algorithm.NewtonLineSearch`
#. :meth:`algorithm.ModifiedNewton`
#. :meth:`algorithm.KrylovNewton`
#. :meth:`algorithm.SecantNewton`
#. :meth:`algorithm.RaphsonNewton`
#. :meth:`algorithm.PeriodicNewton`
#. :meth:`algorithm.BFGS`
#. :meth:`algorithm.Broyden`
	       
.. classmethod:: algorithm.Linear(secant=False,initial=False,factorOnce=False)

   Create a Linear :class:`algorithm` which takes one iteration to solve the system of equations.

   ================================   =============================================================
   ``secant`` |bool|                  Flag to indicate to use secant stiffness. (optional)
   ``initial`` |bool|                 Flag to indicate to use initial stiffness. (optional)
   ``factorOnce`` |bool|              Flag to indicate to only set up and
		                      factor matrix once. (optional)
   ================================   =============================================================

   As the tangent matrix typically will not change during the analysis in case of an elastic system it is highly advantageous to use the -factorOnce option. Do not use this option if you have a nonlinear system and you want the tangent used to be actual tangent at time of the analysis step.
   
.. classmethod:: algorithm.Newton(secant=False,initial=False,initialThenCurrent=False)

   Create a Newton-Raphson :class:`algorithm`. The Newton-Raphson method is the most widely used and most robust method for solving nonlinear algebraic equations. 

   ================================   =============================================================
   ``secant`` |bool|                  Flag to indicate to use secant stiffness. (optional)
   ``initial`` |bool|                 Flag to indicate to use initial stiffness.(optional)
   ``initialThenCurrent`` |bool|      Flag to indicate to use initial stiffness
		                      on first step, then use current stiffness
                                      for subsequent steps. (optional)
   ================================   =============================================================

.. classmethod:: algorithm.NewtonLineSearch(Bisection=False,Secant=False,RegulaFalsi=False,InitialInterpolated=False,tol=0.8,maxIter=10,minEta=0.1,maxEta=10.0)

   Create a NewtonLineSearch :class:`algorithm`. Introduces line search to the :meth:`algorithm.Newton` algorithm to solve the nonlinear residual equation. 

   ================================   =============================================================
   ``Bisection`` |bool|               Flag to use Bisection line search. (optional)
   ``Secant`` |bool|                  Flag to use Secant line search. (optional)
   ``RegulaFalsi`` |bool|             Flag to use RegulaFalsi line search. (optional)
   ``InitialInterpolated`` |bool|     Flag to use InitialInterpolated line search.(optional)
   ``tol`` |float|                    Tolerance for search. (optional)
   ``maxIter`` |float|                Max num of iterations to try. (optional)
   ``minEta`` |float|                 Min :math:`\eta` value. (optional)
   ``maxEta`` |float|                 Max :math:`\eta` value. (optional)
   ================================   =============================================================

.. classmethod:: algorithm.ModifiedNewton(secant=False,initial=False)

   Create a ModifiedNewton :class:`algorithm`. The difference to :meth:`algorithm.Newton` is that the tangent at the initial guess is used in the iterations, instead of the current tangent.
		 
   See :meth:`algorithm.Newton` for parameters.

.. classmethod:: algorithm.KrylovNewton(iterate='current',increment='current',maxDim=3)

   Create a KrylovNewton :class:`algorithm` which uses a Krylov subspace accelerator to accelerate the convergence of the modified newton method.

   ================================   =============================================================
   ``iterate`` |str|                  Tangent to iterate on,
		                      ``'current'``, ``'initial'``, ``'noTangent'`` (optional)
   ``increment`` |str|                Tangent to increment on,
		                      ``'current'``, ``'initial'``, ``'noTangent'`` (optional)
   ``maxDim`` |int|                   Max number of iterations until
		                      the tangent is reformed and
                                      the acceleration restarts. (optional)
   ================================   =============================================================

.. classmethod:: algorithm.SecantNewton(iterate='current',increment='current',maxDim=3)

   Create a SecantNewton :class:`algorithm` which uses the two-term update to accelerate the convergence of the modified newton method.

   The default "cut-out" values recommended by Crisfield (R1=3.5, R2=0.3) are used.

   See :meth:`algorithm.KrylovNewton` for parameters.

.. classmethod:: algorithm.RaphsonNewton(iterate='current',increment='current')

   Create a RaphsonNewton :class:`algorithm` which uses Raphson accelerator.


   See :meth:`algorithm.KrylovNewton` for parameters.

.. classmethod:: algorithm.PeriodicNewton(iterate='current',increment='current',maxDim=3)

   Create a PeriodicNewton :class:`algorithm` using periodic accelerator.

   See :meth:`algorithm.KrylovNewton` for parameters.

.. classmethod:: algorithm.BFGS(secant=False,initial=False,count=10)

   Create a BFGS :class:`algorithm`.  The BFGS method is one of the most effective matrix-update or quasi Newton methods for iteration on a nonlinear system of equations. The method computes new search directions at each iteration step based on the initial jacobian, and subsequent trial solutions. The unlike regular :class:`Newton` does not require the tangent matrix be reformulated and refactored at every iteration, however unlike :class:`ModifiedNewton` it does not rely on the tangent matrix from a previous iteration.

   ================================   =============================================================
   ``secant`` |bool|                  Flag to indicate to use secant stiffness. (optional)
   ``initial`` |bool|                 Flag to indicate to use initial stiffness.(optional)
   ``count`` |int|                    Number of iterations. (optional)
   ================================   =============================================================

.. classmethod:: algorithm.Broyden(secant=False,initial=False,count=10)

   Create a Broyden :class:`algorithm` for general unsymmetric systems which performs successive rank-one updates of the tangent at the first iteration of the current time step.

   See :meth:`algorithm.BFGS` for parameters.

