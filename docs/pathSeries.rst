.. include:: sub.txt

==========================================
 pathSeries class
==========================================

.. class:: pathSeries(dt=0.0,values=[],time=[],filePath='',fileTime='',factor=1.0,startTime=0.0,useLast=0,prependZero=0)

   Create a Path :class:`timeSeries` object.The relationship between load
   factor and time is input by the user as a series of discrete points in
   the 2d space (load factor, time). The input points can come from a
   file or from a list in the script. When the time specified does not match
   any of the input points, linear interpolation is used between points.
   There are many ways to specify the load path, for example,
   the load factors set with ``values`` or ``filePath``,
   and the time set with ``dt``, ``time``, or ``fileTime``.
   A subclass of :class:`timeSeries`.

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

   * attributes

     #. :attr:`tagged.tag`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`



