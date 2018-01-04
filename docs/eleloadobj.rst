.. include:: sub.txt

===========================
 eleLoad -- Elemental Load
===========================

.. class:: eleLoad()

   A subclass of :class:`tagged`.
   To create a :class:`eleLoad` object, use :meth:`pattern.eleLoad`.

   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`eleLoad.ele`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`


.. attribute:: eleLoad.ele

   An object attribute (get) |element|.
   The :class:`element` where the eleLoad is applied.

   ::

      print(el.ele)

