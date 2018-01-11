.. include:: sub.txt

==========================================
 trigSeries class
==========================================

.. class:: trigSeries(tStart,tEnd,period,factor=1.0,shift=0.0,zeroShift=0.0)

   Create a Trignometric :class:`timeSeries` object,   in which the load factor
   is some trigonemtric function of the time in the domain.
   A subclass of :class:`timeSeries`.

   .. math::

      \lambda = f(t) = 
      \begin{cases}
          cFactor * sin(\frac{2.0\pi(t-tStart)}{period}+\phi), &  tStart<=t<=tEnd\\
          0.0, & otherwise
      \end{cases}

      \phi = shift - \frac{period}{2.0\pi} * \arcsin(\frac{zeroShift}{cFactor})

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



