.. _pattern-obj:

Pattern Object
=======================

.. index:: object: pattern

.. class:: pattern()

   A python pattern object
   is a wrapper to the OpenSees ``LoadPattern`` object.

   One cannot create an pattern object
   directly, but only through
   the :ref:`class methods <pattern_class_methods>` below.

   .. attribute:: tag
      
      An object attribute (get).
      The pattern tag.

   .. method:: __str__()

      The string reprsentation of the pattern. Usually
      used in the `print`_ function.

   .. method:: sp(nd,dof,value,const=False)

      Create and add a OpenSees ``SP_Constraint`` object to the pattern.
      The arguments are same as :class:`sp`.
      Return a python :class:`sp` object.

   .. method:: remove()

      Remove the corresponding OpenSees ``LoadPattern`` object.
	       
      .. note::
      
	 The python :class:`pattern` object is not removed, but
	 any operation on the python :class:`pattern` object will fail.
	 When you ``del`` a :class:`pattern` or set it to ``None``,
	 the python :class:`pattern` object is removed, but
	 the OpenSees ``LoadPattern`` is not.

   .. method:: wipe()

      Wipe all OpenSees ``SP_Constraint``, ``NodalLoad``,
      and ``ElementalLoad`` objects
      from the pattern.

.. _pattern_class_methods:

   Class methods:

   #. :meth:`Plain`
	       
   .. classmethod:: Plain(tag, ts, factor=1.0)

      Create a plain load pattern, where
      ``tag`` is the pattern tag,
      ``ts`` is a :class:`timeSeries` object, and
      ``factor`` is the load factor.


   Examples::

     patt = pattern.Plain(1, ts)
     print(patt)

.. _print: https://docs.python.org/3/library/functions.html#print
