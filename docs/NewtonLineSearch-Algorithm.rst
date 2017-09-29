NewtonLineSearch-Algorithm
===========================

.. py:currentmodule:: opensees

.. py:function:: algorithm( 'NewtonLineSearch', *opt )
   :noindex:

   NewtonLineSearch algorithm introduces line search to the :doc:`Newton-Algorithm` to solve the nonlinear residual equation. Line search increases the effectiveness of the Newton method when convergence is slow due to roughness of the residual. The command is of the following form:

   :param opt:

      * ``'-type',typeSearch(str)'`` -- line search algorithm. optional default is ``'InitialInterpoled'``. valid types are: ``'Bisection'``, ``'Secant'``, ``'RegulaFalsi'``, ``'InitialInterpolated'``
      * ``'-tol',tol(float)`` -- tolerance for search. optional, defeulat = 0.8
      * ``'-maxIter',maxIter(int)`` -- max num of iterations to try. optional, default = 10
      * ``'-minEta',minEta(float)`` -- a min :math:`\eta` value. optional, default = 0.1
      * ``'-maxEta',maxEta(float)`` -- a max :math:`\eta` value. optional, default = 10.0
   :type opt: list


.. note::

   see `Newton Line Search Algorithm`_


.. _Newton Line Search Algorithm: http://opensees.berkeley.edu/wiki/index.php/Newton_with_Line_Search_Algorithm
