.. include:: sub.txt

staticAnalysis 
-----------------------------------

.. class:: staticAnalysis()

   Create a OpenSees StaticAnalysis object. A subclass of :class:`analysis`.


   * methods

     #. :meth:`staticAnalysis.analyze`

   .. note::
   
      There is only one global :class:`staticAnalysis` object.
      Creating another :class:`staticAnalysis` object
      will automatically invalidate the previous one.

      If the component objects are not defined before hand,
      the :class:`staticAnalysis` automatically creates default
      component objects and issues warning messages to this effect.


.. method:: staticAnalysis.analyze(numIncr)

   Perform the static analysis.

   ===============================   ======================================================================================
   ``numIncr`` |int|                 Number of analysis steps to perform.
   ===============================   ======================================================================================

   ::

      static.analyze(numIncr = 10)






