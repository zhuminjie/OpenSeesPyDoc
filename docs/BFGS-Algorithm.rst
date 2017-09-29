BFGS-Algorithm
==============

.. py:currentmodule:: opensees

.. py:function:: algorithm( 'BFGS')
   :noindex:

   Broyden–Fletcher–Goldfarb–Shanno (BFGS) algorithm object. The BFGS method is one of the most effective matrix-update or quasi Newton methods for iteration on a nonlinear system of equations. The method computes new search directions at each iteration step based on the initial jacobian, and subsequent trial solutions. The unlike regular Newton-Raphson does not require the tangent matrix be reformulated and refactored at every iteration, however unlike ModifiedNewton it does not rely on the tangent matrix from a previous iteration.

.. note::

   See also `BFGS Algorithm <http://opensees.berkeley.edu/wiki/index.php/BFGS_Algorithm>`_

