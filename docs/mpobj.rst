.. include:: sub.txt

==============================
 mp -- Multi-point constraint
==============================

.. class:: mp()

   A subclass of :class:`tagged`.
   To create a :class:`mp` object, use :meth:`node.mp`,
   :meth:`node.equalDOF`, :meth:`node.rigidDiaphragm`, or :meth:`node.rigidLink`. 

   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`mp.rnd`
     #. :attr:`mp.cnd`
     #. :attr:`mp.rdofs`
     #. :attr:`mp.cdofs`
     #. :attr:`mp.cmat`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`

.. attribute:: mp.rnd

   An object attribute (get) |node|.
   The retained :class:`node`.

   ::

      print(mpobj.rnd)

.. attribute:: mp.cnd

   An object attribute (get) |node|.
   The constrained :class:`node`.

   ::

      print(mpobj.cnd)

.. attribute:: mp.rdofs

   An object attribute (get) |listi|.
   The retained dofs of the :attr:`mp.rnd`.
   The value starts from 1 through :attr:`node.ndf`.

   ::

      print(mpobj.rdofs)

.. attribute:: mp.cdofs

   An object attribute (get) |listi|.
   The constrained dofs of the :attr:`mp.cnd`.
   The value starts from 1 through :attr:`node.ndf`.

   ::

      print(mpobj.cdofs)

.. attribute:: mp.cmat

   An object attribute (get) |listl|.
   The constraint matrix of the :class:`mp` object.


   ::

      print(mpobj.cmat)

