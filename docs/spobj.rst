.. _sp-obj:

SP Object
=====================

.. index:: object: sp

.. class:: sp(nd,dof,value,const=False)

   Create a python sp object, which
   is a wrapper to the OpenSees ``SP_Constraint`` object.

   The ``nd`` is a python :class:`node` object.

   The ``dof`` is an integer for which dof is to be constrained.

   The ``value`` is a double of constrained value.

   The optional ``const`` indicates if the constraint
   is constant.

   The :meth:`model.fix` method may return
   a list of the :class:`sp` objects.
	   
   .. attribute:: tag
      
      An object attribute (get).
      The unique tag of the sp object, which is
      same in python and in OpenSees.

   .. attribute:: ndtag

      An object attribute (get).
      The tag of the constrained node.

   .. attribute:: dof

      An object attribute (get).
      The constrained dof of the node .
      The value
      of ``dof`` starts from 1 through ``ndf`` of the :class:`node`.

   .. attribute:: value

      An object attribute (get).
      The constrained value.

   .. method:: remove()

      Remove the corresponding OpenSees ``SP_Constraint`` object.
	       
      .. note::
      
	 The python :class:`sp` object is not removed, but
	 any operation on the python :class:`sp` object will fail.
	 When you ``del`` a :class:`sp` or set it to ``None``,
	 the python :class:`ps` object is removed, but
	 the OpenSees SP_Constraint is not.

   .. method:: __str__()

      The string reprsentation of the node. Usually
      used in the `print`_ function.

   Examples::

     s = sp(nd, dof=1, value=1.0, const=True)
     print(s)

     for nd in nds:
         sps = m.fix(nd, fix=[1,1])
	 for spi in sps:
             print(spi.tag, spi.ndtag,spi.dof,spi.value)
             print(spi)

.. _print: https://docs.python.org/3/library/functions.html#print
