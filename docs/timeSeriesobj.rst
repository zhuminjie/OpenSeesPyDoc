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

.. attribute:: timeSeries.tag
      
   An object attribute (get) |int|.
   The :class:`timeSeries` tag.

Object methods
---------------

#. :meth:`timeSeries.__str__`
#. :meth:`timeSeries.remove`

.. method:: timeSeries.__str__()

   The string reprsentation of the :class:timeSeries`. Usually
   used in the `print`_ function.

.. method:: timeSeries.remove()

   Remove the corresponding OpenSees ``TimeSeries`` object.
	       
   .. seealso::

      :meth:`node.remove`


.. _timeSeries-class-methods:

Class methods
--------------

   #. :meth:`Linear`

   .. classmethod:: timeSeries.Linear(tag, factor=1.0)

      Create a Linear :class:`timeSeries` object.

      ========================   =============================================================
      ``tag`` |int|              :class:`timeSeries` tag.
      ``factor`` |float|         Linear factor. (optional)
      ========================   =============================================================
	


Examples
---------

::

     ts = timeSeries.Linear(1)
     print(ts)

