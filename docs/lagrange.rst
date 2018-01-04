.. include:: sub.txt

lagrange -- Handle with Lagrange Multipliers
============================================

.. class:: lagrange(alphaS=1.0, alphaM=1.0)

   Create a Lagrange Multipliers constraint handler. A subclass of :class:`handler`.

   ========================   ================================================================
   ``alphaS`` |float|         Penalty :math:`\alpha_S` factor on :class:`sp` constraints.
		              (optional)
   ``alphaM`` |float|         Penalty :math:`\alpha_M` factor on :class:`mp` constraints.
		              (optional)
   ========================   ================================================================

   The Lagrange multiplier method introduces new unknowns to the system of equations. The diagonal part of the system corresponding to these new unknowns is 0.0. This ensure that the system IS NOT symmetric positive definite.
