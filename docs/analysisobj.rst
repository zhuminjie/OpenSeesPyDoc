.. include:: sub.txt

Analysis Object
=======================

.. class:: analysis()

   A python :class:`analysis` object
   is a wrapper to the OpenSees ``Analysis`` object.

   .. note::
   
      One cannot create an :class:`analysis` object
      directly, but only through the :ref:`analysis-class-methods`.

      There is only one global :class:`analysis` object.
      Creating another :class:`analysis` object
      will automatically invalid the previous :class:`analysis` objects.

      As the :class:`model` object, you must assign it
      to a variable in order to keep it from being destructed.
      See :ref:`analysisobj-example`.

      If the component objects are not defined before hand, the :class:`analysis` automatically creates default component objects and issues warning messages to this effect.


Object methods
--------------

#. :meth:`analysis.analyze`
#. :meth:`analysis.eigen`

.. method:: analysis.analyze(numIncr=1, dt=0.0, dtMin=0.0, dtMax=0.0, Jd=0)

   Perform the analysis.

   ===============================   ======================================================================================
   ``numIncr`` |int|                 Number of analysis steps to perform. (required except for :meth:`analysis.PFEM`)
   ``dt`` |float|                    Time-step increment. (required for :meth:`analysis.Transient` and :meth:`analysis.VariableTransient`)
   ``dtMin`` |float|                 Minimum time steps. (required for :meth:`analysis.VariableTransient`)
   ``dtMax`` |float|                 Maximum time steps (required for :meth:`analysis.VariableTransient`)
   ``Jd`` |float|                    Number of iterations user would like performed at each step. The variable transient analysis will change current time step if last analysis step took more or less iterations than this to converge (required for :meth:`analysis.VariableTransient`)
   ===============================   ======================================================================================

.. method:: analysis.eigen(numEigen,genBandArpack=True,symmBandLapack=False,fullGenLapack=False,frequency=True,findLargest=False)

   Perform the analysis. Return eigen values |listf|.

   ===============================   ======================================================================================
   ``numEigen`` |int|                Number of eigenvalues required.
   ``genBandArpack`` |bool|          Use genBandArpack eigen solver. (optional)
   ``symmBandLapack`` |bool|         Use symmBandLapack eigen solver. (optional)
   ``fullGenLapack`` |bool|          Use fullGenLapack eigen solver. (optional)
   ``frequency`` |bool|              Use generalized algorithm. (optional)
   ``findLargest`` |bool|            Find the largest. (optional)
   ===============================   ======================================================================================

   #. The eigenvectors are stored at the nodes and can be printed out using a Node Recorder, the nodeEigenvector command, or the Print command.
   #. The default eigensolver is able to solve only for N-1 eigenvalues, where N is the number of inertial DOFs. When running into this limitation the -fullGenLapack solver can be used instead of the default Arpack solver.


.. _analysis-class-methods:

Class methods
--------------

#. :meth:`analysis.Static`
#. :meth:`analysis.Transient`
#. :meth:`analysis.VariableTransient`
#. :meth:`analysis.PFEM`
	       
.. classmethod:: analysis.Static()

   Create a Static :class:`analysis`.


.. classmethod:: analysis.Transient()

   Create a Transient :class:`analysis`.

.. classmethod:: analysis.VariableTransient()

   Create a VariableTransient :class:`analysis`.

.. classmethod:: analysis.PFEM(dtmax,dtmin,gravity,ratio=0.5)

   Create a PFEM :class:`analysis`.

   ===============================   ======================================================================================
   ``dtmax`` |float|                 Maximum time steps.
   ``dtmin`` |float|                 Mimimum time steps.
   ``gravity`` |float|               Gravity acceleration used to move isolated particles.
   ``ratio`` |float|                 The ratio to reduce time steps if it was not converged.
   ===============================   ======================================================================================


.. _analysisobj-example:

Examples
----------

::

   analy = analysis.Static()
   analy.analyze(numIncr = 10)

   pfem = analysis.PFEM(dtmax=1e-3, dtmin=1e-6, gravity=-9.81)

   for i in range(100):
       pfem.analyze()
