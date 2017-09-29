RaphsonNewton-Algorithm
=======================

.. py:currentmodule:: opensees

.. py:function:: algorithm( 'RaphsonNewton', *opt)
   :noindex:

   Accelerated Newton-Raphson algorithm

   :param opt:

      * ``'-iterate', tangIter(str)`` -- tangent to iterate on, options are ``'current'``, ``'initial'``, ``'noTangent'``. default is ``'current'``.
      * ``'-increment', tangIncr(str)`` -- tangent to increment on, options are ``'current'``, ``'initial'``, ``'noTangent'``. default is ``'current'``.

   :type opt: list

