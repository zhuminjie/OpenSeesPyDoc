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

   The :func:`fix` function may return
   a list of the :class:`sp` objects.
	   
   .. attribute:: tag
      
      A class attribute.
      The unique tag of the sp object, which is
      same in python and in OpenSees.
      You **can't** set a tag of sp object.

   .. attribute:: ndtag

      A class attribute.
      The tag of the constrained node.
      You **can't** set it.

   .. attribute:: dof

      A class attribute.
      The constrained dof of the node .
      You **can't** set it. The value
      of ``dof`` starts from 1 through ``ndf`` of the :class:`node`.

   .. attribute:: value

      A class attribute.
      The constrained value.
      You **can't** set it.

   .. method:: remove()

      A class method.
      Remove the corresponding OpenSees ``SP_Constraint`` object.
	       
      .. note::
      
	 The python :class:`sp` object is not removed, but
	 any operation on the python :class:`sp` object will fail.

   .. method:: __str__()

      The string reprsentation of the node. Usually
      used in the `print`_ function.

   Examples::

     sp(nd, dof=1, value=1.0, const=True)

     for nd in nds:
         sps = fix(nd, fix=[1,1])
	 for spi in sps:
             print(spi.tag, spi.ndtag,spi.dof,spi.value)
             print(spi)

.. _print: https://docs.python.org/3/library/functions.html#print
