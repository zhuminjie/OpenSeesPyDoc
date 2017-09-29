SecantNewton-Algorithm
=======================

.. py:currentmodule:: opensees

.. py:function:: algorithm( 'SecantNewton', *opt)
   :noindex:

   Accelerated Newton-Raphson algorithm

   :param opt:

      * ``'-iterate', tangIter(str)`` -- tangent to iterate on, options are ``'current'``, ``'initial'``, ``'noTangent'``. default is ``'current'``.
      * ``'-increment', tangIncr(str)`` -- tangent to increment on, options are ``'current'``, ``'initial'``, ``'noTangent'``. default is ``'current'``.
      * ``'-maxDim', maxDim(int)`` -- max number of iterations until the tangent is reformed and the acceleration restarts (default = 3).

   :type opt: list


.. note::

   See `Secant Newton Algorithm <http://opensees.berkeley.edu/wiki/index.php/Secant_Newton_Algorithm>`_
