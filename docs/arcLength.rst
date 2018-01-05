.. include:: sub.txt

arcLength 
===================================================

.. class:: arcLength(s,alpha)

   Create a ArcLength integrator. In an analysis step with ArcLength we seek to determine the time step that will result in our constraint equation being satisfied. A subclass of :class:`integrator`.

   ========================   ================================================================
   ``s`` |float|              The arcLength.
   ``alpha`` |float|          :math:`\alpha` a scaling factor on the reference loads.
   ========================   ================================================================

   ::

      arcLenght(s=1.0, alpha=0.1)



