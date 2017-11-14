.. _timeSeries-obj:

TimeSeries Object
=======================

.. index:: object: timeSeries

.. class:: timeSeries()

   A python timeSeries object
   is a wrapper to the OpenSees ``TimeSeries`` object.

   One cannot create an timeSeries object
   directly, but only through
   the :ref:`class methods <timeSeries_class_methods>` below.

   .. attribute:: tag
      
      An object attribute (get).
      The timeSeries tag.

   .. method:: __str__()

      The string reprsentation of the timeSeries. Usually
      used in the `print`_ function.

   .. method:: remove()

      Remove the corresponding OpenSees ``TimeSeries`` object.
	       
      .. note::
      
	 The python :class:`timeSeries` object is not removed, but
	 any operation on the python :class:`timeSeries` object will fail.
	 When you ``del`` a :class:`timeSeries` or set it to ``None``,
	 the python :class:`timeSeries` object is removed, but
	 the OpenSees ``TimeSeries`` is not.


.. _timeSeries_class_methods:

   Class methods:

   #. :meth:`Linear`

   .. classmethod:: Linear(tag, factor=1.0)

      Create a Truss timeSeries, where
      ``tag`` is the timeSeries tag and
      ``factor`` is the linear factor.


   Examples::

     ts = timeSeries.Linear(1)
     print(ts)

.. _print: https://docs.python.org/3/library/functions.html#print
