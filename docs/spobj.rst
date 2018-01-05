.. include:: sub.txt

===============================
 sp 
===============================

.. class:: sp()

   A subclass of :class:`tagged`.
   To create a :class:`sp` object, use :meth:`node.sp`,
   :meth:`node.fix` or :meth:`pattern.sp`.

   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`sp.nd`
     #. :attr:`sp.dof`
     #. :attr:`sp.value`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`


.. attribute:: sp.nd

   An object attribute (get) |node|.
   The constrained :class:`node`.

   ::

      print(s.nd)

.. attribute:: sp.dof

   An object attribute (get) |int|.
   The constrained dof of the :class:`node`.
   The value starts from 1 through :attr:`node.ndf` of the :class:`node`.

   ::

      print(s.dof)

.. attribute:: sp.value

   An object attribute (get) |float|.
   The constrained value.

   ::

      print(s.value)


	       




