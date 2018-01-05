.. include:: sub.txt

penalty 
=========================================

.. class:: penalty(alphaS, alphaM)

   Create a penalty constraint handler. A subclass of :class:`handler`.

   ========================   =============================================================
   ``alphaS`` |float|         Penalty :math:`\alpha_S` factor on :class:`sp` constraints.
   ``alphaM`` |float|         Penalty :math:`\alpha_M` factor on :class:`mp` constraints.
   ========================   =============================================================

   The degree to which the constraints are enforced is dependent on the penalty values chosen. Problems can arise if these values are too small (constraint not enforced strongly enough) or too large (problems associated with conditioning of the system of equations).



