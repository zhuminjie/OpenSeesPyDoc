.. include:: sub.txt

==================================
 timeSeries -- A Series of Values
==================================

.. class:: timeSeries()

   A subclass of :class:`tagged` and
   a base class for the OpenSees TimeSeries object.

   One cannot create an :class:`timeSeries` object
   directly, but only through its subclasses.

   * attributes

     #. :attr:`tagged.tag`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`


Following are timeSeries subclasses available in the OpenSees:

#. :meth:`timeSeries.Constant`
#. :meth:`timeSeries.Linear`
#. :meth:`timeSeries.Trig`
#. :meth:`timeSeries.Triangle`
#. :meth:`timeSeries.Rectangular`
#. :meth:`timeSeries.Pulse`
#. :meth:`timeSeries.Path`

.. classmethod:: timeSeries.Constant(factor=1.0)

   Create a Constant :class:`timeSeries` object, in which the load
   factor applied remains constant and is independent of the time in the
   domain, i.e. :math:`\lambda = f(t) = C`.

   ========================   =============================================================
   ``factor`` |float|         The load factor. (optional)
   ========================   =============================================================

   ::

      ts = timeSeries.Constant()



.. classmethod:: timeSeries.Linear(factor=1.0)

   Create a Linear :class:`timeSeries` object,  in which the load factor
   applied is linearly proportional to the time in the domain, i.e
   :math:`\lambda = f(t) = cFactor * t`.

   ========================   =============================================================
   ``factor`` |float|         Linear factor. (optional)
   ========================   =============================================================

   ::

      ts = timeSeries.Linear(factor = 0.1)


.. classmethod:: timeSeries.Trig(tStart,tEnd,period,factor=1.0,shift=0.0,zeroShift=0.0)

   Create a Trignometric :class:`timeSeries` object,   in which the load factor
   is some trigonemtric function of the time in the domain,

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

   ::

      ts = timeSeries.Trig(tStart=0.0,tTend=1.0,period=2*pi)


.. classmethod:: timeSeries.Triangle(tStart,tEnd,period,factor=1.0,shift=0.0,zeroShift=0.0)

   Create a Triangle :class:`timeSeries` object,   in which the load factor
   is some triangular function of the time in the domain,

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

   ::

      ts = timeSeries.Triangle(tStart=0.0,tTend=1.0,period=2*pi)


.. classmethod:: timeSeries.Rectangular(tStart,tEnd,factor=1.0)

   Create a Rectangular :class:`timeSeries` object,   in which the load factor
   is constant for a specified period and 0 otherwise, i.e.

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

   ::

      ts = timeSeries.Rectangular(tStart=0.0,tTend=1.0)



.. classmethod:: timeSeries.Pulse(tStart,tEnd,period,width=0.5,shift=0.0,factor=1.0,zeroShift=0.0)

   Create a Pulse :class:`timeSeries` object,   in which the load factor
   is some pulse function of the time, i.e.

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

   ::

      ts = timeSeries.Pulse(tStart=0.0,tTend=1.0, period=0.5)


.. classmethod:: timeSeries.Path(dt=0.0,values=[],time=[],filePath='',fileTime='',factor=1.0,startTime=0.0,useLast=0,prependZero=0)

   Create a Path :class:`timeSeries` object.The relationship between load
   factor and time is input by the user as a series of discrete points in
   the 2d space (load factor, time). The input points can come from a
   file or from a list in the script. When the time specified does not match
   any of the input points, linear interpolation is used between points.
   There are many ways to specify the load path, for example,
   the load factors set with ``values`` or ``filePath``,
   and the time set with ``dt``, ``time``, or ``fileTime``.

   ========================   =============================================================
   ``dt`` |float|             Time interval between specified points. (optional)
   ``values`` |listf|         Load factor values in a |list|. (optional)
   ``time`` |listf|           Time values in a |list|. (optional)
   ``filePath`` |str|         File containing the load factors values. (optional)
   ``fileTime`` |str|         File containing the time values for corresponding
		              load factors. (optional)
   ``factor`` |float|         A factor to multiply load factors by. (optional)
   ``startTime`` |float|      Provide a start time for provided load factors. (optional)
   ``useLast`` |int|          Use last value after the end of the series. (optional)
   ``prependZero`` |int|      Prepend a zero value to the series of load factors. (optional)
   ========================   =============================================================


   * Linear interpolation between points.
   * If the specified time is beyond last point (AND WATCH FOR NUMERICAL ROUNDOFF), 0.0 is returned. Specify ``useLast=1`` to use the last data point instead of 0.0.
   * The :ref:`transient integration methods <transient-integrators>` in OpenSees assume zero initial conditions. So it is important that any |timeSeries| that is being used in a :meth:`analysis.Transient` starts from zero (first data point in the timeSeries = 0.0). To guarantee that this is the case the optional parameter ``prependZero`` can be specified to prepend a zero value to the provided |timeSeries|.

   ::

      ts = timeSeries.Path(dt=0.02, filePath='A-ELC270.AT2', factor=G)
      ts = timeSeries.Path(time=[0.0,0.0,0.0,1.0], values=[0.0,1.0,2.0,0.0])
