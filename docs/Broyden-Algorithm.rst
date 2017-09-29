Broyden-Algorithm
=================

.. py:currentmodule:: opensees

.. py:function:: algorithm( 'Broyden', opt)
   :noindex:

      Broyden algorithm for general unsymmetric systems which performs successive rank-one updates of the tangent at the first iteration of the current time step.

   :param opt:

      * ``'-secant'`` -- use secant stiffness
      * ``'-initial'`` -- use initial stiffness
      * ``count`` -- number of iterations within a time step until a new tangent is formed


   :type opt: str or int

.. note::

   See `Broden Algorithm <http://opensees.berkeley.edu/wiki/index.php/Broyden_Algorithm>`_
