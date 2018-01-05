.. include:: sub.txt

=============================
 node 
=============================

.. class:: node(crds,ndf=model.ndf)

   Create a OpenSees Node object. A subclass of :class:`tagged`.

   ========================   =====================================================================
   ``crds`` |listf|           Coordinates of :class:`node`, its length must
                              be :attr:`model.ndm`.
   ``ndf`` |int|              Ndf of :class:`node`, it can be different
                              to :attr:`model.ndf`. (optional)
   ========================   =====================================================================

   * attributes
   
     #. :attr:`tagged.tag`
     #. :attr:`node.crds`
     #. :attr:`node.disp`
     #. :attr:`node.vel`
     #. :attr:`node.accel`
     #. :attr:`node.mass`
     #. :attr:`node.ndf`
     #. :attr:`node.reaction`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`
     #. :meth:`node.fix`
     #. :meth:`node.sp`
     #. :meth:`node.mp`
     #. :meth:`node.equalDOF`
     #. :meth:`node.rigidDiaphragm`
     #. :meth:`node.rigidLink`
     #. :meth:`node.rigidBeam`
     


   ::

      nd = node([0.0, 0.0]) 
      nd = node(crds=[72.0, 0.0]) 
      nds = [node([168.0,0.0]), node([48.0, 144.0])] 
      nds = [node([i*0.1,0.0]) for i in range(100)]
   



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

.. attribute:: node.reaction

   An object attribute (get) |listf|.
   The nodal reactions.

   ::

      print(nd.reaction)




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
	    




