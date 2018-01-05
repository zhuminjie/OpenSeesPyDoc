.. include:: sub.txt
   
=============
dispBeamColum
=============

.. class:: dispBeamColumn(nds,transf,bi,mass=0.0,tol=1e-12,maxIter=10)

   Create a dispBeamColumn :class:`element` object. A subclass of :class:`element`

   ========================   =============================================================
   ``nds`` |list|             Two end :class:`node` objects.
   ``transf`` |transf|        Previously-defined |transf| object.
   ``bi`` |bi|                Previously-defined |bi| object.
   ``mass`` |float|           Element mass per unit length, from which a lumped-mass matrix is formed  (optional)
   ``tol`` |float|            Tolerance for satisfaction of element compatibility (optional)
   ``maxIter`` |int|          maximum number of iterations to undertake to satisfy element compatibility (optional)
   ========================   =============================================================

.. class:: dispBeamColumn(ele)

   Convert an :class:`element` to :class:`dispBeamColumn`


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
     #. :attr:`dispBeamColumn.force`
     #. :attr:`dispBeamColumn.localForce`
     #. :attr:`dispBeamColumn.basicForce`
     #. :attr:`dispBeamColumn.basicStiff`
     #. :attr:`dispBeamColumn.chordRotation`
     #. :attr:`dispBeamColumn.plasticRotation`
     #. :attr:`dispBeamColumn.dvdh`
     #. :attr:`dispBeamColumn.dcurvdh`
     #. :attr:`dispBeamColumn.integrationPoints`
     #. :attr:`dispBeamColumn.integrationWeights`
     #. :attr:`dispBeamColumn.rayleighForces`
     #. :attr:`dispBeamColumn.secs`

   * method
   
   #. :meth:`tagged.__str__`
   #. :meth:`tagged.remove`

.. attribute:: dispBeamColumn.force

   An object attribute (get) |listf|
   The global force of dispBeamColumn.

.. attribute:: dispBeamColumn.localForce

   An object attribute (get) |listf|
   The local force of dispBeamColumn.

.. attribute:: dispBeamColumn.basicForce

   An object attribute (get) |listf|
   The basic force of dispBeamColumn.

.. attribute:: dispBeamColumn.basicStiff

   An object attribute (get) |listf|
   The basic stiffness of dispBeamColumn.

.. attribute:: dispBeamColumn.chordRotation

   An object attribute (get) |listf|
   The chord rotation of the element.

.. attribute:: dispBeamColumn.plasticRotation

   An object attribute (get) |listf|
   The plastic rotation of the element.

.. attribute:: dispBeamColumn.dvdh

   An object attribute (get) |listf|
   The basic deformation sensitivity of the element.

.. attribute:: dispBeamColumn.dcurvdh

   An object attribute (get) |listf|
   The curvature sensitivity along element length.


.. attribute:: dispBeamColumn.integrationPoints

   An object attribute (get) |listf|   T
   the integration points of the element.

.. attribute:: dispBeamColumn.integrationWeights

   An object attribute (get) |listf|

   The integration weights of the element.

.. attribute:: dispBeamColumn.rayleighForces

   An object attribute (get) |listf|
   The rayleigh disps of the element.

.. attribute:: dispBeamColumn.secs

   An object attribute (get) |list|
   The sections of the element, which can be used to get section responses.



