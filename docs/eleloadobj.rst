.. include:: sub.txt

EleLoad Object
=====================

.. class:: eleLoad()

   A python :class:`eleLoad` object is a wrapper to
   the OpenSees ``ElementalLoad`` object.

   .. note::
   
      One cannot create an python :class:`eleLoad` object
      directly, but only through :meth:`pattern.eleLoad`.

Object attributes
------------------

#. :attr:`eleLoad.tag`
#. :attr:`eleLoad.ele`

.. attribute:: eleLoad.tag
      
   An object attribute (get) |int|.
   The unique tag of the :class:`eleLoad` object.

   ::

      print(el.tag)

.. attribute:: eleLoad.ele

   An object attribute (get) |element|.
   The :class:`element` where the eleLoad is applied.

   ::

      print(el.ele)

Object methods
---------------

#. :meth:`eleLoad.__str__`
#. :meth:`eleLoad.remove`

.. method:: eleLoad.__str__()

   The string reprsentation of the :class:`eleLoad`. Usually
   used in the `print`_ function.

   ::

      print(el)

.. method:: eleLoad.remove()

   Remove the corresponding OpenSees ``ElementalLoad`` object
   from its :class:`pattern`.
	       
   .. seealso::

      :meth:`node.remove`

   ::

      el.remove()
