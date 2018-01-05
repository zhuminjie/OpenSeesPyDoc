.. include:: sub.txt

pfemAnalysis 
----------------------------------------------

.. class:: pfemAnalysis(dtmax,dtmin,gravity,ratio=0.5)

   Create a OpenSees PFEMAnalysis object. A subclass of :class:`analysis`.

   ===============================   ======================================================================================
   ``dtmax`` |float|                 Maximum time steps.
   ``dtmin`` |float|                 Mimimum time steps.
   ``gravity`` |float|               Gravity acceleration used to move isolated particles.
   ``ratio`` |float|                 The ratio to reduce time steps if it was not converged.
   ===============================   ======================================================================================


   * methods

     #. :meth:`PFEMAnalysis.analyze`

   
   .. note::
   
      There is only one global :class:`PFEMAnalysis` object.
      Creating another :class:`PFEMAnalysis` object
      will automatically invalidate the previous one.

      If the component objects are not defined before hand,
      the :class:`PFEMAnalysis` automatically creates default
      component objects and issues warning messages to this effect.

   ::

      pfem = pfemAnalysis(dtmax=1e-3, dtmin=1e-6, gravity=-9.81)

      for i in range(100):
          pfem.analyze()



.. method:: PFEMAnalysis.analyze()

   Perform the PFEM analysis with one time step.

   ::

      PFEM.analyze()




