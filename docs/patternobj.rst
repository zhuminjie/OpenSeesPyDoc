.. include:: sub.txt

Pattern Object
=======================

.. class:: pattern()

   A python :class:`pattern` object
   is a wrapper to the OpenSees ``LoadPattern`` object.

   .. note::
   
      One cannot create an :class:`pattern` object
      directly, but only through the :ref:`pattern-class-methods`.

Object attributes
------------------

.. attribute:: pattern.tag
      
   An object attribute (get) |int|.
   The :class:`pattern` tag.

.. attribute:: pattern.sps
      
   An object attribute (get) |list|.
   All python :class:`sp` objects in the :class:`pattern`.

.. attribute:: pattern.loads
      
   An object attribute (get) |list|.
   All python :class:`load` objects in the :class:`pattern`.

.. attribute:: pattern.loadFactor
      
   An object attribute (get) |float|.
   Get current load factor in the :class:`pattern`.

Object methods
---------------

#. :meth:`pattern.__str__`
#. :meth:`pattern.sp`
#. :meth:`pattern.load`
#. :meth:`pattern.wipe`
#. :meth:`pattern.remove`

.. method:: pattern.__str__()

   The string reprsentation of the pattern. Usually
   used in the `print`_ function.

.. method:: pattern.sp(nd,dof,value,const=False)

   Create and add a python :class:`sp` object to the :class:`pattern`.
   Return the python :class:`sp` object.

   ========================   =============================================================
   ``nd`` |node|              A python :class:`node` object to be constrained.
   ``dof`` |int|              The dof of the :class:`node` to be constrained.
   ``value`` |float|          The constrained value.
   ``const`` |bool|           If the constraint is constant. (optional)
   ========================   =============================================================

.. method:: pattern.load(nd,load,const=False)

   Create and add a python :class:`load` object to the :class:`pattern`.
   Return the python :class:`load` object.

   ========================   =============================================================
   ``nd`` |node|              :class:`node` object.
   ``load`` |listf|           Load values.
   ``const`` |bool|           Whether the load is constant. (optional)
   ========================   =============================================================
	    
.. method:: pattern.wipe()

   Wipe all :class:`sp`, :class:`load`, and :class:`eleLoad` objects
   from the :class:`pattern`.

.. method:: pattern.remove()

   Remove the corresponding OpenSees ``LoadPattern`` object
   and every thing in it.

   .. seealso::

      :meth:`node.remove`

.. _pattern-class-methods:

Class methods
--------------

#. :meth:`pattern.Plain`
	       
.. classmethod:: pattern.Plain(tag, ts, factor=1.0)

   Create a plain load :class:`pattern`.

   ========================   =============================================================
   ``tag`` |int|              :class:`pattern` tag.
   ``ts`` |timeSeries|        A :class:`timeSeries` object.
   ``factor`` |float|         Load factor. (optional)
   ========================   =============================================================

   
Examples
----------

::

   ptn = pattern.Plain(1, ts)

   ptn.sp(nd, dof=1, value=0.0)
   ptn.load(nd, load=[0,1.0])

   print(ptn)


