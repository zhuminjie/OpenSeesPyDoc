KrylovNewton-Algorithm
=======================

.. py:currentmodule:: opensees

.. py:function:: algorithm( 'KryloveNewton', *opt)
   :noindex:

   Newton-Raphson algorithm, iteratively solve the nonlinear equations 

   :param opt:

      * ``'-iterate', tangIter(str)`` -- tangent to iterate on, options are ``'current'``, ``'initial'``, ``'noTangent'``. default is ``'current'``.
      * ``'-increment', tangIncr(str)`` -- tangent to increment on, options are ``'current'``, ``'initial'``, ``'noTangent'``. default is ``'current'``.
      * ``'-maxDim', maxDim(int)`` -- max number of iterations until the tangent is reformed and the acceleration restarts (default = 3).


   :type opt: list

.. note::

   see `Krylov-Newton Algorithm`_

   Scott, M.H. and G.L. Fenves. "A Krylov Subspace Accelerated Newton Algorithm: Application to Dynamic Progressive Collapse Simulation of Frames." Journal of Structural Engineering, 136(5), May 2010. `DOI`_

.. _DOI: http://dx.doi.org/10.1061/(ASCE)ST.1943-541X.0000143

.. _Krylov-Newton Algorithm: http://opensees.berkeley.edu/wiki/index.php/Krylov-Newton_Algorithm
