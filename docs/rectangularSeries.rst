.. include:: sub.txt

==========================================
 rectangularSeries class
==========================================

.. class:: rectangularSeries(tStart,tEnd,factor=1.0)

   Create a Rectangular :class:`timeSeries` object,   in which the load factor
   is constant for a specified period and 0 otherwise.
   A subclass of :class:`timeSeries`.

   .. math::

      \lambda = f(t) = 
      \begin{cases}
          cFactor, &  tStart<=t<=tEnd\\
	  0.0, & otherwise
      \end{cases}

   ========================   =============================================================
   ``tStart`` |float|         Starting time of non-zero load factor.
   ``tEnd`` |float|           Ending time of non-zero load factor.
   ``factor`` |float|         Load factor. (optional)
   ========================   =============================================================

   * attributes

     #. :attr:`tagged.tag`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`



