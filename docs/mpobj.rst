.. include:: sub.txt

MP Object
=====================

.. class:: mp()

   A python :class:`mp` object is a wrapper to the OpenSees ``MP_Constraint`` object.

   .. note::

      To create a python :class:`mp` object, use :meth:`node.mp`,
      :meth:`node.equalDOF`, :meth:`node.rigidDiaphragm`, or :meth:`node.rigidLink`. 


Object attributes
------------------

.. attribute:: mp.tag
      
   An object attribute (get) |int|.
   The unique tag of the :class:`mp` object.

   ::

      print(mpobj.tag)

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

Object methods
-----------------

#. :meth:`mp.__str__`
#. :meth:`mp.remove`
	       
.. method:: mp.__str__()

      The string reprsentation of the :class:`mp` object. Usually
      used in the |print| function.

   ::

      print(mpobj)


.. method:: mp.remove()

   Remove the corresponding OpenSees ``MP_Constraint`` object.
	       
   .. seealso::

      :meth:`node.remove`


   ::

      mpobj.remove()

