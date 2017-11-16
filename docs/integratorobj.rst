.. include:: sub.txt

Integrator Object
=======================

.. class:: integrator()

   A python :class:`integrator` object
   is a wrapper to the OpenSees ``Integrator`` object.

   .. note::
   
      One cannot create an :class:`integrator` object
      directly, but only through the :ref:`integrator-class-methods`.

      There is only one global :class:`integrator` object.
      Creating another :class:`integrator` object
      will automatically invalid the previous :class:`integrator` objects.

.. _integrator-class-methods:

Class methods
--------------

#. :meth:`integrator.LoadControl`
#. :meth:`integrator.DisplacementControl`
	       
.. classmethod:: integrator.LoadControl(incr,numIter=1,minIncr=incr,maxIncr=incr)

   Create a LoadControl :class:`integrator`.

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

.. classmethod:: integrator.DisplacementControl(nd,dof,incr,numIter=1,dUmin=incr,dUmax=incr)

   Create a DisplacementControl :class:`integrator`.

   ========================   =============================================================
   ``nd`` |node|              :class:`node` whose response controls solution
   ``dof`` |int|              Degree of freedom at the :class:`node`,
		              1 through :attr:`node.ndf`.
   ``incr`` |float|           First displacement increment :math:`\Delta U_{dof}`.
   ``numIter`` |int|          Number of iterations the user would
		              like to occur in the solution algorithm. (optional)
   ``minIncr`` |float|        Min stepsize the user will allow :math:`\Delta U_{min}`.
		              (optional)
   ``maxIncr`` |float|        Max stepsize the user will allow :math:`\Delta U_{max}`.
		              (optional)
   ========================   =============================================================

Examples
----------

::

   integrator.LoadControl(incr=1.0/Nsteps)


