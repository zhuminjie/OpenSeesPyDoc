.. include:: sub.txt

Element Object
=======================

.. class:: element(tag)

   A python :class:`element` object
   is a wrapper to the OpenSees ``Element`` object.

   ========================   ===========================================================
   ``tag`` |int|              Tag of :class:`element`, when only ``tag`` is given,
	                      it creates a wrapper to an existing OpenSees ``Element``.
   ========================   ===========================================================

   .. note::
   
      One cannot create an :class:`element` object
      directly, but only through :ref:`element-class-methods`.


Object attributes
-------------------

.. attribute:: element.tag
      
   An object attribute (get) |int|.
   The :class:`element` tag.

.. attribute:: element.nds

   An object attribute (get) |list|.
   The element :class:`node` objects.

.. attribute:: element.ndf

   An object attribute (get) |int|.
   The element number of dofs.

.. attribute:: element.stiff

   An object attribute (get) |listl|.
   The element stiffness matrix.

.. attribute:: element.damp

   An object attribute (get) |listl|.
   The element damping matrix.

.. attribute:: element.mass

   An object attribute (get) |listl|.
   The element mass matrix.

Object methods
---------------

#. :meth:`element.__str__`
#. :meth:`element.remove`

.. method:: element.__str__()

   The string reprsentation of the :class:`element`. Usually
   used in the |print| function.

.. method:: element.remove()

   Remove the corresponding OpenSees ``Element`` object.
	       
   .. seealso::

      :meth:`node.remove`

.. _element-class-methods:

Class methods
---------------

#. :meth:`element.Truss`

.. classmethod:: element.Truss(tag, nds, A, mat, rho=0.0, cMass=0,doRayleigh=0)

   Create a Truss :class:`element` object.

   ========================   =============================================================
   ``tag`` |int|              :class:`element` tag.
   ``nds`` |list|             Truss end :class:`node` objects.
   ``A`` |float|              Cross-sectional area of element.
   ``mat`` |unimat|           A |unimat| object.
   ``rho`` |float|            Mass per unit length. (optional)
   ``cMass`` |int|            Consistent mass flag (0 lumped mass, 1 consistent mass).
		              (optional)
   ``doRayleigh`` |int|       Rayleigh damping flag (0 no rayleigh damping,
		              1 include rayleigh damping). (optional)
   ========================   =============================================================
		 

Examples
-----------

::

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


