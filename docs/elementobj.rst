.. include:: sub.txt

Element Object
=======================

.. class:: element()

   A python :class:`element` object
   is a wrapper to the OpenSees ``Element`` object.

   .. note::
   
      One cannot create an :class:`element` object
      directly, but only through :ref:`element-class-methods`.


Object attributes
-------------------

.. attribute:: element.tag
      
   An object attribute (get) |int|.
   The :class:`element` tag.

   ::

      print(ele.tag)

.. attribute:: element.nds

   An object attribute (get) |list|.
   The element :class:`node` objects.

   ::

      print(ele.nds)

.. attribute:: element.ndf

   An object attribute (get) |int|.
   The element number of dofs.

   ::

      print(ele.ndf)

.. attribute:: element.stiff

   An object attribute (get) |listl|.
   The element stiffness matrix.

   ::

      print(ele.stiff)

.. attribute:: element.damp

   An object attribute (get) |listl|.
   The element damping matrix.

   ::

      print(ele.damp)

.. attribute:: element.mass

   An object attribute (get) |listl|.
   The element mass matrix.

   ::

      print(ele.mass)

Object methods
---------------
#. :meth:`element.__str__`
#. :meth:`element.remove`

.. method:: element.__str__()

   The string reprsentation of the :class:`element`. Usually
   used in the |print| function.

   ::

      print(ele)

.. method:: element.remove()

   Remove the corresponding OpenSees ``Element`` object.
	       
   .. seealso::

      :meth:`node.remove`

   ::

      ele.remove()

.. _element-class-methods:

Class methods
---------------
* Truss Elements

  #. :meth:`element.Truss`

.. _Beam-Column-Elements:
  
* Beam-Column Elements

  #. :meth:`element.elasticBeamColumn`
  #. :meth:`element.forceBeamColumn`

.. classmethod:: element.Truss(nds, A, mat, rho=0.0, cMass=0,doRayleigh=0)

   Create a Truss :class:`element` object.

   ========================   =============================================================
   ``nds`` |list|             Truss end :class:`node` objects.
   ``A`` |float|              Cross-sectional area of element.
   ``mat`` |unimat|           A |unimat| object.
   ``rho`` |float|            Mass per unit length. (optional)
   ``cMass`` |int|            Consistent mass flag (0 lumped mass, 1 consistent mass).
		              (optional)
   ``doRayleigh`` |int|       Rayleigh damping flag (0 no rayleigh damping,
		              1 include rayleigh damping). (optional)
   ========================   =============================================================


   ::

      # create a truss element
      ele = element.Truss(nds=[nds[1],nds[4]], A=A, mat=mat)
   
      # create 100 truss elements
      eles = [element.Truss(nds=[nds[i],nds[i+1]], A=A, mat=mat) for i in range(100)] 



.. classmethod:: element.elasticBeamColumn(nds,A,E,Iz,transf,mass=0.0,alpha=0.0,depth=0.0,cMass=0)

   Create a 2D elasticBeamColumn :class:`element` object.

.. classmethod:: element.elasticBeamColumn(nds,transf,A=0.0,E=0.0,G=0.0,J=0.0,Iy=0.0,Iz=0.0,sec=None,mass=0.0,cMass=0)

   Create a 3D elasticBeamColumn :class:`element` object.

   ========================   =============================================================
   ``nds`` |list|             End :class:`node` objects.
   ``A`` |float|              Cross-sectional area of element.
   ``E`` |float|              Young's Modulus
   ``G`` |float|              Shear Modulus
   ``J`` |float|              torsional moment of inertia of cross section
   ``Iz`` |float|             second moment of area about the local z-axis
   ``Iy`` |float|             second moment of area about the local y-axis
   ``transf`` |transf|        Previously-defined |transf| object.
   ``sec`` |section|          Previously-defined |section| object. (optional)
   ``mass`` |float|           Element mass per unit length (optional)
   ``alpha`` |float|          Element coefficient of thermal expansion (optional)
   ``depth`` |float|          Element beam depth (optional)
   ``cMass`` |int|            Consistent mass flag (0 lumped mass, 1 consistent mass).
		              (optional)
   ========================   =============================================================


   ::

      ele = element.elasticBeamColumn(nds=[nd1,nd2], A=5.5, E=100, Iz=1e6, transf=transf)



.. classmethod:: element.forceBeamColumn(nds,transf,bi,mass=0.0,tol=1e-12,maxIter=10)

   Create a 3D forceBeamColumn :class:`element` object.

   ========================   =============================================================
   ``nds`` |list|             End :class:`node` objects.
   ``transf`` |transf|        Previously-defined |transf| object.
   ``bi`` |bi|                Previously-defined |bi| object.
   ``mass`` |float|           Element mass per unit length, from which a lumped-mass matrix is formed  (optional)
   ``tol`` |float|            Tolerance for satisfaction of element compatibility (optional)
   ``maxIter`` |int|          maximum number of iterations to undertake to satisfy element compatibility (optional)
   ========================   =============================================================


   ::

      ele = element.forceBeamColumn(nds=[nd1,nd2], transf=transf, bi=bi)
