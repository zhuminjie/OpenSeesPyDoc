.. include:: sub.txt

Node Object
===========

.. class:: node(crds,disp=[],vel=[],accel=[],mass=[],ndf=0)

   Create a python :class:`node` object, which
   is a wrapper to the OpenSees ``Node`` object.

   ========================   =====================================================================
   ``crds`` |listf|           Coordinates of :class:`node`, its length must
                              be :attr:`model.ndm`.
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
   ========================   =====================================================================


   ::

      nd = node([0.0, 0.0], disp=[1.0,0.0]) # create a node with initial disp
      nd = node(crds=[72.0, 0.0], vel=[1.0,0.0]) # create a node with initial vel
      nds = [node([168.0,0.0]), node([48.0, 144.0])] # create a list of 2 nodes
      nds = [node([i*0.1,0.0]) for i in range(100)] # create a list of 100 nodes
   
Object attributes
-----------------

#. :attr:`node.tag`
#. :attr:`node.crds`
#. :attr:`node.disp`
#. :attr:`node.vel`
#. :attr:`node.accel`
#. :attr:`node.mass`
#. :attr:`node.ndf`

.. attribute:: node.tag
      
   An object attribute (get) |int|.
   A unique tag of the :class:`node` object.

   ::

      print(nd.tag)

.. attribute:: node.crds

   An object attribute (get/set) |listf|.
   Nodal coordinates.

   ::

      nd.crds = [1.0, 0.0]

.. attribute:: node.disp

   An object attribute (get/set) |listf|.
   Nodal displacements.

   ::

      nd.disp = [1.0, 0.0]
   
.. attribute:: node.vel

   An object attribute (get/set) |listf|.
   Nodal velocities.

   ::

      nd.vel = [1.0, 0.0]
   
.. attribute:: node.accel

   An object attribute (get/set) |listf|.
   Nodal accelerations.

   ::

      nd.accel = [1.0, 0.0]
   
.. attribute:: node.mass

   An object attribute (get/set) |listf|.
   Nodal mass.

   ::

      nd.mass = [1.0, 1.0]
   
.. attribute:: node.ndf

   An object attribute (get) |int|.
   The number of degrees of freedoms of the :class:`node`.

   ::

      print(nd.ndf)

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

   ::

      print(nd)

.. method:: node.remove()

   Remove the corresponding OpenSees ``Node`` object.

   .. note::
      
      By calling :meth:`node.remove`, 
      the python :class:`node` object is not removed, but
      any operation on the python :class:`node` object will fail.
      However, when you |del| a :class:`node` or set it to |None|,
      the python :class:`node` object is removed, but
      the OpenSees ``Node`` is not.

   ::

      nd.remove()

.. method:: node.fix(fix)

   Fix the :class:`node` in multiple dofs. Return :class:`sp` objects  |list|.
	    
   ========================   ===========================================================
   ``fix`` |listi|            A list of ``1`` and ``0`` to indicate corresponding dofs fixed or not. Its lenght must be :attr:`node.ndf`.
   ========================   ===========================================================

   ::

      ss = nd.fix([1,1,0])
      for s in ss:
          print(s)

.. method:: node.sp(dof,value,const=False)

   Constrain the :class:`node` in one dof. Return a :class:`sp` object.

   ========================   =============================================================
   ``dof`` |int|              The dof of the :class:`node` to be constrained.
   ``value`` |float|          The constrained value.
   ``const`` |bool|           If the constraint is constant. (optional)
   ========================   =============================================================

   ::

      s = nd.sp(dof=1, value=0.0, const=True)
	    
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

   ::

      mpobj = nd2.mp(cnd=nd1, rdofs=[1,2], cdofs=[1,2], cMat=[[1.0,0.1],[0.1,0.2]])
	    
.. method:: node.equalDOF(cnd,dofs)

   Constrain another :class:`node` (:attr:`mp.cnd`)
   to the calling :class:`node` (:attr:`mp.rnd`)
   with :class:`mp` constraints. Return a :class:`mp` object.

   ========================   =============================================================
   ``cnd`` |node|             The :class:`node` to be constrained.
   ``dofs`` |listi|           The constrained dofs.
   ========================   =============================================================

   ::

      mpobj = nd2.equalDOF(cnd=nd1, dofs=[1,2,3])

.. method:: node.rigidDiaphragm(perpDirn,cnds)

   Constrain ``cnds`` objects
   to the calling :class:`node` (:attr:`mp.rnd`)
   for them to move as if in a rigid plane with the calling :class:`node`.
   Return  :class:`mp` objects |list|.


   ========================   =============================================================
   ``perpDirn`` |int|         Direction perpendicular to the rigid plane.
   ``cnds`` |list|            A list of :class:`node` objects to be constrained.
   ========================   =============================================================


   ::

      mpobj = nd3.rigidDiaphragm(perpDirn=2, cnds=[nd1,nd2])

.. method:: node.rigidLink(cnd)

   Constrain the translational dof of constrained :class:`node`
   to the calling :class:`node` (:attr:`mp.rnd`). Return a :class:`mp` object.

   ========================   =============================================================
   ``cnd`` |node|             The node to be constrained
   ========================   =============================================================

   ::

      mpobj = nd2.rigidLink(cnd=nd1)
   
.. method:: node.rigidBeam(cnd)

   Constrain both the translational and rotational dofs of constrained :class:`node`
   to the calling :class:`node` (:attr:`mp.rnd`). Return a :class:`mp` object.

   ========================   =============================================================
   ``cnd`` |node|             The node to be constrained
   ========================   =============================================================

   ::

      mpobj = nd2.rigidBeam(cnd=nd1)
	    
