.. include:: sub.txt

SP Object
=====================

.. class:: sp(nd,dof,value,const=False)

   Create a python :class:`sp` object, which
   is a wrapper to the OpenSees ``SP_Constraint`` object.

   ========================   =============================================================
   ``nd`` |node|              A python :class:`node` object to be constrained.
   ``dof`` |int|              The dof of the :class:`node` to be constrained.
   ``value`` |float|          The constrained value.
   ``const`` |bool|           If the constraint is constant. (optional)
   ========================   =============================================================
	   
   .. note::
   
      The :meth:`model.fix` method may return
      :class:`sp` objects |list|.


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


Examples
--------

::

     s = sp(nd, dof=1, value=1.0, const=True)
     print(s)

     for nd in nds:
         sps = m.fix(nd, fix=[1,1])
	 for spi in sps:
             print(spi.tag, spi.ndtag,spi.dof,spi.value)
             print(spi)

