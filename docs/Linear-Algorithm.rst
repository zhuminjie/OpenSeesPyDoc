Linear-Algorithm
================

.. py:currentmodule:: opensees

.. py:function:: algorithm( 'Linear', opt)
   :noindex:

   Linear algorithm, solve the system of equations once.

   .. math:: \Delta U = -K^{-1}R(U)

   :param str opt:

      * ``'-secant'`` -- use secant stiffness
      * ``'-initial'`` -- use initial stiffness
      * ``'-factorOnce'`` -- only set up an factor matrixe once

.. note:: As the tangent matrix typically will not change during the analysis in case of an elastic system it is highly advantageous to use the ``'--factorOnce'`` option. Do not use this option if you have a nonlinear system and you want the tangent used to be actual tangent at time of the analysis step.
