.. _element-obj:

Element Object
=======================

.. index:: object: element

.. class:: element()

   A python element object
   is a wrapper to the OpenSees ``Element`` object.

   One cannot create an element object
   directly, but only through the class methods below.

   .. attribute:: tag
      
      An object attribute (get).
      The element tag.

   .. attribute:: nds

      An object attribute (get).
      The element nodes.

   .. attribute:: ndf

      An object attribute (get).
      The element number of dofs.

   .. attribute:: stiff

      An object attribute (get).
      The element stiffness matrix.

   .. attribute:: damp

      An object attribute (get).
      The element damping matrix.

   .. attribute:: mass

      An object attribute (get).
      The element mass matrix.

   .. method:: __str__()

      The string reprsentation of the node. Usually
      used in the `print`_ function.

   .. method:: remove()

      Remove the corresponding OpenSees ``Element`` object.
	       
      .. note::
      
	 The python :class:`element` object is not removed, but
	 any operation on the python :class:`element` object will fail.
	 When you ``del`` a :class:`element` or set it to ``None``,
	 the python :class:`element` object is removed, but
	 the OpenSees ``Element`` is not.
	       
   .. classmethod:: Truss(tag, nds, A, mat, rho=0.0, cMass=0,doRayleigh=0)

      Create a Truss element, where
      ``tag`` is the element tag,
      ``nds`` is list of Truss :class:`node` objects,
      ``A`` the cross-sectional area of element,
      ``mat`` is a :class:`uniaxialMaterial` object,
      ``rho`` is the mass per unit length,
      ``cMass`` is the consistent mass flag, 
      (0 lumped mass, 1 consistent mass),
      and ``doRayleigh`` is the
      Rayleigh damping flag, (0 no rayleigh damping,
      1 include rayleigh damping)


   Examples::

     mat = uniaxialMaterial.Hardening(1, E=E, sigmaY=sY, Hiso=0.0, Hkin=alpha/(1-alpha)*E)

     eles = {}
     eles[1] = element.Truss(1, nds=[nds[1],nds[4]], A=A, mat=mat)
     eles[2] = element.Truss(2, nds=[nds[2],nds[4]], A=A, mat=mat)
     eles[3] = element.Truss(3, nds=[nds[3],nds[4]], A=A, mat=mat)

     for tag,ele in eles.items():
         print(ele.nds, ele.ndf)
	 print(np.array(ele.stiff))
	 print(np.array(ele.damp))
	 print(np.array(ele.mass))
	 print(ele)

.. _print: https://docs.python.org/3/library/functions.html#print
