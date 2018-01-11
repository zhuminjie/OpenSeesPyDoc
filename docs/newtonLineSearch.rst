.. include:: sub.txt

=========================
 newtonLineSearch  class
=========================

.. class:: newtonLineSearch(Bisection=False,Secant=False,RegulaFalsi=False,InitialInterpolated=False,tol=0.8,maxIter=10,minEta=0.1,maxEta=10.0)

   Create a NewtonLineSearch algorithm. Introduces line search to the :class:`newton` algorithm to solve the nonlinear residual equation. A subclass of :class:`algorithm`.

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




