.. include:: sub.txt

======================
elasticBeamColum class
======================

.. class:: elasticBeamColumn(nds,A,E,Iz,transf,mass=0.0,alpha=0.0,depth=0.0,cMass=0)
   
   Create a 2D elasticBeamColumn :class:`element` object. A subclass of :class:`element`

.. class:: elasticBeamColumn(nds,transf,A=0.0,E=0.0,G=0.0,J=0.0,Iy=0.0,Iz=0.0,sec=None,mass=0.0,cMass=0)
   
   Create a 3D elasticBeamColumn :class:`element` object

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

.. class:: elasticBeamColumn(ele)

   Convert an :class:`element` to :class:`elasticBeamColumn`
	   
   ========================   =============================================================
   ``ele`` |element|          A :class:`element` object.
   ========================   =============================================================
	   
   * attribute
   
     #. :attr:`tagged.tag`
     #. :attr:`element.nds`
     #. :attr:`element.ndf`
     #. :attr:`element.stiff`
     #. :attr:`element.damp`
     #. :attr:`element.mass`
     #. :attr:`element.force`
     #. :attr:`element.dampingForce`
     #. :attr:`element.dynamicForce`
     #. :attr:`elasticBeamColumn.localForce`
     #. :attr:`elasticBeamColumn.basicForce`
     #. :attr:`elasticBeamColumn.deformation`
     #. :attr:`elasticBeamColumn.chordRotation`

   * method
   
     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`
     #. :meth:`element.section`
     #. :meth:`element.uniMat`
     #. :meth:`element.nDMat`

.. attribute:: elasticBeamColumn.localForce

   An object attribute (get) |listf|
   The force force of elasticBeamColumn.

.. attribute:: elasticBeamColumn.basicForce

   An object attribute (get) |listf|
   The basic force of elasticBeamColumn.

.. attribute:: elasticBeamColumn.deformation

   An object attribute (get) |listf|
   The deformation of elasticBeamColumn.

.. attribute:: elasticBeamColumn.chordRotation
   
   An object attribute (get) |listf|
   The rotation of chord.




