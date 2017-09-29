analyze
=======

.. py:currentmodule:: opensees

.. py:function:: analyze([numIncr[, dt, dtMin, dtMin, Jd]])

   perform the analysis

   :param int numIncr: 	number of analysis steps to perform. Not needed if :ref:`PFEM-Analysis` is specified.
   :param float dt: time-step increment. Required if :ref:`Transient-Analysis` or :ref:`VariableTransient-Analysis`.
   :param float dtMin: minimum time steps. Required if a :ref:`VariableTransient-Analysis` was specified.
   :param float dtMax: maximum time steps. Required if a :ref:`VariableTransient-Analysis` was specified.
   :param float Jd: Required if a :ref:`VariableTransient-Analysis` was specified.

