.. include:: sub.txt

==========================================
 truss class
==========================================

.. class:: truss(nds, A, mat, rho=0.0, cMass=0,doRayleigh=0)

   Create a Truss :class:`element` object. A subclass of :class:`element`.

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


.. class:: truss(ele)

   Convert an :class:`element` to :class:`truss`.

   ========================   =============================================================
   ``ele`` |element|          A :class:`element` object.
   ========================   =============================================================


   * attributes

     #. :attr:`tagged.tag`
     #. :attr:`element.nds`
     #. :attr:`element.ndf`
     #. :attr:`element.stiff`
     #. :attr:`element.damp`
     #. :attr:`element.mass`
     #. :attr:`element.force`
     #. :attr:`element.dampingForce`
     #. :attr:`element.dynamicForce`
     #. :attr:`truss.N`
     #. :attr:`truss.deformation`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`
     #. :meth:`element.section`
     #. :meth:`element.uniMat`
     #. :meth:`element.nDMat`


.. attribute:: truss.N

   An object attribute (get) |listf|.
   The axial force of truss.


.. attribute:: truss.deformation

   An object attribute (get) |listf|.
   The deformation of truss.


