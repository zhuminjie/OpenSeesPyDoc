.. include:: sub.txt

=============
 load  class
=============

.. class:: load()

   A subclass of :class:`tagged`.
   To create a :class:`load` object, use :meth:`pattern.load`.

   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`load.nd`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`


.. attribute:: load.nd

   An object attribute (get) |node|.
   The :class:`node` where the load is applied.

   ::

      print(l.nd)






