.. include:: sub.txt

===========================
 element -- Finite Element
===========================

.. class:: element()

   A subclass of :class:`tagged` and
   a base class for the OpenSees Element objects.

   One cannot create an :class:`element` object
   directly, but only through its subclasses.


   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`element.nds`
     #. :attr:`element.ndf`
     #. :attr:`element.stiff`
     #. :attr:`element.damp`
     #. :attr:`element.mass`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`

   

Following are element subclasses available in the OpenSees:

Zero-Length Elements

.. toctree::
   :maxdepth: 2



Truss Elements

.. toctree::
   :maxdepth: 2


.. _Beam-Column-Elements:
  
Beam-Column Elements

.. toctree::
   :maxdepth: 2


Triangular Elements

.. toctree::
   :maxdepth: 2


.. _PFEM-Elements:
  
PFEM Elements

.. toctree::
   :maxdepth: 2

   bubble2d





	      

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



.. classmethod:: element.zeroLengthSection(nds, sec, x=[1.0,0.0,0.0], yp=[0.0,1.0,0.0], doRayleigh=1)

   Create a zeroLengthSection :class:`element` object, which is defined by two |node| objects at the same location. The nodes are connected by a single |section| object to represent the force-deformation relationship for the element.

   ========================   =============================================================
   ``nds`` |list|             Two end :class:`node` objects.
   ``sec`` |section|          A |section| object.
   ``x`` |listf|              Vector components in global coordinates defining
		              local x-axis. (optional)
   ``yp`` |listf|             Vector components in global coordinates defining
		              vector yp which lies in the local x-y plane for
                              the element. (optional)
   ``doRayleigh`` |int|       Rayleigh damping flag (0 no rayleigh damping,
		              1 include rayleigh damping). (optional)
   ========================   =============================================================


   ::

      # create a  element
      ele = element.zeroLengthSection(nds=[nds[1],nds[4]], sec=sec)
   

.. classmethod:: element.Truss(nds, A, mat, rho=0.0, cMass=0,doRayleigh=0)

   Create a Truss :class:`element` object.

   ========================   =============================================================
   ``nds`` |list|             Two end :class:`node` objects.
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
   ``nds`` |list|             Two end :class:`node` objects.
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
   ``nds`` |list|             Two end :class:`node` objects.
   ``transf`` |transf|        Previously-defined |transf| object.
   ``bi`` |bi|                Previously-defined |bi| object.
   ``mass`` |float|           Element mass per unit length, from which a lumped-mass matrix is formed  (optional)
   ``tol`` |float|            Tolerance for satisfaction of element compatibility (optional)
   ``maxIter`` |int|          maximum number of iterations to undertake to satisfy element compatibility (optional)
   ========================   =============================================================


   ::

      ele = element.forceBeamColumn(nds=[nd1,nd2], transf=transf, bi=bi)


.. classmethod:: element.tri31(nds, thk, type, mat, pressure=0.0, rho=0.0, b1=0.0, b2=0.0)

   Create a constant strain triangular :class:`element` object, which which uses three nodes and one integration points.

   ========================   =============================================================
   ``nds`` |list|             Three end :class:`node` objects.
   ``thk`` |section|          Element thickness.
   ``type`` |str|             String representing material behavior.
		              The type parameter can be
                              either ``'PlaneStrain'`` or ``'PlaneStress'``.
   ``mat`` |ndmat|            A :class:`NDMaterial` object.
   ``pressure`` |float|       Surface pressure. (optional)
   ``rho`` |float|            Element mass density (per unit volume) from
		              which a lumped element mass matrix
                              is computed. (optional)
   ``b1`` |float|             Constant body forces defined in the domain. (optional)
   ``b2`` |float|             Constant body forces defined in the domain. (optional)
   ========================   =============================================================


   ::

      # create a  element
      ele = element.tri31(nds=[nd1,nd2,nd3], thk=0.1, type='PlaneStress', mat=mat)
  



.. classmethod:: element.PFEMElement2DBubble(nds, rho, mu, b1, b2, thk=1.0, kappa=-1)

   Create a PFEM :class:`element` object, which uses P1+P1 formulation, i.e.
   three velocity nodes and three pressure nodes. The bubble mode is
   condensed internally. 

   ========================   =============================================================
   ``nds`` |list|             Six velocity and pressure :class:`node` objects in
		              the order of
		              ``[vnd1,pnd1,vnd2,pnd2,vnd3,pnd3]``.
   ``rho`` |float|            Fluid density.
   ``mu`` |float|             Fluid viscosity.
   ``b1`` |float|             Body acceleration in x direction.
   ``b2`` |float|             Body acceleration in y direction.
   ``thk`` |float|            Element thickness. (optional)
   ``kappa`` |float|          Fluid bulk modulus. Negative values mean incompressible
		              fluid. (optional)
   ========================   =============================================================


   ::

      # create an element
      ele = element.PFEMElement2DBubble(nds=[vnd1,pnd1,vnd2,pnd2,vnd3,pnd3],
                                        rho=1000.0, mu=1e-3, b1=0.0, b2=-9.81)
  
