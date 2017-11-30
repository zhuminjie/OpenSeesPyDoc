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

#. :attr:`pattern.tag`
#. :attr:`pattern.sps`
#. :attr:`pattern.loads`
#. :attr:`pattern.loadFactor`

.. attribute:: pattern.tag
      
   An object attribute (get) |int|.
   The :class:`pattern` tag.

   ::

      print(ptn.tag)

.. attribute:: pattern.sps
      
   An object attribute (get) |list|.
   All python :class:`sp` objects in the :class:`pattern`.

   ::

      print(ptn.sps)

.. attribute:: pattern.loads
      
   An object attribute (get) |list|.
   All python :class:`load` objects in the :class:`pattern`.

   ::

      print(ptn.loads)

.. attribute:: pattern.loadFactor
      
   An object attribute (get) |float|.
   Get current load factor in the :class:`pattern`.

   ::

      print(ptn.loadFactor)

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

   ::

      print(ptn)

.. method:: pattern.sp(nd,dof,value,const=False)

   Create and add a python :class:`sp` object to the :class:`pattern`.
   Return the python :class:`sp` object.

   ========================   =============================================================
   ``nd`` |node|              A python :class:`node` object to be constrained.
   ``dof`` |int|              The dof of the :class:`node` to be constrained.
   ``value`` |float|          The constrained value.
   ``const`` |bool|           If the constraint is constant. (optional)
   ========================   =============================================================

   ::

      s = ptn.sp(nd=nd, dof=1, value=0.1)

.. method:: pattern.load(nd,load,const=False)

   Create and add a python :class:`load` object to the :class:`pattern`.
   Return the python :class:`load` object.

   ========================   =============================================================
   ``nd`` |node|              :class:`node` object.
   ``load`` |listf|           Load values.
   ``const`` |bool|           Whether the load is constant. (optional)
   ========================   =============================================================

   ::

      l = ptn.load(nd=nd, load=[1.0,-1.0])
	    
.. method:: pattern.wipe()

   Wipe all :class:`sp`, :class:`load`, and :class:`eleLoad` objects
   from the :class:`pattern`.

   ::

      ptn.wipe()

.. method:: pattern.remove()

   Remove the corresponding OpenSees ``LoadPattern`` object
   and every thing in it.

   .. seealso::

      :meth:`node.remove`

   ::

      ptn.remove()

.. _pattern-class-methods:

Class methods
--------------

#. :meth:`pattern.Plain`
	       
.. classmethod:: pattern.Plain(ts, factor=1.0)

   Create a plain load :class:`pattern`.

   ========================   =============================================================
   ``ts`` |timeSeries|        A :class:`timeSeries` object.
   ``factor`` |float|         Load factor. (optional)
   ========================   =============================================================


   ::

      ptn = pattern.Plain(ts = ts)
