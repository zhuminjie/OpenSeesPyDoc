.. include:: sub.txt

variableTransientAnalysis -- Transient Analysis with variable time steps
--------------------------------------------------------------------------

.. class:: variableTransientAnalysis()

   Create a OpenSees Variable Transient Analysis object. A subclass of :class:`analysis`.

   * methods

     #. :meth:`variableTransientAnalysis.analyze`


   .. note::
   
      There is only one global :class:`variableTransientAnalysis` object.
      Creating another :class:`variableTransientAnalysis` object
      will automatically invalidate the previous one.

      If the component objects are not defined before hand,
      the :class:`variableTransientAnalysis` automatically creates default
      component objects and issues warning messages to this effect.



.. method:: variableTransientAnalysis.analyze(numIncr, dt, dtMin, dtMax, Jd)

   Perform the variableTransient analysis.

   ===============================   ======================================================================================
   ``numIncr`` |int|                 Number of analysis steps to perform.
   ``dt`` |float|                    Time-step increment.
   ``dtMin`` |float|                 Minimum time steps. 
   ``dtMax`` |float|                 Maximum time steps.
   ``Jd`` |float|                    Number of iterations user would like performed at each step. The variable transient analysis will change current time step if last analysis step took more or less iterations than this to converge.
   ===============================   ======================================================================================

   ::

      variableTransient.analyze(numIncr = 10, dt = 0.01, dtMin=1e-6, dtMax=0.01, Jd=1)

