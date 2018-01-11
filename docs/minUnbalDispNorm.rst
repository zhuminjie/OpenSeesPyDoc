.. include:: sub.txt

=========================
 minUnbalDispNorm  class
=========================

.. class:: minUnbalDispNorm(dlambda1,Jd=1,minLambda=dlambda1,maxLambda=dlambda1,det=False)

   Create a MinUnbalDispNorm integrator.  A subclass of :class:`integrator`.

   ========================   ================================================================
   ``dlambda1`` |float|       First load increment (pseudo-time step) at the first
		              iteration in the next invocation of the analysis command.
   ``Jd`` |int|               Factor relating first load increment at subsequent
		              time steps. (optional)
   ``minLambda`` |float|      Min load increment. (optional)
   ``maxLambda`` |float|      Max load increment. (optional)
   ========================   ================================================================

   ::

      minUnbalDispNorm(dlambda1=0.1)




