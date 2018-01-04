.. include:: sub.txt

loadControl -- Static Integratrion by controlling load
=========================================================

.. class:: loadControl(incr,numIter=1,minIncr=incr,maxIncr=incr)

   Create a OpenSees LoadControl integrator object. A subclass of :class:`integrator`.

   ========================   =============================================================
   ``incr`` |float|           Load factor increment :math:`\lambda`.
   ``numIter`` |int|          Number of iterations the user would
		              like to occur in the solution algorithm. (optional)
   ``minIncr`` |float|        Min stepsize the user will allow :math:`\lambda_{min}`.
		              (optional)
   ``maxIncr`` |float|        Max stepsize the user will allow :math:`\lambda_{max}`.
		              (optional)
   ========================   =============================================================

   #. The change in applied loads that this causes depends on the active load :class:`pattern` (those load :class:`pattern` not set constant) and the :class:`load` in the load :class:`pattern`. If the only active :class:`load` acting on the ``Domain`` are in load :class:`pattern` with a Linear :class:`timeSeries` with a factor of 1.0, this :class:`integrator` is the same as the classical load control method.
   #. The optional arguments are supplied to speed up the step size in cases where convergence is too fast and slow down the step size in cases where convergence is too slow.

   ::

      loadControl(incr=1.0/Nsteps)

