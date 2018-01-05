.. include:: sub.txt

====================================
 triangleSeries
====================================

.. class:: triangleSeries(tStart,tEnd,period,factor=1.0,shift=0.0,zeroShift=0.0)

   Create a Triangle :class:`timeSeries` object,   in which the load factor
   is some triangular function of the time in the domain.
   A subclass of :class:`timeSeries`.

   .. math::

      \lambda = f(t) = 
      \begin{cases}
          slope*k*period+zeroShift, & k < 0.25\\
	  cFactor-slope*(k-0.25)*period+zeroShift, & k < 0.75\\
	  -cFactor+slope*(k-0.75)*period+zeroShift, & k < 1.0\\
	  0.0, & otherwise
      \end{cases}

   .. math::
      
      slope = \frac{cFactor}{period/4}
      
      k = \frac{t+\phi-tStart}{period}-floor(\frac{t+\phi-tStart}{period})
      
      \phi = shift - \frac{zeroShift}{slope}

   ========================   =============================================================
   ``tStart`` |float|         Starting time of non-zero load factor.
   ``tEnd`` |float|           Ending time of non-zero load factor.
   ``period`` |float|         Characteristic period of sine wave.
   ``shift`` |float|          Phase shift in radians. (optional)
   ``factor`` |float|         Load factor. (optional)
   ``zeroShift`` |float|      Zero shift. (optional)
   ========================   =============================================================

   * attributes

     #. :attr:`tagged.tag`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`


