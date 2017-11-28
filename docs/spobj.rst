.. include:: sub.txt

SP Object
=====================

.. class:: sp()

   A python :class:`sp` object is a wrapper to the OpenSees ``SP_Constraint`` object.

   .. note::

      To create a python :class:`sp` object, use :meth:`node.sp`,
      :meth:`node.fix` or :meth:`pattern.sp`.


Object attributes
------------------

.. attribute:: sp.tag
      
   An object attribute (get) |int|.
   The unique tag of the :class:`sp` object.
      
.. attribute:: sp.nd

   An object attribute (get) |node|.
   The constrained :class:`node`.

.. attribute:: sp.dof

   An object attribute (get) |int|.
   The constrained dof of the :class:`node`.
   The value starts from 1 through :attr:`node.ndf` of the :class:`node`.

.. attribute:: sp.value

   An object attribute (get) |float|.
   The constrained value.

Object methods
-----------------

#. :meth:`sp.__str__`
#. :meth:`sp.remove`
	       
.. method:: sp.__str__()

      The string reprsentation of the :class:`sp` object. Usually
      used in the |print| function.


.. method:: sp.remove()

   Remove the corresponding OpenSees ``SP_Constraint`` object.
   The :class:`sp` object knows if it is in the OpenSees
   ``Domain`` or
   in a :class:`pattern`.
	       
   .. seealso::

      :meth:`node.remove`



