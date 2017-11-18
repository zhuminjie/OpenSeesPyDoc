.. include:: sub.txt

Node Object
===========

.. class:: node(tag,crds=[],disp=[],vel=[],accel=[],mass=[],ndf=0)

   Create a python :class:`node` object, which
   is a wrapper to the OpenSees ``Node`` object.

   ========================   ===========================================================
   ``tag`` |int|              Tag of :class:`node`, when only ``tag`` is given,
	                      it creates a wrapper to the existing Opensees ``Node``.
   ``crds`` |listf|           Coordinates of :class:`node`, its length must
                              be :attr:`model.ndm`. (optional)
   ``disp`` |listf|           Displacements of :class:`node`, its length
	                      must be :attr:`node.ndf`. (optional)
   ``vel`` |listf|            Velocities of :class:`node`, its length
	                      must be :attr:`node.ndf`. (optional)
   ``accel`` |listf|          Accelerations of :class:`node`, its length
	                      must be :attr:`node.ndf`. (optional)
   ``mass`` |listf|           Mass of :class:`node`, its length
	                      must be :attr:`node.ndf`. (optional)
   ``ndf`` |int|              Ndf of :class:`node`, it can be different
                              to :attr:`model.ndf`. (optional)
   ========================   ===========================================================

   
Object attributes
-----------------

.. attribute:: node.tag
      
   An object attribute (get) |int|.
   A unique tag of the :class:`node` object.

.. attribute:: node.crds

   An object attribute (get/set) |listf|.
   Nodal coordinates.

.. attribute:: node.disp

   An object attribute (get/set) |listf|.
   Nodal displacements.

.. attribute:: node.vel

   An object attribute (get/set) |listf|.
   Nodal velocities.

.. attribute:: node.accel

   An object attribute (get/set) |listf|.
   Nodal accelerations.

.. attribute:: node.mass

   An object attribute (get/set) |listf|.
   Nodal mass.

.. attribute:: node.ndf

   An object attribute (get) |int|.
   The number of degrees of freedoms of the :class:`node`.


Object methods
---------------

#. :meth:`node.__str__`
#. :meth:`node.remove`
#. :meth:`node.fix`
#. :meth:`node.sp`
#. :meth:`node.mp`
#. :meth:`node.equalDOF`
#. :meth:`node.rigidDiaphragm`
#. :meth:`node.rigidLink`
#. :meth:`node.rigidBeam`

.. method:: node.__str__()

   The string reprsentation of the :class:`node` object. Usually
   used in the |print| function.

.. method:: node.remove()

   Remove the corresponding OpenSees ``Node`` object.

   .. note::
      
      By calling :meth:`node.remove`, 
      the python :class:`node` object is not removed, but
      any operation on the python :class:`node` object will fail.
      However, when you |del| a :class:`node` or set it to |None|,
      the python :class:`node` object is removed, but
      the OpenSees ``Node`` is not.


.. method:: node.fix(fix)

   Fix the :class:`node` in multiple dofs. Return :class:`sp` objects  |list|.
	    
   ========================   ===========================================================
   ``fix`` |listi|            A list of ``1`` and ``0`` to indicate corresponding dofs fixed or not. Its lenght must be :attr:`node.ndf`.
   ========================   ===========================================================


.. method:: node.sp(dof,value,const=False)

   Constrain the :class:`node` in one dof. Return a :class:`sp` object.

   ========================   =============================================================
   ``dof`` |int|              The dof of the :class:`node` to be constrained.
   ``value`` |float|          The constrained value.
   ``const`` |bool|           If the constraint is constant. (optional)
   ========================   =============================================================
	    
.. method:: node.mp(cnd,rdofs,cdofs,cMat)

   Constrain another :class:`node` (:attr:`mp.cnd`)
   to the calling :class:`node` (:attr:`mp.rnd`)
   with the constraint matrix. Return a :class:`mp` object.

   ========================   =============================================================
   ``cnd`` |node|             The :class:`node` to be constrained.
   ``rdofs`` |listi|          The constrained dofs of :attr:`mp.rnd`.
   ``cdofs`` |listi|          The constrained dofs of :attr:`mp.cnd`.
   ``cMat`` |listl|           The constraint matrix. 
   ========================   =============================================================

	    
.. method:: node.equalDOF(cnd,dofs)

   Constrain another :class:`node` (:attr:`mp.cnd`)
   to the calling :class:`node` (:attr:`mp.rnd`)
   with :class:`mp` constraints. Return a :class:`mp` object.

   ========================   =============================================================
   ``cnd`` |node|             The :class:`node` to be constrained.
   ``dofs`` |listi|           The constrained dofs.
   ========================   =============================================================

.. method:: node.rigidDiaphragm(perpDirn,cnds)

   Constrain ``cnds`` objects
   to the calling :class:`node` (:attr:`mp.rnd`)
   for them to move as if in a rigid plane with the calling :class:`node`.
   Return  :class:`mp` objects |list|.


   ========================   =============================================================
   ``perpDirn`` |int|         Direction perpendicular to the rigid plane.
   ``cnds`` |list|            A list of :class:`node` objects to be constrained.
   ========================   =============================================================

.. method:: node.rigidLink(cnd)

   Constrain the translational dof of constrained :class:`node`
   to the calling :class:`node` (:attr:`mp.rnd`). Return a :class:`mp` object.

   ========================   =============================================================
   ``cnd`` |node|             The node to be constrained
   ========================   =============================================================

.. method:: node.rigidBeam(cnd)

   Constrain both the translational and rotational dofs of constrained :class:`node`
   to the calling :class:`node` (:attr:`mp.rnd`). Return a :class:`mp` object.

   ========================   =============================================================
   ``cnd`` |node|             The node to be constrained
   ========================   =============================================================

	    
Examples
--------
::

     node(1, crds=[0.0, 0.0], disp=[1.0, 0.0])

     nds = [node(1, crds=[0.0, 0.0],disp=[0.0,0.0]),
            node(2, [72.0, 0.0], vel = [0.0,0.0]),
            node(3, [168.0, 0.0], mass = [0.0, 0.0]),
            node(4, [48.0, 144.0], ndf = 2)]

     for nd in nds:
         nd.disp = [-1.0, -2.0]
	 nd.vel = [50.0, -20.0]
	 nd.accel = [1.9, 2.8]
	 nd.mass = [3.19, 0.12]
	 print(nd.ndf, nd.tag, nd.mass, nd.crds, nd.disp, nd.vel, nd.accel)
	 print(nd)
         nd.remove()

     del nds
   
     nds = {}
     nds[1] = node(1)
     nds[2] = node(2)
     nds[3] = node(3)
     nds[4] = node(4)

     for tag, nd in nds.items():
         print(nd)

