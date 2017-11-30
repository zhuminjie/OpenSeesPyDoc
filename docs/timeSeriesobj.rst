.. include:: sub.txt

TimeSeries Object
=======================

.. class:: timeSeries()

   A python :class:`timeSeries` object
   is a wrapper to the OpenSees ``TimeSeries`` object.

   .. note::
   
      One cannot create an :class:`timeSeries` object
      directly, but only through :ref:`timeSeries-class-methods`.


Object attributes
------------------

#. :attr:`timeSeries.tag`

.. attribute:: timeSeries.tag
      
   An object attribute (get) |int|.
   The :class:`timeSeries` tag.

   ::

      print(ts.tag)

Object methods
---------------

#. :meth:`timeSeries.__str__`
#. :meth:`timeSeries.remove`

.. method:: timeSeries.__str__()

   The string reprsentation of the :class:timeSeries`. Usually
   used in the `print`_ function.

   ::

      print(ts)

.. method:: timeSeries.remove()

   Remove the corresponding OpenSees ``TimeSeries`` object.
	       
   .. seealso::

      :meth:`node.remove`

   ::

      rs.remove()
   
.. _timeSeries-class-methods:

Class methods
--------------

   #. :meth:`Linear`

   .. classmethod:: timeSeries.Linear(factor=1.0)

      Create a Linear :class:`timeSeries` object.

      ========================   =============================================================
      ``factor`` |float|         Linear factor. (optional)
      ========================   =============================================================

      ::

	 ts = timeSeries.Linear(factor = 0.1)

