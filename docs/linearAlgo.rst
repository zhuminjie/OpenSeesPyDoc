.. include:: sub.txt

linearAlgo -- Linear Algorithm
================================

.. class:: linearAlgo(secant=False,initial=False,factorOnce=False)

   Create a Linear algorithm which takes one iteration to solve the system of equations.
   A subclass of :class:`algorithm`.

   ================================   =============================================================
   ``secant`` |bool|                  Flag to indicate to use secant stiffness. (optional)
   ``initial`` |bool|                 Flag to indicate to use initial stiffness. (optional)
   ``factorOnce`` |bool|              Flag to indicate to only set up and
		                      factor matrix once. (optional)
   ================================   =============================================================

   As the tangent matrix typically will not change during the analysis in case of an elastic system it is highly advantageous to use the -factorOnce option. Do not use this option if you have a nonlinear system and you want the tangent used to be actual tangent at time of the analysis step.
