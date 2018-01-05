.. include:: sub.txt

transientAnalysis 
----------------------------------------

.. class:: transientAnalysis()

   Create a OpenSees Transient Analysis object. A subclass of :class:`analysis`.

   * methods

     #. :meth:`analysis.eigen`
     #. :meth:`analysis.wipe`
     #. :meth:`transientAnalysis.analyze`


   .. note::
   
      There is only one global :class:`transientAnalysis` object.
      Creating another :class:`transientAnalysis` object
      will automatically invalidate the previous one.

      If the component objects are not defined before hand,
      the :class:`transientAnalysis` automatically creates default
      component objects and issues warning messages to this effect.


.. method:: transientAnalysis.analyze(numIncr, dt)

   Perform the transient analysis.

   ===============================   ======================================================================================
   ``numIncr`` |int|                 Number of analysis steps to perform.
   ``dt`` |float|                    Time-step increment.
   ===============================   ======================================================================================

   ::

      transient.analyze(numIncr = 10, dt = 0.01)



