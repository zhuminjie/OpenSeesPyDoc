.. include:: sub.txt

Load Object
=====================

.. class:: load()

   A python :class:`load` object is a wrapper to
   the OpenSees ``NodalLoad`` object.

   .. note::
   
      One cannot create an python :class:`load` object
      directly, but only through :meth:`pattern.load`.

Object attributes
------------------

.. attribute:: load.tag
      
   An object attribute (get) |int|.
   The unique tag of the :class:`load` object.

   ::

      print(l.tag)

.. attribute:: load.nd

   An object attribute (get) |node|.
   The :class:`node` where the load is applied.

   ::

      print(l.nd)

Object methods
---------------

#. :meth:`load.__str__`
#. :meth:`load.remove`

.. method:: load.__str__()

   The string reprsentation of the :class:`load`. Usually
   used in the `print`_ function.

   ::

      print(l)

.. method:: load.remove()

   Remove the corresponding OpenSees ``NodalLoad`` object
   from its :class:`pattern`.
	       
   .. seealso::

      :meth:`node.remove`

   ::

      l.remove()
