.. include:: sub.txt

===============================
 pattern -- Loading Pattern
===============================

.. class:: pattern(ts, factor=1.0)

   Create a plain load :class:`pattern`.
   A subclass of :class:`tagged` and
   a base class of other patterns.

   ========================   =============================================================
   ``ts`` |timeSeries|        A :class:`timeSeries` object.
   ``factor`` |float|         Load factor. (optional)
   ========================   =============================================================


   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`pattern.sps`
     #. :attr:`pattern.loads`
     #. :attr:`pattern.eleLoads`
     #. :attr:`pattern.loadFactor`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`
     #. :meth:`pattern.wipe`
     #. :meth:`pattern.sp`
     #. :meth:`pattern.load`
     #. :meth:`pattern.eleLoad`

   ::

      ptn = pattern.Plain(ts = ts)



Following are pattern subclasses available in the OpenSees:

.. toctree::
   :maxdepth: 2
      

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

.. attribute:: pattern.eleLoads
      
   An object attribute (get) |list|.
   All python :class:`eleLoad` objects in the :class:`pattern`.

   ::

      for el in ptn.eleLoads:
          print(el)

.. attribute:: pattern.loadFactor
      
   An object attribute (get) |float|.
   Get current load factor in the :class:`pattern`.

   ::

      print(ptn.loadFactor)



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


.. method:: pattern.eleLoad(eles,beamUniform=[],beamPoint=[])

   Create and add a |list| of python :class:`eleLoad` object to the :class:`pattern`.
   Return a |list| of python :class:`eleLoad` object.

   ========================   =============================================================
   ``eles`` |list|            A list of :class:`element` objects.
   ``beamUniform`` |listf|    Beam uniform loads, ``[Wy,Wx]`` for 2D and ``[Wy,Wz,Wx]``
	                      for 3D, ``Wx`` is along member length, ``Wy`` is in local
	                      y direction and ``Wz`` local z direction.
   ``beamPoint`` |listf|      Beam point loads, ``[Py,xL,Px]`` for 2D and
	                      ``[Py,Pz,xL,Px]``
	                      for 3D, ``Px`` is along member length, ``Py`` is in local
	                      y direction and ``Pz`` local z direction, ``xL``
	                      is the location of point load relative to |node| I,
	                      prescribed as fraction of |element| length.
   ========================   =============================================================

   ::

      el = ptn.eleLoad(eles=[e1,e2,e3], beamUniform=[-0.1, 0.5])
   
.. method:: pattern.wipe()

   Wipe all :class:`sp`, :class:`load`, and :class:`eleLoad` objects
   from the :class:`pattern`.

   ::

      ptn.wipe()

