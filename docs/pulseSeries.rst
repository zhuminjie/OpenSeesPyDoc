.. include:: sub.txt

==========================================
 pulseSeries class
==========================================

.. class:: pulseSeries(tStart,tEnd,period,width=0.5,shift=0.0,factor=1.0,zeroShift=0.0)

   Create a Pulse :class:`timeSeries` object,   in which the load factor
   is some pulse function of the time. A subclass of :class:`timeSeries`.

   .. math::

      \lambda = f(t) = 
      \begin{cases}
          cFactor+zeroShift, &  k < width\\
	  zeroshift, & k < 1\\
	  0.0, & otherwise
      \end{cases}

   .. math::

      k = \frac{t+shift-tStart}{period}-floor(\frac{t+shift-tStart}{period})

   ========================   =============================================================
   ``tStart`` |float|         Starting time of non-zero load factor.
   ``tEnd`` |float|           Ending time of non-zero load factor.
   ``period`` |float|         Characteristic period of pulse.
   ``width`` |float|          Pulse width as a fraction of the period. (optinal)
   ``shift`` |float|          Phase shift in seconds. (optional)
   ``factor`` |float|         Load factor. (optional)
   ``zeroShift`` |float|      Zero shift. (optional)
   ========================   =============================================================

   * attributes

     #. :attr:`tagged.tag`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`



